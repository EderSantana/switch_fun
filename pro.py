#!/usr/bin/env python
#
# by Eder Santana
# modified from the work of Kevin J. Walchko 26 Aug 2014
#
# Nintendo Switch Pro Controller has 4 axes, 14 buttons, 1 hat
# Tested with a PowerA controller

import sdl2
import time

def prettyPrintPS4(ps4):
    print '------------------------------------'
    print '    press [-] button to quit     '
    print '   left axis (x,y):',ps4['la']['x'],ps4['la']['y']
    print '  right axis (x,y):',ps4['ra']['x'],ps4['ra']['y']
    print '---'
    print '  left trigger1:',ps4['lt1'],'\t\t','right trigger1:',ps4['rt1']
    print '  left trigger2:',ps4['lt2'],'\t\t','right trigger2:',ps4['rt2']
    print '---'
    print '    Y:',ps4['Y']
    print '    X:',ps4['X']
    print '    A:',ps4['A']
    print '    B:',ps4['B']
    print '---'
    print '  hat:',ps4['hat']

# init stuff
sdl2.SDL_Init(sdl2.SDL_INIT_JOYSTICK)

js = sdl2.SDL_JoystickOpen(0)

# grab info
a = sdl2.SDL_JoystickNumAxes(js)
b = sdl2.SDL_JoystickNumButtons(js)
h = sdl2.SDL_JoystickNumHats(js)
print 'axes:',a,'buttons:',b,'hats:',h
# exit()
# Data structure holding the PS4 info
ps4 = {
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
    ps4['la']['x'] = sdl2.SDL_JoystickGetAxis(js,0)
    ps4['la']['y'] = sdl2.SDL_JoystickGetAxis(js,1)
    
    # right axis
    ps4['ra']['x'] = sdl2.SDL_JoystickGetAxis(js,2)
    ps4['ra']['y'] = sdl2.SDL_JoystickGetAxis(js,3)
    
    # left trigger axis
    # ps4['lt2'] = sdl2.SDL_JoystickGetAxis(js,6)
    ps4['lt2'] = sdl2.SDL_JoystickGetButton(js,6)
    
    # right trigger axis
    # ps4['rt2'] = sdl2.SDL_JoystickGetAxis(js,7)
    ps4['rt2'] = sdl2.SDL_JoystickGetButton(js,7)
    
    # get buttons
    ps4['Y'] = sdl2.SDL_JoystickGetButton(js,0)
    ps4['B'] = sdl2.SDL_JoystickGetButton(js,1)
    ps4['A'] = sdl2.SDL_JoystickGetButton(js,2)
    ps4['X'] = sdl2.SDL_JoystickGetButton(js,3)
    ps4['lt1'] = sdl2.SDL_JoystickGetButton(js,4)
    ps4['rt1'] = sdl2.SDL_JoystickGetButton(js,5)
    
    # use share button as a quit
    quit = sdl2.SDL_JoystickGetButton(js,8)
    
    # get hat
    ps4['hat'] = sdl2.SDL_JoystickGetHat(js,0)
    
    prettyPrintPS4(ps4)
    
    if quit == True:
        break
    
    time.sleep(0.3)
 
sdl2.SDL_JoystickClose(js)
print 'Bye ...'
