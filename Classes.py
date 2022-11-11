import pygame as pg
from pygame import *
from pygame.locals import *

class Button:
	def __init__(self, weight, height, activeim, unactiveim, centerx, centery):
		self.weight = weight
		self.height = height
		self.activeim = activeim
		self.unactiveim = unactiveim
		self.centerx = centerx
		self.centery = centery

class ClassLetter(pg.sprite.Sprite):	
	def __init__(self, picture, weight, height, centerx, centery):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.image.load(picture).convert()
		self.image = pg.transform.scale(self.image, (weight, height))
		self.image.set_colorkey((0, 0, 0))
		self.rect = self.image.get_rect(center = (centerx, centery))
		self.weight = weight
		self.height = height
		self.centerx = centerx
		self.centery = centery
	def LetterUpdate(self, TrueWeightScreen, TrueHeightScreen, WeightScreen, HeightScreen, virtual_surface, lst3):
		mouse = pg.mouse.get_pos()
		click = pg.mouse.get_pressed()
		TrueCenterx = self.centerx*TrueWeightScreen/WeightScreen
		TrueCentery = self.centery*TrueHeightScreen/HeightScreen
		TrueRect = Rect(TrueCenterx-(self.weight*TrueWeightScreen/WeightScreen)/2, TrueCentery-(self.height*TrueHeightScreen/HeightScreen)/2, self.weight*TrueWeightScreen/WeightScreen, self.height*TrueHeightScreen/HeightScreen)
		if click[0] == 1 and TrueRect.left < mouse[0] < TrueRect.right and TrueRect.top < mouse[1] < TrueRect.bottom:
			self.rect = self.image.get_rect(center = (mouse[0]/(TrueWeightScreen/WeightScreen), mouse[1]/(TrueHeightScreen/HeightScreen)))
			virtual_surface.blit(self.image, self.rect)
			# print(lst3)
			# Sprite.kill()	
		else:
			virtual_surface.blit(self.image, self.rect)

class ClassCell(pg.sprite.Sprite):
	def __init__(self, picture, weight, height, centerx, centery):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.image.load(picture).convert()
		self.image = pg.transform.scale(self.image, (weight, height))
		self.image.set_colorkey((0, 0, 0))
		self.rect = self.image.get_rect(center = (centerx, centery))
		self.weight = weight
		self.height = height
		self.centerx = centerx
		self.centery = centery
	# def Cention(self):
	def CellUpdate(self, virtual_surface):
		virtual_surface.blit(self.image, self.rect)

