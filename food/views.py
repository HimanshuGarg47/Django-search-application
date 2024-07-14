from django.shortcuts import render
from .models import Dish
from .forms import SearchForm
from django.http import JsonResponse


def search_view(request):
    form = SearchForm()
    results = []
    query = ''
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Dish.objects.filter(name__icontains=query).order_by('name')

    return render(request, 'food/search.html', {'form': form, 'results': results, 'query': query})


def search_view_live(request):
    if 'term' in request.GET:
        print(request.GET)
        query = request.GET.get('term')
        results = Dish.objects.filter(name__icontains=query).order_by('-name')[:20]
        titles = [f"{dish.name} | Cost Rs. {dish.price} | Restaurant - {dish.restaurant.name}" for dish in results]
        print("Successfully")
        return JsonResponse(titles, safe=False)
    else:
        return render(request, 'food/search_live.html')



