import pygame as pg
from pygame import *
from pygame.locals import *
import sys
from Classes import Button
class ClassSubjectsMenu:
	def __init__(self, TrueWeight, TrueHeight):
		self.TrueWeight = TrueWeight
		self.TrueHeight = TrueHeight
	def subjectsmenu(self):
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
		SubjMenuBackgroundImage, SubjMenuBackgroundRect = loader('ImagesForProjects/BackgroundSubjectsMenu.png', self.TrueWeight, self.TrueHeight, self.TrueWeight/2, self.TrueHeight/2)
		# # Характеристики кнопок
		# При 960 540: 280х120 - размеры, (320, 200) - корды центра
		RussianLang = Button(380*(self.TrueWeight/960), 70*(self.TrueHeight/540), 'ImagesForProjects/RusLangActive.png', 'ImagesForProjects/RusLangUnactive.png', 360*(self.TrueWeight/960), 210*(self.TrueHeight/540))
		RLButtonActiveIm, RLButtonActiveRc = loader(RussianLang.activeim, RussianLang.weight, RussianLang.height, RussianLang.centerx, RussianLang.centery)
		RLButtonUnactiveIm, RLButtonUnactiveRc = loader(RussianLang.unactiveim, RussianLang.weight, RussianLang.height, RussianLang.centerx, RussianLang.centery)
		# При 960 540: 320х120 - размеры, (740, 200) - корды центра		
		Maths = Button(320*(self.TrueWeight/960), 70*(self.TrueHeight/540), 'ImagesForProjects/MathsActive.png', 'ImagesForProjects/MathsUnactive.png', 620*(self.TrueWeight/960), 310*(self.TrueHeight/540))
		MathsButtonActiveIm, MathsButtonActiveRc = loader(Maths.activeim, Maths.weight, Maths.height, Maths.centerx, Maths.centery)
		MathsButtonUnactiveIm,MathsButtonUnactiveRc = loader(Maths.unactiveim, Maths.weight, Maths.height, Maths.centerx, Maths.centery)
		# При 960 540: 420х120 - размеры, (480, 430) - корды центра
		Science = Button(470*(self.TrueWeight/960), 75*(self.TrueHeight/540), 'ImagesForProjects/ScienceActive.png', 'ImagesForProjects/ScienceUnactive.png', 410*(self.TrueWeight/960), 430*(self.TrueHeight/540))
		ScButtonActiveIm, ScButtonActiveRc = loader(Science.activeim, Science.weight, Science.height, Science.centerx, Science.centery)
		ScButtonUnactiveIm, ScButtonUnactiveRc = loader(Science.unactiveim, Science.weight, Science.height, Science.centerx, Science.centery)
		Back = Button(110*(self.TrueWeight/960), 30*(self.TrueHeight/540), 'ImagesForProjects/BackMenuActive.png', 'ImagesForProjects/BackMenuUnactive.png', 90*(self.TrueWeight/960), 55*(self.TrueHeight/540))
		BackButtonActiveIm, BackButtonActiveRc = loader(Back.activeim, Back.weight, Back.height, Back.centerx, Back.centery)
		BackButtonUnactiveIm, BackButtonUnactiveRc = loader(Back.unactiveim, Back.weight, Back.height, Back.centerx, Back.centery)
		# # Отображение и функции кнопок
		def SubjectMenuButtons():
			mouse = pg.mouse.get_pos()
			click = pg.mouse.get_pressed()
			TrueWeightScreen = screen.get_size()[0]
			TrueHeightScreen = screen.get_size()[1]
			RLTrueXCenter = RussianLang.centerx*TrueWeightScreen/self.TrueWeight
			RLTrueYCenter = RussianLang.centery*TrueHeightScreen/self.TrueHeight
			# Кнопка Русский язык
			RLButtonActiveRc = Rect(RLTrueXCenter-(RussianLang.weight*TrueWeightScreen/self.TrueWeight)/2, RLTrueYCenter-(RussianLang.height*TrueHeightScreen/self.TrueHeight)/2, RussianLang.weight*TrueWeightScreen/self.TrueWeight, RussianLang.height*TrueHeightScreen/self.TrueHeight)
			if RLButtonActiveRc.left < mouse[0] < RLButtonActiveRc.right and RLButtonActiveRc.top < mouse[1] < RLButtonActiveRc.bottom:
				RLButtonActiveRc = RLButtonUnactiveRc
				virtual_surface.blit(RLButtonActiveIm, RLButtonActiveRc)
				if click[0] == 1:
					from RusLang1Class import ClassRusLang
					GoRusLang = ClassRusLang(TrueWeightScreen, TrueHeightScreen)
					GoRusLang.ruslang()
			else:
				virtual_surface.blit(RLButtonUnactiveIm, RLButtonUnactiveRc)

			# Кнопка Математика
			MathsTrueXCenter = Maths.centerx*TrueWeightScreen/self.TrueWeight
			MathsTrueYCenter = Maths.centery*TrueHeightScreen/self.TrueHeight
			MathsButtonActiveRc = Rect(MathsTrueXCenter-(Maths.weight*TrueWeightScreen/self.TrueWeight)/2, MathsTrueYCenter-(Maths.height*TrueHeightScreen/self.TrueHeight)/2, Maths.weight*TrueWeightScreen/self.TrueWeight, Maths.height*TrueHeightScreen/self.TrueHeight)
			if MathsButtonActiveRc.left < mouse[0] < MathsButtonActiveRc.right and MathsButtonActiveRc.top < mouse[1] < MathsButtonActiveRc.bottom:
				MathsButtonActiveRc = MathsButtonUnactiveRc
				virtual_surface.blit(MathsButtonActiveIm, MathsButtonActiveRc)
			else:
				virtual_surface.blit(MathsButtonUnactiveIm,MathsButtonUnactiveRc)

			# Кнопка Окружающий мир
			ScienceTrueXCenter = Science.centerx*TrueWeightScreen/self.TrueWeight
			ScienceTrueYCenter = Science.centery*TrueHeightScreen/self.TrueHeight
			ScButtonActiveRc = Rect(ScienceTrueXCenter-(Science.weight*TrueWeightScreen/self.TrueWeight)/2, ScienceTrueYCenter-(Science.height*TrueHeightScreen/self.TrueHeight)/2, Science.weight*TrueWeightScreen/self.TrueWeight, Science.height*TrueHeightScreen/self.TrueHeight) 
			if ScButtonActiveRc.left < mouse[0] < ScButtonActiveRc.right and ScButtonActiveRc.top < mouse[1] < ScButtonActiveRc.bottom:
				ScButtonActiveRc = ScButtonUnactiveRc
				virtual_surface.blit(ScButtonActiveIm, ScButtonActiveRc)
			else:
				virtual_surface.blit(ScButtonUnactiveIm, ScButtonUnactiveRc)

			# Кнопка <-- 
			BackTrueXCenter = Back.centerx*TrueWeightScreen/self.TrueWeight
			BackTrueYCenter = Back.centery*TrueHeightScreen/self.TrueHeight
			BackActiveRc = Rect(BackTrueXCenter-(Back.weight*TrueWeightScreen/self.TrueWeight)/2, BackTrueYCenter-(Back.height*TrueHeightScreen/self.TrueHeight)/2, Back.weight*TrueWeightScreen/self.TrueWeight, Back.height*TrueHeightScreen/self.TrueHeight) 
			if BackActiveRc.left < mouse[0] < BackActiveRc.right and BackActiveRc.top < mouse[1] < BackActiveRc.bottom:
				BackActiveRc = BackButtonUnactiveRc
				virtual_surface.blit(BackButtonActiveIm, BackButtonActiveRc)
				if click[0] == 1:
					from Menu import ClassMenu
					GoMenu = ClassMenu(TrueWeightScreen, TrueHeightScreen)
					GoMenu.menu()
			else:
				virtual_surface.blit(BackButtonUnactiveIm, BackButtonUnactiveRc)
		#Главный Цикл 
		while 1:
			for event in pg.event.get():
				if event.type == pg.QUIT:
					pg.quit()
					exit()
				elif event.type == VIDEORESIZE: 
					current_size = event.size
			virtual_surface.blit(SubjMenuBackgroundImage, SubjMenuBackgroundRect)
			SubjectMenuButtons()
			scaled_surface = transform.scale(virtual_surface, current_size)
			screen.blit(scaled_surface, (0, 0))
			pg.display.update()
			clock.tick(30)