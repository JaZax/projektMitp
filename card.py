from PIL import Image, ImageDraw, ImageFont
import textwrap

font60 = ImageFont.truetype(fr'.\fonts\Roboto_Mono\static\RobotoMono-Medium.ttf', 60)
font40 = ImageFont.truetype(fr'.\fonts\Roboto_Mono\static\RobotoMono-Medium.ttf', 40)

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

        d = ImageDraw.Draw(accessoryLayer)

        # nanoszenie nazwy 

        _, _, wName, hName = d.textbbox((0, 0), self.name, font=font60)
        d.text(((imageWidth-wName)/2, 1150), self.name, font=font60, fill='black')

        # nanoszenie opisu

        wrapperDesc = textwrap.TextWrapper(width=25)
        word_list = wrapperDesc.wrap(text=self.desc)

        caption_new = ''
        for ii in word_list[:-1]:
            caption_new = caption_new + ii + '\n'
        caption_new += word_list[-1]

        d.multiline_text((imageWidth / 2, 1250 + hName + 50), caption_new, fill="black", font=font40, align='center', anchor="mm")


        accessoryLayer.show()
        
