import csv
import json
from decimal import Decimal
from django.core.management.base import BaseCommand
from ...models import Restaurant, Dish

class Command(BaseCommand):
    help = 'Import data from CSV file into Restaurant and Dish models'

    def handle(self, *args, **kwargs):
        csv_file_path = '/home/himanshu/Development/django-tut/mysite/food/management/commands/restaurant.csv'

        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                restaurant_name = row['name'].strip()
                restaurant_location = row['location'].strip()
                items_json = row['items'].strip()

                # Create or get the restaurant
                restaurant, created = Restaurant.objects.get_or_create(
                    name=restaurant_name,
                    location=restaurant_location
                )

                # Parse the JSON items
                items = json.loads(items_json)

                # Create Dish objects for each item
                for dish_name, dish_price in items.items():
                    # Remove the "onwards" text if present
                    dish_price = dish_price.replace("onwards", "").strip()

                    # Convert the price to Decimal
                    try:
                        dish_price_decimal = Decimal(dish_price)
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(f"Error converting price for {dish_name}: {e}"))
                        continue

                    # Create or update the Dish object
                    dish, created = Dish.objects.get_or_create(
                        name=dish_name,
                        restaurant=restaurant,
                        defaults={'price': dish_price_decimal}
                    )

                    if not created:
                        dish.price = dish_price_decimal
                        dish.save()

                self.stdout.write(self.style.SUCCESS(f'Successfully imported dishes for restaurant {restaurant_name}'))
