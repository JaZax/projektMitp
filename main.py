from card import card 
from gui import *
from images import *

import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
    # testCard = card("pimpek", "fajny ten pimpek", [35, 20, 100], hatMag, bodyMag, accessoryMag, template, frontBg1, frontBand, backImg, 40)

    # testCard.renderCard()


# testCard2 = card("hihi", "fajny ten pimpek fajny ten pimpek fajny ten pimpek fajny ten pimpek fajny ten pimpek fajny ten pimpek", ["100", "100", "100"], hatKnight, bodyKnight, accessoryKnight, template, frontBg2, frontBand, backImg, 100)

# testCard2.renderCard()

# testCard3 = card("ehfaiuwhfieahufahw", "Testowy opis karty. To jest testowy opis karty, nic ciekawego, karta jaka jest każdy widzi", ["2", "2", "2"], hatRomantic, bodyKnight, accessoryMag, template, frontBg1, frontBand, backImg, 180)

# testCard3.renderCard()

