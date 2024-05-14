from PIL import Image

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

        # nakładanie na siebie kolejnych warstw z parametrami

        bgLayer = Image.alpha_composite(frontBg, template)
        bandLayer = Image.alpha_composite(bgLayer, frontBand)
        hatLayer = Image.alpha_composite(bandLayer, hat)
        bodyLayer = Image.alpha_composite(hatLayer, body)
        accessoryLayer = Image.alpha_composite(bodyLayer, accessory)

        accessoryLayer.show()
        
