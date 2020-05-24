import urllib.request
import wikipedia

def save_img(page):
    page_image = wikipedia.page(page)
    image_down_link = page_image.images[1]


    urllib.request.urlretrieve(image_down_link , "{}-loc.jpg".format(page))
    