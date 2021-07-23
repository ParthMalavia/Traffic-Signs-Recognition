import tkinter as tk
from tkinter import filedialog
from tkinter import *
import os

import numpy as np
from PIL import ImageTk, Image

from tensorflow.keras.models import load_model
model = load_model('TFClassifier.model')

# dictionary to label all traffic signs class.
classes = {1: 'Speed limit (20km/h)',
           2: 'Speed limit (30km/h)',
           3: 'Speed limit (50km/h)',
           4: 'Speed limit (60km/h)',
           5: 'Speed limit (70km/h)',
           6: 'Speed limit (80km/h)',
           7: 'End of speed limit (80km/h)',
           8: 'Speed limit (100km/h)',
           9: 'Speed limit (120km/h)',
           10: 'No passing',
           11: 'No passing veh over 3.5 tons',
           12: 'Right-of-way at intersection',
           13: 'Priority road',
           14: 'Yield',
           15: 'Stop',
           16: 'No vehicles',
           17: 'Veh > 3.5 tons prohibited',
           18: 'No entry',
           19: 'General caution',
           20: 'Dangerous curve left',
           21: 'Dangerous curve right',
           22: 'Double curve',
           23: 'Bumpy road',
           24: 'Slippery road',
           25: 'Road narrows on the right',
           26: 'Road work',
           27: 'Traffic signals',
           28: 'Pedestrians',
           29: 'Children crossing',
           30: 'Bicycles crossing',
           31: 'Beware of ice/snow',
           32: 'Wild animals crossing',
           33: 'End speed + passing limits',
           34: 'Turn right ahead',
           35: 'Turn left ahead',
           36: 'Ahead only',
           37: 'Go straight or right',
           38: 'Go straight or left',
           39: 'Keep right',
           40: 'Keep left',
           41: 'Roundabout mandatory',
           42: 'End of no passing',
           43: 'End no passing veh > 3.5 tons'}


def classify(file_path):
    print(file_path)
    image = Image.open(file_path)
    image = image.resize((64, 64))
    image = np.expand_dims(image, axis=0)
    image = np.array(image)[:, :, :, :3]
    pred = np.argmax(model.predict(image))
    sign = classes[pred + 1]
    print(sign)
    label.configure(foreground='#011638', text=sign)


def show_classify_button(file_path):
    classify_b = Button(top, text="Classify Image", command=lambda: classify(file_path), padx=2, pady=1)
    classify_b.configure(background='#364156', foreground='white', font=('arial', 10, 'bold'))
    classify_b.place(relx=0.79, rely=0.46)


def upload_image():
    try:
        file_path = filedialog.askopenfilename(initialdir=os.path.join(os.curdir,"Meta"))
        uploaded = Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2), (top.winfo_height()/2)))
        im = ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image = im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass


# initialise GUI
top = tk.Tk()
top.geometry('600x300')
top.title('Traffic sign classification')
top.configure(background='#CDCDCD')

heading = Label(top, text="Know Your Traffic Sign", pady=4, font=('arial', 20, 'bold'))
heading.configure(background='#CDCDCD', foreground='#364156')
heading.pack(side=TOP)

label = Label(top, background='#CDCDCD', font=('arial', 15, 'bold'))
blank = Label(top, background='#CDCDCD').pack(side=TOP)
sign_image = Label(top, pady=4)

upload = Button(top, text="Upload an image", command=upload_image, padx=2, pady=1)
upload.configure(background='#364156', foreground='white', font=('arial', 10, 'bold'))

upload.pack(side=BOTTOM, pady=10)
label.pack(side=BOTTOM, expand=True)
sign_image.pack(side=LEFT, expand=True)

top.mainloop()
