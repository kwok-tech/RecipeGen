import cv2
import pytesseract
import requests

def extractIngredients(imageOfReciept):
    # ingredient dictionary
    food_ingredients = {
        "flour": ["all-purpose flour", "whole wheat flour", "bread flour"],
        "sugar": ["granulated sugar", "brown sugar", "powdered sugar"],
        "oil": ["vegetable oil", "olive oil", "coconut oil"],
        "eggs": ["large eggs"],
        "milk": ["whole milk", "2% milk", "non-dairy milk"],
        "meat": ["chicken", "beef", "pork"],
        "vegetables": ["tomatoes", "onions", "bell peppers", "spinach"],
        "spices": ["salt", "pepper", "cumin", "oregano", "paprika", "onion powder", "garlic powder"],
    }

    non_food_ingredients = {
        "tax": ["sales tax", "VAT"],
        "service charge": ["service fee", "gratuity"],
        "miscellaneous": ["gift card", "gift certificate"],
    }

    # Load the image and preprocess it
    image = cv2.imread(imageOfReciept)
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Extract the text from the image
    text = pytesseract.image_to_string(grayscale)

    # Tokenize the text
    tokens = text.split()

    # Identify potential ingredients
    food_items = []
    for token in tokens:
        if token in food_ingredients:
            continue
        food_items.append(token)

    # Filter out non-food items
    filtered_items = []
    for item in food_items:
        if item not in non_food_ingredients:
            filtered_items.append(item)
    return filtered_items

# Get name of picture file of receipt
receipt = "receipt.jpg"

# Set the base URL for the search API
base_url = "https://recipeland.com/api/v1/recipes/by_ingredient"

# Set the search parameters
ingredients = extractIngredients(receipt) # append to list, if adding more receipts or manually add
params = {
    "ingredients": ",".join(ingredients),
    "page": 1,
}

# Send the HTTP request and retrieve the search results
response = requests.get(base_url, params=params)
results = response.json()["results"]

# Print the search results
for result in results:
    print(result["name"])