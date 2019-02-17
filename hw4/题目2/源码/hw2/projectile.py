from math import sin, cos, radians

class Projectile:

     def __init__(self, angle, velocity, height,):
          """
          Create a projectile with given launch angle, initial
          velocity and height.
          """
          self.xpos = 0.0
          self.ypos = height
          theta = radians(angle)
          self.xvel = velocity * cos(theta)
          self.yvel = velocity * sin(theta)
          self.maxypos = height

     def update(self, time):
          """Update the state of this projectile to move it time seconds
          farther into its flight"""
          self.xpos = self.xpos + time * self.xvel
          yvel1 = self.yvel - 9.8 * time
          self.ypos = self.ypos + time * (self.yvel + yvel1) / 2.0
          self.maxypos = max(self.maxypos, self.ypos)
          self.yvel = yvel1

     def getY(self):
          "Returns the y position (height) of this projectile."
          return self.ypos

     def getX(self):
          "Returns the x position (distance) of this projectile."
          return self.xpos

     def getMaxY(self):
          "Returns MAX height of this projectile."
          return self.maxypos