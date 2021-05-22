import pygame
import math


pygame.init()
pygame.font.init()

Dimensions = (1067, 650) #2,02m == 1067
Window = pygame.display.set_mode(Dimensions)
Title = pygame.display.set_caption("FLL Dimentions Simulation")
Bg = pygame.image.load(r"FLL2021.png")

DimensionsRobotXcm = float(input("Comprimento [cm]: "))#16
DimensionsRobotYcm = float(input("Largura [cm]: "))#15
DimensionsRobotXpx = ((DimensionsRobotXcm * 1067) / 202)
DimensionsRobotYpx = ((DimensionsRobotYcm * 1067) / 202)


HeaderDraw = pygame.Surface((1100, 50))
HeaderDraw.fill((0,104,250))
RobotDraw = pygame.Surface((DimensionsRobotXpx, DimensionsRobotYpx))
RobotDraw.fill((255, 0, 0))
RobotCenterDraw = pygame.Surface((DimensionsRobotXpx / 10, DimensionsRobotYpx / 10))
RobotCenterDraw.fill((55,0,0))

UseGriD = 0
CoordinateX = 0
CoordinateY = 0
MouseX = 0
MouseX = 0
MouseCoordinates = 0

ClickMouseSetup = 1
SelectDirection = 0
MovingToDirection = 0

Hipotenusa = 0
Tangente = 0
CatetoO = 0
CatetoA = 0

Degrees = 0
errorDeg = False

Lines = []
Distances = []
Angles = []
lenMov = 0

while True:
	while ClickMouseSetup:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit(0)
			if event.type == pygame.MOUSEBUTTONDOWN:
				if Degrees != 0:
					pass
				else:
					ClickMouseSetup = 0
					SelectDirection = 1
					MovingToDirection = 0

		MouseCoordinates = pygame.mouse.get_pos()
		MouseX, MouseY = MouseCoordinates

		RobotDraw.set_colorkey((0,0,0))
		RobotCenterDraw.set_colorkey((0,0,0))
		Window.fill((0,0,0))
		Window.blit(Bg, (0,50))

		Key = pygame.key.get_pressed()
		if Key[ord("a")]:
			UseGriD = not(UseGriD)
			pygame.time.delay(200)
		if Key[ord("c")]:
			Degrees = 0
		if Key[ord(".")]:
			Degrees -= 1
		if Key[ord(",")]:
			Degrees += 1
		if Degrees >= 360 or Degrees <= -360:
			Degrees = 0
		if Degrees != 0:
			errorDeg = True
		elif Degrees == 0:
			errorDeg = False

		CoordinateX, CoordinateY = MouseX, MouseY
		if UseGriD:
			for x in range(5, 1100, 16):
				pygame.draw.line(Window, (100, 100, 100), (x, 0), (x, 1100)) #31quadrados == 47.4cm
			for y in range(55, 1100, 21):
				pygame.draw.line(Window, (100, 100, 100), (0, y), (1100, y))
		
		Window.blit(HeaderDraw, (0,0))

		if (CoordinateX < ((DimensionsRobotXpx / 2) + 6)) and (MouseX < ((DimensionsRobotXpx / 2) + 6)):
			CoordinateX = ((DimensionsRobotXpx / 2) + 6)
			MouseX = ((DimensionsRobotXpx / 2) + 6)
		if (CoordinateX > (1062 - (DimensionsRobotXpx / 2))) and (MouseX > (1062 - (DimensionsRobotXpx / 2))):
			CoordinateX = (1062 - (DimensionsRobotXpx / 2))
			MouseX = (1062 - (DimensionsRobotXpx / 2))
		if (CoordinateY < ((DimensionsRobotYpx / 2) + 55)) and (MouseY < ((DimensionsRobotYpx / 2) + 55)):
			CoordinateY = ((DimensionsRobotYpx / 2) + 55)
			MouseY = ((DimensionsRobotYpx / 2) + 55)
		if (CoordinateY > (646 - (DimensionsRobotYpx / 2))) and (MouseY > (646 - (DimensionsRobotYpx / 2))):
			CoordinateY = (646 - (DimensionsRobotYpx / 2))
			MouseY = (646 - (DimensionsRobotYpx / 2))

		RobotDrawCopy = pygame.transform.rotate(RobotDraw, Degrees)
		RobotCenterDrawCopy = pygame.transform.rotate(RobotCenterDraw, Degrees)
		Window.blit(RobotDrawCopy, (MouseX - int(RobotDrawCopy.get_width() / 2), MouseY - int(RobotDrawCopy.get_height() / 2)))
		Window.blit(RobotCenterDrawCopy, (MouseX - int(RobotCenterDrawCopy.get_width() / 2), MouseY - int(RobotCenterDrawCopy.get_height() / 2)))

		FontSys = pygame.font.SysFont("Consolas", 14)
		Font = FontSys.render("Coloque o Robô.", 5, (0,9,155))
		Window.blit(Font,(10,5))
		Font = FontSys.render("Degrees: {}.".format(Degrees), 5, (0,9,155))
		Window.blit(Font,(10,18))
		if errorDeg:
			Font = FontSys.render("Press 'C'", 5, (0,9,155))
			Window.blit(Font,(10,31))


		pygame.display.update()
		pygame.time.delay(20)


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
	while SelectDirection:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit(0)
			if event.type == pygame.MOUSEBUTTONDOWN:
				if Degrees != 0:
					pass
				else:
					Lines.append([(MouseX, MouseY), (int(CoordinateX + 4 - ((DimensionsRobotXpx / 10)/ 2)), int(CoordinateY + 4 - ((DimensionsRobotYpx / 10)/2)))])
					Distances.append(float("{:.2f}".format(Hipotenusa)))
					Angles.append(float("{:.2f}".format(Tangente)))
					print("-------------------------->")
					print("Movimento:", lenMov)
					print("Distancias:", Distances[lenMov])
					print("Angulos:", Angles[lenMov])
					print("<--------------------------")
					lenMov = lenMov + 1
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_z and len(Lines) > 1:
					Lines.pop()
					Distances.pop()
					Angles.pop()
					lenMov = lenMov - 1

		Window.fill((0,0,0))
		Window.blit(Bg, (0,50))
		RobotDraw.set_colorkey((0,0,0))
		Key = pygame.key.get_pressed()
		if Key[ord("a")]:
			UseGriD = not(UseGriD)
			pygame.time.delay(200)
		if UseGriD:
			for x in range(5, 1100, 16):
				pygame.draw.line(Window, (100, 100, 100), (x, 0), (x, 1100)) #31quadrados == 47.4cm
			for y in range(55, 1100, 21):
				pygame.draw.line(Window, (100, 100, 100), (0, y), (1100, y))
		
		MouseCoordinates = pygame.mouse.get_pos()
		MouseX, MouseY = MouseCoordinates
		if len(Lines) > 0:
			CoordinateX = Lines[len(Lines)-1][0][0]
			CoordinateY = Lines[len(Lines)-1][0][1]
		Window.blit(HeaderDraw, (0,0))
		
		RobotDrawCopy = pygame.transform.rotate(RobotDraw, Degrees)
		RobotCenterDrawCopy = pygame.transform.rotate(RobotCenterDraw, Degrees)
		Window.blit(RobotDrawCopy, (CoordinateX - int(RobotDrawCopy.get_width() / 2), CoordinateY - int(RobotDrawCopy.get_height() / 2)))
		Window.blit(RobotCenterDrawCopy, (CoordinateX - int(RobotCenterDrawCopy.get_width() / 2), CoordinateY - int(RobotCenterDrawCopy.get_height() / 2)))

		if MouseX < 5:
			MouseX = 5
		if MouseX > 1062:
			MouseX = 1062
		if MouseY < 55:
			MouseY = 55
		if MouseY > 645:
			MouseY = 645

		if CatetoO != 0 and CatetoA != 0:
			Hipotenusa = math.sqrt(math.pow(CatetoA, 2) + math.pow(CatetoO, 2))
			Hipotenusa = ((Hipotenusa * 2.02) / 1067) * 100
			Tangente = ((CatetoO * 2.02) / 1067) / ((CatetoA * 2.02) / 1067)
			Tangente = (math.atan(Tangente) * 57.2958)
			Tangente = Tangente - Degrees

		if (CoordinateX <= MouseX):
			CatetoA = (MouseX - CoordinateX) + 2
			pygame.draw.rect(Window, (0, 0, 255), [CoordinateX - ((DimensionsRobotXpx/20)/2), CoordinateY - ((DimensionsRobotYpx/20)/2), CatetoA, 4])

		if (CoordinateY <= MouseY):
			CatetoO = (MouseY - CoordinateY) + 2
			pygame.draw.rect(Window, (0, 0, 255), [CoordinateX - ((DimensionsRobotXpx/20)/2), CoordinateY - ((DimensionsRobotYpx/20)/2), 4, CatetoO])

		if (CoordinateX > MouseX):
			CatetoA = (CoordinateX - MouseX)
			pygame.draw.rect(Window, (0, 0, 255), [MouseX, CoordinateY - ((DimensionsRobotYpx/20)/2), CatetoA, 4])

		if (CoordinateY > MouseY):
			CatetoO = (CoordinateY - MouseY) + 2
			pygame.draw.rect(Window, (0, 0, 255), [CoordinateX - ((DimensionsRobotXpx/20)/2), MouseY, 4, CatetoO])

		if Key[ord("l")]:
			for i in range(len(Lines)):
				pygame.draw.polygon(Window, (10,10,245), [Lines[i][0], Lines[i][1], Lines[i][0]], 4)
			pygame.draw.polygon(Window, (10,10,245), [(MouseX, MouseY), (CoordinateX + 4 - ((DimensionsRobotXpx / 10)/ 2), CoordinateY + 4 - ((DimensionsRobotYpx / 10)/2)), (MouseX, MouseY)], 4)

		sdeaeKey = pygame.key.get_pressed()
		if Key[ord("r")]:
			ClickMouseSetup = 1
			SelectDirection = 0
			MovingToDirection = 0
			Distances = []
			Angles = []
			Lines = []
			lenMov = 0
		if Key[ord("c")]:
			Degrees = 0
		if Key[ord(".")]:
			Degrees -= 1
		if Key[ord(",")]:
			Degrees += 1
		if Degrees >= 360 or Degrees <= -360:
			Degrees = 0
		if Degrees != 0:
			errorDeg = True
		elif Degrees == 0:
			errorDeg = False

		FontSys = pygame.font.SysFont("Consolas", 14)
		Font = FontSys.render("Dist: {:.2f}cm".format(Hipotenusa), 5, (0,9,155))
		Window.blit(Font,(10,5))

		Font = FontSys.render("Graus: {:.1f}°".format(Tangente), 5, (0,9,155))
		Window.blit(Font,(10,18))

		Font = FontSys.render("GrausIn: {:.1f}°".format(Degrees), 5, (0,9,155))
		Window.blit(Font,(10,31))
		if errorDeg:
			FontSys = pygame.font.SysFont("Consolas", 18)
			Font = FontSys.render("Press 'C'", 5, (0,9,155))
			Window.blit(Font,(150,15))

		
		pygame.time.delay(20)
		pygame.display.update()
