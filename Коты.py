from tkinter import *
from PIL import Image,ImageTk
import requests
from io import BytesIO

from pygame.examples.aliens import load_image
from клик import window

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
