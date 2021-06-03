import time
import random
import sys
import socket
import smtplib
import pyrebase
from tkinter import *
from threading import Timer
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5.uic import loadUi
from firebase import firebase
sys.setrecursionlimit(1500)
global user
user = ""
title = "Helicopter Fire"
icon = "data\icon.png"
done = False
with open("data/user_status.txt", "r")as f:
    user = f.read()
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
def otp_email(recever):
    global otpg
    otpg = "".join([str(random.randint(0, 9)) for i in range(4)])
    print(otpg)

    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('adithya.sellapillai.n@gmail.com',password = "grffimnvhpkyrhgi")
    msg=r'Hello, Your Helicopter Fire game\'s OTP is here-' + str(otpg) + " Enjoy playing fun Thanks for loging in " \
                                                                    "Thank You...."
    server.sendmail('adithya.sellapillai.n@gmail.com', recever,msg)
    server.quit()

def logedinsuc():
    with open(r"data\logstatus.txt", 'w') as f:
        f.write(str(1))

def get_loged_in():
    with open("data\logstatus.txt", "r") as f:
        return f.read()

verf = False
class LogMenue(QDialog):
    def __init__(self):
        super(LogMenue, self).__init__()
        loadUi("logmenue.ui", self)
        self.neterror.setVisible(False)
        self.Login.clicked.connect(self.funclog)
        self.Sign_in.clicked.connect(self.funcsign)
        self.shownet()

    def funclog(self):
        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.show()
    def funcsign(self):
        createacc = Signup()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.show()
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
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Exit:
            self.close()
            QApplication.quit()

    def netshow(self):
        if self.neterror.isVisible()==False:
            self.neterror.setVisible(True)

class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("login.ui", self)
        self.loginbutton.clicked.connect(self.loginfunction)
        self.cancel.clicked.connect(self.back)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createaccbutton.clicked.connect(self.gotocreate)
        self.invalid_lable_2.setVisible(False)
        self.invalid_lable_3.setVisible(False)
        self.invalid_lable_4.setVisible(False)
        self.neterror.setVisible(False)
        self.shownet()

    def back(self):
        Back = LogMenue()
        widget.addWidget(Back)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.show()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Exit:
            self.back()


    def loginfunction(self):
        global username
        username = self.user.text()
        email = self.email.text()
        password = self.password.text()

        check = base.get(username, None)
        print(check)
        if check == None:
            self.invalid_lable_3.setVisible(True)
            print("user is none")
        else:
            self.invalid_lable_3.setVisible(False)
            print("user is valid")
            g = username + '/email'
            p = username + '/pasword'
            print(g)
            f = base.get(g, None)
            passw = base.get(p, None)
            print(p)
            if f == email:
                self.invalid_lable_4.setVisible(False)
                print(f, email)

                #loging process
                if passw == password:
                    try:
                        auth.sign_in_with_email_and_password(email, password)
                        self.invalid_lable_3.setVisible(False)
                        self.invalid_lable_2.setVisible(False)
                        Done = True
                        self.user.clear()
                        self.email.clear()
                        self.password.clear()
                        print("auth finished")
                        self.user.clear()
                        self.email.clear()
                        self.password.clear()
                        if Done == True:
                            print("done is true")
                            global done
                            done = True
                        try:
                            if done == True:
                                logstate = 1
                                with open("data\logstatus.txt", "w")as f:
                                    f.write(str(logstate))
                                    f.truncate()
                                with open(r"data\user_status.txt", "w")as f:
                                    f.write(str(username))
                                    f.truncate()
                                user = username
                                print(user)
                        except:
                            print("after_loger not working")
                        self.close()
                        QApplication.quit()
                    except:
                        print("no")

                else:
                    self.invalid_lable_2.setVisible(True)
            else:
                self.invalid_lable_4.setVisible(True)

    def gotocreate(self):
        createacc = Signup()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex()+1)

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

class Verify(QDialog):
    def __init__(self):
        super(Verify, self).__init__()
        loadUi("verify.ui", self)
        self.passerror_5.setVisible(False)
        self.verify.clicked.connect(lambda: self.verifyc())
        self.resendotp.clicked.connect(lambda: self.resend())
        self.cancel_OTP.clicked.connect(lambda: self.back())
        self.login_OTP.clicked.connect(lambda: self.changemail())
        self.neterror.setVisible(False)
        self.shownet

        recmailID = "jdfjdk@gmail.com"
        self.email_OTP.setText(recmailID)
        otp_email(recmailID)
    def verifyc(self):
        if self.otpe.text() == otpg:
            self.passerror_5.setVisible(False)
            print("verified................................................................."
                  "loging in")
            self.otpe.clear()
            self.otpe.clear()
            try:
                auth.create_user_with_email_and_password(email=email, password=password)
                auth.sign_in_with_email_and_password(email, password)
                print("created")
                # data
                data = {"username": username, "email": email, "pasword": password}
                db.child(username).set(data)
                print("creaed succesfully")
                global loged
                loged  = 1
                Back = LogMenue()
                widget.addWidget(Back)
                widget.setCurrentIndex(widget.currentIndex() + 1)
                widget.show()
                print("done is true")
                global done
                done = True
                try:
                    if done == True:
                        logstate = 1
                        with open(r"data\logstatus.txt", "w")as f:
                            f.write(str(logstate))
                            f.truncate()
                        with open(r"data\user_status.txt", "w")as f:
                            f.write(str(username))
                            f.truncate()
                        user = username
                        print(user)
                except:
                    print("after_loger not working")
                self.close()
                QApplication.quit()
            except:
                Back = Signup()
                widget.addWidget(Back)
                widget.setCurrentIndex(widget.currentIndex() + 1)
                widget.show()
        else:
            self.passerror_5.setVisible(True)
    def changemail(self):
        pass

    def back(self):
        Back = Signup()
        widget.addWidget(Back)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.show()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Exit:
            self.back()

    def resend(self):
        recmailID = "bloombuddy@gmail.com"
        otp_email(recmailID)
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

class Signup(QDialog):
    def __init__(self):
        super(Signup, self).__init__()
        loadUi("createacc.ui", self)
        self.signupbutton.clicked.connect(self.signupfunction)
        self.cancel.clicked.connect(self.back)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confpassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.logintobutton.clicked.connect(self.gotologin)
        self.invalid_lable.setVisible(False)
        self.invalid_lable_2.setVisible(False)
        self.passerror_1.setVisible(False)
        self.passerror_2.setVisible(False)
        self.passerror_3.setVisible(False)
        self.passerror_4.setVisible(False)
        self.passerror_5.setVisible(False)
        self.neterror.setVisible(False)
        self.shownet()

    def back(self):
        Back = LogMenue()
        widget.addWidget(Back)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.show()
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Exit:
            self.back()
    def gotologin(self):
        Back = Login()
        widget.addWidget(Back)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.show()
    def signupfunction(self):
        done=0
        global username
        global email
        username = self.username.text()
        email = self.email.text()
        ed = ""
        check = base.get(username, None)
        eck = "".join(str(base.get(ed, None)))
        print(check)
        print(eck)
        if check== None:
            self.passerror_4.setVisible(False)
            done+=1
            print("eck1")
        else:
            self.passerror_4.setVisible(True)

        if ".com" in email and "@" in email:
            self.passerror_3.setVisible(False)
            done += 1
            print("ecgsk2")
        else:
            self.passerror_3.setVisible(True)
        if email in eck:
            self.passerror_5.setVisible(True)
            done += 1
            print("eck3")
        else:
            self.passerror_5.setVisible(False)

        if len(self.password.text()) >= 6:
            print("eck4")
            self.invalid_lable.setVisible(False)
            done += 1
            print(eck)
        else:
            print("eck5")
            self.invalid_lable.setVisible(True)
        if self.password.text() == self.confpassword.text():
            global password
            password = self.password.text()
            self.passerror_1.setVisible(False)
            self.passerror_2.setVisible(False)
            done += 1
            print("eck6")
        else:
            self.passerror_1.setVisible(True)
            self.passerror_2.setVisible(True)
        if username =="" and email == "":
            self.invalid_lable_2.setVisible(True)
        else:
            print(done)
            self.invalid_lable_2.setVisible(False)

        if done == 4:
            verf = True
            self.veri(verf)

    def veri(self,verfg):
        if verfg == True:
            Back = Verify()
            widget.addWidget(Back)
            widget.setCurrentIndex(widget.currentIndex() + 1)
            widget.show()

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


def logfunc():
    if Int_connection() == True:
        app = QApplication(sys.argv)
        mainwindow = LogMenue()
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
            guli()
            print("Exiting")
    else:
        print("no network")

def guli():
    if done == True:
        main.start()

logfunc()