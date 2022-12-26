# RecipeGen
This program generates recipes based off a picture of a receipt

Progress so far:

`Natural Language Processing`
First, I preprocess the image to prepare it for analysis by converting the image to grayscale using `cv2`. Then using an OCR (Optical Character Recognition) tool call `pytesseract`, I extracted text from the image and tokenized it to identify the names of food ingredients and filter out any non-food items that may have been included. My dictionary is small at the moment and needs to be improved.

The `requests` library to send an HTTP request to the website's search API and parse the resulting HTML or JSON data to extract the search results.

Plans for the future:
Creating a front-end interface with Kivy
~ Allows the user to take photos of multiple receipts to add to personal `ingredients` list
~ Allows manual addition to the `ingredients` list
~ Allows deletion from personal `ingredients` list

Extract and reformat search results into app
