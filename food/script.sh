#!/bin/bash

# Define the directory containing images
IMAGES_DIR="images/"

# Ensure the directory exists
if [ ! -d "$IMAGES_DIR" ]; then
    echo "Error: Directory $IMAGES_DIR does not exist."
    exit 1
fi

# Change to the images directory
cd "$IMAGES_DIR" || exit

# Counter for renaming
counter=1

# Iterate over each file in the directory
for file in *; do
    # Check if the file is a regular file (not a directory)
    if [ -f "$file" ]; then
        # Get the file extension
        extension="${file##*.}"
        # Rename the file to imageN.extension (N is the counter)
        new_name="image${counter}.${extension}"
        mv "$file" "$new_name"
        echo "Renamed $file to $new_name"
        # Increment counter
        ((counter++))
    fi
done

echo "Renaming complete."
