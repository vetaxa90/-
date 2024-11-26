from tkinter import *
from PIL import Image,ImageTk
import requests
from io import BytesIO

from pygame.display import update


def load_image(url):
    try:
        response =requests.get(url)
        response.raise_for_status()
        image_data =BytesIO(response.content)
        img = Image.open(image_data)
        img.thumbnail((600,480),Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e :
        print(f"Произошла ошибка{e}")
        return None

def open_new_window():
    img = load_image(url)
    if img:
        new_widndow = Toplevel()
        new_widndow.title("Картина коты")
        new_widndow.geometry('600x 480')
        label= Label(new_widndow,image=img)
        label.pack()
        label.image = img

def exit():
    window.destroy()

window =Tk()
window.title("Cats")
window.geometry("600x620")


label= Label()
label.pack()
# update_button =Button(text= "Обновить",command = set_image)
# update_button.pack()
meny_bar= Menu(window)
window.config(menu=meny_bar)

file_menu =Menu(meny_bar,tearoff=0)
meny_bar.add_cascade(label="Файл",menu=file_menu)
file_menu.add_command(label="Загрузить фото",command=open_new_window)
file_menu.add_separator()
file_menu.add_command(label="Выход",command=exit)
url = "https://cataas.com/cat"
set_image()

window.mainloop()
