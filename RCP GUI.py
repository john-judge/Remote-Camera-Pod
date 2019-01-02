# -*- coding: utf-8 -*-
import serial
from Tkinter import *
import time
from random import randint

#finds open COM port and connects
def getconnectcom():
    baud = 9600
    for i in range (2,99):
        port ='COM'+str(i)
        try:
            ser = serial.Serial(port, baud, bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=0)
            if ser.isOpen():
                return(port)
                break 
        except:
            pass  
                   
#set internal commands
def set_internalcmds(): #check sync and identify and set to continuous repeating cmds
    ser.write('AT CS\r\n')
    sync_stat = ser.read(30)
    ser.write('AT I\r\n')
    id_elm = ser.read(30)
    ser.write('AT R 0\r\n') #continuous repetition
    cont_rep=ser.read(30)
    message = id_elm[5:17] + ' ' + sync_stat[7:14] + ' ' + cont_rep[0:7]
    return message
    
def create_buttons():
   #create power buttons
    pwrbutton1=Button(top, text="Wake Camera", command=sendpulse)
    pwrbutton1.grid()
    pwrbutton2=Button(top, text='Sleep Camera', command=poweroff)
    pwrbutton2.grid()
    
def create_buttons2():
    #create record button
    recbutton=Button(top, text='Record/Stop', command=recstop)
    recbutton.grid()
        
def sendpulse():
    #wake cam by sending pulse
    ser.write('AT SP\r\n')
    global var2
    var2.set('♪\'Cause waking up is hard to do.♪ \n ♪♪♪')
        
def poweroff():
    #power off camera, sleep
    ser.write('185E\r\n')
    global var2
    rand=randint(0,9)
    if rand<=6:
        var2.set('Trying to sleep. \n Don\'t worry, I don\'t snore.')  
    if rand==7:
        var2.set('To die, to sleep; \n To sleep: perchance to dream')
    if rand==8:
        var2.set('I\'m so good at sleep, \n I can do it with my eyes closed.')
    
def recstop():
    #stop or start recording
    ser.write('1833\r\n')
    global var2
    var2.set('Command Rec/Stop sent. \n HDRunners may or may not be watching you.')
    
def create_label(txt):
    #creates a label that displays instructions to use GUI  
    label1 = Label(top, text=txt, font='Times 12')
    label1.grid() 
    
def create_varlabel(var,font):
     #creates a label that can change
     label1=Label(top, textvariable=var, font=(font))
     label1.grid() 
    
def create_zoomscale():
    #creates a scale, values [-8,8], to zoom at 17 different speeds    
    zmscale=Scale(top, orient=HORIZONTAL,length=300,width=20, from_=-8,to=8,tickinterval=1, command=new_zoom)
    zmscale.grid()

def new_zoom(zmcounter):
    '''event handler for scale:
    reads the scale and executes zoom at the appropriate velocity'''
    ser.write(' \r\n')
    global var2
    time.sleep(.02)
    zmcounter=int(zmcounter)
    if zmcounter==0:
        ser.write(' \r\n')
    if zmcounter>0:
        ser.write(str(hex(10238+zmcounter*2))[2:]+'\r\n')
        var2.set('Zooming in! \n  ')
    if zmcounter<0:
        ser.write(str(hex(10254-zmcounter*2))[2:]+'\r\n')
        var2.set('Zooming out! \n  ')

#event handler: mouse button 1 on frame
#get ready to take keyboard input, focus set to frame
def callback(event):
    #calls focus to the keyboard bound frame
    global frame
    frame.focus_set()
    global var1
    var1.set('Ready to pan/tilt with keys W, A, S, D (feature not yet supported)')
    
def keypressed(event):
    global var2
    var2.set('You pressed: \n ' + repr(event.char))
    
def create_homebutton():
    recbutton=Button(top, text='Home', command=go_home)
    recbutton.grid()
    
def create_homescale():
    #creates scale for selecting home location as zoom magnification 1-20x
    zmscale=Scale(top, orient=HORIZONTAL,length=300,width=20, from_=1,to=20,tickinterval=1, command=new_home)
    zmscale.grid()
    
def new_home(scale_reads):
    global hmcounter
    hmcounter=scale_reads
    
def go_home():
    ser.write(' \r\n')
    time.sleep(.02)
    #set zoom to home
    global hmcounter
    global var2
    hmcounter=float(hmcounter)
    #find the zoom limit closest to home, 1x or 20x
    if hmcounter>10:
        #zoom in to 20x 
        ser.write('280E\r\n')
        time.sleep(2.4)
        #find home at zoom speed 6
        ser.write(' \r\n')
        time.sleep(.02)
        ser.write('281A\r\n')
        timer=9.403*(20.0-hmcounter)/20.0
        time.sleep(timer)
        ser.write(' \r\n')
        var2.set('There\'s no place like home. \n Thank you for patiently waiting ' + str(timer+2.44) + ' seconds.')
    if hmcounter<=10:
        #zoom out to 1x 
        ser.write('281E\r\n')
        time.sleep(2.4)
        #find home at zoom speed 6
        ser.write(' \r\n')
        time.sleep(.02)
        ser.write('280A\r\n')
        timer=9.403*(hmcounter-1.0)/20.0
        time.sleep(timer)
        ser.write(' \r\n')
        var2.set('\'Home\' run! \n Thank you for patiently waiting ' + str(timer+2.44) + ' seconds.')

def on_closing():
    #close serial port on exit. conditional to check if ser is already closed
    if ser.isOpen():
        ser.close()
        top.destroy()
    else:
        top.destroy()
       
#setup functions called:
port = getconnectcom() #open virtual serial port, report
baud=9600
ser = serial.Serial(port, baud, bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=0)
status='Oh no! No serial port found! \n Check connections and restart.'
if ser.isOpen():
    status=port + ' is open!'
    status =status + ' ' + set_internalcmds() #set internal commands.

#GUI mainloop:   
top = Tk()
top.title("Remote Camera Pod Controller Beta v0.9.1")
top.geometry("500x800")
create_label('Please make sure Canon is in Camera Mode, physically.')
create_buttons() #wake, sleep, reboot ELM624 buttons
create_buttons2() #rec/stop button

#Create an updating status message (not finished)
create_label(' ')
stat_label = Label(top, text='Status:', font=("Times 24 bold"))
stat_label.grid() 
var2=StringVar()
create_varlabel(var2, 'Times 16 bold')
var2.set(status)

#call zoom scale functions
create_label(' ')
create_label(' ')
create_label('Zoom Slider')
create_label('For best results: avoid quick \"turns\"')
create_label('(e.g. selecting 5, 6, 5 in rapid succession.)')
create_zoomscale() # zoom scale slider

#create frame in which to click to enable keyboard input
#binds events. see above for event handlers
frame = Frame(top, highlightcolor='red', highlightbackground='blue', width=500, height=100)
frame.bind("<Button-1>", callback)
frame.bind('<Key>', keypressed)
frame.grid()

#create a changing label to display whether keyboard input enabled
var1=StringVar()
create_varlabel(var1, 'Times 12')
var1.set('Click in the space above to enable keyboard input.')

#here the user chooses the "Home Location" zoom
create_label(' ')
create_label('Select Home zoom location, in focal length multiplier (1x to 20x):')
hmcounter=20 #global variable for home location, default 20x zoom
create_homescale()
create_homebutton()





create_label(' ')
create_label(' ')
create_label('J&G 2015')


#close serial port on exit
top.protocol("WM_DELETE_WINDOW", on_closing)    
 
top.mainloop()       

