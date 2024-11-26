from tkinter import *
from PIL import Image,ImageTk
import requests
from io import BytesIO

from bottle import response, request
from pygame.examples.aliens import load_image
from клик import window


def loade_image():
    try:
        response =requests.get(url)
        response.raise_for_status()
        image_data =BytesIO(response.content)
        img = Image.open(image_data)
        return ImageTk.PhotoImage(img)
    except Exception as e :
        print(f"Произошла ошибка{e}")
        return None


window =Tk()
window.title("Cats")
window.geometry("600x400")


label= label()
label.pack()



url = "hrttps:// cataas.com/cat"
img= load_image(url)
if img:
    label.config(image=img)
    label.image = img
window.mainloop()
