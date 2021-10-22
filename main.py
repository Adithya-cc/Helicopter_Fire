import pygame  #pip instlaa pygame
import time
import random 
import math
import sys
import socket   #pip install sockets
import smtplib  #pip install secure-smtplib
import pyrebase     #pip install Pyrebase4
import subprocess       #pip install subprocess32
from tkinter import *
from threading import Timer
from operator import itemgetter
from PyQt5 import QtWidgets, QtCore, QtGui  pip install PyQt5
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5.uic import loadUi
from firebase import firebase    #pip install firebase
sys.setrecursionlimit(1500)
global playg
playg = False
global startm
startm = False
exitmain = True
global retrygm
retrygm = False
W = 750
global f
f = 0
global high_score
high_score = 0
global player
player = 1
global drc
drc = u"New folder/Player1"
global color
color="Player"
title = "Helicopter Fire"
icon = "data\icon.png"
done = False
def hig_score():
    with open('data/highscore.txt', 'r') as f:
        return f.read()
def colour():
    with open('data/color.txt', 'r') as f:
        return f.read()
def username():
    with open("data/user_status.txt", "r")as f:
        return f.read()
def get_loged_in():
    with open("data\logstatus.txt", "r") as f:
        return f.read()
global logload
if get_loged_in() == "0":
    logload = False
elif get_loged_in() == "1":
    logload = True
base = firebase.FirebaseApplication('https://authdum-default-rtdb.firebaseio.com/')
##################################################################################
firebaseConfig = {
    'apiKey': "AIzaSyArxnGXpRqI-_5i02zPtdTbCyhParveFIw",
    'authDomain': "authdum.firebaseapp.com",
    'databaseURL': "https://authdum-default-rtdb.firebaseio.com",
    'projectId': "authdum",
    'storageBucket': "authdum.appspot.com",
    'messagingSenderId': "381396703977",
    'appId': "1:381396703977:web:32b4aaba9bffa7de956e78",
    'measurementId': "G-ERHKDMCEZ9"
}
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
auth = firebase.auth()
############################################

def  Int_connection():
    try:
        socket.create_connection(('google.com',80))
        return True
    except OSError:
        return False

###########################################
user = username()
def playgame():
    global playg
    playg = False
    global mainrun
    mainrun = True
    W = 750
    H = 400
    # Display setup
    pygame.init()
    screen = pygame.display.set_mode((W, H))

    global hscoresave
    # Inisialization
    hscoresave = 0
    bgimg = pygame.image.load(r'data\bg.png')
    himg = pygame.image.load(r'data\bgh.png')
    lbimg = pygame.image.load(r'data\bglb.png')
    game_over = pygame.image.load(u'data\game over.png')

    icon = pygame.image.load(r'data\icon.png')
    pygame.display.set_icon(icon)
    pygame.display.set_caption('Helicopter Fire')
    CLOCK = pygame.time.Clock()
    Fps = 260

    # score value
    def get_high_score():
        with open("data/highscore.txt", "r") as f:
            return f.read()

        # Pause Page

    def paus():
        try:
            global click

            def text_object(text, font):
                textsurface = font.render(text, True, (0, 0, 0))
                return textsurface, textsurface.get_rect()

            passed = True
            while passed:
                screen.fill((255, 255, 255))
                screen.blit(bgimg, (0, 0))

                x, y = pygame.mouse.get_pos()
                clickp = pygame.mouse.get_pressed()
                button1 = pygame.Rect(200, 250, 100, 50)
                button2 = pygame.Rect(450, 250, 100, 50)
                pygame.draw.rect(screen, (0, 100, 0), button1)
                pygame.draw.rect(screen, (165, 0, 0), button2)
                if button1.collidepoint(x, y):
                    pygame.draw.rect(screen, (0, 250, 100), button1)
                    if click == True and clickp[0] == 1:
                        pygame.draw.rect(screen, (0, 0, 0), button1)
                        passed = False
                if button2.collidepoint(x, y):
                    pygame.draw.rect(screen, (255, 0, 0), button2)
                    if click == True and clickp[0] == 1:
                        pygame.draw.rect(screen, (0, 0, 0), button2)
                        ##
                        pygame.quit()

                click = False
                playT = pygame.font.Font('freesansbold.ttf', 20)
                helpT = pygame.font.Font('freesansbold.ttf', 20)
                testsurf, textrect = text_object("Resume", playT)
                testhsurf, texthrect = text_object("Menu", helpT)
                textrect.center = ((200 + (100 / 2)), (225 + (100 / 2)))
                texthrect.center = ((450 + (100 / 2)), (225 + (100 / 2)))
                screen.blit(testsurf, textrect)
                screen.blit(testhsurf, texthrect)

                headt = pygame.font.Font('freesansbold.ttf', 50)
                textlx = (W / 2) - 180
                textly = (H / 2) - 50

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        ##
                        pygame.quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button - - 1:
                            click = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_c:
                            passed = False
                        elif event.key == pygame.K_ESCAPE:
                            passed = False

                headt = pygame.font.Font('freesansbold.ttf', 50)
                headts = pygame.font.Font('freesansbold.ttf', 20)
                textlx = 150
                textly = 100

                def head(x, y):
                    topic = headt.render("Paused", True, (0, 0, 0))
                    screen.blit(topic, (x + 130, y))

                head(textlx, textly)
                pygame.display.update()
                CLOCK.tick(Fps)
        except:
            pass

    # Main Game
    def game():
        try:
            # Game starts here
            X = 0
            # Program starts
            overX = 125
            overY = -10

            with open("data/color.txt", "r") as f:
                colour = f.read()
            plima = r'New folder\player1.png'
            if colour == "Player":
                plima = r'New folder\player1.png'
            elif colour == "Player2":
                plima = r'New folder\player2.png'
            elif colour == "Player3":
                plima = r'New folder\player3.png'
            playerImg = pygame.image.load(plima)
            playerX = 50
            playerY = 170
            playerY_move = 0

            blastImg = pygame.image.load(r'data\blast.png')
            blastX = 0
            blastY = 0

            enemyImg = (pygame.image.load(r'data\enemy.png'))
            enemyX = (random.randint(700, 800))
            enemyY = (random.randint(10, 300))
            enemyY_change = (1)

            bulletImg = pygame.image.load(r'data\bullet.png')
            bulletX = -1000
            bulletY = playerY
            bulletX_change = 10
            bullet_state = "ready"

            ebulletImg = pygame.image.load(r'data\enemy bullet.png')
            ebulletX = 0
            ebulletY = 0
            ebulletX_change = 4
            ebullet_state = "ready"

            jetImg = (pygame.image.load(r'data/jet.png'))
            jetx = 2000
            jety = 170
            jet_speed = 5

            score_value = 0
            fonts = pygame.font.Font('freesansbold.ttf', 16)

            textsx = 600
            textsy = 10

            player_life = 3
            fontl = pygame.font.Font('freesansbold.ttf', 16)
            textlx = 10
            textly = 10

            lifeimg = []
            lifX = []
            lifY = []
            poch = []
            noolife = player_life
            for i in range(noolife):
                lifeimg.append(pygame.image.load(r'data\life.png'))
                lifX.append(1)
                lifY.append(30)
                poch.append(5)

            try:
                high_score = int(get_high_score())
            except:
                high_score = 0

            hsx = 315
            hsy = 10

            def show_score(x, y):
                score = fonts.render("SCORE:" + str(score_value), True, (255, 255, 255))
                screen.blit(score, (x, y))

            def show_hscore(x, y):
                hscore = fonts.render("HIGH SCORE:" + str(high_score), True, (255, 255, 255))
                screen.blit(hscore, (x, y))

            def show_player_life(x, y):
                life = fontl.render("LIFE:" + str(player_life), True, (255, 255, 255))
                screen.blit(life, (x, y))

            def lifes(x, y, i):
                screen.blit(lifeimg[i], (x, y))

            def blast(x, y):
                screen.blit(blastImg, (x, y))

            def player(x, y):
                screen.blit(playerImg, (x, y))

            def enemy(x, y):
                screen.blit(enemyImg, (x, y))

            def jet(x,y):
                screen.blit(jetImg, (x,y))

            def gameover(x, y):
                screen.blit(game_over, (x, y))

            def bullet(x, y):
                global bullet_state
                bullet_state = "fire"
                screen.blit(bulletImg, (x + 45, y + 28))

            def fire_ebullet(x, y):
                global ebullet_state
                ebullet_state = "fire"
                screen.blit(ebulletImg, (x - 30, y + 28))

            def HCollision(tankX, tankY, bulletX, bulletY):
                distance = math.sqrt((math.pow(tankX - bulletX, 2)) + (math.pow(tankY - bulletY, 2)))
                if distance < 20:
                    return True
                else:
                    return False

            def jbCollision(jetx, jety, bulletX, bulletY):
                distance = math.sqrt((math.pow(jetx - bulletX, 2)) + (math.pow(jety - bulletY, 2)))
                if distance < 20:
                    return True
                else:
                    return False

            def jCollision(playerX, playerY, jetx, jety):
                distance = math.sqrt((math.pow(playerX - jetx, 2)) + (math.pow(playerY - jety, 2)))
                if distance < 20:
                    return True
                else:
                    return False

            def playerCollision(playerX, playerY, ebulletX, ebulletY):
                distancep = math.sqrt((math.pow(playerX - ebulletX, 2)) + (math.pow(playerY - ebulletY, 2)))
                if distancep < 20:
                    return True
                else:
                    return False

            g = 0
            run = True
            while run:
                screen.fill((0, 0, 0))
                screen_x = X % bgimg.get_rect().width
                screen.blit(bgimg, (screen_x - bgimg.get_rect().width, 0))
                if screen_x < W:
                    screen.blit(bgimg, (screen_x, 0))
                X -= 1

                player(playerX, playerY)
                enemy(enemyX, enemyY)
                jet(jetx, jety)
                show_score(textsx, textsy)
                show_hscore(hsx, hsy)
                for i in range(noolife):
                    poch[i] = 10 + (10 * i * 2)
                    lifes(lifX[i] + poch[i], lifY[i], i)

                show_player_life(textlx, textly)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        paus()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            paus()
                        if event.key == pygame.K_UP:
                            playerY_move = -2
                        if event.key == pygame.K_DOWN:
                            playerY_move = 2
                        if event.key == pygame.K_SPACE:
                            if bullet_state == "ready":
                                bullet_state = "fire"
                                bulletX = 50
                                bulletY = playerY
                                bullet(bulletX, playerY)
                        if event.key == pygame.K_p:
                            paus()
                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                                playerY_move = 0

                        if g == 0:
                            if ebullet_state == "ready":
                                ebullet_state = "fire"
                                fire_ebullet(ebulletX, enemyY)
                                ebulletY = enemyY

                collision = HCollision(enemyX, enemyY, bulletX, bulletY)
                if collision:
                    bulletX = -1000
                    bullet_state = "ready"
                    score_value += 10
                    enemyX = (random.randint(700, 800))
                    enemyY = (random.randint(10, 300))
                pcollusion = playerCollision(playerX, playerY, ebulletX, ebulletY)
                if pcollusion:
                    ebulletX = enemyX
                    ebullet_state = "ready"
                    player_life -= 1
                    noolife -= 1
                    blastX = playerX
                    blastY = playerY
                    blast(playerX, playerY)
                jpcollision = jCollision(playerX, playerY, jetx, jety)
                if jpcollision:
                    jetx = 10
                    player_life -= 1
                    noolife -= 1
                    blastX = playerX
                    blastY = playerY
                    blast(playerX, playerY)
                Collisionj = jbCollision(jetx, jety, bulletX, bulletY)
                if Collisionj:
                    bulletX = -1000
                    bullet_state = "ready"
                    score_value += 20
                    jetx = 2500

                if bulletX == ebulletX:
                    if bulletY == ebulletY:
                        bullet_state = "ready"
                        ebullet_state = "ready"

                if playerY <= 0:
                    playerY = 0
                elif playerY >= 330:
                    playerY = 330

                if enemyY <= 0:
                    enemyY_change = 1
                if enemyY >= 300:
                    enemyY_change = -1
                if enemyX >= 500:
                    if enemyX >= random.randint(550, 850):
                        enemyX -= 1

                if bullet_state == "fire":

                    bullet(bulletX, bulletY)
                    bulletX += bulletX_change
                if bulletX >= 700:
                    bulletX = -1000
                    bullet_state = "ready"
                if ebulletX <= 0:
                    ebulletX = enemyX
                    ebulletY = enemyY
                    ebullet_state = "ready"
                if ebullet_state == "fire":
                    fire_ebullet(ebulletX, ebulletY)
                    ebulletX -= ebulletX_change

                place = jetx
                if place >= -100:
                    jetx -= jet_speed
                    place = jetx
                else:
                    jetx = 2500

                if player_life <= 0:
                    if high_score < score_value:
                        high_score = score_value
                    with open("data/highscore.txt", "w")as f:
                        f.write(str(high_score))
                    data = {"high_score": high_score}
                    db.child(user).update(data)
                    gameover(overX, overY)
                    player_life -= 1

                if player_life == -2:
                    pygame.time.delay(1000)
                    run = False
                    pygame.quit()

                if game == False:
                    RUN = False
                    pygame.quit()

                playerY += playerY_move
                enemyY += enemyY_change
                try:
                 pygame.display.update()
                except:
                    break
                CLOCK.tick(Fps+160)
        except:
            pass
    game()
#=======================================================================================================================
class Menu(QDialog):
    def __init__(self):
        super (Menu, self).__init__()
        global men
        men = True
        global retrygm
        retrygm = False
        loadUi("menu.ui", self)
        usernam = username()
        print("menu")
        self.neterror.setVisible(False)
        self.Play.clicked.connect(lambda: self.play())
        self.Help.clicked.connect(lambda: self.help())
        self.Option.clicked.connect(lambda: self.option())
        self.User.clicked.connect(lambda: self.userclicklogout())
        self.Exit.clicked.connect(lambda: self.exit())
        self.LeaderBoard.clicked.connect(lambda: self.leaderboard())
        self.logout.clicked.connect(lambda: self.logouta())
        self.logout.setVisible(False)
        self.userlabl.setText(str(usernam))
        global mainrun
        mainrun = True
        self.pexit()
        self.setscore()
        self.shownet()

    def leaderboard(self):
        load = Leader()
        widget.addWidget(load)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.show()


    def setscore(self):
        user = username()
        g = str(user)+'/high_score'
        try:
            a = db.child(g).get()
        except:
            self.netcheck()
        with open(r"data\highscore.txt", "w")as f:
            f.write(str(a.val()))

    def userclicklogout(self):
        if self.logout.isVisible():
            self.logout.setVisible(False)
        else:
            self.logout.setVisible(True)

    def play(self):
        global playg
        playg = True
        pass

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Exit:
            self.close()
            QApplication.quit()

    def logouta(self):
        l=0
        with open(r"data\logstatus.txt", "w")as f:
            f.write(str(l))
        with open(r"data\user_status.txt", "w")as f:
            f.write(str(" "))
        with open(r"data\highscore.txt", "w")as f:
            f.write(str(l))
        with open(r"data\color.txt", "w")as f:
            f.write("player")
            f.truncate()
        global mainrun
        mainrun = True
        global logload
        logload = True
        self.close()
        QApplication.quit()


    def option(self):
        load = Option()
        widget.addWidget(load)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.show()


    def help(self):
        load = Help()
        widget.addWidget(load)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.show()

    def exit(self):
        self.close()
        global mainrun
        mainrun=False
        self.close()
        QApplication.quit()
        print("in exit")

    def pexit(self):
        if playg == True:
            self.close()
            QApplication.quit()
        QtCore.QTimer.singleShot(100, self.pexit)

    def shownet(self):
        netcnt = Int_connection()
        if netcnt == True:
            try:
                hk = self.neterror.isVisible()
            except:
                hk = False

            if hk == True:
                self.neterror.setVisible(False)
            pass
        else:
            self.netshow()
        Timer(5, self.shownet).start()

    def netshow(self):
        if self.neterror.isVisible()==False:
            self.neterror.setVisible(True)

class Option(QDialog):
    def __init__(self):
        super(Option, self).__init__()
        loadUi("option.ui", self)
        global men
        men = False
        color = colour()
        high_score = hig_score()
        self.Back.clicked.connect(lambda: self.back())
        self.pre.clicked.connect(lambda: self.prev())
        self.next.clicked.connect(lambda: self.nextt())
        if high_score == None:
            self.optscore.setText(str(0))
        else:
            self.optscore.setText(str(high_score))
        self.UsersName.setText(str(user))
        self.Player.setPixmap(QPixmap(str(drc)))

        global mainrun
        mainrun = True
        self.selected.setVisible(True)
        if color == "Player":
            self.Player2.setVisible(False)
            self.Player3.setVisible(False)
        elif color == "Player2":
            self.Player2.setVisible(True)
            self.Player3.setVisible(False)
            self.Player.setVisible(False)
        elif color == "Player3":
            self.Player2.setVisible(False)
            self.Player3.setVisible(True)
            self.Player.setVisible(False)

    def nextt(self):
        self.selected.setVisible(False)
        if self.Player.isVisible():
            self.pre.setVisible(True)
            self.next.setVisible(False)
            self.Player2.setVisible(True)
            self.Player.setVisible(False)
            self.Player3.setVisible(False)
        elif self.Player3.isVisible():
            self.pre.setVisible(True)
            self.Player2.setVisible(False)
            self.Player.setVisible(True)
            self.Player3.setVisible(False)

    def prev(self):
        self.selected.setVisible(False)
        if self.Player.isVisible():
            self.next.setVisible(True)
            self.pre.setVisible(False)
            self.Player2.setVisible(False)
            self.Player.setVisible(False)
            self.Player3.setVisible(True)
        elif self.Player2.isVisible():
            self.next.setVisible(True)
            self.Player2.setVisible(False)
            self.Player.setVisible(True)
            self.Player3.setVisible(False)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Exit:
            self.back()

    def back(self):
        global color
        color = "Player"
        if self.Player2.isVisible():
            color = "Player2"
        elif self.Player3.isVisible():
            color = "Player3"

        with open('data/color.txt', 'w') as f:
            f.write(color)
        load = Menu()
        widget.addWidget(load)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.show()
class Help(QDialog):
    def __init__(self):
        super(Help, self).__init__()
        loadUi("help.ui", self)
        global men
        men = False
        high_score = hig_score()
        if high_score != "None":
            self.score_value.setText(str(high_score))
        else:
            self.score_value.setText(str("0"))
        self.Reset_score.clicked.connect(lambda: self.highscore_reset())
        self.Back.clicked.connect(lambda: self.back())
        self.score_value.setText(str(high_score))
        global mainrun
        mainrun = True


    def highscore_reset(self):
        high_scorer = '0'
        self.score_value.setText(str(high_scorer))
        with open('data/highscore.txt', 'w') as f:
            f.write(high_scorer)
    def back(self):
        load = Menu()
        widget.addWidget(load)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.show()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Exit:
            self.back()

class Leader(QDialog):
    def __init__(self):
        super(Leader, self).__init__()
        loadUi("leader.ui", self)
        hs=hig_score()
        self.Back.clicked.connect(lambda: self.back())
        self.ledscore.setText(str(hs))
        self.table.setColumnWidth(0,350)
        self.table.setColumnWidth(1, 150)
        self.table.setColumnWidth(2, 133)

        def getinfo():
            data = db.get()
            data = data.val()
            a = [item for item in data]
            g = ""
            li = []
            score = {}
            for i in a:
                d = str(i + '/high_score')
                g = db.child(d).get()
                g = g.val()
                score["user"] = i
                li.append(score)
                score["score"] = str(g)
                score = {}

            li.sort(reverse=True, key=itemgetter("score"))
            return li
        li = getinfo()
        row =0
        self.table.setRowCount(len(li))
        for user in li:
            self.table.setItem(row, 0, QtWidgets.QTableWidgetItem(user["user"]))
            self.table.setItem(row, 1, QtWidgets.QTableWidgetItem(user["score"]))
            row+=1
    def back(self):
        load = Menu()
        widget.addWidget(load)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.show()
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Exit:
            self.back()


class Neterror(QDialog):
    def __init__(self):
        super(Neterror, self).__init__()
        loadUi("nonet.ui", self)
        self.ops.setVisible(False)
        self.retry.clicked.connect(lambda: self.retryrun())
        self.quit.clicked.connect(lambda: self.quitg())

    def retryrun(self):
        if self.ops.isVisible()==True:
            self.ops.setVisible(False)
        time.sleep(2)
        netcnt = Int_connection()
        if netcnt == True:
            self.ops.setVisible(False)
            global retrygm
            retrygm = True
            self.close()
            QApplication.quit()
        else:
            if self.ops.isVisible() == False:
                self.ops.setVisible(True)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Exit:
            self.quitg()

    def quitg(self):
        self.close()
        QApplication.quit()

mainrun = True
def start():
    app = QApplication(sys.argv)
    mainwindow = Menu()
    global widget
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.setWindowTitle(title)
    widget.setWindowIcon(QtGui.QIcon(icon))
    widget.setFixedWidth(750)
    widget.setFixedHeight(400)
    widget.show()
    try:
        sys.exit(app.exec_())
    except:
        if men == True:
            global  mainrun
            mainrun = False

        else:
            pass

def call_loginsys():
        cmd = 'python logsys.py'
        p=subprocess.Popen(cmd,shell=True)
        out,err = p.communicate()
        print(err)
        print(out)

def stop():
    global mainrun
    mainrun=False
def run():
    status = int(get_loged_in())
    if Int_connection() == True:
        while mainrun:
            status = int(get_loged_in())
            if status == 1:
                print("start")
                start()

            if logload == False :
                print("login")
                try:
                    call_loginsys()
                except:
                    pass
                stop()


            if playg == True:
                print("game")
                playgame()
    else:
        print("net", Int_connection())
        app = QApplication(sys.argv)
        mainwindow = Neterror()
        global widget
        widget = QtWidgets.QStackedWidget()
        widget.addWidget(Neterror())
        widget.setWindowTitle(title)
        widget.setWindowIcon(QtGui.QIcon(icon))
        widget.setFixedWidth(750)
        widget.setFixedHeight(400)
        widget.show()
        try:
            sys.exit(app.exec_())
        except:
            print("exit")

run()

if retrygm == True:
    print("run over")
    run()
