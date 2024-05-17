from PIL import Image, ImageDraw, ImageFont
import textwrap
import numpy as np
import colorsys

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
    def __init__(self, name: str, desc: str, stats: list, hat, body, accessory, template, frontBg, frontBand, backImg, hue: int):
        self.name = name
        self.desc = desc
        self.stats = stats # (mana, stamina, health)
        self.hat = hat
        self.body = body
        self.accessory = accessory
        self.template = template
        self.frontBg = frontBg
        self.frontBand = frontBand
        self.backImg = backImg
        self.hue = hue

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
        print("Rendering card...")

        imageWidth, imageHeight = self.template.size

        # nakładanie na siebie kolejnych warstw z parametrami
        # alpha_composite(warstwaNiżej, warstwaWyżej)

        bgLayer = Image.alpha_composite(self.frontBg, self.template)
        bandLayer = Image.alpha_composite(bgLayer, colorize(self.frontBand, self.hue))
        hatLayer = Image.alpha_composite(bandLayer, self.hat)
        bodyLayer = Image.alpha_composite(hatLayer, self.body)
        accessoryLayer = Image.alpha_composite(bodyLayer, self.accessory)

        d = ImageDraw.Draw(accessoryLayer)

        # nanoszenie nazwy 

        _, _, wName, hName = d.textbbox((0, 0), self.name, font=font90)
        d.text((imageWidth/2, 1200), self.name, font=font90, fill='black', align='center', anchor="mm")

        # nanoszenie opisu - zawijanie wierszy: textwrap, centrowanie: align='center', anchor="mm"

        wrapperDesc = textwrap.TextWrapper(width=20)
        word_list = wrapperDesc.wrap(text=self.desc)

        caption_new = ''
        for ii in word_list[:-1]:
            caption_new = caption_new + ii + '\n'
        caption_new += word_list[-1]

        d.multiline_text((imageWidth / 2, 1275 + hName + 50), caption_new, fill="black", font=font40, align='center', anchor="mm")

        # nanoszenie statystyk

        renderText(self.stats[0], font90, 'black', 105, 95, d)
        renderText(self.stats[1], font70, 'black', 80, imageHeight - 85, d)
        renderText(self.stats[2], font70, 'black', imageWidth - 80, imageHeight - 85, d)

        # rewers obok, colorize: zmiana koloru rewersu

        dst = Image.new('RGBA', (2 * imageWidth, imageHeight))
        dst.paste(accessoryLayer, (0, 0))
        dst.paste(colorize(self.backImg, self.hue), (imageWidth, 0))
        
        return dst
        
