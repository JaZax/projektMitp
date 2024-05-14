from PIL import Image, ImageDraw, ImageFont
import textwrap

font60 = ImageFont.truetype(fr'C:\Users\Iza\Desktop\studia\mitp\projektMitp\fonts\Roboto_Mono\static\RobotoMono-Medium.ttf', 60)
font40 = ImageFont.truetype(fr'C:\Users\Iza\Desktop\studia\mitp\projektMitp\fonts\Roboto_Mono\static\RobotoMono-Medium.ttf', 40)


# klasa tworząca karte z podanych parametrów

class card:
    def __init__(self, name, desc, hat, body, accessory, template, frontBg, frontBand, backImg):
        self.name = name
        self.desc = desc
        self.hat = hat
        self.body = body
        self.accessory = accessory
        self.template = template
        self.frontBg = frontBg
        self.frontBand = frontBand
        self.backImg = backImg

    def printCardData(self):
        print(f'''
                Nazwa = {self.name}
                Opis = {self.desc}
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

        template = Image.open(self.template)
        frontBg = Image.open(self.frontBg)
        frontBand = Image.open(self.frontBand)
        hat = Image.open(self.hat)
        body = Image.open(self.body)
        accessory = Image.open(self.accessory)

        imageWidth = template.size[0]
        imageHeight = template.size[1]

        # nakładanie na siebie kolejnych warstw z parametrami
        # alpha_composite(warstwaNiżej, warstwaWyżej)

        bgLayer = Image.alpha_composite(frontBg, template)
        bandLayer = Image.alpha_composite(bgLayer, frontBand)
        hatLayer = Image.alpha_composite(bandLayer, hat)
        bodyLayer = Image.alpha_composite(hatLayer, body)
        accessoryLayer = Image.alpha_composite(bodyLayer, accessory)

        # nanoszenie nazwy 

        d = ImageDraw.Draw(accessoryLayer)
        _, _, wName, hName = d.textbbox((0, 0), self.name, font=font60)
        d.text(((imageWidth-wName)/2, 1150), self.name, font=font60, fill='black')

        # nanoszenie opisu

        wrapperDesc = textwrap.TextWrapper(width=28)
        word_list = wrapperDesc.wrap(text=self.desc)

        caption_new = ''.center(28)
        for ii in word_list[:-1]:
            caption_new = caption_new + ii + '\n'
        caption_new += word_list[-1]
        print(word_list)

        _, _, wDesc, hDesc = d.textbbox((0, 0), word_list[0], font=font40)

        d.multiline_text(((imageWidth - wDesc) / 2, 1150 + hName + 50), caption_new, fill="black", font=font40)


        accessoryLayer.show()
        
