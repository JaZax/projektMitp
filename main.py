from card import card 
from PIL import Image

template = Image.open("img/template1.png")
frontBg = Image.open("img/frontBg1.png")
frontBand = Image.open("img/frontBand1.png")
backImg = Image.open("img/backImg1.png")
hat = Image.open("img/hat1.png")
body = Image.open("img/body1.png")
accessory = Image.open("img/accessory1.png")

testCard = card("pimpek", "fajny ten pimpek", ["35", "20", "100"], hat, body, accessory, template, frontBg, frontBand, backImg)

testCard.renderCard()

testCard2 = card("hihi", "fajny ten pimpek fajny ten pimpek fajny ten pimpek fajny ten pimpek fajny ten pimpek fajny ten pimpek", ["100", "100", "100"], hat, body, accessory, template, frontBg, frontBand, backImg)

testCard2.renderCard()

testCard3 = card("ehfaiuwhfieahufahw", "Testowy opis karty. To jest testowy opis karty, nic ciekawego, karta jaka jest każdy widzi", ["2", "2", "2"], hat, body, accessory, template, frontBg, frontBand, backImg)

testCard3.renderCard()

