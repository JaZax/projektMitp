from PIL import Image

nameTranslate = {
    "hatMag": "Mag",
    "bodyMag": "Mag",
    "accessoryMag": "Mag",

    "hatKnight": "Rycerz",
    "bodyKnight": "Rycerz",
    "accessoryKnight": "Rycerz",

    "hatRomantic": "Romantyk",
    "bodyRomantic": "Romantyk",
    "accessoryRomantic": "Romantyk",

    "frontBg1": "Niebo",
    "frontBg2": "Ogień",
}

template = Image.open(fr"img\template1.png")
frontBg1 = Image.open(fr"img\frontBg1.png")
frontBg2 = Image.open(fr"img\frontBg2.png")
frontBand = Image.open(fr"img\frontBand1.png")

backImg = Image.open(fr"img\backImg1.png")

hatMag = Image.open(fr"img\hatMag.png")
bodyMag = Image.open(fr"img\bodyMag.png")
accessoryMag = Image.open(fr"img\accessoryMag.png")

hatKnight = Image.open(fr"img\hatKnight.png")
bodyKnight = Image.open(fr"img\bodyKnight.png")
accessoryKnight = Image.open(fr"img\accessoryKnight.png")

hatRomantic = Image.open(fr"img\hatRomantic.png")
bodyRomantic = Image.open(fr"img\bodyRomantic.png")
accessoryRomantic = Image.open(fr"img\accessoryRomantic.png")