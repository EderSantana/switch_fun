#!/usr/bin/env python
#
# by Eder Santana
# modified from the work of Kevin J. Walchko 26 Aug 2014
#
# Nintendo Switch Pro Controller has 4 axes, 14 buttons, 1 hat
# Tested with a PowerA controller

import sdl2
import time

def prettyPrintPRO(pro):
    print '------------------------------------'
    print '    press [-] button to quit     '
    print '   left axis (x,y):',pro['la']['x'],pro['la']['y']
    print '  right axis (x,y):',pro['ra']['x'],pro['ra']['y']
    print '---'
    print '  left trigger1:',pro['lt1'],'\t\t','right trigger1:',pro['rt1']
    print '  left trigger2:',pro['lt2'],'\t\t','right trigger2:',pro['rt2']
    print '---'
    print '    Y:',pro['Y']
    print '    X:',pro['X']
    print '    A:',pro['A']
    print '    B:',pro['B']
    print '---'
    print '  hat:',pro['hat']

# init stuff
sdl2.SDL_Init(sdl2.SDL_INIT_JOYSTICK)

js = sdl2.SDL_JoystickOpen(0)

# grab info
a = sdl2.SDL_JoystickNumAxes(js)
b = sdl2.SDL_JoystickNumButtons(js)
h = sdl2.SDL_JoystickNumHats(js)
print 'axes:',a,'buttons:',b,'hats:',h
# exit()
# Data structure holding the PRO info
pro = {
    'la': {'x': 0, 'y': 0},  # left axis
    'ra': {'x': 0, 'y': 0},
    'lt1': 0, # left trigger 1
    'rt1': 0,
    'lt2': 0, # left trigger 2
    'rt2': 0,
    'A': 0,  
    'X': 0,   
    'Y': 0,
    'B': 0,
    'hat': 0,
    }

while True:
    sdl2.SDL_JoystickUpdate()
    
    # left axis
    pro['la']['x'] = sdl2.SDL_JoystickGetAxis(js,0)
    pro['la']['y'] = sdl2.SDL_JoystickGetAxis(js,1)
    
    # right axis
    pro['ra']['x'] = sdl2.SDL_JoystickGetAxis(js,2)
    pro['ra']['y'] = sdl2.SDL_JoystickGetAxis(js,3)
    
    # left trigger axis
    # pro['lt2'] = sdl2.SDL_JoystickGetAxis(js,6)
    pro['lt2'] = sdl2.SDL_JoystickGetButton(js,6)
    
    # right trigger axis
    # pro['rt2'] = sdl2.SDL_JoystickGetAxis(js,7)
    pro['rt2'] = sdl2.SDL_JoystickGetButton(js,7)
    
    # get buttons
    pro['Y'] = sdl2.SDL_JoystickGetButton(js,0)
    pro['B'] = sdl2.SDL_JoystickGetButton(js,1)
    pro['A'] = sdl2.SDL_JoystickGetButton(js,2)
    pro['X'] = sdl2.SDL_JoystickGetButton(js,3)
    pro['lt1'] = sdl2.SDL_JoystickGetButton(js,4)
    pro['rt1'] = sdl2.SDL_JoystickGetButton(js,5)
    
    # use share button as a quit
    quit = sdl2.SDL_JoystickGetButton(js,8)
    
    # get hat
    pro['hat'] = sdl2.SDL_JoystickGetHat(js,0)
    
    prettyPrintPRO(pro)
    
    if quit == True:
        break
    
    time.sleep(0.3)
 
sdl2.SDL_JoystickClose(js)
print 'Bye ...'
