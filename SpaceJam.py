from direct.showbase.ShowBase import ShowBase
#import DefensePaths as defensePaths
import SpaceJamClasses as SpaceJamClasses
import random
class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.SetupScene()
    def SetupScene(self):
        self.Universe = SpaceJamClasses.Universe(self.loader, "./Assets/Universe/Universe/Universe.x", self.render, 'Universe', "Assets/Universe/Universe.jpg", (0,0,0), 10000)
        self.Planet1 = SpaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet1', "Assets/Planets/Venus.jpg", (-3987, 3207, -2121), 495)
        self.Planet2 = SpaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet2', "Assets/Planets/Mercury.jpg", (7722, 6445, 2563), 225)
        self.Planet3 = SpaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet3', "Assets/Planets/Earth.jpg", (1932, 1472, -7752), 500)
        self.Planet4 = SpaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet4', "Assets/Planets/Mars.jpg", (5449, 7330, -852), 285)
        self.Planet5 = SpaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet5', "Assets/Planets/Jupiter.jpg", (3804, -1679, 6040), 800)
        self.Planet6 = SpaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet6', "Assets/Planets/Neptune.jpg", (-6022, -5789, -4502), 565)
        self.Planet7 = SpaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet7', "Assets/Planets/Pink Planet.jpg", (-1728, -3244, 4692), 615)
        self.SpaceStation1 = SpaceJamClasses.SpaceStation(self.loader, "./Assets/Space Station/SpaceStation1B/spaceStation.egg", self.render, 'Space Station', "Assets/Space Station/SpaceStation1B/SpaceStation1_Dif2.png", (0,6600,0), 95)
        self.Player = SpaceJamClasses.Player(self.loader, "./Assets/Spaceships/Dumbledore/Dumbledore.egg", self.render, 'Player', "Assets/Spaceships/Dumbledore/spacejet_C.png", (-100,1200,-200), 300)
    
    #def DrawBaseballSeams(self, centralObject, droneName, step, numSeams, radius = 1):
        #unitVec = defensePaths.BaseballSeams(step, numSeams, B = 0.4)
        #unitVec.normalize()
        #position = unitVec * radius * 250 + centralObject.modelNode.getPos()
        #SpaceJamClasses.Drone(self.loader, "./Assets/Drone Defender/DroneDefender.obj", self.render, droneName, "./Assets/Drone Defender/octotoad1_auv.png", position, 5)

    #def DrawCloudDefense(self, centralObject, droneName):
        #unitVec = defensePaths.Cloud()
        #unitVec.normalize()
        #position = unitVec * 500 + centralObject.modelNode.getPos()
        #SpaceJamClasses.Drone(self.loader, "./Assets/Drone Defender/DroneDefender.obj", self.render, droneName, "./Assets/Drone Defender/octotoad1_auv.png", position, 10)

    #fullCycle = 60
    #for j in range(fullCycle):
        #SpaceJamClasses.Drone.droneCount += 1
       # nickName = "Drone" + str(SpaceJamClasses.Drone.droneCount)

        #self.DrawCloudDefense(self.Planet1, nickName)
        #self.DrawBaseballSeam(self.SpaceStation1, nickName, j, fullCycle, 2)

app=MyApp()
app.run()