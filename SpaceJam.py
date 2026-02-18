from direct.showbase.ShowBase import ShowBase
import random
class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.SetupScene()
    def SetupScene(self):
        self.Universe = self.loader.loadModel('./Assets/Universe/Universe/Universe.x')
        self.Universe.reparentTo(self.render)
        self.Universe.setScale(15000)
        tex1 = self.loader.loadTexture('./Assets/Universe/Universe.jpg')
        self.Universe.setTexture(tex1, 1)
        textures = [
            './Assets/Planets/Venus.jpg',
            './Assets/Planets/Mercury.jpg',
            './Assets/Planets/Earth.jpg',
            './Assets/Planets/Mars.jpg',
            './Assets/Planets/Neptune.jpg',
            './Assets/Planets/Pink Planet.jpg',
        ]
        self.planets = []
        for tex in textures:
            Planets = self.loader.loadModel('./Assets/Planets/protoPlanet.x')
            Planets.reparentTo(self.render)
            Planets.setPos(
                random.randint(-13000,13000),
                random.randint(-5000, 5000),
                random.randint(-8000, 8000))
            Planets.setScale(250)
            Planets.setH(90)
            textures = self.loader.loadTexture(tex)
            Planets.setTexture(textures, 1)
            self.planets.append(Planets)
        
        self.SpaceStation = self.loader.loadModel('./Assets/Space Station/SpaceStation1B/spaceStation.x')
        self.SpaceStation.reparentTo(self.render)
        self.SpaceStation.setScale(300)
        self.SpaceStation.setPos(
            random.randint(-13000, 13000),
            random.randint(-5000, 5000),
            random.randint(-8000, 8000))
        self.SpaceShip = self.loader.loadModel('./Assets/Spaceships/Dumbledore/Dumbledore.x')
        self.SpaceShip.reparentTo(self.render)
        self.SpaceShip.setScale(150)
        self.SpaceShip.setPos(0,1000,0)

app=MyApp()
app.run()