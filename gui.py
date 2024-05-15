import tkinter as tk
import PIL
from PIL import ImageTk, Image

from card import card 
from images import *

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Card Generator App")

        self.renderGui()

    def renderGui(self):
        testCardObj = card("pimpek", "fajny ten pimpek", [55, 20, 100], hatMag, bodyMag, accessoryMag, template, frontBg1, frontBand, backImg, 240)

        testCard = testCardObj.renderCard()

        testCard = testCard.resize((450, 350), Image.LANCZOS)

        image = ImageTk.PhotoImage(testCard)
        panel = tk.Label(self.root, image = image)
    
        # set the image as img 
        panel.image = image
        panel.grid(row = 2)