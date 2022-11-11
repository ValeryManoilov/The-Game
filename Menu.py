import pygame as pg
from pygame import *
from pygame.locals import *
import sys
from Classes import Button
class ClassMenu:
	def __init__(self, TrueWeight, TrueHeight):
		self.TrueWeight = TrueWeight
		self.TrueHeight = TrueHeight
	def menu(self):
		pg.init()
		pg.display.set_caption('Название игры')
		screen = pg.display.set_mode((self.TrueWeight, self.TrueHeight), RESIZABLE)
		current_size = screen.get_size()
		virtual_surface = Surface((self.TrueWeight, self.TrueHeight))
		clock = pg.time.Clock()
		def loader(scr, w, h ,x, y):
			Image = pg.image.load(scr).convert()
			Image = pg.transform.scale(Image, (w, h))
			Image.set_colorkey((0, 0, 0))
			Rect = Image.get_rect(center = (x, y))
			return Image, Rect			
		MenuBackgroundImage, MenuBackgroundRect = loader('ImagesForProjects/BackgroundMenu.png', self.TrueWeight, self.TrueHeight, self.TrueWeight/2, self.TrueHeight/2)
		# Характеристики кнопок
		# При 960 540: 300х80 - размеры, (480, 250) - корды центра
		Play = Button(300*(self.TrueWeight/960), 80*(self.TrueHeight/540), 'ImagesForProjects/PlayActive.png', 'ImagesForProjects/PlayUnactive.png', 480*(self.TrueWeight/960), 250*(self.TrueHeight/540))
		PlayButtonActiveIm, PlayButtonActiveRc = loader(Play.activeim, Play.weight, Play.height, Play.centerx, Play.centery)
		PlayButtonUnactiveIm, PlayButtonUnactiveRc = loader(Play.unactiveim, Play.weight, Play.height, Play.centerx, Play.centery)
		# При 960 540: 350х80 - размеры, (480, 350) - корды центра
		Settings = Button (350*(self.TrueWeight/960), 80*(self.TrueHeight/540), 'ImagesForProjects/SettingsActive.png', 'ImagesForProjects/SettingsUnactive.png', 480*(self.TrueWeight/960), 350*(self.TrueHeight/540))
		SettingsButtonActiveIm, SettingsButtonActiveRc = loader(Settings.activeim, Settings.weight, Settings.height, Settings.centerx, Settings.centery)
		SettingsButtonUnactiveIm, SettingsButtonUnactiveRc = loader(Settings.unactiveim, Settings.weight, Settings.height, Settings.centerx, Settings.centery)
		# При 960 540: 250х80 - размеры, (480, 450) - корды центра
		Exit = Button(250*(self.TrueWeight/960), 80*(self.TrueHeight/540), 'ImagesForProjects/ExitActive.png', 'ImagesForProjects/ExitUnactive.png', 480*(self.TrueWeight/960), 450*(self.TrueHeight/540))
		ExitButtonActiveIm, ExitButtonActiveRc = loader(Exit.activeim, Exit.weight, Exit.height, Exit.centerx, Exit.centery)
		ExitButtonUnactiveIm, ExitButtonUnactiveRc = loader(Exit.unactiveim, Exit.weight, Exit.height, Exit.centerx, Exit.centery)
		# Отображение и функции кнопок
		def MenuButtons():
			mouse = pg.mouse.get_pos()
			click = pg.mouse.get_pressed()
			TrueWeightScreen = screen.get_size()[0]
			TrueHeightScreen = screen.get_size()[1]
			# Кнопка Играть
			PlayTrueXCenter = Play.centerx*TrueWeightScreen/self.TrueWeight
			PlayTrueYCenter = Play.centery*TrueHeightScreen/self.TrueHeight
			PlayButtonActiveRc = Rect(PlayTrueXCenter-(Play.weight*TrueWeightScreen/self.TrueWeight)/2, PlayTrueYCenter-(Play.height*TrueHeightScreen/self.TrueHeight)/2, Play.weight*TrueWeightScreen/self.TrueWeight, Play.height*TrueHeightScreen/self.TrueHeight)
			if PlayButtonActiveRc.left < mouse[0] < PlayButtonActiveRc.right and PlayButtonActiveRc.top < mouse[1] < PlayButtonActiveRc.bottom:
				PlayButtonActiveRc = PlayButtonUnactiveRc
				virtual_surface.blit(PlayButtonActiveIm, PlayButtonActiveRc)
				if click[0] == 1:
					from SubjectsMenu import ClassSubjectsMenu
					GoSubjectsMenu = ClassSubjectsMenu(TrueWeightScreen, TrueHeightScreen)
					GoSubjectsMenu.subjectsmenu()
			else:
				virtual_surface.blit(PlayButtonUnactiveIm, PlayButtonUnactiveRc)

			# Кнопка Настройки
			SettingsTrueXCenter = Settings.centerx*TrueWeightScreen/self.TrueWeight
			SettingsTrueYCenter = Settings.centery*TrueHeightScreen/self.TrueHeight
			SettingsButtonActiveRc = Rect(SettingsTrueXCenter-(Settings.weight*TrueWeightScreen/self.TrueWeight)/2, SettingsTrueYCenter-(Settings.height*TrueHeightScreen/self.TrueHeight)/2, Settings.weight*TrueWeightScreen/self.TrueWeight, Settings.height*TrueHeightScreen/self.TrueHeight)
			if SettingsButtonActiveRc.left < mouse[0] < SettingsButtonActiveRc.right and SettingsButtonActiveRc.top < mouse[1] < SettingsButtonActiveRc.bottom:
				SettingsButtonActiveRc = SettingsButtonUnactiveRc
				virtual_surface.blit(SettingsButtonActiveIm, SettingsButtonActiveRc)
			else:
				virtual_surface.blit(SettingsButtonUnactiveIm, SettingsButtonUnactiveRc)

			# Кнопка Выход
			ExitTrueXCenter = Exit.centerx*TrueWeightScreen/self.TrueWeight
			ExitTrueYCenter = Exit.centery*TrueHeightScreen/self.TrueHeight
			ExitButtonActiveRc = Rect(ExitTrueXCenter-(Exit.weight*TrueWeightScreen/self.TrueWeight)/2, ExitTrueYCenter-(Exit.height*TrueHeightScreen/self.TrueHeight)/2, Exit.weight*TrueWeightScreen/self.TrueWeight, Exit.height*TrueHeightScreen/self.TrueHeight)
			if ExitButtonActiveRc.left < mouse[0] < ExitButtonActiveRc.right and ExitButtonActiveRc.top < mouse[1] < ExitButtonActiveRc.bottom:
				ExitButtonActiveRc = ExitButtonUnactiveRc
				virtual_surface.blit(ExitButtonActiveIm, ExitButtonActiveRc)
				if click[0] == 1:
					pg.quit()
					exit()
			else:
				virtual_surface.blit(ExitButtonUnactiveIm, ExitButtonUnactiveRc)
		#Инициализация
		while 1:
			for event in pg.event.get():
				if event.type == pg.QUIT:
					pg.quit()
					exit()
				elif event.type == VIDEORESIZE: 
					current_size = event.size
			virtual_surface.blit(MenuBackgroundImage, MenuBackgroundRect)
			MenuButtons()
			scaled_surface = transform.scale(virtual_surface, current_size)
			screen.blit(scaled_surface, (0, 0))
			pg.display.update()
			clock.tick(30)