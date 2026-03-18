from CollideObjectBase import SphereCollideObject
from panda3d.core import Loader, NodePath, Vec3
from direct.task.Task import TaskManager
from typing import Callable
from direct.task import Task
from SpaceJamClasses import Missile

class Spaceship(SphereCollideObject):
    def __init__(self, loader: Loader, taskMgr: TaskManager, accept: Callable[[str, Callable], None], modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        super(Spaceship, self).__init__(loader, modelPath, parentNode, nodeName, Vec3(0,0,0), .75)

        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)
        self.modelNode.setName(nodeName)
        
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)
        self.loader = loader
        
        self.taskMgr = taskMgr
        self.accept = accept
        self.render = parentNode
        
        self.taskMgr.add(self.CheckIntervals, 'checkMissiles', 34)

        self.reloadTime = .25
        self.missleDistance = 4000
        self.missilebay = 1

        self.SetKeyBindings()

    def Fire(self):
        if self.missilebay:
            travRate = self.missleDistance
            aim = self.render.getRelativeVector(self.modelNode, Vec3.forward())
            aim.normalize()
            fireSolution = aim * travRate
            inFront = aim * 150
            travVec = fireSolution + self.modelNode.getPos()
            self.missilebay -= 1
            tag = 'Missile' + str(Missile.missileCount)
            posVec = self.modelNode.getPos() + inFront
            currentMissle = Missile(self.loader, './Assets/Phaser/phaser.egg', self.render, tag, posVec, 4.0)
            Missile.Intervals[tag] = currentMissle.modelNode.posInterval(2.0, travVec, startPos = posVec, fluid = 1)
            Missile.Intervals[tag].start()
        else:
            if not self.taskMgr.hasTaskNamed('reload'):
                print('Starting reload...')
                self.taskMgr.doMethodLater(0, self.Reload, 'reload')
                return Task.cont 

    def Reload(self, task):
        if task.time > self.reloadTime:
            self.missilebay += 1
            print('reload complete')
            return Task.done
        if self.missilebay > 1:
            self.missilebay = 1 
        elif  task.time <= self.reloadTime:
            print('reload proceeding...')
            return Task.cont
    
    def CheckIntervals(self, task):
        for i in Missile.Intervals:
            if not Missile.Intervals[i].isPlaying():
                Missile.cNodes[i].detachNode()
                Missile.fireModels[i].detachNode()
                del Missile.Intervals[i]
                del Missile.fireModels[i]
                del Missile.cNodes[i]
                del Missile.collisonSolids[i]
                print(i + ' has reached the end of its fire solution')
                break
        return Task.cont            
    
    def SetKeyBindings(self):
        self.accept('w', self.Thrust, [1])
        self.accept('w-up', self.Thrust, [0])
        self.accept('a', self.Left, [1])
        self.accept('a-up', self.Left, [0])
        self.accept('d', self.Right, [1])
        self.accept('d-up', self.Right, [0])
        self.accept('s', self.Reverse, [1])
        self.accept('s-up', self.Reverse, [0])
        self.accept('q', self.LeftTurn, [1])
        self.accept('q-up', self.LeftTurn, [0])
        self.accept('e', self.RightTurn, [1])
        self.accept('e-up', self.RightTurn, [0])
        self.accept('1', self.Up, [1])
        self.accept('1-up', self.Up, [0])
        self.accept('2', self.Down, [1])
        self.accept('2-up', self.Down, [0])
        self.accept('f', self.Fire) 
        
    def Thrust(self, keyDown): 
        if keyDown: 
            self.taskMgr.add(self.ApplyThrust, 'forward-thrust') 
        else: self.taskMgr.remove('forward-thrust')

    def ApplyThrust(self, task): 
        trajectory = self.render.getRelativeVector(self.modelNode, Vec3.forward())
        trajectory.normalize() 
        rate = 5 
        self.modelNode.setFluidPos(self.modelNode.getPos() + trajectory * rate) 
        return Task.cont 
    
    def Reverse(self, keyDown): 
        if keyDown: 
            self.taskMgr.add(self.ApplyReverse, 'backwards-thrust') 
        else: self.taskMgr.remove('backwards-thrust') 

    def ApplyReverse(self,task): 
        trajectory = self.render.getRelativeVector(self.modelNode, -Vec3.forward()) 
        trajectory.normalize() 
        rate = 5
        self.modelNode.setFluidPos(self.modelNode.getPos() + trajectory * rate) 
        return Task.cont 
    
    def ApplyLeft(self, task): 
        trajectory = self.modelNode.getRelativeVector(self.modelNode , -Vec3.right())
        trajectory.normalize() 
        rate = 5
        self.modelNode.setFluidPos(self.modelNode.getPos() + trajectory * rate) 
        return Task.cont 
    
    def Left(self, keyDown): 
        if keyDown: 
            self.taskMgr.add(self.ApplyLeft, 'left-thrust') 
        else: self.taskMgr.remove('left-thrust')

    def ApplyRight(self, task): 
        trajectory = self.modelNode.getRelativeVector(self.modelNode, Vec3.right()) 
        trajectory.normalize() 
        rate = 5
        self.modelNode.setFluidPos(self.modelNode.getPos() + trajectory * rate) 
        return Task.cont 
    
    def Right(self, keyDown): 
        if keyDown: 
            self.taskMgr.add(self.ApplyRight, 'right-thrust') 
        else: 
            self.taskMgr.remove('right-thrust') 

    def LeftTurn(self, keyDown): 
        if keyDown: 
            self.taskMgr.add(self.ApplyLeftTurn, 'left-turn') 
        else: 
             self.taskMgr.remove('left-turn') 

    def ApplyLeftTurn(self, task): 
        rate = .5 
        self.modelNode.setH(self.modelNode.getH() + rate)
        return Task.cont 
    
    def RightTurn(self, keyDown): 
        if keyDown: 
            self.taskMgr.add(self.ApplyRightTurn, 'right-turn') 
        else: 
            self.taskMgr.remove('right-turn') 

    def ApplyRightTurn(self, task): 
        rate = .5 
        self.modelNode.setH(self.modelNode.getH() - rate)
        return Task.cont
    
    def ApplyUp(self, task): 
        trajectory = self.modelNode.getRelativeVector(self.modelNode, Vec3.up()) 
        trajectory.normalize() 
        rate = 5
        self.modelNode.setFluidPos(self.modelNode.getPos() + trajectory * rate) 
        return Task.cont 
    
    def Up(self, keyDown): 
        if keyDown: 
            self.taskMgr.add(self.ApplyUp, 'up-thrust') 
        else: 
            self.taskMgr.remove('up-thrust') 

    def ApplyDown(self, task): 
        trajectory = self.modelNode.getRelativeVector(self.modelNode, -Vec3.up()) 
        trajectory.normalize() 
        rate = 5 
        self.modelNode.setFluidPos(self.modelNode.getPos() + trajectory * rate) 
        return Task.cont 
    
    def Down(self, keyDown): 
        if keyDown: 
            self.taskMgr.add(self.ApplyDown, 'down-thrust') 
        else: 
            self.taskMgr.remove('down-thrust')


