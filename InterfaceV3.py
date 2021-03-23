#!/usr/bin/python

##import all necesary librarys
import tkinter
from tkinter import *
import sys
from format_usb import format_device
import subprocess
import time
from datetime import datetime
from log import Log


##become root in the terninal to avoid permission denied errors
sudo = subprocess.check_output(['sudo su'], shell = True)


##create an instance of the Tk object
tk = tkinter.Tk()

##get the current date and time for creating the folders for logs
now = datetime.now()
LogPath = (now.strftime('%Y/%m/%d'))
make_str = ('sudo mkdir -p %s'%LogPath)
make_directory = subprocess.check_output([make_str], shell = True)


####### needs updating to be relative
chmod_str = ('sudo chmod 777 /home/pi/Desktop/startup/%s'%(now.strftime('%Y/%m/%d')))
chmod = subprocess.check_output([chmod_str], shell = True)
##########



##use the date and time to create the new files and create a log file with the time
now_str = now.strftime('/%Y/%m/%d/%H:%M:%S')
log_file = ('%s_Log.txt'%now_str)
log_file = '/home/pi/Desktop/startup' + log_file##add the absolute path to the string



##write the first line to the log
Log(log_file, 'Sucsesfully started program and imported all nessecary librarys\n')


##gets width and height of screen for setting button sizes
w, h= tk.winfo_screenwidth(), tk.winfo_screenheight()


##global variables for later use
global clicked
clicked = 0

global fullscreen
fullscreen = False


##when set to true window will open in full screen
##make sure that the probram has an escape function before making this true

##tk.attributes('-fullscreen', fullscreen)


####create a function to toggle full screen ##needs work
##def is_fullscreen(event):
##    global fullscreen
##    fullscreen = not fullscreen
##    tk.attributes('-fullscreen', fullscreen)
##    print(event.char)
##tk.bind('<F11>', lambda a : is_fullscreen(a))



##ceate variables for dynamic text updating 
L2_Text = StringVar()
B3_Text = StringVar()


##command to be executed when button 1 is clicked
def button1command():
    Log(log_file,'Button 1 pressed\n')
    tk1 = Toplevel(tk)


    ##create a new lable
    L2 = tkinter.Label(tk1, textvariable =L2_Text, bg = 'DeepSkyBLue2', fg = 'black', activebackground = 'DeepSkyBlue2')
    L2.config(font=('helvetica', 48, 'underline'))
    L2_Text.set('Insert USB')

    
    ##create bottom left button
    B3 = tkinter.Button(tk1, textvariable = B3_Text, command = button3command, bg = 'RoyalBlue2', fg = 'black', activebackground = 'RoyalBlue3')
    B3.config(font=('helvetica', 32, 'underline'))
    B3_Text.set('Format')


    ##create bottom right button
    B4 = tkinter.Button(tk1, text ="Cancel", command = button2command, bg = 'RoyalBlue2', fg = 'black', activebackground = 'RoyalBlue3')
    B4.config(font=('helvetica', 32, 'underline'))


    ##place all the buttons on to the screen
    L2.place(height = (h/2),width = w,x=0,y=0)
    B3.place(height = (h/2),width = (w/2),x=0,y=(h/2))
    B4.place(height = (h/2),width = (w/2),x=(w/2),y=(h/2))
    Log(log_file,'Button 1 command executed\n')
    

##the command to be executed when button 2 is pressed
def button2command():
    Log(log_file,'Button 2 pressed and executed\n')
    tk.destroy()
    ##shutdown = subprocess.check_output(['sudo shutdown now'], shell = True)
    


##the command to be executed when button 3 is pressed
def button3command():
    Log(log_file,'Button 3 pressed\n')

    ##variable used to determine weather this is the first or second click of button 3
    global clicked
    clicked += 1


    ##on the first click execte this
    if clicked == 1:
        L2_Text.set('Formating...')
        chosenOption = M1_options.get()
        optionLength = chosenOption.find('(')
        option = ''
        for x in range(0, optionLength):
            letter = chosenOption[x]
            option = option + letter
        format_device(option, log_file)
        time.sleep(2)
        L2_Text.set('Done')
        B3_Text.set('Finish')
        Log(log_file,'Button 3 command executed\n')

        
    ##on the second click execute this    
    else:
        Log(log_file,'Button 3 command executed\n')
        Log(log_file,'Program appears to have run sucessfully\nShuting down the pi\n')
        shutdown = subprocess.check_output(['sudo shutdown now'], shell = True)


##create all the widgets for the main screen    
    
##create label for menu 1
M1_options = StringVar(tk)
M1_options.set("File System to format to:")

##create the top label for the first screen
L1 = tkinter.Label(tk, text ="USB Sanitiser", bg = 'DeepSkyBLue2', fg = 'black', activebackground = 'DeepSkyBlue2')
L1.config(font=('helvetica', 48, 'underline'))

##create bottom left button
B1 = tkinter.Button(tk, text ="Next", command = button1command, bg = 'RoyalBlue2', fg = 'black', activebackground = 'RoyalBlue3')
B1.config(font=('helvetica', 32, 'underline'))

##create bottom right button
B2 = tkinter.Button(tk, text ="Cancel", command = button2command, bg = 'RoyalBlue2', fg = 'black', activebackground = 'RoyalBlue3')
B2.config(font=('helvetica', 32, 'underline'))

##create exit button
exitBtn = tkinter.Button(tk, text ="X", command = button2command, bg = 'RoyalBlue2', fg = 'black', activebackground = 'RoyalBlue3')
exitBtn.config(font=('helvetica', 32))

#create the option menu for the first screen
M1 = OptionMenu(tk, M1_options, "FAT32(small flash drives, older)", "exFAT(small flash drive, newer, default)", "NTFS(large drives)")
M1.config(font=('helvetica', 20, 'underline'))
menu = M1.nametowidget(M1.menuname)
menu.configure(font=('helvetica', 20))

##specify where to place buttons onto main window and specify size
L1.place(height = (h/2),width = w,x=0,y=0)
B1.place(height = (h/2),width = (w/2),x=0,y=(h/2))
M1.place(x=0, y=(h/2))
B2.place(height = (h/2),width = (w/2),x=(w/2),y=(h/2))
exitBtn.place(height = (h/10), width = (h/10), x = h-(h/10), y = w-(h/10))


Log(log_file,'Screen 1 created and displayed\n')

tk.mainloop()

