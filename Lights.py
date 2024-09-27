import numpy as np
from MathLib import *
class Light(object):
  def __init__(self, color = [1,1,1], intensity = 1, lightType = "None"):
    self.color = color
    self.intensity = intensity
    self.lightType = lightType

  def GetLightColor(self, intercept = None):
    return [(i* self.intensity) for i in self.color]

  def GetSpecularColor(self, intercept, viewPos):
    return [0,0,0]




class AmbientLight(Light):
  def __init__(self, color=[1, 1, 1], intensity=1):
    super().__init__(color, intensity, "Ambient")
  

class DirectionalLight(Light):
  def __init__(self, color=[1, 1, 1], intensity=1, direction = {0,-1,0}):
    super().__init__(color, intensity,"Directional")
    self.direction = direction / np.linalg.norm(direction)
  
  def GetLightColor(self, intercept = None):
    lightColor = super().GetLightColor()
    if intercept:
      dir = [-x for x in self.direction]
      intensity = np.dot(intercept.normal, dir)
      intensity = max(0, min(1, intensity))
      intensity *= (1-intercept.obj.material.ks)
      lightColor = [(i * intensity ) for i in lightColor]
    return lightColor
  
  def GetSpecularColor(self, intercept, viewPos):
    specColor = self.color
    if intercept:
      dir =  [-x for x in self.direction]
      reflect  = reflectVector(intercept.normal, dir)
      viewDIr = np.subtract(viewPos, intercept.point)
      viewDIr /= np.linalg.norm(viewDIr)
      specularity = max(0,np.dot(viewDIr, reflect)) ** intercept.obj.material.spec
      specularity *= intercept.obj.material.ks
      specularity *= self.intensity
      specColor = [(i*specularity) for i in specColor]
    return specColor