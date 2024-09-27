
from gl import *
import pygame
from pygame.locals import *
from Figuras import *
from Material import *
from Lights import *
from texture import Texture
width = 720
height = 720

screen = pygame.display.set_mode((width, height), pygame.SCALED )
clock = pygame.time.Clock()

rt = RendererRT(screen)
rt.enveriomentMap = Texture("Fondo.bmp")
rt.glClearColor(0.5,0.0,0.0)
rt.glClear()


#materiales opacos
redOpaque = Material(texture=Texture("Mundo.bmp"), spec=32, ks=0.1, matType=OPAQUE)
greenOpaque = Material(difuse=[0, 1, 0], spec=64, ks=0.2, matType=OPAQUE)

#materiales reflectivos
mirrorReflective = Material(texture=Texture("Prueba.bmp"), spec=128, ks=0.2, matType=REFLECTIVE)
blueMirrorReflective = Material(difuse=[0.5, 0.5, 1], spec=128, ks=0.2, matType=REFLECTIVE)

#materiales transparentes
glass = Material(texture=Texture("Prueba2.bmp"), ior=1.5, spec=128, ks=0.2, matType=TRANSPARENT)
waterTransparent = Material(ior=1.33, spec=64, ks=0.1, matType=TRANSPARENT)


#Lights 
rt.lights.append(DirectionalLight(direction=[-1,-1,-1], intensity=0.8 ))
rt.lights.append(AmbientLight(intensity=0.1))

#objetos (esferas que vamos a intentar renderizar)
# Esferas opacas
rt.scene.append(Sphere([-2, 1, -5], radius=1, material=redOpaque))     # Esfera roja opaca
rt.scene.append(Sphere([0, 1, -5], radius=1, material=greenOpaque))    # Esfera verde opaca

# Esferas reflectivas
rt.scene.append(Sphere([2, 1, -5], radius=1, material=mirrorReflective))  # Esfera reflectiva blanca
rt.scene.append(Sphere([-2, -1, -5], radius=1, material=blueMirrorReflective))  # Esfera reflectiva azul

# Esferas transparentes
rt.scene.append(Sphere([0, -1, -5], radius=1, material=glass))  # Esfera transparente de vidrio
rt.scene.append(Sphere([2, -1, -5], radius=1, material=waterTransparent))  # Esfera transparente de agua

rt.glRender()
isRunning = True
while isRunning:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			isRunning = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				isRunning = False
				
				
	pygame.display.flip()
	clock.tick(60)
	
pygame.quit()