import pygame as pg
from pygame import *
from pygame.locals import *
import sys
from Classes import Button
import random
from Classes import ClassLetter
from Classes import ClassCell
class ClassRusLang:
	def __init__(self, TrueWeight, TrueHeight):
		self.TrueWeight = TrueWeight
		self.TrueHeight = TrueHeight
	def ruslang(self):
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
		def loader2(scr):
			Image = pg.image.load(scr).convert()
			# Image = pg.transform.scale(Image, (w, h))
			Image.set_colorkey((0, 0, 0))
			return Image	
		Centerx = 480
		Centery = 450		
		RusLangBackgroundImage, RusLangBackgroundRect = loader('ImagesForProjects/BackgroundRuslang.png', self.TrueWeight, self.TrueHeight, self.TrueWeight/2, self.TrueHeight/2)
		Back = Button(110*(self.TrueWeight/960), 30*(self.TrueHeight/540), 'ImagesForProjects/BackMenuActive.png', 'ImagesForProjects/BackMenuUnactive.png', 90*(self.TrueWeight/960), 55*(self.TrueHeight/540))
		Again = Button(60*(self.TrueWeight/960), 60*(self.TrueHeight/540), 'ImagesForProjects/AgainActive.png', 'ImagesForProjects/AgainActive.png', 880*(self.TrueWeight/960), 80*(self.TrueHeight/540))
		BackButtonActiveIm, BackButtonActiveRc = loader(Back.activeim, Back.weight, Back.height, Back.centerx, Back.centery)
		BackButtonUnactiveIm, BackButtonUnactiveRc = loader(Back.unactiveim, Back.weight, Back.height, Back.centerx, Back.centery)
		AgainButtonActiveIm, AgainButtonActiveRc = loader(Again.activeim, Again.weight, Again.height, Again.centerx, Again.centery)
		AgainButtonUnactiveIm, AgainButtonUnactiveRc = loader(Again.unactiveim, Again.weight, Again.height, Again.centerx, Again.centery)
		TrueWeightScreen = screen.get_size()[0]
		TrueHeightScreen = screen.get_size()[1]
		WordsList = ['заяц', 'вода', 'гусь', 'нога', 'сила', 'мама', 'зима', 'тина', 'день', 'врач', 'ночь', 'круг', 'лист', 'язык', 'глаз', 'палец', 'зебра', 'пират', 'пирог', 'песня', 'пакет', 'фокус', 'конец', 'плечо', 'чашка', 'марка', 'лампа', 'туман', 'искра', 'батут', 'нитка', 'груша', 'апрель', 'альбом', 'музыка', 'молоко', 'корова', 'ребята', 'погода', 'ананас', 'облако', 'огород']
		a = random.randint(0, len(WordsList)-1)
		CountLetters = len(WordsList[a])
		def WhichLetter(letter):
			if letter == 'а':
				LetterIm = 'Letters/А.png'
			if letter == 'б':
				LetterIm = 'Letters/Б.png'
			if letter == 'в':
				LetterIm = 'Letters/В.png'
			if letter == 'г':
				LetterIm = 'Letters/Г.png'
			if letter == 'д':
				LetterIm = 'Letters/Д.png'
			if letter == 'е':
				LetterIm = 'Letters/Е.png'
			if letter == 'ж':
				LetterIm = 'Letters/Ж.png'
			if letter == 'з':
				LetterIm = 'Letters/З.png'
			if letter == 'и':
				LetterIm = 'Letters/И.png'
			if letter == 'й':
				LetterIm = 'Letters/Й.png'
			if letter == 'к':
				LetterIm = 'Letters/К.png'
			if letter == 'л':
				LetterIm = 'Letters/Л.png'
			if letter == 'м':
				LetterIm = 'Letters/М.png'
			if letter == 'н':
				LetterIm = 'Letters/Н.png'
			if letter == 'о':
				LetterIm = 'Letters/О.png'
			if letter == 'п':
				LetterIm = 'Letters/П.png'
			if letter == 'р':
				LetterIm = 'Letters/Р.png'
			if letter == 'с':
				LetterIm = 'Letters/С.png'
			if letter == 'т':
				LetterIm = 'Letters/Т.png'
			if letter == 'у':
				LetterIm = 'Letters/У.png'
			if letter == 'ф':
				LetterIm = 'Letters/Ф.png'
			if letter == 'х':
				LetterIm = 'Letters/Х.png'
			if letter == 'ц':
				LetterIm = 'Letters/Ц.png'
			if letter == 'ч':
				LetterIm = 'Letters/Ч.png'
			if letter == 'ш':
				LetterIm = 'Letters/Ш.png'
			if letter == 'щ':
				LetterIm = 'Letters/Щ.png'
			if letter == 'ъ':
				LetterIm = 'Letters/Ъ.png'
			if letter == 'ы':
				LetterIm = 'Letters/Ы.png'
			if letter == 'ь': 
				LetterIm = 'Letters/Ь.png'
			if letter == 'э':
				LetterIm = 'Letters/Э.png'
			if letter == 'ю':
				LetterIm = 'Letters/Ю.png'
			if letter == 'я':
				LetterIm = 'Letters/Я.png'
			return LetterIm
		lst2 = [] #Верхние ячейки
		lst3 = [] #Буквы
		lst4 = [] #Нижние ячейки
		u = 1
		for i in WordsList[a]:
			mouse = pg.mouse.get_pos()
			click = pg.mouse.get_pressed()
			Cellweight = 72*self.TrueWeight/960
			Cellheight = 72*self.TrueHeight/540
			CellCenterx = ((480*self.TrueWeight/960)-(Cellweight*((CountLetters/2)-0.5)))+Cellweight*(u-1)
			CellCentery = 240*self.TrueHeight/540
			lst = [Cellweight, Cellheight, CellCenterx, CellCentery]
			lst2.append(lst)
			u+=1
		u = 1
		for i in WordsList[a]:
			mouse = pg.mouse.get_pos()
			click = pg.mouse.get_pressed()
			LetterIm1 = WhichLetter(i)
			Letterweight = 68*self.TrueWeight/960
			Letterheight = 68*self.TrueHeight/540
			Cellweight = 72*self.TrueWeight/960
			Cellheight = 72*self.TrueHeight/540
			CellCenterx = ((480*self.TrueWeight/960)-(Cellweight*((CountLetters/2)-0.5)))+Cellweight*(u-1)
			CellCentery = 450*self.TrueHeight/540
			lst = [LetterIm1, Letterweight, Letterheight, CellCenterx, CellCentery]
			lst3.append(lst)
			u+=1
		for i in range(len(lst2)):
			lst4.append([lst2[i][0], lst2[i][1], lst3[i][3], lst3[i][4]])
		lst4 = lst4 + lst2
		def CellInit(): #Нижние ячейки
			for i in range(len(lst2)):
				Cell = ClassCell('Letters/Cell.png', lst2[i][0], lst2[i][1], lst3[i][3], lst3[i][4])
				Cell.CellUpdate(virtual_surface)
				lst4.append([lst2[i][0], lst2[i][1], lst3[i][3], lst3[i][4]])
		def WordInit(): #Буквы
			TrueWeightScreen = screen.get_size()[0]
			TrueHeightScreen = screen.get_size()[1]
			for i in range(len(lst3)):
				Letter = ClassLetter(lst3[i][0], lst3[i][1], lst3[i][2], lst3[i][3], lst3[i][4])
				Letter.LetterUpdate(TrueWeightScreen, TrueHeightScreen, self.TrueWeight, self.TrueHeight, virtual_surface, lst3)
		def CellInit2(): #Верхние ячейки
			for i in range(len(lst2)):
				# if lst2[i][2] == 
				Cell = ClassCell('Letters/Cell.png', lst2[i][0], lst2[i][1], lst2[i][2], lst2[i][3])
				Cell.CellUpdate(virtual_surface)
		lst4 = lst4 + lst2
		print(lst4)
		# Характеристики кнопок
		def button():
			mouse = pg.mouse.get_pos()
			click = pg.mouse.get_pressed()
			TrueWeightScreen = screen.get_size()[0]
			TrueHeightScreen = screen.get_size()[1]
			# Кнопка назад
			AgainTrueXCenter = Again.centerx*TrueWeightScreen/self.TrueWeight
			AgainTrueYCenter = Again.centery*TrueHeightScreen/self.TrueHeight
			AgainActiveRc = Rect(AgainTrueXCenter-(Again.weight*TrueWeightScreen/self.TrueWeight)/2, AgainTrueYCenter-(Again.height*TrueHeightScreen/self.TrueHeight)/2, Again.weight*TrueWeightScreen/self.TrueWeight, Again.height*TrueHeightScreen/self.TrueHeight) 
			if AgainActiveRc.left < mouse[0] < AgainActiveRc.right and AgainActiveRc.top < mouse[1] < AgainActiveRc.bottom:
				AgainActiveRc = AgainButtonUnactiveRc
				virtual_surface.blit(AgainButtonActiveIm, AgainButtonActiveRc)
				if click[0] == 1:
					from RusLang1Class import ClassRusLang
					GoAgain = ClassRusLang(TrueWeightScreen, TrueHeightScreen)
					GoAgain.ruslang()
			else:
				virtual_surface.blit(AgainButtonUnactiveIm, AgainButtonUnactiveRc)
			# Кнопка заново
			BackTrueXCenter = Back.centerx*TrueWeightScreen/self.TrueWeight
			BackTrueYCenter = Back.centery*TrueHeightScreen/self.TrueHeight
			BackActiveRc = Rect(BackTrueXCenter-(Back.weight*TrueWeightScreen/self.TrueWeight)/2, BackTrueYCenter-(Back.height*TrueHeightScreen/self.TrueHeight)/2, Back.weight*TrueWeightScreen/self.TrueWeight, Back.height*TrueHeightScreen/self.TrueHeight) 
			if BackActiveRc.left < mouse[0] < BackActiveRc.right and BackActiveRc.top < mouse[1] < BackActiveRc.bottom:
				BackActiveRc = BackButtonUnactiveRc
				virtual_surface.blit(BackButtonActiveIm, BackButtonActiveRc)
				if click[0] == 1:
					from SubjectsMenu import ClassSubjectsMenu
					GoBack = ClassSubjectsMenu(TrueWeightScreen, TrueHeightScreen)
					GoBack.subjectsmenu()
			else:
				virtual_surface.blit(BackButtonUnactiveIm, BackButtonUnactiveRc)
		#Инициализация
		while 1:
			for event in pg.event.get():
				if event.type == pg.QUIT:
					pg.quit()
					exit()
				elif event.type == VIDEORESIZE: 
					current_size = event.size
			virtual_surface.blit(RusLangBackgroundImage, RusLangBackgroundRect)
			CellInit()
			CellInit2()
			WordInit()
			button()
			scaled_surface = transform.scale(virtual_surface, current_size)
			screen.blit(scaled_surface, (0, 0))
			pg.display.update()
			clock.tick(30)