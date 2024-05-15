from PIL import Image, ImageDraw, ImageFont
import textwrap

font90 = ImageFont.truetype(fr'.\fonts\Roboto_Mono\static\RobotoMono-Bold.ttf', 90)
font70 = ImageFont.truetype(fr'.\fonts\Roboto_Mono\static\RobotoMono-Bold.ttf', 70)
font60 = ImageFont.truetype(fr'.\fonts\Roboto_Mono\static\RobotoMono-Bold.ttf', 60)
font40 = ImageFont.truetype(fr'.\fonts\Roboto_Mono\static\RobotoMono-Medium.ttf', 40)

# klasa tworząca karte z podanych parametrów

class card:
    def __init__(self, name: str, desc: str, stats: list, hat, body, accessory, template, frontBg, frontBand, backImg):
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
        bandLayer = Image.alpha_composite(bgLayer, self.frontBand)
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

        _, _, wMana, hMana = d.textbbox((50 , 50), self.stats[0], font=font90)
        d.text((105 , 95), self.stats[0], font=font90, fill='black', align='center', anchor="mm")

        _, _, wStamina, hStamina = d.textbbox((50 , 50), self.stats[1], font=font70)
        d.text((80 , imageHeight - 85), self.stats[1], font=font70, fill='black', align='center', anchor="mm")

        _, _, wHealth, hHealth = d.textbbox((50 , 50), self.stats[1], font=font70)
        d.text((imageWidth - 80 , imageHeight - 85), self.stats[1], font=font70, fill='black', align='center', anchor="mm")

        accessoryLayer.show()
        
