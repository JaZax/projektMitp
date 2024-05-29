from PIL import Image, ImageDraw, ImageFont
import textwrap
import numpy as np
import colorsys
import pickle

font90 = ImageFont.truetype(fr'.\fonts\Roboto_Mono\static\RobotoMono-Bold.ttf', 90)
font70 = ImageFont.truetype(fr'.\fonts\Roboto_Mono\static\RobotoMono-Bold.ttf', 70)
font60 = ImageFont.truetype(fr'.\fonts\Roboto_Mono\static\RobotoMono-Bold.ttf', 60)
font40 = ImageFont.truetype(fr'.\fonts\Roboto_Mono\static\RobotoMono-Medium.ttf', 40)

def renderText(text, font, color, x, y, d):
    _, _, w, h = d.textbbox((50 , 50), text, font=font)
    d.text((x , y), text, font=font, fill=color, align='center', anchor="mm")

rgb_to_hsv = np.vectorize(colorsys.rgb_to_hsv)
hsv_to_rgb = np.vectorize(colorsys.hsv_to_rgb)

def shift_hue(arr, hout):
    r, g, b, a = np.rollaxis(arr, axis=-1)
    h, s, v = rgb_to_hsv(r, g, b)
    h = hout
    r, g, b = hsv_to_rgb(h, s, v)
    arr = np.dstack((r, g, b, a))
    return arr

def colorize(image, hue):
    """
    Colorize PIL image `original` with the given
    `hue` (hue within 0-360); returns another PIL image.
    """
    img = image.convert('RGBA')
    arr = np.array(np.asarray(img).astype('float'))
    new_img = Image.fromarray(shift_hue(arr, hue/360.).astype('uint8'), 'RGBA')

    return new_img


# klasa tworząca karte z podanych parametrów

class card:
    def __init__(self, name: str, desc: str, stats: list, hat: str, body: str, accessory: str, template: str, frontBg: str, frontBand: str, backImg: str, hue: int):
        self.name = name
        self.desc = desc
        self.stats = stats # (mana, stamina, health)

        self.hat = ""
        self.hatName = ""
        if len(hat) > 0:   
            self.hat = Image.open(hat)
            self.hatName = self.hat.filename
        else: pass

        self.body = ""
        self.bodyName = ""
        if len(body) > 0:
            self.body = Image.open(body)
            self.bodyName = self.body.filename
        else: pass

        self.accessory = ""
        self.accessoryName = ""
        if len(accessory) > 0:
            self.accessory = Image.open(accessory)
            self.accessoryName = self.accessory.filename
        else: pass

        self.template = Image.open(template)

        self.frontBg = Image.open(frontBg)
        self.frontBgName = self.frontBg.filename

        self.frontBand = Image.open(frontBand)
        self.backImg = Image.open(backImg)
        self.hue = hue

        # 🔥 todo: limity:
        # name: 1-23
        # desc: 1-125
        # stats: 0-100
        # hue: 0-360

        for stat in self.stats:
            index = self.stats.index(stat)
            self.stats[index] = str(stat)


    def printCardData(self):
        print(f'''
                Nazwa = {self.name}
                Opis = {self.desc}
                Statystyki = {self.stats} (mana, stamina, zdrowie)
                Czapka = {self.hat}
                Wdzianko = {self.body}
                Akcesorium = {self.accessory}
                Template = {self.template}
                Tło = {self.frontBg}
                Obwódka = {self.frontBand}
                Rewers = {self.backImg}
            ''')


    def renderCard(self):
        imageWidth, imageHeight = self.template.size

        # nakładanie na siebie kolejnych warstw z parametrami
        # alpha_composite(warstwaNiżej, warstwaWyżej)

        bgLayer = Image.alpha_composite(self.frontBg, self.template)
        bandLayer = Image.alpha_composite(bgLayer, colorize(self.frontBand, self.hue))

        # to samo, ale ze sprawdzaniem czy renderować z atrybutem czy nie

        if len(self.hatName) > 0:
            hatLayer = Image.alpha_composite(bandLayer, self.hat)
        else:    hatLayer = bandLayer

        if len(self.bodyName) > 0:
            bodyLayer = Image.alpha_composite(hatLayer, self.body)
        else:   bodyLayer = hatLayer

        if len(self.accessoryName) > 0:
            accessoryLayer = Image.alpha_composite(bodyLayer, self.accessory)
        else:   accessoryLayer = bodyLayer

        d = ImageDraw.Draw(accessoryLayer)

        # nanoszenie nazwy 

        renderText(self.name, font70, 'black', imageWidth/2, 1180, d)

        # nanoszenie opisu - zawijanie wierszy: textwrap, centrowanie: align='center', anchor="mm"

        if len(self.desc) == 0:
            pass
        else:
            wrapperDesc = textwrap.TextWrapper(width=25)
            word_list = wrapperDesc.wrap(text=self.desc)

            caption_new = ''
            for ii in word_list[:-1]:
                caption_new = caption_new + ii + '\n'
            caption_new += word_list[-1]

            d.multiline_text((imageWidth / 2, 1405), caption_new, fill="black", font=font40, align='center', anchor="mm")

        # nanoszenie statystyk

        renderText(self.stats[0], font90, 'black', 105, 95, d)
        renderText(self.stats[1], font70, 'black', 80, imageHeight - 85, d)
        renderText(self.stats[2], font70, 'black', imageWidth - 80, imageHeight - 85, d)

        # rewers obok, colorize: zmiana koloru rewersu

        self.final = Image.new('RGBA', (2 * imageWidth, imageHeight))
        self.final.paste(accessoryLayer, (0, 0))
        self.final.paste(colorize(self.backImg, self.hue), (imageWidth, 0))

        return self.final
        

    def exportCardToPDF(self, destination: str):
        if destination: self.final.save(destination)
        else: raise Exception("Brak lokalizacji eksportowanego pliku")


    def saveCardEdit(self, destination: str):
        if destination: 
            with open(destination, 'wb') as handle:
                pickle.dump(self, handle, protocol=pickle.HIGHEST_PROTOCOL)
        else: raise Exception("Brak lokalizacji zapisywanego pliku")
