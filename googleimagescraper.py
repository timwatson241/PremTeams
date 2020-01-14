from google_images_download import google_images_download   #importing the library
import os

def scrape_from_google(number,team):
    os.mkdir("Images/"+team)
    response = google_images_download.googleimagesdownload()   #class instantiation
    arguments = {"keywords":team+" home jersey","limit":number,"print_urls":True,"output_directory":"Images", "image_directory":team}   #creating list of arguments
    paths = response.download(arguments)   #passing the arguments to the function
    print(paths)
