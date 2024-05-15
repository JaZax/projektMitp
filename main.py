from card import card 
from PIL import Image

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

testCard = card("pimpek", "fajny ten pimpek", ["35", "20", "100"], hatMag, bodyMag, accessoryMag, template, frontBg1, frontBand, backImg, 0)

testCard.renderCard()

testCard2 = card("hihi", "fajny ten pimpek fajny ten pimpek fajny ten pimpek fajny ten pimpek fajny ten pimpek fajny ten pimpek", ["100", "100", "100"], hatKnight, bodyKnight, accessoryKnight, template, frontBg2, frontBand, backImg, 100)

testCard2.renderCard()

testCard3 = card("ehfaiuwhfieahufahw", "Testowy opis karty. To jest testowy opis karty, nic ciekawego, karta jaka jest każdy widzi", ["2", "2", "2"], hatRomantic, bodyRomantic, accessoryRomantic, template, frontBg1, frontBand, backImg, 180)

testCard3.renderCard()

