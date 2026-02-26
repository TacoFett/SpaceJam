import math, random
from direct.showbase.ShowBase import ShowBase
class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        x = 0
        for i in range(100):
            theta = 2 * math.pi * i / 100 
            self.placeholder2 = self.render.attachNewNode('Placeholder2')
            self.parent = self.loader.loadModel("./Assets/Drone Defender/DroneDefender/DroneDefender.obj")
            self.parent.setScale(0.4)
            self.placeholder2.setPos(50.0 * math.cos(theta), 50.0 * math.sin(theta), 0.0)
            self.placeholder2.setColorScale(1.0, 0.0, 0.0, 1.0)  
            self.parent.instanceTo(self.placeholder2)
app = MyApp()
app.run()



# x,y,0 = random xz ring 0,y,z = random zy ring x,0,z = random xy ring
