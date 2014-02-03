import kivy
import time


from kivy.app import App
from kivy.uix.button import Label
from kivy.clock import Clock

from ctypes import *
mylib = CDLL("libcCtypeLib.so")

class A(Structure):
    _fields_ = [
        ("a1", c_char_p),
        ("a2", c_int)]


python_cb_t = CFUNCTYPE(None, POINTER(A));



theLabel = Label(text='Nothin Yet...',font_size='40sp')

CurrentCount=1
def PythonCallback(theStruct):
    global CurrentCount
    global theLabel
    print "PythonCallback:"
    print "\t str = ",theStruct.contents.a1
    print "\t int = ",theStruct.contents.a2
    theLabel.text = "%s:%d"%(theStruct.contents.a1,theStruct.contents.a2)
    if CurrentCount < 10:
        Clock.schedule_once(testCB, 1)

python_cb = python_cb_t(PythonCallback)


def testCB(dt):
    global CurrentCount
    mylib.testCB(python_cb,CurrentCount)
    CurrentCount+=1

class MyApp(App):
    def build(self):
        global theLabel
        #return Label(text='Hello World')
        return theLabel

if __name__ == '__main__':
    Clock.schedule_once(testCB, 3)
    MyApp().run()



#for i in range (10):
#    print "i=",i
#    print "cb = ",python_cb
#    testCB(i);
