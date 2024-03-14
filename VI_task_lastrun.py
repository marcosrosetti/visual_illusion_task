#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on March 14, 2024, at 14:04
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2022.2.5')


# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLib'] = 'ptb'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, iohub, hardware
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'Pilot'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\roset\\Dropbox\\PC (3)\\Downloads\\Visual_Ilusion_Task\\VI_task_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
    blendMode='add', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup eyetracking
ioConfig['eyetracker.hw.mouse.EyeTracker'] = {
    'name': 'tracker',
    'controls': {
        'move': [],
        'blink':('LEFT_BUTTON',),
        'saccade_threshold': 0.5,
    }
}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = ioServer.getDevice('tracker')

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "hello" ---
text = visual.TextStim(win=win, name='text',
    text='A continuación, te presentaremos dos imágenes, \nuna del lado derecho y una del lado izquierdo. \nDebes elegir la imagen que mejor cumpla lo que la \ninstrucción te indicará. \nEscucha con atención cada instrucción y trata de \nresponder tan rápido como puedas.',
    font='Open Sans',
    pos=(0, 0.25), height=0.06, wrapWidth=10.0, ori=0.0, 
    color=[-0.4902, -0.1765, 0.7647], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
buttonhello = visual.ButtonStim(win, 
    text='INICIAR', font='Arvo',
    pos=[0,-0.25],
    letterHeight=0.08,
    size=[0.4,0.2], borderWidth=1.0,
    fillColor='orangered', borderColor=[-1.0000, -1.0000, -1.0000],
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='buttonhello'
)
buttonhello.buttonClock = core.Clock()
sound_1 = sound.Sound('Stimuli/Instructions/Instrucción inicial2.ogg', secs=-1, stereo=True, hamming=True,
    name='sound_1')
sound_1.setVolume(1.0)

# --- Initialize components for Routine "hello_training" ---
hellotraining_poly = visual.ShapeStim(
    win=win, name='hellotraining_poly',
    size=(0.15, 0.15), vertices='circle',
    ori=0.0, pos=(0, -0.20), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor=[1.0000, -0.4588, -1.0000],
    opacity=None, depth=0.0, interpolate=True)
hellomouse = event.Mouse(win=win)
x, y = [None, None]
hellomouse.mouseClock = core.Clock()
hellotraining = visual.TextStim(win=win, name='hellotraining',
    text='Pero primero, \n¡un poco de entrenamiento!\n\n\nHas click sobre EL CIRCULO ROJO',
    font='Open Sans',
    pos=(0, 0.2), height=0.08, wrapWidth=None, ori=0.0, 
    color=[-0.4902, -0.1765, 0.7647], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "longerline_1" ---
longerline1pic = visual.ImageStim(
    win=win,
    name='longerline1pic', 
    image='Stimuli/Training/longerline1.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=[2,1],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
longerline1area = visual.Rect(
    win=win, name='longerline1area',
    width=(0.8, 0.32)[0], height=(0.8, 0.32)[1],
    ori=0.0, pos=[-0.23, -0.30], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor=None,
    opacity=None, depth=-1.0, interpolate=True)
Longerlinetext1 = visual.TextBox2(
     win, text='Elige el LINEA MÁS LARGA!', font='Calibri',
     pos=[0, 0.45],     letterHeight=0.06,
     size=(None, None), borderWidth=2.0,
     color=[-1.0000, -1.0000, 1.0000], colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='Longerlinetext1',
     autoLog=True,
)
longerlinemouse1 = event.Mouse(win=win)
x, y = [None, None]
longerlinemouse1.mouseClock = core.Clock()

# --- Initialize components for Routine "longerline_2" ---
longerline2pic = visual.ImageStim(
    win=win,
    name='longerline2pic', 
    image='Stimuli/Training/longerline2.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=[1.9,1],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
longerline2area = visual.Rect(
    win=win, name='longerline2area',
    width=(0.72, 0.37)[0], height=(0.72, 0.37)[1],
    ori=0.0, pos=[0.5, 0.24], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor=None,
    opacity=None, depth=-1.0, interpolate=True)
Longerlinetext2 = visual.TextBox2(
     win, text='Elige el LINEA MÁS LARGA!', font='Calibri',
     pos=[0, 0.45],     letterHeight=0.06,
     size=(None, None), borderWidth=2.0,
     color=[-1.0000, -1.0000, 1.0000], colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='Longerlinetext2',
     autoLog=True,
)
longerline2mouse = event.Mouse(win=win)
x, y = [None, None]
longerline2mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "longerline_3" ---
longerline3pic = visual.ImageStim(
    win=win,
    name='longerline3pic', 
    image='Stimuli/Training/longerline3.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=[1.9,1],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
longerline3area = visual.Rect(
    win=win, name='longerline3area',
    width=(1, 0.17)[0], height=(1, 0.17)[1],
    ori=0.0, pos=[0.49, -0.3], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor=None,
    opacity=None, depth=-1.0, interpolate=True)
Longerlinetext3 = visual.TextBox2(
     win, text='Elige el LINEA MÁS LARGA!', font='Calibri',
     pos=[0, 0.45],     letterHeight=0.06,
     size=(None, None), borderWidth=2.0,
     color=[-1.0000, -1.0000, 1.0000], colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='Longerlinetext3',
     autoLog=True,
)
longerline3mouse = event.Mouse(win=win)
x, y = [None, None]
longerline3mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "clickcircle1" ---
circle_click_text1 = visual.TextBox2(
     win, text='Has click sobre EL CIRCULO', font='Calibri',
     pos=[0, 0.45],     letterHeight=0.06,
     size=(None, None), borderWidth=2.0,
     color=[-1.0000, -1.0000, 1.0000], colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='circle_click_text1',
     autoLog=True,
)
circle_click = visual.ShapeStim(
    win=win, name='circle_click',
    size=(0.35, 0.35), vertices='circle',
    ori=0.0, pos=(0.25, 0.22), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='green', fillColor='green',
    opacity=None, depth=-1.0, interpolate=True)
circle_mouse1 = event.Mouse(win=win)
x, y = [None, None]
circle_mouse1.mouseClock = core.Clock()

# --- Initialize components for Routine "clickcircle2" ---
circle_click_2 = visual.ShapeStim(
    win=win, name='circle_click_2',
    size=(0.28, 0.28), vertices='circle',
    ori=0.0, pos=(-0.3, 0.1), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='green', fillColor='green',
    opacity=None, depth=0.0, interpolate=True)
circle_click_text1_2 = visual.TextBox2(
     win, text='Has click sobre EL CIRCULO', font='Calibri',
     pos=[0, 0.45],     letterHeight=0.06,
     size=(None, None), borderWidth=2.0,
     color=[-1.0000, -1.0000, 1.0000], colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='circle_click_text1_2',
     autoLog=True,
)
circle_mouse2 = event.Mouse(win=win)
x, y = [None, None]
circle_mouse2.mouseClock = core.Clock()

# --- Initialize components for Routine "clickcircle3" ---
circle_click_3 = visual.ShapeStim(
    win=win, name='circle_click_3',
    size=(0.15, 0.15), vertices='circle',
    ori=0.0, pos=(0.2, -0.45), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='green', fillColor='green',
    opacity=None, depth=0.0, interpolate=True)
circle_click_text1_3 = visual.TextBox2(
     win, text='Has click sobre EL CIRCULO', font='Calibri',
     pos=[0, 0.45],     letterHeight=0.06,
     size=(None, None), borderWidth=2.0,
     color=[-1.0000, -1.0000, 1.0000], colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='circle_click_text1_3',
     autoLog=True,
)
circle_mouse3 = event.Mouse(win=win)
x, y = [None, None]
circle_mouse3.mouseClock = core.Clock()

# --- Initialize components for Routine "clickcircle4" ---
circle_click_4 = visual.ShapeStim(
    win=win, name='circle_click_4',
    size=(0.1, 0.1), vertices='circle',
    ori=0.0, pos=(0.45, 0.4), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='green', fillColor='green',
    opacity=None, depth=0.0, interpolate=True)
circle_click_text1_4 = visual.TextBox2(
     win, text='Has click sobre EL CIRCULO', font='Calibri',
     pos=[0, 0.45],     letterHeight=0.06,
     size=(None, None), borderWidth=2.0,
     color=[-1.0000, -1.0000, 1.0000], colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='circle_click_text1_4',
     autoLog=True,
)
circle_mouse4 = event.Mouse(win=win)
x, y = [None, None]
circle_mouse4.mouseClock = core.Clock()

# --- Initialize components for Routine "clickcircle5" ---
circle_click_5 = visual.ShapeStim(
    win=win, name='circle_click_5',
    size=(0.075, 0.075), vertices='circle',
    ori=0.0, pos=(-0.25, 0.1), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='green', fillColor='green',
    opacity=None, depth=0.0, interpolate=True)
circle_click_text1_5 = visual.TextBox2(
     win, text='Has click sobre EL CIRCULO', font='Calibri',
     pos=[0, 0.45],     letterHeight=0.06,
     size=(None, None), borderWidth=2.0,
     color=[-1.0000, -1.0000, 1.0000], colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='circle_click_text1_5',
     autoLog=True,
)
circle_mouse5 = event.Mouse(win=win)
x, y = [None, None]
circle_mouse5.mouseClock = core.Clock()

# --- Initialize components for Routine "clickcircle6" ---
circle_click_6 = visual.ShapeStim(
    win=win, name='circle_click_6',
    size=(0.075, 0.075), vertices='circle',
    ori=0.0, pos=(-0.45, -0.3), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='green', fillColor='green',
    opacity=None, depth=0.0, interpolate=True)
circle_click_text1_6 = visual.TextBox2(
     win, text='Has click sobre EL CIRCULO', font='Calibri',
     pos=[0, 0.45],     letterHeight=0.06,
     size=(None, None), borderWidth=2.0,
     color=[-1.0000, -1.0000, 1.0000], colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='circle_click_text1_6',
     autoLog=True,
)
circle_mouse6 = event.Mouse(win=win)
x, y = [None, None]
circle_mouse6.mouseClock = core.Clock()

# --- Initialize components for Routine "clickcircle7" ---
circle_click_7 = visual.ShapeStim(
    win=win, name='circle_click_7',
    size=(0.075, 0.075), vertices='circle',
    ori=0.0, pos=(-0.4, 0.36), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='green', fillColor='green',
    opacity=None, depth=0.0, interpolate=True)
circle_click_text1_7 = visual.TextBox2(
     win, text='Has click sobre EL CIRCULO', font='Calibri',
     pos=[0, 0.45],     letterHeight=0.06,
     size=(None, None), borderWidth=2.0,
     color=[-1.0000, -1.0000, 1.0000], colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='circle_click_text1_7',
     autoLog=True,
)
circle_mouse7 = event.Mouse(win=win)
x, y = [None, None]
circle_mouse7.mouseClock = core.Clock()

# --- Initialize components for Routine "clickcircle8" ---
circle_click_8 = visual.ShapeStim(
    win=win, name='circle_click_8',
    size=(0.055, 0.055), vertices='circle',
    ori=0.0, pos=(0.1, 0.38), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='green', fillColor='green',
    opacity=None, depth=0.0, interpolate=True)
circle_click_text1_8 = visual.TextBox2(
     win, text='Has click sobre EL CIRCULO', font='Calibri',
     pos=[0, 0.45],     letterHeight=0.06,
     size=(None, None), borderWidth=2.0,
     color=[-1.0000, -1.0000, 1.0000], colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='circle_click_text1_8',
     autoLog=True,
)
circle_mouse8 = event.Mouse(win=win)
x, y = [None, None]
circle_mouse8.mouseClock = core.Clock()

# --- Initialize components for Routine "clickcircle9" ---
circle_click_9 = visual.ShapeStim(
    win=win, name='circle_click_9',
    size=(0.055, 0.055), vertices='circle',
    ori=0.0, pos=(0.4, -0.42), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='green', fillColor='green',
    opacity=None, depth=0.0, interpolate=True)
circle_click_text1_9 = visual.TextBox2(
     win, text='Has click sobre EL CIRCULO', font='Calibri',
     pos=[0, 0.45],     letterHeight=0.06,
     size=(None, None), borderWidth=2.0,
     color=[-1.0000, -1.0000, 1.0000], colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='circle_click_text1_9',
     autoLog=True,
)
circle_mouse9 = event.Mouse(win=win)
x, y = [None, None]
circle_mouse9.mouseClock = core.Clock()

# --- Initialize components for Routine "clickcircle10" ---
circle_click_10 = visual.ShapeStim(
    win=win, name='circle_click_10',
    size=(0.055, 0.055), vertices='circle',
    ori=0.0, pos=(0.43, 0.42), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='green', fillColor='green',
    opacity=None, depth=0.0, interpolate=True)
circle_click_text1_10 = visual.TextBox2(
     win, text='Has click sobre EL CIRCULO', font='Calibri',
     pos=[0, 0.45],     letterHeight=0.06,
     size=(None, None), borderWidth=2.0,
     color=[-1.0000, -1.0000, 1.0000], colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='circle_click_text1_10',
     autoLog=True,
)
circle_mouse10 = event.Mouse(win=win)
x, y = [None, None]
circle_mouse10.mouseClock = core.Clock()

# --- Initialize components for Routine "ML_INTRO" ---
ml_intro_text = visual.TextStim(win=win, name='ml_intro_text',
    text='\nElige la línea horizontal que te parezca \n¡MÁS LARGA!',
    font='Open Sans',
    pos=(0, 0.2), height=0.1, wrapWidth=20.0, ori=0.0, 
    color=[-0.4902, -0.1765, 0.7647], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
sound_2 = sound.Sound('Stimuli/Instructions/ML_long.ogg', secs=-1, stereo=True, hamming=True,
    name='sound_2')
sound_2.setVolume(1.0)
START_ML = visual.ButtonStim(win, 
    text='INICIAR', font='Arvo',
    pos=(0, -0.3),
    letterHeight=0.05,
    size=[0.3,0.15], borderWidth=1.0,
    fillColor=[1.0000, -0.4588, -1.0000], borderColor=[-1.0000, -1.0000, -1.0000],
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='START_ML'
)
START_ML.buttonClock = core.Clock()

# --- Initialize components for Routine "TEST_ML" ---
image_ML = visual.ImageStim(
    win=win,
    name='image_ML', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
LEFT_ML = visual.Rect(
    win=win, name='LEFT_ML',
    width=[0.86, 0.95][0], height=[0.86, 0.95][1],
    ori=0.0, pos=[-0.44,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor=None,
    opacity=0.0, depth=-1.0, interpolate=True)
RIGHT_ML = visual.Rect(
    win=win, name='RIGHT_ML',
    width=[0.86, 0.95][0], height=[0.86, 0.95][1],
    ori=0.0, pos=[0.44, 0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor=None,
    opacity=0.0, depth=-2.0, interpolate=True)
mouse_ML = event.Mouse(win=win)
x, y = [None, None]
mouse_ML.mouseClock = core.Clock()
sound_3 = sound.Sound('Stimuli/Instructions/ML_short.ogg', secs=-1, stereo=True, hamming=True,
    name='sound_3')
sound_3.setVolume(1.0)
ML_tracker = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Start and Stop'
)
ROI_left_ML = visual.ROI(win, name='ROI_left_ML', device=eyetracker,
    debug=False,
    shape='rectangle',
    pos=[-0.44, 0], size=[0.86, 0.95], anchor='center', ori=0.0)
ROI_right_ML = visual.ROI(win, name='ROI_right_ML', device=eyetracker,
    debug=False,
    shape='rectangle',
    pos=[0.44, 0], size=[0.86, 0.95], anchor='center', ori=0.0)
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "pressspace" ---
Next_text = visual.TextBox2(
     win, text='Para ver la siguiente imagen\nHas click sobre EL CIRCULO ROJO', font='Calibri',
     pos=[0, 0.3],     letterHeight=0.06,
     size=(None, None), borderWidth=2.0,
     color=[-1.0000, -1.0000, 1.0000], colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='Next_text',
     autoLog=True,
)
Next_polygon = visual.ShapeStim(
    win=win, name='Next_polygon',
    size=(0.15, 0.15), vertices='circle',
    ori=0.0, pos=(0, -0.20), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor=[1.0000, -0.4588, -1.0000],
    opacity=None, depth=-1.0, interpolate=True)
Next_mouse = event.Mouse(win=win)
x, y = [None, None]
Next_mouse.mouseClock = core.Clock()
key_resp_2 = keyboard.Keyboard()

# --- Initialize components for Routine "Contrast_illusion_INTRO" ---
contrast_intro_text = visual.TextStim(win=win, name='contrast_intro_text',
    text='\nElige el círculo que te parezca  \nMÁS OSCURO!\n',
    font='Open Sans',
    pos=(0, 0.2), height=0.1, wrapWidth=20.0, ori=0.0, 
    color='royalblue', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
sound_4 = sound.Sound('Stimuli/Instructions/CT_long.ogg', secs=-1, stereo=True, hamming=True,
    name='sound_4')
sound_4.setVolume(1.0)
START_contrast = visual.ButtonStim(win, 
    text='INICIAR', font='Arvo',
    pos=(0, -0.3),
    letterHeight=0.05,
    size=[0.3,0.15], borderWidth=1.0,
    fillColor='orangered', borderColor='black',
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='START_contrast'
)
START_contrast.buttonClock = core.Clock()

# --- Initialize components for Routine "TEST_contrast" ---
image_cont = visual.ImageStim(
    win=win,
    name='image_cont', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
LEFT_cont = visual.Rect(
    win=win, name='LEFT_cont',
    width=[0.86, 0.95][0], height=[0.86, 0.95][1],
    ori=0.0, pos=[-0.44,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor=None,
    opacity=0.0, depth=-1.0, interpolate=True)
RIGHT_cont = visual.Rect(
    win=win, name='RIGHT_cont',
    width=[0.86, 0.95][0], height=[0.86, 0.95][1],
    ori=0.0, pos=[0.44, 0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor=None,
    opacity=0.0, depth=-2.0, interpolate=True)
mouse_cont = event.Mouse(win=win)
x, y = [None, None]
mouse_cont.mouseClock = core.Clock()
sound_8 = sound.Sound('Stimuli/Instructions/CT_short.ogg', secs=-1, stereo=True, hamming=True,
    name='sound_8')
sound_8.setVolume(1.0)
contrast_tracker = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Start and Stop'
)
ROI_LEFT_cont = visual.ROI(win, name='ROI_LEFT_cont', device=eyetracker,
    debug=False,
    shape='rectangle',
    pos=[-0.44, 0], size=[0.86, 0.95], anchor='center', ori=0.0)
ROI_RIGHT_cont = visual.ROI(win, name='ROI_RIGHT_cont', device=eyetracker,
    debug=False,
    shape='rectangle',
    pos=[0.44, 0], size=[0.86, 0.95], anchor='center', ori=0.0)
key_resp_3 = keyboard.Keyboard()

# --- Initialize components for Routine "pressspace" ---
Next_text = visual.TextBox2(
     win, text='Para ver la siguiente imagen\nHas click sobre EL CIRCULO ROJO', font='Calibri',
     pos=[0, 0.3],     letterHeight=0.06,
     size=(None, None), borderWidth=2.0,
     color=[-1.0000, -1.0000, 1.0000], colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='Next_text',
     autoLog=True,
)
Next_polygon = visual.ShapeStim(
    win=win, name='Next_polygon',
    size=(0.15, 0.15), vertices='circle',
    ori=0.0, pos=(0, -0.20), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor=[1.0000, -0.4588, -1.0000],
    opacity=None, depth=-1.0, interpolate=True)
Next_mouse = event.Mouse(win=win)
x, y = [None, None]
Next_mouse.mouseClock = core.Clock()
key_resp_2 = keyboard.Keyboard()

# --- Initialize components for Routine "Ebbing_INTRO" ---
ebbing_intro_text = visual.TextStim(win=win, name='ebbing_intro_text',
    text='\nElige el círculo naranja que te parezca \n¡MÁS GRANDE!\n',
    font='Open Sans',
    pos=(0, 0.2), height=0.1, wrapWidth=20.0, ori=0.0, 
    color='royalblue', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
sound_5 = sound.Sound('Stimuli/Instructions/EB_long.ogg', secs=-1, stereo=True, hamming=True,
    name='sound_5')
sound_5.setVolume(1.0)
START_ebbing = visual.ButtonStim(win, 
    text='INICIAR', font='Arvo',
    pos=(0, -0.3),
    letterHeight=0.05,
    size=[0.3, 0.15], borderWidth=1.0,
    fillColor='orangered', borderColor='black',
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='START_ebbing'
)
START_ebbing.buttonClock = core.Clock()

# --- Initialize components for Routine "TEST_ebbing" ---
RIGHT_ebbing = visual.Rect(
    win=win, name='RIGHT_ebbing',
    width=[0.86, 0.95][0], height=[0.86, 0.95][1],
    ori=0.0, pos=[0.44, 0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor=None,
    opacity=0.0, depth=0.0, interpolate=True)
LEFT_ebbing = visual.Rect(
    win=win, name='LEFT_ebbing',
    width=[0.86, 0.95][0], height=[0.86, 0.95][1],
    ori=0.0, pos=[-0.44,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor=None,
    opacity=0.0, depth=-1.0, interpolate=True)
image_ebbing = visual.ImageStim(
    win=win,
    name='image_ebbing', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
mouse_ebbing = event.Mouse(win=win)
x, y = [None, None]
mouse_ebbing.mouseClock = core.Clock()
sound_9 = sound.Sound('Stimuli/Instructions/EB_short.ogg', secs=-1, stereo=True, hamming=True,
    name='sound_9')
sound_9.setVolume(1.0)
ebbing_tracker = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Start and Stop'
)
ROI_LEFT_ebbing = visual.ROI(win, name='ROI_LEFT_ebbing', device=eyetracker,
    debug=False,
    shape='rectangle',
    pos=[-0.44, 0], size=[0.86, 0.95], anchor='center', ori=0.0)
ROI_RIGHT_ebbingroi = visual.ROI(win, name='ROI_RIGHT_ebbingroi', device=eyetracker,
    debug=False,
    shape='rectangle',
    pos=[0.44, 0], size=[0.86, 0.95], anchor='center', ori=0.0)
key_resp_4 = keyboard.Keyboard()

# --- Initialize components for Routine "pressspace" ---
Next_text = visual.TextBox2(
     win, text='Para ver la siguiente imagen\nHas click sobre EL CIRCULO ROJO', font='Calibri',
     pos=[0, 0.3],     letterHeight=0.06,
     size=(None, None), borderWidth=2.0,
     color=[-1.0000, -1.0000, 1.0000], colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='Next_text',
     autoLog=True,
)
Next_polygon = visual.ShapeStim(
    win=win, name='Next_polygon',
    size=(0.15, 0.15), vertices='circle',
    ori=0.0, pos=(0, -0.20), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor=[1.0000, -0.4588, -1.0000],
    opacity=None, depth=-1.0, interpolate=True)
Next_mouse = event.Mouse(win=win)
x, y = [None, None]
Next_mouse.mouseClock = core.Clock()
key_resp_2 = keyboard.Keyboard()

# --- Initialize components for Routine "Kanizsa_INTRO" ---
kanizsa_intro_text = visual.TextStim(win=win, name='kanizsa_intro_text',
    text='\nElige el lado con el\n¡CUADRADO BLANCO!',
    font='Open Sans',
    pos=(0, 0.2), height=0.1, wrapWidth=20.0, ori=0.0, 
    color='royalblue', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
sound_6 = sound.Sound('Stimuli/Instructions/KZS_long.ogg', secs=-1, stereo=True, hamming=True,
    name='sound_6')
sound_6.setVolume(1.0)
START_KN = visual.ButtonStim(win, 
    text='INICIAR', font='Arvo',
    pos=[0, -0.3],
    letterHeight=0.05,
    size=[0.3, 0.15], borderWidth=1.0,
    fillColor='orangered', borderColor='black',
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='START_KN'
)
START_KN.buttonClock = core.Clock()

# --- Initialize components for Routine "trainingKZS" ---
triangle = visual.ImageStim(
    win=win,
    name='triangle', 
    image='Stimuli/Training/triang.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.5, 0.25), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
threefourth = visual.ImageStim(
    win=win,
    name='threefourth', 
    image='Stimuli/Training/whitesquare3p4.png', mask=None, anchor='center',
    ori=0.0, pos=(0.3, 0.25), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
twofourth = visual.ImageStim(
    win=win,
    name='twofourth', 
    image='Stimuli/Training/whitesquare2p4.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.3, -0.25), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
whitesquare = visual.ImageStim(
    win=win,
    name='whitesquare', 
    image='Stimuli/Training/whitesquare.png', mask=None, anchor='center',
    ori=0.0, pos=(0.5, -0.15), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()

# --- Initialize components for Routine "trainingKZS_2" ---
triangle_2 = visual.ImageStim(
    win=win,
    name='triangle_2', 
    image='Stimuli/Training/triang.png', mask=None, anchor='center',
    ori=23.0, pos=[-0.3, -0.25], size=[0.5,0.5],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
threefourth_2 = visual.ImageStim(
    win=win,
    name='threefourth_2', 
    image='Stimuli/Training/whitesquare3p4.png', mask=None, anchor='center',
    ori=350.0, pos=(0.5, -0.15), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
twofourth_2 = visual.ImageStim(
    win=win,
    name='twofourth_2', 
    image='Stimuli/Training/whitesquare2p4.png', mask=None, anchor='center',
    ori=0.0, pos=(0.3, 0.25), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
whitesquare_2 = visual.ImageStim(
    win=win,
    name='whitesquare_2', 
    image='Stimuli/Training/whitesquare.png', mask=None, anchor='center',
    ori=45.0, pos=(-0.5, 0.25), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
mouse_3 = event.Mouse(win=win)
x, y = [None, None]
mouse_3.mouseClock = core.Clock()

# --- Initialize components for Routine "TEST_knzs" ---
image_KN = visual.ImageStim(
    win=win,
    name='image_KN', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
LEFT_KN = visual.Rect(
    win=win, name='LEFT_KN',
    width=[0.86, 0.95][0], height=[0.86, 0.95][1],
    ori=0.0, pos=[-0.44,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor=None,
    opacity=0.0, depth=-1.0, interpolate=True)
RIGHT_KN = visual.Rect(
    win=win, name='RIGHT_KN',
    width=[0.86, 0.95][0], height=[0.86, 0.95][1],
    ori=0.0, pos=[0.44, 0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor=None,
    opacity=0.0, depth=-2.0, interpolate=True)
mouse_KN = event.Mouse(win=win)
x, y = [None, None]
mouse_KN.mouseClock = core.Clock()
sound_11 = sound.Sound('Stimuli/Instructions/KZS_short.ogg', secs=-1, stereo=True, hamming=True,
    name='sound_11')
sound_11.setVolume(1.0)
Kanizsa_tracker = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Start and Stop'
)
ROI_LEFT_KN = visual.ROI(win, name='ROI_LEFT_KN', device=eyetracker,
    debug=False,
    shape='rectangle',
    pos=[-0.44, 0], size=[0.86, 0.95], anchor='center', ori=0.0)
ROI_RIGHT_KN = visual.ROI(win, name='ROI_RIGHT_KN', device=eyetracker,
    debug=False,
    shape='rectangle',
    pos=[0.44, 0], size=[0.86, 0.95], anchor='center', ori=0.0)
key_resp_5 = keyboard.Keyboard()

# --- Initialize components for Routine "pressspace" ---
Next_text = visual.TextBox2(
     win, text='Para ver la siguiente imagen\nHas click sobre EL CIRCULO ROJO', font='Calibri',
     pos=[0, 0.3],     letterHeight=0.06,
     size=(None, None), borderWidth=2.0,
     color=[-1.0000, -1.0000, 1.0000], colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='Next_text',
     autoLog=True,
)
Next_polygon = visual.ShapeStim(
    win=win, name='Next_polygon',
    size=(0.15, 0.15), vertices='circle',
    ori=0.0, pos=(0, -0.20), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor=[1.0000, -0.4588, -1.0000],
    opacity=None, depth=-1.0, interpolate=True)
Next_mouse = event.Mouse(win=win)
x, y = [None, None]
Next_mouse.mouseClock = core.Clock()
key_resp_2 = keyboard.Keyboard()

# --- Initialize components for Routine "MS_INTRO" ---
MS_intro_text = visual.TextStim(win=win, name='MS_intro_text',
    text='\nElige aquella en la que notas \n¡MAYOR MOVIMIENTO!\n',
    font='Open Sans',
    pos=(0, 0.2), height=0.1, wrapWidth=20.0, ori=0.0, 
    color='royalblue', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
sound_7 = sound.Sound('Stimuli/Instructions/MS_long.ogg', secs=-1, stereo=True, hamming=True,
    name='sound_7')
sound_7.setVolume(1.0)
START_MS = visual.ButtonStim(win, 
    text='INICIAR', font='Arvo',
    pos=[0, -0.3],
    letterHeight=0.05,
    size=[0.3, 0.15], borderWidth=1.0,
    fillColor='orangered', borderColor='black',
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='START_MS'
)
START_MS.buttonClock = core.Clock()

# --- Initialize components for Routine "TEST_MS" ---
image_MS = visual.ImageStim(
    win=win,
    name='image_MS', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
LEFT_MS = visual.Rect(
    win=win, name='LEFT_MS',
    width=[0.86, 0.95][0], height=[0.86, 0.95][1],
    ori=0.0, pos=[-0.44,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor=None,
    opacity=0.0, depth=-1.0, interpolate=True)
RIGHT_MS = visual.Rect(
    win=win, name='RIGHT_MS',
    width=[0.86, 0.95][0], height=[0.86, 0.95][1],
    ori=0.0, pos=[0.44, 0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor=None,
    opacity=0.0, depth=-2.0, interpolate=True)
mouse_MS = event.Mouse(win=win)
x, y = [None, None]
mouse_MS.mouseClock = core.Clock()
sound_10 = sound.Sound('Stimuli/Instructions/MS_short.ogg', secs=-1, stereo=True, hamming=True,
    name='sound_10')
sound_10.setVolume(1.0)
MS_tracker = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Start and Stop'
)
ROI_LEFT_MS = visual.ROI(win, name='ROI_LEFT_MS', device=eyetracker,
    debug=False,
    shape='rectangle',
    pos=[-0.44, 0], size=[0.86, 0.95], anchor='center', ori=0.0)
ROI_RIGHT_MS = visual.ROI(win, name='ROI_RIGHT_MS', device=eyetracker,
    debug=False,
    shape='rectangle',
    pos=[0.44, 0], size=[0.86, 0.95], anchor='center', ori=0.0)
key_resp_6 = keyboard.Keyboard()

# --- Initialize components for Routine "pressspace" ---
Next_text = visual.TextBox2(
     win, text='Para ver la siguiente imagen\nHas click sobre EL CIRCULO ROJO', font='Calibri',
     pos=[0, 0.3],     letterHeight=0.06,
     size=(None, None), borderWidth=2.0,
     color=[-1.0000, -1.0000, 1.0000], colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='Next_text',
     autoLog=True,
)
Next_polygon = visual.ShapeStim(
    win=win, name='Next_polygon',
    size=(0.15, 0.15), vertices='circle',
    ori=0.0, pos=(0, -0.20), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor=[1.0000, -0.4588, -1.0000],
    opacity=None, depth=-1.0, interpolate=True)
Next_mouse = event.Mouse(win=win)
x, y = [None, None]
Next_mouse.mouseClock = core.Clock()
key_resp_2 = keyboard.Keyboard()

# --- Initialize components for Routine "bye" ---
text_2 = visual.TextStim(win=win, name='text_2',
    text='¡GRACIAS!',
    font='Open Sans',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color=[-0.4902, -0.1765, 0.7647], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "hello" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
sound_1.setSound('Stimuli/Instructions/Instrucción inicial2.ogg', hamming=True)
sound_1.setVolume(1.0, log=False)
# keep track of which components have finished
helloComponents = [text, buttonhello, sound_1]
for thisComponent in helloComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "hello" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *buttonhello* updates
    if buttonhello.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        buttonhello.frameNStart = frameN  # exact frame index
        buttonhello.tStart = t  # local t and not account for scr refresh
        buttonhello.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(buttonhello, 'tStartRefresh')  # time at next scr refresh
        buttonhello.setAutoDraw(True)
    if buttonhello.status == STARTED:
        # check whether buttonhello has been pressed
        if buttonhello.isClicked:
            if not buttonhello.wasClicked:
                buttonhello.timesOn.append(globalClock.getTime()) # store time of first click
                buttonhello.timesOff.append(globalClock.getTime()) # store time clicked until
            else:
                buttonhello.timesOff[-1] = globalClock.getTime() # update time clicked until
            if not buttonhello.wasClicked:
                continueRoutine = False  # end routine when buttonhello is clicked
                None
            buttonhello.wasClicked = True  # if buttonhello is still clicked next frame, it is not a new click
        else:
            buttonhello.wasClicked = False  # if buttonhello is clicked next frame, it is a new click
    else:
        buttonhello.wasClicked = False  # if buttonhello is clicked next frame, it is a new click
    # start/stop sound_1
    if sound_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sound_1.frameNStart = frameN  # exact frame index
        sound_1.tStart = t  # local t and not account for scr refresh
        sound_1.tStartRefresh = tThisFlipGlobal  # on global time
        sound_1.play(when=win)  # sync with win flip
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in helloComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "hello" ---
for thisComponent in helloComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('buttonhello.numClicks', buttonhello.numClicks)
if buttonhello.numClicks:
   thisExp.addData('buttonhello.timesOn', buttonhello.timesOn)
   thisExp.addData('buttonhello.timesOff', buttonhello.timesOff)
else:
   thisExp.addData('buttonhello.timesOn', "")
   thisExp.addData('buttonhello.timesOff', "")
sound_1.stop()  # ensure sound has stopped at end of routine
# the Routine "hello" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "hello_training" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# setup some python lists for storing info about the hellomouse
hellomouse.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
hello_trainingComponents = [hellotraining_poly, hellomouse, hellotraining]
for thisComponent in hello_trainingComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "hello_training" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *hellotraining_poly* updates
    if hellotraining_poly.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        hellotraining_poly.frameNStart = frameN  # exact frame index
        hellotraining_poly.tStart = t  # local t and not account for scr refresh
        hellotraining_poly.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(hellotraining_poly, 'tStartRefresh')  # time at next scr refresh
        hellotraining_poly.setAutoDraw(True)
    # *hellomouse* updates
    if hellomouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        hellomouse.frameNStart = frameN  # exact frame index
        hellomouse.tStart = t  # local t and not account for scr refresh
        hellomouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(hellomouse, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('hellomouse.started', t)
        hellomouse.status = STARTED
        prevButtonState = hellomouse.getPressed()  # if button is down already this ISN'T a new click
    if hellomouse.status == STARTED:  # only update if started and not finished!
        buttons = hellomouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(hellotraining_poly)
                    clickableList = hellotraining_poly
                except:
                    clickableList = [hellotraining_poly]
                for obj in clickableList:
                    if obj.contains(hellomouse):
                        gotValidClick = True
                        hellomouse.clicked_name.append(obj.name)
                if gotValidClick:  
                    continueRoutine = False  # abort routine on response
    
    # *hellotraining* updates
    if hellotraining.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        hellotraining.frameNStart = frameN  # exact frame index
        hellotraining.tStart = t  # local t and not account for scr refresh
        hellotraining.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(hellotraining, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'hellotraining.started')
        hellotraining.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in hello_trainingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "hello_training" ---
for thisComponent in hello_trainingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
x, y = hellomouse.getPos()
buttons = hellomouse.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    try:
        iter(hellotraining_poly)
        clickableList = hellotraining_poly
    except:
        clickableList = [hellotraining_poly]
    for obj in clickableList:
        if obj.contains(hellomouse):
            gotValidClick = True
            hellomouse.clicked_name.append(obj.name)
thisExp.addData('hellomouse.x', x)
thisExp.addData('hellomouse.y', y)
thisExp.addData('hellomouse.leftButton', buttons[0])
thisExp.addData('hellomouse.midButton', buttons[1])
thisExp.addData('hellomouse.rightButton', buttons[2])
if len(hellomouse.clicked_name):
    thisExp.addData('hellomouse.clicked_name', hellomouse.clicked_name[0])
thisExp.nextEntry()
# the Routine "hello_training" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "longerline_1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
Longerlinetext1.reset()
# setup some python lists for storing info about the longerlinemouse1
longerlinemouse1.x = []
longerlinemouse1.y = []
longerlinemouse1.leftButton = []
longerlinemouse1.midButton = []
longerlinemouse1.rightButton = []
longerlinemouse1.time = []
longerlinemouse1.clicked_name = []
gotValidClick = False  # until a click is received
longerlinemouse1.mouseClock.reset()
# keep track of which components have finished
longerline_1Components = [longerline1pic, longerline1area, Longerlinetext1, longerlinemouse1]
for thisComponent in longerline_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "longerline_1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *longerline1pic* updates
    if longerline1pic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        longerline1pic.frameNStart = frameN  # exact frame index
        longerline1pic.tStart = t  # local t and not account for scr refresh
        longerline1pic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(longerline1pic, 'tStartRefresh')  # time at next scr refresh
        longerline1pic.setAutoDraw(True)
    
    # *longerline1area* updates
    if longerline1area.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        longerline1area.frameNStart = frameN  # exact frame index
        longerline1area.tStart = t  # local t and not account for scr refresh
        longerline1area.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(longerline1area, 'tStartRefresh')  # time at next scr refresh
        longerline1area.setAutoDraw(True)
    
    # *Longerlinetext1* updates
    if Longerlinetext1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Longerlinetext1.frameNStart = frameN  # exact frame index
        Longerlinetext1.tStart = t  # local t and not account for scr refresh
        Longerlinetext1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Longerlinetext1, 'tStartRefresh')  # time at next scr refresh
        Longerlinetext1.setAutoDraw(True)
    # *longerlinemouse1* updates
    if longerlinemouse1.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        longerlinemouse1.frameNStart = frameN  # exact frame index
        longerlinemouse1.tStart = t  # local t and not account for scr refresh
        longerlinemouse1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(longerlinemouse1, 'tStartRefresh')  # time at next scr refresh
        longerlinemouse1.status = STARTED
        prevButtonState = longerlinemouse1.getPressed()  # if button is down already this ISN'T a new click
    if longerlinemouse1.status == STARTED:  # only update if started and not finished!
        buttons = longerlinemouse1.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(longerline1area)
                    clickableList = longerline1area
                except:
                    clickableList = [longerline1area]
                for obj in clickableList:
                    if obj.contains(longerlinemouse1):
                        gotValidClick = True
                        longerlinemouse1.clicked_name.append(obj.name)
                if gotValidClick:
                    x, y = longerlinemouse1.getPos()
                    longerlinemouse1.x.append(x)
                    longerlinemouse1.y.append(y)
                    buttons = longerlinemouse1.getPressed()
                    longerlinemouse1.leftButton.append(buttons[0])
                    longerlinemouse1.midButton.append(buttons[1])
                    longerlinemouse1.rightButton.append(buttons[2])
                    longerlinemouse1.time.append(longerlinemouse1.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in longerline_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "longerline_1" ---
for thisComponent in longerline_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('longerlinemouse1.x', longerlinemouse1.x)
thisExp.addData('longerlinemouse1.y', longerlinemouse1.y)
thisExp.addData('longerlinemouse1.leftButton', longerlinemouse1.leftButton)
thisExp.addData('longerlinemouse1.midButton', longerlinemouse1.midButton)
thisExp.addData('longerlinemouse1.rightButton', longerlinemouse1.rightButton)
thisExp.addData('longerlinemouse1.time', longerlinemouse1.time)
thisExp.addData('longerlinemouse1.clicked_name', longerlinemouse1.clicked_name)
thisExp.nextEntry()
# the Routine "longerline_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "longerline_2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
Longerlinetext2.reset()
# setup some python lists for storing info about the longerline2mouse
longerline2mouse.x = []
longerline2mouse.y = []
longerline2mouse.leftButton = []
longerline2mouse.midButton = []
longerline2mouse.rightButton = []
longerline2mouse.time = []
longerline2mouse.clicked_name = []
gotValidClick = False  # until a click is received
longerline2mouse.mouseClock.reset()
# keep track of which components have finished
longerline_2Components = [longerline2pic, longerline2area, Longerlinetext2, longerline2mouse]
for thisComponent in longerline_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "longerline_2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *longerline2pic* updates
    if longerline2pic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        longerline2pic.frameNStart = frameN  # exact frame index
        longerline2pic.tStart = t  # local t and not account for scr refresh
        longerline2pic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(longerline2pic, 'tStartRefresh')  # time at next scr refresh
        longerline2pic.setAutoDraw(True)
    
    # *longerline2area* updates
    if longerline2area.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        longerline2area.frameNStart = frameN  # exact frame index
        longerline2area.tStart = t  # local t and not account for scr refresh
        longerline2area.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(longerline2area, 'tStartRefresh')  # time at next scr refresh
        longerline2area.setAutoDraw(True)
    
    # *Longerlinetext2* updates
    if Longerlinetext2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Longerlinetext2.frameNStart = frameN  # exact frame index
        Longerlinetext2.tStart = t  # local t and not account for scr refresh
        Longerlinetext2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Longerlinetext2, 'tStartRefresh')  # time at next scr refresh
        Longerlinetext2.setAutoDraw(True)
    # *longerline2mouse* updates
    if longerline2mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        longerline2mouse.frameNStart = frameN  # exact frame index
        longerline2mouse.tStart = t  # local t and not account for scr refresh
        longerline2mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(longerline2mouse, 'tStartRefresh')  # time at next scr refresh
        longerline2mouse.status = STARTED
        prevButtonState = longerline2mouse.getPressed()  # if button is down already this ISN'T a new click
    if longerline2mouse.status == STARTED:  # only update if started and not finished!
        buttons = longerline2mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(longerline2area)
                    clickableList = longerline2area
                except:
                    clickableList = [longerline2area]
                for obj in clickableList:
                    if obj.contains(longerline2mouse):
                        gotValidClick = True
                        longerline2mouse.clicked_name.append(obj.name)
                if gotValidClick:
                    x, y = longerline2mouse.getPos()
                    longerline2mouse.x.append(x)
                    longerline2mouse.y.append(y)
                    buttons = longerline2mouse.getPressed()
                    longerline2mouse.leftButton.append(buttons[0])
                    longerline2mouse.midButton.append(buttons[1])
                    longerline2mouse.rightButton.append(buttons[2])
                    longerline2mouse.time.append(longerline2mouse.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in longerline_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "longerline_2" ---
for thisComponent in longerline_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('longerline2mouse.x', longerline2mouse.x)
thisExp.addData('longerline2mouse.y', longerline2mouse.y)
thisExp.addData('longerline2mouse.leftButton', longerline2mouse.leftButton)
thisExp.addData('longerline2mouse.midButton', longerline2mouse.midButton)
thisExp.addData('longerline2mouse.rightButton', longerline2mouse.rightButton)
thisExp.addData('longerline2mouse.time', longerline2mouse.time)
thisExp.addData('longerline2mouse.clicked_name', longerline2mouse.clicked_name)
thisExp.nextEntry()
# the Routine "longerline_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "longerline_3" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
Longerlinetext3.reset()
# setup some python lists for storing info about the longerline3mouse
longerline3mouse.x = []
longerline3mouse.y = []
longerline3mouse.leftButton = []
longerline3mouse.midButton = []
longerline3mouse.rightButton = []
longerline3mouse.time = []
longerline3mouse.clicked_name = []
gotValidClick = False  # until a click is received
longerline3mouse.mouseClock.reset()
# keep track of which components have finished
longerline_3Components = [longerline3pic, longerline3area, Longerlinetext3, longerline3mouse]
for thisComponent in longerline_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "longerline_3" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *longerline3pic* updates
    if longerline3pic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        longerline3pic.frameNStart = frameN  # exact frame index
        longerline3pic.tStart = t  # local t and not account for scr refresh
        longerline3pic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(longerline3pic, 'tStartRefresh')  # time at next scr refresh
        longerline3pic.setAutoDraw(True)
    
    # *longerline3area* updates
    if longerline3area.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        longerline3area.frameNStart = frameN  # exact frame index
        longerline3area.tStart = t  # local t and not account for scr refresh
        longerline3area.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(longerline3area, 'tStartRefresh')  # time at next scr refresh
        longerline3area.setAutoDraw(True)
    
    # *Longerlinetext3* updates
    if Longerlinetext3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Longerlinetext3.frameNStart = frameN  # exact frame index
        Longerlinetext3.tStart = t  # local t and not account for scr refresh
        Longerlinetext3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Longerlinetext3, 'tStartRefresh')  # time at next scr refresh
        Longerlinetext3.setAutoDraw(True)
    # *longerline3mouse* updates
    if longerline3mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        longerline3mouse.frameNStart = frameN  # exact frame index
        longerline3mouse.tStart = t  # local t and not account for scr refresh
        longerline3mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(longerline3mouse, 'tStartRefresh')  # time at next scr refresh
        longerline3mouse.status = STARTED
        prevButtonState = longerline3mouse.getPressed()  # if button is down already this ISN'T a new click
    if longerline3mouse.status == STARTED:  # only update if started and not finished!
        buttons = longerline3mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(longerline3area)
                    clickableList = longerline3area
                except:
                    clickableList = [longerline3area]
                for obj in clickableList:
                    if obj.contains(longerline3mouse):
                        gotValidClick = True
                        longerline3mouse.clicked_name.append(obj.name)
                if gotValidClick:
                    x, y = longerline3mouse.getPos()
                    longerline3mouse.x.append(x)
                    longerline3mouse.y.append(y)
                    buttons = longerline3mouse.getPressed()
                    longerline3mouse.leftButton.append(buttons[0])
                    longerline3mouse.midButton.append(buttons[1])
                    longerline3mouse.rightButton.append(buttons[2])
                    longerline3mouse.time.append(longerline3mouse.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in longerline_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "longerline_3" ---
for thisComponent in longerline_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('longerline3mouse.x', longerline3mouse.x)
thisExp.addData('longerline3mouse.y', longerline3mouse.y)
thisExp.addData('longerline3mouse.leftButton', longerline3mouse.leftButton)
thisExp.addData('longerline3mouse.midButton', longerline3mouse.midButton)
thisExp.addData('longerline3mouse.rightButton', longerline3mouse.rightButton)
thisExp.addData('longerline3mouse.time', longerline3mouse.time)
thisExp.addData('longerline3mouse.clicked_name', longerline3mouse.clicked_name)
thisExp.nextEntry()
# the Routine "longerline_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "clickcircle1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
circle_click_text1.reset()
# setup some python lists for storing info about the circle_mouse1
circle_mouse1.x = []
circle_mouse1.y = []
circle_mouse1.leftButton = []
circle_mouse1.midButton = []
circle_mouse1.rightButton = []
circle_mouse1.time = []
circle_mouse1.clicked_name = []
gotValidClick = False  # until a click is received
circle_mouse1.mouseClock.reset()
# keep track of which components have finished
clickcircle1Components = [circle_click_text1, circle_click, circle_mouse1]
for thisComponent in clickcircle1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "clickcircle1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *circle_click_text1* updates
    if circle_click_text1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        circle_click_text1.frameNStart = frameN  # exact frame index
        circle_click_text1.tStart = t  # local t and not account for scr refresh
        circle_click_text1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(circle_click_text1, 'tStartRefresh')  # time at next scr refresh
        circle_click_text1.setAutoDraw(True)
    
    # *circle_click* updates
    if circle_click.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        circle_click.frameNStart = frameN  # exact frame index
        circle_click.tStart = t  # local t and not account for scr refresh
        circle_click.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(circle_click, 'tStartRefresh')  # time at next scr refresh
        circle_click.setAutoDraw(True)
    # *circle_mouse1* updates
    if circle_mouse1.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        circle_mouse1.frameNStart = frameN  # exact frame index
        circle_mouse1.tStart = t  # local t and not account for scr refresh
        circle_mouse1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(circle_mouse1, 'tStartRefresh')  # time at next scr refresh
        circle_mouse1.status = STARTED
        prevButtonState = circle_mouse1.getPressed()  # if button is down already this ISN'T a new click
    if circle_mouse1.status == STARTED:  # only update if started and not finished!
        buttons = circle_mouse1.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(circle_click)
                    clickableList = circle_click
                except:
                    clickableList = [circle_click]
                for obj in clickableList:
                    if obj.contains(circle_mouse1):
                        gotValidClick = True
                        circle_mouse1.clicked_name.append(obj.name)
                if gotValidClick:
                    x, y = circle_mouse1.getPos()
                    circle_mouse1.x.append(x)
                    circle_mouse1.y.append(y)
                    buttons = circle_mouse1.getPressed()
                    circle_mouse1.leftButton.append(buttons[0])
                    circle_mouse1.midButton.append(buttons[1])
                    circle_mouse1.rightButton.append(buttons[2])
                    circle_mouse1.time.append(circle_mouse1.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in clickcircle1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "clickcircle1" ---
for thisComponent in clickcircle1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('circle_mouse1.x', circle_mouse1.x)
thisExp.addData('circle_mouse1.y', circle_mouse1.y)
thisExp.addData('circle_mouse1.leftButton', circle_mouse1.leftButton)
thisExp.addData('circle_mouse1.midButton', circle_mouse1.midButton)
thisExp.addData('circle_mouse1.rightButton', circle_mouse1.rightButton)
thisExp.addData('circle_mouse1.time', circle_mouse1.time)
thisExp.addData('circle_mouse1.clicked_name', circle_mouse1.clicked_name)
thisExp.nextEntry()
# the Routine "clickcircle1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "clickcircle2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
circle_click_text1_2.reset()
# setup some python lists for storing info about the circle_mouse2
circle_mouse2.x = []
circle_mouse2.y = []
circle_mouse2.leftButton = []
circle_mouse2.midButton = []
circle_mouse2.rightButton = []
circle_mouse2.time = []
circle_mouse2.clicked_name = []
gotValidClick = False  # until a click is received
circle_mouse2.mouseClock.reset()
# keep track of which components have finished
clickcircle2Components = [circle_click_2, circle_click_text1_2, circle_mouse2]
for thisComponent in clickcircle2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "clickcircle2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *circle_click_2* updates
    if circle_click_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        circle_click_2.frameNStart = frameN  # exact frame index
        circle_click_2.tStart = t  # local t and not account for scr refresh
        circle_click_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(circle_click_2, 'tStartRefresh')  # time at next scr refresh
        circle_click_2.setAutoDraw(True)
    
    # *circle_click_text1_2* updates
    if circle_click_text1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        circle_click_text1_2.frameNStart = frameN  # exact frame index
        circle_click_text1_2.tStart = t  # local t and not account for scr refresh
        circle_click_text1_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(circle_click_text1_2, 'tStartRefresh')  # time at next scr refresh
        circle_click_text1_2.setAutoDraw(True)
    # *circle_mouse2* updates
    if circle_mouse2.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        circle_mouse2.frameNStart = frameN  # exact frame index
        circle_mouse2.tStart = t  # local t and not account for scr refresh
        circle_mouse2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(circle_mouse2, 'tStartRefresh')  # time at next scr refresh
        circle_mouse2.status = STARTED
        prevButtonState = circle_mouse2.getPressed()  # if button is down already this ISN'T a new click
    if circle_mouse2.status == STARTED:  # only update if started and not finished!
        buttons = circle_mouse2.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(circle_click_2)
                    clickableList = circle_click_2
                except:
                    clickableList = [circle_click_2]
                for obj in clickableList:
                    if obj.contains(circle_mouse2):
                        gotValidClick = True
                        circle_mouse2.clicked_name.append(obj.name)
                if gotValidClick:
                    x, y = circle_mouse2.getPos()
                    circle_mouse2.x.append(x)
                    circle_mouse2.y.append(y)
                    buttons = circle_mouse2.getPressed()
                    circle_mouse2.leftButton.append(buttons[0])
                    circle_mouse2.midButton.append(buttons[1])
                    circle_mouse2.rightButton.append(buttons[2])
                    circle_mouse2.time.append(circle_mouse2.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in clickcircle2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "clickcircle2" ---
for thisComponent in clickcircle2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('circle_mouse2.x', circle_mouse2.x)
thisExp.addData('circle_mouse2.y', circle_mouse2.y)
thisExp.addData('circle_mouse2.leftButton', circle_mouse2.leftButton)
thisExp.addData('circle_mouse2.midButton', circle_mouse2.midButton)
thisExp.addData('circle_mouse2.rightButton', circle_mouse2.rightButton)
thisExp.addData('circle_mouse2.time', circle_mouse2.time)
thisExp.addData('circle_mouse2.clicked_name', circle_mouse2.clicked_name)
thisExp.nextEntry()
# the Routine "clickcircle2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "clickcircle3" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
circle_click_text1_3.reset()
# setup some python lists for storing info about the circle_mouse3
circle_mouse3.x = []
circle_mouse3.y = []
circle_mouse3.leftButton = []
circle_mouse3.midButton = []
circle_mouse3.rightButton = []
circle_mouse3.time = []
circle_mouse3.clicked_name = []
gotValidClick = False  # until a click is received
circle_mouse3.mouseClock.reset()
# keep track of which components have finished
clickcircle3Components = [circle_click_3, circle_click_text1_3, circle_mouse3]
for thisComponent in clickcircle3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "clickcircle3" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *circle_click_3* updates
    if circle_click_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        circle_click_3.frameNStart = frameN  # exact frame index
        circle_click_3.tStart = t  # local t and not account for scr refresh
        circle_click_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(circle_click_3, 'tStartRefresh')  # time at next scr refresh
        circle_click_3.setAutoDraw(True)
    
    # *circle_click_text1_3* updates
    if circle_click_text1_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        circle_click_text1_3.frameNStart = frameN  # exact frame index
        circle_click_text1_3.tStart = t  # local t and not account for scr refresh
        circle_click_text1_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(circle_click_text1_3, 'tStartRefresh')  # time at next scr refresh
        circle_click_text1_3.setAutoDraw(True)
    # *circle_mouse3* updates
    if circle_mouse3.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        circle_mouse3.frameNStart = frameN  # exact frame index
        circle_mouse3.tStart = t  # local t and not account for scr refresh
        circle_mouse3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(circle_mouse3, 'tStartRefresh')  # time at next scr refresh
        circle_mouse3.status = STARTED
        prevButtonState = circle_mouse3.getPressed()  # if button is down already this ISN'T a new click
    if circle_mouse3.status == STARTED:  # only update if started and not finished!
        buttons = circle_mouse3.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(circle_click_3)
                    clickableList = circle_click_3
                except:
                    clickableList = [circle_click_3]
                for obj in clickableList:
                    if obj.contains(circle_mouse3):
                        gotValidClick = True
                        circle_mouse3.clicked_name.append(obj.name)
                if gotValidClick:
                    x, y = circle_mouse3.getPos()
                    circle_mouse3.x.append(x)
                    circle_mouse3.y.append(y)
                    buttons = circle_mouse3.getPressed()
                    circle_mouse3.leftButton.append(buttons[0])
                    circle_mouse3.midButton.append(buttons[1])
                    circle_mouse3.rightButton.append(buttons[2])
                    circle_mouse3.time.append(circle_mouse3.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in clickcircle3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "clickcircle3" ---
for thisComponent in clickcircle3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('circle_mouse3.x', circle_mouse3.x)
thisExp.addData('circle_mouse3.y', circle_mouse3.y)
thisExp.addData('circle_mouse3.leftButton', circle_mouse3.leftButton)
thisExp.addData('circle_mouse3.midButton', circle_mouse3.midButton)
thisExp.addData('circle_mouse3.rightButton', circle_mouse3.rightButton)
thisExp.addData('circle_mouse3.time', circle_mouse3.time)
thisExp.addData('circle_mouse3.clicked_name', circle_mouse3.clicked_name)
thisExp.nextEntry()
# the Routine "clickcircle3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "clickcircle4" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
circle_click_text1_4.reset()
# setup some python lists for storing info about the circle_mouse4
circle_mouse4.x = []
circle_mouse4.y = []
circle_mouse4.leftButton = []
circle_mouse4.midButton = []
circle_mouse4.rightButton = []
circle_mouse4.time = []
circle_mouse4.clicked_name = []
gotValidClick = False  # until a click is received
circle_mouse4.mouseClock.reset()
# keep track of which components have finished
clickcircle4Components = [circle_click_4, circle_click_text1_4, circle_mouse4]
for thisComponent in clickcircle4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "clickcircle4" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *circle_click_4* updates
    if circle_click_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        circle_click_4.frameNStart = frameN  # exact frame index
        circle_click_4.tStart = t  # local t and not account for scr refresh
        circle_click_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(circle_click_4, 'tStartRefresh')  # time at next scr refresh
        circle_click_4.setAutoDraw(True)
    
    # *circle_click_text1_4* updates
    if circle_click_text1_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        circle_click_text1_4.frameNStart = frameN  # exact frame index
        circle_click_text1_4.tStart = t  # local t and not account for scr refresh
        circle_click_text1_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(circle_click_text1_4, 'tStartRefresh')  # time at next scr refresh
        circle_click_text1_4.setAutoDraw(True)
    # *circle_mouse4* updates
    if circle_mouse4.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        circle_mouse4.frameNStart = frameN  # exact frame index
        circle_mouse4.tStart = t  # local t and not account for scr refresh
        circle_mouse4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(circle_mouse4, 'tStartRefresh')  # time at next scr refresh
        circle_mouse4.status = STARTED
        prevButtonState = circle_mouse4.getPressed()  # if button is down already this ISN'T a new click
    if circle_mouse4.status == STARTED:  # only update if started and not finished!
        buttons = circle_mouse4.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(circle_click_4)
                    clickableList = circle_click_4
                except:
                    clickableList = [circle_click_4]
                for obj in clickableList:
                    if obj.contains(circle_mouse4):
                        gotValidClick = True
                        circle_mouse4.clicked_name.append(obj.name)
                if gotValidClick:
                    x, y = circle_mouse4.getPos()
                    circle_mouse4.x.append(x)
                    circle_mouse4.y.append(y)
                    buttons = circle_mouse4.getPressed()
                    circle_mouse4.leftButton.append(buttons[0])
                    circle_mouse4.midButton.append(buttons[1])
                    circle_mouse4.rightButton.append(buttons[2])
                    circle_mouse4.time.append(circle_mouse4.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in clickcircle4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "clickcircle4" ---
for thisComponent in clickcircle4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('circle_mouse4.x', circle_mouse4.x)
thisExp.addData('circle_mouse4.y', circle_mouse4.y)
thisExp.addData('circle_mouse4.leftButton', circle_mouse4.leftButton)
thisExp.addData('circle_mouse4.midButton', circle_mouse4.midButton)
thisExp.addData('circle_mouse4.rightButton', circle_mouse4.rightButton)
thisExp.addData('circle_mouse4.time', circle_mouse4.time)
thisExp.addData('circle_mouse4.clicked_name', circle_mouse4.clicked_name)
thisExp.nextEntry()
# the Routine "clickcircle4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "clickcircle5" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
circle_click_text1_5.reset()
# setup some python lists for storing info about the circle_mouse5
circle_mouse5.x = []
circle_mouse5.y = []
circle_mouse5.leftButton = []
circle_mouse5.midButton = []
circle_mouse5.rightButton = []
circle_mouse5.time = []
circle_mouse5.clicked_name = []
gotValidClick = False  # until a click is received
circle_mouse5.mouseClock.reset()
# keep track of which components have finished
clickcircle5Components = [circle_click_5, circle_click_text1_5, circle_mouse5]
for thisComponent in clickcircle5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "clickcircle5" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *circle_click_5* updates
    if circle_click_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        circle_click_5.frameNStart = frameN  # exact frame index
        circle_click_5.tStart = t  # local t and not account for scr refresh
        circle_click_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(circle_click_5, 'tStartRefresh')  # time at next scr refresh
        circle_click_5.setAutoDraw(True)
    
    # *circle_click_text1_5* updates
    if circle_click_text1_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        circle_click_text1_5.frameNStart = frameN  # exact frame index
        circle_click_text1_5.tStart = t  # local t and not account for scr refresh
        circle_click_text1_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(circle_click_text1_5, 'tStartRefresh')  # time at next scr refresh
        circle_click_text1_5.setAutoDraw(True)
    # *circle_mouse5* updates
    if circle_mouse5.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        circle_mouse5.frameNStart = frameN  # exact frame index
        circle_mouse5.tStart = t  # local t and not account for scr refresh
        circle_mouse5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(circle_mouse5, 'tStartRefresh')  # time at next scr refresh
        circle_mouse5.status = STARTED
        prevButtonState = circle_mouse5.getPressed()  # if button is down already this ISN'T a new click
    if circle_mouse5.status == STARTED:  # only update if started and not finished!
        buttons = circle_mouse5.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(circle_click_5)
                    clickableList = circle_click_5
                except:
                    clickableList = [circle_click_5]
                for obj in clickableList:
                    if obj.contains(circle_mouse5):
                        gotValidClick = True
                        circle_mouse5.clicked_name.append(obj.name)
                if gotValidClick:
                    x, y = circle_mouse5.getPos()
                    circle_mouse5.x.append(x)
                    circle_mouse5.y.append(y)
                    buttons = circle_mouse5.getPressed()
                    circle_mouse5.leftButton.append(buttons[0])
                    circle_mouse5.midButton.append(buttons[1])
                    circle_mouse5.rightButton.append(buttons[2])
                    circle_mouse5.time.append(circle_mouse5.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in clickcircle5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "clickcircle5" ---
for thisComponent in clickcircle5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('circle_mouse5.x', circle_mouse5.x)
thisExp.addData('circle_mouse5.y', circle_mouse5.y)
thisExp.addData('circle_mouse5.leftButton', circle_mouse5.leftButton)
thisExp.addData('circle_mouse5.midButton', circle_mouse5.midButton)
thisExp.addData('circle_mouse5.rightButton', circle_mouse5.rightButton)
thisExp.addData('circle_mouse5.time', circle_mouse5.time)
thisExp.addData('circle_mouse5.clicked_name', circle_mouse5.clicked_name)
thisExp.nextEntry()
# the Routine "clickcircle5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "clickcircle6" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
circle_click_text1_6.reset()
# setup some python lists for storing info about the circle_mouse6
circle_mouse6.x = []
circle_mouse6.y = []
circle_mouse6.leftButton = []
circle_mouse6.midButton = []
circle_mouse6.rightButton = []
circle_mouse6.time = []
circle_mouse6.clicked_name = []
gotValidClick = False  # until a click is received
circle_mouse6.mouseClock.reset()
# keep track of which components have finished
clickcircle6Components = [circle_click_6, circle_click_text1_6, circle_mouse6]
for thisComponent in clickcircle6Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "clickcircle6" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *circle_click_6* updates
    if circle_click_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        circle_click_6.frameNStart = frameN  # exact frame index
        circle_click_6.tStart = t  # local t and not account for scr refresh
        circle_click_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(circle_click_6, 'tStartRefresh')  # time at next scr refresh
        circle_click_6.setAutoDraw(True)
    
    # *circle_click_text1_6* updates
    if circle_click_text1_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        circle_click_text1_6.frameNStart = frameN  # exact frame index
        circle_click_text1_6.tStart = t  # local t and not account for scr refresh
        circle_click_text1_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(circle_click_text1_6, 'tStartRefresh')  # time at next scr refresh
        circle_click_text1_6.setAutoDraw(True)
    # *circle_mouse6* updates
    if circle_mouse6.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        circle_mouse6.frameNStart = frameN  # exact frame index
        circle_mouse6.tStart = t  # local t and not account for scr refresh
        circle_mouse6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(circle_mouse6, 'tStartRefresh')  # time at next scr refresh
        circle_mouse6.status = STARTED
        prevButtonState = circle_mouse6.getPressed()  # if button is down already this ISN'T a new click
    if circle_mouse6.status == STARTED:  # only update if started and not finished!
        buttons = circle_mouse6.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(circle_click_6)
                    clickableList = circle_click_6
                except:
                    clickableList = [circle_click_6]
                for obj in clickableList:
                    if obj.contains(circle_mouse6):
                        gotValidClick = True
                        circle_mouse6.clicked_name.append(obj.name)
                if gotValidClick:
                    x, y = circle_mouse6.getPos()
                    circle_mouse6.x.append(x)
                    circle_mouse6.y.append(y)
                    buttons = circle_mouse6.getPressed()
                    circle_mouse6.leftButton.append(buttons[0])
                    circle_mouse6.midButton.append(buttons[1])
                    circle_mouse6.rightButton.append(buttons[2])
                    circle_mouse6.time.append(circle_mouse6.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in clickcircle6Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "clickcircle6" ---
for thisComponent in clickcircle6Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('circle_mouse6.x', circle_mouse6.x)
thisExp.addData('circle_mouse6.y', circle_mouse6.y)
thisExp.addData('circle_mouse6.leftButton', circle_mouse6.leftButton)
thisExp.addData('circle_mouse6.midButton', circle_mouse6.midButton)
thisExp.addData('circle_mouse6.rightButton', circle_mouse6.rightButton)
thisExp.addData('circle_mouse6.time', circle_mouse6.time)
thisExp.addData('circle_mouse6.clicked_name', circle_mouse6.clicked_name)
thisExp.nextEntry()
# the Routine "clickcircle6" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "clickcircle7" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
circle_click_text1_7.reset()
# setup some python lists for storing info about the circle_mouse7
circle_mouse7.x = []
circle_mouse7.y = []
circle_mouse7.leftButton = []
circle_mouse7.midButton = []
circle_mouse7.rightButton = []
circle_mouse7.time = []
circle_mouse7.clicked_name = []
gotValidClick = False  # until a click is received
circle_mouse7.mouseClock.reset()
# keep track of which components have finished
clickcircle7Components = [circle_click_7, circle_click_text1_7, circle_mouse7]
for thisComponent in clickcircle7Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "clickcircle7" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *circle_click_7* updates
    if circle_click_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        circle_click_7.frameNStart = frameN  # exact frame index
        circle_click_7.tStart = t  # local t and not account for scr refresh
        circle_click_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(circle_click_7, 'tStartRefresh')  # time at next scr refresh
        circle_click_7.setAutoDraw(True)
    
    # *circle_click_text1_7* updates
    if circle_click_text1_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        circle_click_text1_7.frameNStart = frameN  # exact frame index
        circle_click_text1_7.tStart = t  # local t and not account for scr refresh
        circle_click_text1_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(circle_click_text1_7, 'tStartRefresh')  # time at next scr refresh
        circle_click_text1_7.setAutoDraw(True)
    # *circle_mouse7* updates
    if circle_mouse7.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        circle_mouse7.frameNStart = frameN  # exact frame index
        circle_mouse7.tStart = t  # local t and not account for scr refresh
        circle_mouse7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(circle_mouse7, 'tStartRefresh')  # time at next scr refresh
        circle_mouse7.status = STARTED
        prevButtonState = circle_mouse7.getPressed()  # if button is down already this ISN'T a new click
    if circle_mouse7.status == STARTED:  # only update if started and not finished!
        buttons = circle_mouse7.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(circle_click_7)
                    clickableList = circle_click_7
                except:
                    clickableList = [circle_click_7]
                for obj in clickableList:
                    if obj.contains(circle_mouse7):
                        gotValidClick = True
                        circle_mouse7.clicked_name.append(obj.name)
                if gotValidClick:
                    x, y = circle_mouse7.getPos()
                    circle_mouse7.x.append(x)
                    circle_mouse7.y.append(y)
                    buttons = circle_mouse7.getPressed()
                    circle_mouse7.leftButton.append(buttons[0])
                    circle_mouse7.midButton.append(buttons[1])
                    circle_mouse7.rightButton.append(buttons[2])
                    circle_mouse7.time.append(circle_mouse7.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in clickcircle7Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "clickcircle7" ---
for thisComponent in clickcircle7Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('circle_mouse7.x', circle_mouse7.x)
thisExp.addData('circle_mouse7.y', circle_mouse7.y)
thisExp.addData('circle_mouse7.leftButton', circle_mouse7.leftButton)
thisExp.addData('circle_mouse7.midButton', circle_mouse7.midButton)
thisExp.addData('circle_mouse7.rightButton', circle_mouse7.rightButton)
thisExp.addData('circle_mouse7.time', circle_mouse7.time)
thisExp.addData('circle_mouse7.clicked_name', circle_mouse7.clicked_name)
thisExp.nextEntry()
# the Routine "clickcircle7" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "clickcircle8" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
circle_click_text1_8.reset()
# setup some python lists for storing info about the circle_mouse8
circle_mouse8.x = []
circle_mouse8.y = []
circle_mouse8.leftButton = []
circle_mouse8.midButton = []
circle_mouse8.rightButton = []
circle_mouse8.time = []
circle_mouse8.clicked_name = []
gotValidClick = False  # until a click is received
circle_mouse8.mouseClock.reset()
# keep track of which components have finished
clickcircle8Components = [circle_click_8, circle_click_text1_8, circle_mouse8]
for thisComponent in clickcircle8Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "clickcircle8" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *circle_click_8* updates
    if circle_click_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        circle_click_8.frameNStart = frameN  # exact frame index
        circle_click_8.tStart = t  # local t and not account for scr refresh
        circle_click_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(circle_click_8, 'tStartRefresh')  # time at next scr refresh
        circle_click_8.setAutoDraw(True)
    
    # *circle_click_text1_8* updates
    if circle_click_text1_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        circle_click_text1_8.frameNStart = frameN  # exact frame index
        circle_click_text1_8.tStart = t  # local t and not account for scr refresh
        circle_click_text1_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(circle_click_text1_8, 'tStartRefresh')  # time at next scr refresh
        circle_click_text1_8.setAutoDraw(True)
    # *circle_mouse8* updates
    if circle_mouse8.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        circle_mouse8.frameNStart = frameN  # exact frame index
        circle_mouse8.tStart = t  # local t and not account for scr refresh
        circle_mouse8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(circle_mouse8, 'tStartRefresh')  # time at next scr refresh
        circle_mouse8.status = STARTED
        prevButtonState = circle_mouse8.getPressed()  # if button is down already this ISN'T a new click
    if circle_mouse8.status == STARTED:  # only update if started and not finished!
        buttons = circle_mouse8.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(circle_click_8)
                    clickableList = circle_click_8
                except:
                    clickableList = [circle_click_8]
                for obj in clickableList:
                    if obj.contains(circle_mouse8):
                        gotValidClick = True
                        circle_mouse8.clicked_name.append(obj.name)
                if gotValidClick:
                    x, y = circle_mouse8.getPos()
                    circle_mouse8.x.append(x)
                    circle_mouse8.y.append(y)
                    buttons = circle_mouse8.getPressed()
                    circle_mouse8.leftButton.append(buttons[0])
                    circle_mouse8.midButton.append(buttons[1])
                    circle_mouse8.rightButton.append(buttons[2])
                    circle_mouse8.time.append(circle_mouse8.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in clickcircle8Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "clickcircle8" ---
for thisComponent in clickcircle8Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('circle_mouse8.x', circle_mouse8.x)
thisExp.addData('circle_mouse8.y', circle_mouse8.y)
thisExp.addData('circle_mouse8.leftButton', circle_mouse8.leftButton)
thisExp.addData('circle_mouse8.midButton', circle_mouse8.midButton)
thisExp.addData('circle_mouse8.rightButton', circle_mouse8.rightButton)
thisExp.addData('circle_mouse8.time', circle_mouse8.time)
thisExp.addData('circle_mouse8.clicked_name', circle_mouse8.clicked_name)
thisExp.nextEntry()
# the Routine "clickcircle8" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "clickcircle9" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
circle_click_text1_9.reset()
# setup some python lists for storing info about the circle_mouse9
circle_mouse9.x = []
circle_mouse9.y = []
circle_mouse9.leftButton = []
circle_mouse9.midButton = []
circle_mouse9.rightButton = []
circle_mouse9.time = []
circle_mouse9.clicked_name = []
gotValidClick = False  # until a click is received
circle_mouse9.mouseClock.reset()
# keep track of which components have finished
clickcircle9Components = [circle_click_9, circle_click_text1_9, circle_mouse9]
for thisComponent in clickcircle9Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "clickcircle9" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *circle_click_9* updates
    if circle_click_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        circle_click_9.frameNStart = frameN  # exact frame index
        circle_click_9.tStart = t  # local t and not account for scr refresh
        circle_click_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(circle_click_9, 'tStartRefresh')  # time at next scr refresh
        circle_click_9.setAutoDraw(True)
    
    # *circle_click_text1_9* updates
    if circle_click_text1_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        circle_click_text1_9.frameNStart = frameN  # exact frame index
        circle_click_text1_9.tStart = t  # local t and not account for scr refresh
        circle_click_text1_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(circle_click_text1_9, 'tStartRefresh')  # time at next scr refresh
        circle_click_text1_9.setAutoDraw(True)
    # *circle_mouse9* updates
    if circle_mouse9.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        circle_mouse9.frameNStart = frameN  # exact frame index
        circle_mouse9.tStart = t  # local t and not account for scr refresh
        circle_mouse9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(circle_mouse9, 'tStartRefresh')  # time at next scr refresh
        circle_mouse9.status = STARTED
        prevButtonState = circle_mouse9.getPressed()  # if button is down already this ISN'T a new click
    if circle_mouse9.status == STARTED:  # only update if started and not finished!
        buttons = circle_mouse9.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(circle_click_9)
                    clickableList = circle_click_9
                except:
                    clickableList = [circle_click_9]
                for obj in clickableList:
                    if obj.contains(circle_mouse9):
                        gotValidClick = True
                        circle_mouse9.clicked_name.append(obj.name)
                if gotValidClick:
                    x, y = circle_mouse9.getPos()
                    circle_mouse9.x.append(x)
                    circle_mouse9.y.append(y)
                    buttons = circle_mouse9.getPressed()
                    circle_mouse9.leftButton.append(buttons[0])
                    circle_mouse9.midButton.append(buttons[1])
                    circle_mouse9.rightButton.append(buttons[2])
                    circle_mouse9.time.append(circle_mouse9.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in clickcircle9Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "clickcircle9" ---
for thisComponent in clickcircle9Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('circle_mouse9.x', circle_mouse9.x)
thisExp.addData('circle_mouse9.y', circle_mouse9.y)
thisExp.addData('circle_mouse9.leftButton', circle_mouse9.leftButton)
thisExp.addData('circle_mouse9.midButton', circle_mouse9.midButton)
thisExp.addData('circle_mouse9.rightButton', circle_mouse9.rightButton)
thisExp.addData('circle_mouse9.time', circle_mouse9.time)
thisExp.addData('circle_mouse9.clicked_name', circle_mouse9.clicked_name)
thisExp.nextEntry()
# the Routine "clickcircle9" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "clickcircle10" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
circle_click_text1_10.reset()
# setup some python lists for storing info about the circle_mouse10
circle_mouse10.x = []
circle_mouse10.y = []
circle_mouse10.leftButton = []
circle_mouse10.midButton = []
circle_mouse10.rightButton = []
circle_mouse10.time = []
circle_mouse10.clicked_name = []
gotValidClick = False  # until a click is received
circle_mouse10.mouseClock.reset()
# keep track of which components have finished
clickcircle10Components = [circle_click_10, circle_click_text1_10, circle_mouse10]
for thisComponent in clickcircle10Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "clickcircle10" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *circle_click_10* updates
    if circle_click_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        circle_click_10.frameNStart = frameN  # exact frame index
        circle_click_10.tStart = t  # local t and not account for scr refresh
        circle_click_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(circle_click_10, 'tStartRefresh')  # time at next scr refresh
        circle_click_10.setAutoDraw(True)
    
    # *circle_click_text1_10* updates
    if circle_click_text1_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        circle_click_text1_10.frameNStart = frameN  # exact frame index
        circle_click_text1_10.tStart = t  # local t and not account for scr refresh
        circle_click_text1_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(circle_click_text1_10, 'tStartRefresh')  # time at next scr refresh
        circle_click_text1_10.setAutoDraw(True)
    # *circle_mouse10* updates
    if circle_mouse10.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        circle_mouse10.frameNStart = frameN  # exact frame index
        circle_mouse10.tStart = t  # local t and not account for scr refresh
        circle_mouse10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(circle_mouse10, 'tStartRefresh')  # time at next scr refresh
        circle_mouse10.status = STARTED
        prevButtonState = circle_mouse10.getPressed()  # if button is down already this ISN'T a new click
    if circle_mouse10.status == STARTED:  # only update if started and not finished!
        buttons = circle_mouse10.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(circle_click_10)
                    clickableList = circle_click_10
                except:
                    clickableList = [circle_click_10]
                for obj in clickableList:
                    if obj.contains(circle_mouse10):
                        gotValidClick = True
                        circle_mouse10.clicked_name.append(obj.name)
                if gotValidClick:
                    x, y = circle_mouse10.getPos()
                    circle_mouse10.x.append(x)
                    circle_mouse10.y.append(y)
                    buttons = circle_mouse10.getPressed()
                    circle_mouse10.leftButton.append(buttons[0])
                    circle_mouse10.midButton.append(buttons[1])
                    circle_mouse10.rightButton.append(buttons[2])
                    circle_mouse10.time.append(circle_mouse10.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in clickcircle10Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "clickcircle10" ---
for thisComponent in clickcircle10Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('circle_mouse10.x', circle_mouse10.x)
thisExp.addData('circle_mouse10.y', circle_mouse10.y)
thisExp.addData('circle_mouse10.leftButton', circle_mouse10.leftButton)
thisExp.addData('circle_mouse10.midButton', circle_mouse10.midButton)
thisExp.addData('circle_mouse10.rightButton', circle_mouse10.rightButton)
thisExp.addData('circle_mouse10.time', circle_mouse10.time)
thisExp.addData('circle_mouse10.clicked_name', circle_mouse10.clicked_name)
thisExp.nextEntry()
# the Routine "clickcircle10" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Stimuli/randomblock.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    A = data.TrialHandler(nReps=ML_repeat, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='A')
    thisExp.addLoop(A)  # add the loop to the experiment
    thisA = A.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisA.rgb)
    if thisA != None:
        for paramName in thisA:
            exec('{} = thisA[paramName]'.format(paramName))
    
    for thisA in A:
        currentLoop = A
        # abbreviate parameter names if possible (e.g. rgb = thisA.rgb)
        if thisA != None:
            for paramName in thisA:
                exec('{} = thisA[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "ML_INTRO" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        sound_2.setSound('Stimuli/Instructions/ML_long.ogg', hamming=True)
        sound_2.setVolume(1.0, log=False)
        # keep track of which components have finished
        ML_INTROComponents = [ml_intro_text, sound_2, START_ML]
        for thisComponent in ML_INTROComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "ML_INTRO" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *ml_intro_text* updates
            if ml_intro_text.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                ml_intro_text.frameNStart = frameN  # exact frame index
                ml_intro_text.tStart = t  # local t and not account for scr refresh
                ml_intro_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ml_intro_text, 'tStartRefresh')  # time at next scr refresh
                ml_intro_text.setAutoDraw(True)
            # start/stop sound_2
            if sound_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                sound_2.frameNStart = frameN  # exact frame index
                sound_2.tStart = t  # local t and not account for scr refresh
                sound_2.tStartRefresh = tThisFlipGlobal  # on global time
                sound_2.play(when=win)  # sync with win flip
            
            # *START_ML* updates
            if START_ML.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                START_ML.frameNStart = frameN  # exact frame index
                START_ML.tStart = t  # local t and not account for scr refresh
                START_ML.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(START_ML, 'tStartRefresh')  # time at next scr refresh
                START_ML.setAutoDraw(True)
            if START_ML.status == STARTED:
                # check whether START_ML has been pressed
                if START_ML.isClicked:
                    if not START_ML.wasClicked:
                        START_ML.timesOn.append(globalClock.getTime()) # store time of first click
                        START_ML.timesOff.append(globalClock.getTime()) # store time clicked until
                    else:
                        START_ML.timesOff[-1] = globalClock.getTime() # update time clicked until
                    if not START_ML.wasClicked:
                        continueRoutine = False  # end routine when START_ML is clicked
                        None
                    START_ML.wasClicked = True  # if START_ML is still clicked next frame, it is not a new click
                else:
                    START_ML.wasClicked = False  # if START_ML is clicked next frame, it is a new click
            else:
                START_ML.wasClicked = False  # if START_ML is clicked next frame, it is a new click
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ML_INTROComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ML_INTRO" ---
        for thisComponent in ML_INTROComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        sound_2.stop()  # ensure sound has stopped at end of routine
        A.addData('START_ML.numClicks', START_ML.numClicks)
        if START_ML.numClicks:
           A.addData('START_ML.timesOn', START_ML.timesOn)
           A.addData('START_ML.timesOff', START_ML.timesOff)
        else:
           A.addData('START_ML.timesOn', "")
           A.addData('START_ML.timesOff', "")
        # the Routine "ML_INTRO" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        ML_rep = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('Stimuli/Müller-Lyer trials/ML_condition_file.xlsx'),
            seed=None, name='ML_rep')
        thisExp.addLoop(ML_rep)  # add the loop to the experiment
        thisML_rep = ML_rep.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisML_rep.rgb)
        if thisML_rep != None:
            for paramName in thisML_rep:
                exec('{} = thisML_rep[paramName]'.format(paramName))
        
        for thisML_rep in ML_rep:
            currentLoop = ML_rep
            # abbreviate parameter names if possible (e.g. rgb = thisML_rep.rgb)
            if thisML_rep != None:
                for paramName in thisML_rep:
                    exec('{} = thisML_rep[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "TEST_ML" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            image_ML.setImage(path)
            # setup some python lists for storing info about the mouse_ML
            mouse_ML.x = []
            mouse_ML.y = []
            mouse_ML.leftButton = []
            mouse_ML.midButton = []
            mouse_ML.rightButton = []
            mouse_ML.time = []
            mouse_ML.clicked_name = []
            gotValidClick = False  # until a click is received
            sound_3.setSound('Stimuli/Instructions/ML_short.ogg', secs=10, hamming=True)
            sound_3.setVolume(1.0, log=False)
            # clear any previous roi data
            ROI_left_ML.reset()
            # clear any previous roi data
            ROI_right_ML.reset()
            key_resp.keys = []
            key_resp.rt = []
            _key_resp_allKeys = []
            # keep track of which components have finished
            TEST_MLComponents = [image_ML, LEFT_ML, RIGHT_ML, mouse_ML, sound_3, ML_tracker, ROI_left_ML, ROI_right_ML, key_resp]
            for thisComponent in TEST_MLComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "TEST_ML" ---
            while continueRoutine and routineTimer.getTime() < 15.1:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image_ML* updates
                if image_ML.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
                    # keep track of start time/frame for later
                    image_ML.frameNStart = frameN  # exact frame index
                    image_ML.tStart = t  # local t and not account for scr refresh
                    image_ML.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_ML, 'tStartRefresh')  # time at next scr refresh
                    image_ML.setAutoDraw(True)
                if image_ML.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_ML.tStartRefresh + 15-frameTolerance:
                        # keep track of stop time/frame for later
                        image_ML.tStop = t  # not accounting for scr refresh
                        image_ML.frameNStop = frameN  # exact frame index
                        image_ML.setAutoDraw(False)
                
                # *LEFT_ML* updates
                if LEFT_ML.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    LEFT_ML.frameNStart = frameN  # exact frame index
                    LEFT_ML.tStart = t  # local t and not account for scr refresh
                    LEFT_ML.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(LEFT_ML, 'tStartRefresh')  # time at next scr refresh
                    LEFT_ML.setAutoDraw(True)
                if LEFT_ML.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > LEFT_ML.tStartRefresh + 15-frameTolerance:
                        # keep track of stop time/frame for later
                        LEFT_ML.tStop = t  # not accounting for scr refresh
                        LEFT_ML.frameNStop = frameN  # exact frame index
                        LEFT_ML.setAutoDraw(False)
                
                # *RIGHT_ML* updates
                if RIGHT_ML.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    RIGHT_ML.frameNStart = frameN  # exact frame index
                    RIGHT_ML.tStart = t  # local t and not account for scr refresh
                    RIGHT_ML.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(RIGHT_ML, 'tStartRefresh')  # time at next scr refresh
                    RIGHT_ML.setAutoDraw(True)
                if RIGHT_ML.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > RIGHT_ML.tStartRefresh + 15-frameTolerance:
                        # keep track of stop time/frame for later
                        RIGHT_ML.tStop = t  # not accounting for scr refresh
                        RIGHT_ML.frameNStop = frameN  # exact frame index
                        RIGHT_ML.setAutoDraw(False)
                # *mouse_ML* updates
                if mouse_ML.status == NOT_STARTED and t >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    mouse_ML.frameNStart = frameN  # exact frame index
                    mouse_ML.tStart = t  # local t and not account for scr refresh
                    mouse_ML.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse_ML, 'tStartRefresh')  # time at next scr refresh
                    mouse_ML.status = STARTED
                    mouse_ML.mouseClock.reset()
                    prevButtonState = mouse_ML.getPressed()  # if button is down already this ISN'T a new click
                if mouse_ML.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > mouse_ML.tStartRefresh + 15-frameTolerance:
                        # keep track of stop time/frame for later
                        mouse_ML.tStop = t  # not accounting for scr refresh
                        mouse_ML.frameNStop = frameN  # exact frame index
                        mouse_ML.status = FINISHED
                if mouse_ML.status == STARTED:  # only update if started and not finished!
                    buttons = mouse_ML.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            try:
                                iter([LEFT_ML, RIGHT_ML])
                                clickableList = [LEFT_ML, RIGHT_ML]
                            except:
                                clickableList = [[LEFT_ML, RIGHT_ML]]
                            for obj in clickableList:
                                if obj.contains(mouse_ML):
                                    gotValidClick = True
                                    mouse_ML.clicked_name.append(obj.name)
                            x, y = mouse_ML.getPos()
                            mouse_ML.x.append(x)
                            mouse_ML.y.append(y)
                            buttons = mouse_ML.getPressed()
                            mouse_ML.leftButton.append(buttons[0])
                            mouse_ML.midButton.append(buttons[1])
                            mouse_ML.rightButton.append(buttons[2])
                            mouse_ML.time.append(mouse_ML.mouseClock.getTime())
                            
                            continueRoutine = False  # abort routine on response
                # start/stop sound_3
                if sound_3.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
                    # keep track of start time/frame for later
                    sound_3.frameNStart = frameN  # exact frame index
                    sound_3.tStart = t  # local t and not account for scr refresh
                    sound_3.tStartRefresh = tThisFlipGlobal  # on global time
                    sound_3.play(when=win)  # sync with win flip
                if sound_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > sound_3.tStartRefresh + 10-frameTolerance:
                        # keep track of stop time/frame for later
                        sound_3.tStop = t  # not accounting for scr refresh
                        sound_3.frameNStop = frameN  # exact frame index
                        sound_3.stop()
                # *ML_tracker* updates
                if ML_tracker.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    ML_tracker.frameNStart = frameN  # exact frame index
                    ML_tracker.tStart = t  # local t and not account for scr refresh
                    ML_tracker.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ML_tracker, 'tStartRefresh')  # time at next scr refresh
                    ML_tracker.status = STARTED
                if ML_tracker.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ML_tracker.tStartRefresh + 15-frameTolerance:
                        # keep track of stop time/frame for later
                        ML_tracker.tStop = t  # not accounting for scr refresh
                        ML_tracker.frameNStop = frameN  # exact frame index
                        ML_tracker.status = FINISHED
                if ROI_left_ML.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    ROI_left_ML.frameNStart = frameN  # exact frame index
                    ROI_left_ML.tStart = t  # local t and not account for scr refresh
                    ROI_left_ML.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ROI_left_ML, 'tStartRefresh')  # time at next scr refresh
                    ROI_left_ML.status = STARTED
                if ROI_left_ML.status == STARTED:
                    # check whether ROI_left_ML has been looked in
                    if ROI_left_ML.isLookedIn:
                        if not ROI_left_ML.wasLookedIn:
                            ROI_left_ML.timesOn.append(routineTimer.getTime()) # store time of first look
                            ROI_left_ML.timesOff.append(routineTimer.getTime()) # store time looked until
                        else:
                            ROI_left_ML.timesOff[-1] = routineTimer.getTime() # update time looked until
                        ROI_left_ML.wasLookedIn = True  # if ROI_left_ML is still looked at next frame, it is not a new look
                    else:
                        if ROI_left_ML.wasLookedIn:
                            ROI_left_ML.timesOff[-1] = routineTimer.getTime() # update time looked until
                        ROI_left_ML.wasLookedIn = False  # if ROI_left_ML is looked at next frame, it is a new look
                else:
                    ROI_left_ML.clock.reset() # keep clock at 0 if roi hasn't started / has finished
                    ROI_left_ML.wasLookedIn = False  # if ROI_left_ML is looked at next frame, it is a new look
                if ROI_left_ML.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ROI_left_ML.tStartRefresh + 15-frameTolerance:
                        # keep track of stop time/frame for later
                        ROI_left_ML.tStop = t  # not accounting for scr refresh
                        ROI_left_ML.frameNStop = frameN  # exact frame index
                        ROI_left_ML.status = FINISHED
                if ROI_right_ML.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    ROI_right_ML.frameNStart = frameN  # exact frame index
                    ROI_right_ML.tStart = t  # local t and not account for scr refresh
                    ROI_right_ML.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ROI_right_ML, 'tStartRefresh')  # time at next scr refresh
                    ROI_right_ML.status = STARTED
                if ROI_right_ML.status == STARTED:
                    # check whether ROI_right_ML has been looked in
                    if ROI_right_ML.isLookedIn:
                        if not ROI_right_ML.wasLookedIn:
                            ROI_right_ML.timesOn.append(ROI_right_ML.clock.getTime()) # store time of first look
                            ROI_right_ML.timesOff.append(ROI_right_ML.clock.getTime()) # store time looked until
                        else:
                            ROI_right_ML.timesOff[-1] = ROI_right_ML.clock.getTime() # update time looked until
                        ROI_right_ML.wasLookedIn = True  # if ROI_right_ML is still looked at next frame, it is not a new look
                    else:
                        if ROI_right_ML.wasLookedIn:
                            ROI_right_ML.timesOff[-1] = ROI_right_ML.clock.getTime() # update time looked until
                        ROI_right_ML.wasLookedIn = False  # if ROI_right_ML is looked at next frame, it is a new look
                else:
                    ROI_right_ML.clock.reset() # keep clock at 0 if roi hasn't started / has finished
                    ROI_right_ML.wasLookedIn = False  # if ROI_right_ML is looked at next frame, it is a new look
                if ROI_right_ML.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ROI_right_ML.tStartRefresh + 15-frameTolerance:
                        # keep track of stop time/frame for later
                        ROI_right_ML.tStop = t  # not accounting for scr refresh
                        ROI_right_ML.frameNStop = frameN  # exact frame index
                        ROI_right_ML.status = FINISHED
                
                # *key_resp* updates
                if key_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp.frameNStart = frameN  # exact frame index
                    key_resp.tStart = t  # local t and not account for scr refresh
                    key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                    key_resp.status = STARTED
                    # keyboard checking is just starting
                    key_resp.clock.reset()  # now t=0
                if key_resp.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > key_resp.tStartRefresh + 15-frameTolerance:
                        # keep track of stop time/frame for later
                        key_resp.tStop = t  # not accounting for scr refresh
                        key_resp.frameNStop = frameN  # exact frame index
                        key_resp.status = FINISHED
                if key_resp.status == STARTED:
                    theseKeys = key_resp.getKeys(keyList=['p'], waitRelease=False)
                    _key_resp_allKeys.extend(theseKeys)
                    if len(_key_resp_allKeys):
                        key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                        key_resp.rt = _key_resp_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in TEST_MLComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "TEST_ML" ---
            for thisComponent in TEST_MLComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store data for ML_rep (TrialHandler)
            ML_rep.addData('mouse_ML.x', mouse_ML.x)
            ML_rep.addData('mouse_ML.y', mouse_ML.y)
            ML_rep.addData('mouse_ML.leftButton', mouse_ML.leftButton)
            ML_rep.addData('mouse_ML.midButton', mouse_ML.midButton)
            ML_rep.addData('mouse_ML.rightButton', mouse_ML.rightButton)
            ML_rep.addData('mouse_ML.time', mouse_ML.time)
            ML_rep.addData('mouse_ML.clicked_name', mouse_ML.clicked_name)
            sound_3.stop()  # ensure sound has stopped at end of routine
            # make sure the eyetracker recording stops
            if ML_tracker.status != FINISHED:
                ML_tracker.status = FINISHED
            ML_rep.addData('ROI_left_ML.numLooks', ROI_left_ML.numLooks)
            if ROI_left_ML.numLooks:
               ML_rep.addData('ROI_left_ML.timesOn', ROI_left_ML.timesOn)
               ML_rep.addData('ROI_left_ML.timesOff', ROI_left_ML.timesOff)
            else:
               ML_rep.addData('ROI_left_ML.timesOn', "")
               ML_rep.addData('ROI_left_ML.timesOff', "")
            ML_rep.addData('ROI_right_ML.numLooks', ROI_right_ML.numLooks)
            if ROI_right_ML.numLooks:
               ML_rep.addData('ROI_right_ML.timesOn', ROI_right_ML.timesOn)
               ML_rep.addData('ROI_right_ML.timesOff', ROI_right_ML.timesOff)
            else:
               ML_rep.addData('ROI_right_ML.timesOn', "")
               ML_rep.addData('ROI_right_ML.timesOff', "")
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-15.100000)
            
            # --- Prepare to start Routine "pressspace" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            Next_text.reset()
            # setup some python lists for storing info about the Next_mouse
            Next_mouse.clicked_name = []
            gotValidClick = False  # until a click is received
            key_resp_2.keys = []
            key_resp_2.rt = []
            _key_resp_2_allKeys = []
            # keep track of which components have finished
            pressspaceComponents = [Next_text, Next_polygon, Next_mouse, key_resp_2]
            for thisComponent in pressspaceComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "pressspace" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Next_text* updates
                if Next_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Next_text.frameNStart = frameN  # exact frame index
                    Next_text.tStart = t  # local t and not account for scr refresh
                    Next_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Next_text, 'tStartRefresh')  # time at next scr refresh
                    Next_text.setAutoDraw(True)
                
                # *Next_polygon* updates
                if Next_polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Next_polygon.frameNStart = frameN  # exact frame index
                    Next_polygon.tStart = t  # local t and not account for scr refresh
                    Next_polygon.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Next_polygon, 'tStartRefresh')  # time at next scr refresh
                    Next_polygon.setAutoDraw(True)
                # *Next_mouse* updates
                if Next_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Next_mouse.frameNStart = frameN  # exact frame index
                    Next_mouse.tStart = t  # local t and not account for scr refresh
                    Next_mouse.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Next_mouse, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.addData('Next_mouse.started', t)
                    Next_mouse.status = STARTED
                    prevButtonState = Next_mouse.getPressed()  # if button is down already this ISN'T a new click
                if Next_mouse.status == STARTED:  # only update if started and not finished!
                    buttons = Next_mouse.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            try:
                                iter(Next_polygon)
                                clickableList = Next_polygon
                            except:
                                clickableList = [Next_polygon]
                            for obj in clickableList:
                                if obj.contains(Next_mouse):
                                    gotValidClick = True
                                    Next_mouse.clicked_name.append(obj.name)
                            if gotValidClick:  
                                continueRoutine = False  # abort routine on response
                
                # *key_resp_2* updates
                if key_resp_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_2.frameNStart = frameN  # exact frame index
                    key_resp_2.tStart = t  # local t and not account for scr refresh
                    key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                    key_resp_2.status = STARTED
                    # keyboard checking is just starting
                    key_resp_2.clock.reset()  # now t=0
                if key_resp_2.status == STARTED:
                    theseKeys = key_resp_2.getKeys(keyList=['p'], waitRelease=False)
                    _key_resp_2_allKeys.extend(theseKeys)
                    if len(_key_resp_2_allKeys):
                        key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                        key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in pressspaceComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "pressspace" ---
            for thisComponent in pressspaceComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store data for ML_rep (TrialHandler)
            x, y = Next_mouse.getPos()
            buttons = Next_mouse.getPressed()
            if sum(buttons):
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(Next_polygon)
                    clickableList = Next_polygon
                except:
                    clickableList = [Next_polygon]
                for obj in clickableList:
                    if obj.contains(Next_mouse):
                        gotValidClick = True
                        Next_mouse.clicked_name.append(obj.name)
            ML_rep.addData('Next_mouse.x', x)
            ML_rep.addData('Next_mouse.y', y)
            ML_rep.addData('Next_mouse.leftButton', buttons[0])
            ML_rep.addData('Next_mouse.midButton', buttons[1])
            ML_rep.addData('Next_mouse.rightButton', buttons[2])
            if len(Next_mouse.clicked_name):
                ML_rep.addData('Next_mouse.clicked_name', Next_mouse.clicked_name[0])
            # the Routine "pressspace" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'ML_rep'
        
        # get names of stimulus parameters
        if ML_rep.trialList in ([], [None], None):
            params = []
        else:
            params = ML_rep.trialList[0].keys()
        # save data for this loop
        ML_rep.saveAsExcel(filename + '.xlsx', sheetName='ML_rep',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        thisExp.nextEntry()
        
    # completed ML_repeat repeats of 'A'
    
    # get names of stimulus parameters
    if A.trialList in ([], [None], None):
        params = []
    else:
        params = A.trialList[0].keys()
    # save data for this loop
    A.saveAsExcel(filename + '.xlsx', sheetName='A',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # set up handler to look after randomisation of conditions etc
    B = data.TrialHandler(nReps=contrast_repeat, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='B')
    thisExp.addLoop(B)  # add the loop to the experiment
    thisB = B.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisB.rgb)
    if thisB != None:
        for paramName in thisB:
            exec('{} = thisB[paramName]'.format(paramName))
    
    for thisB in B:
        currentLoop = B
        # abbreviate parameter names if possible (e.g. rgb = thisB.rgb)
        if thisB != None:
            for paramName in thisB:
                exec('{} = thisB[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "Contrast_illusion_INTRO" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        sound_4.setSound('Stimuli/Instructions/CT_long.ogg', hamming=True)
        sound_4.setVolume(1.0, log=False)
        # keep track of which components have finished
        Contrast_illusion_INTROComponents = [contrast_intro_text, sound_4, START_contrast]
        for thisComponent in Contrast_illusion_INTROComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Contrast_illusion_INTRO" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *contrast_intro_text* updates
            if contrast_intro_text.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                contrast_intro_text.frameNStart = frameN  # exact frame index
                contrast_intro_text.tStart = t  # local t and not account for scr refresh
                contrast_intro_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(contrast_intro_text, 'tStartRefresh')  # time at next scr refresh
                contrast_intro_text.setAutoDraw(True)
            # start/stop sound_4
            if sound_4.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                sound_4.frameNStart = frameN  # exact frame index
                sound_4.tStart = t  # local t and not account for scr refresh
                sound_4.tStartRefresh = tThisFlipGlobal  # on global time
                sound_4.play(when=win)  # sync with win flip
            
            # *START_contrast* updates
            if START_contrast.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                START_contrast.frameNStart = frameN  # exact frame index
                START_contrast.tStart = t  # local t and not account for scr refresh
                START_contrast.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(START_contrast, 'tStartRefresh')  # time at next scr refresh
                START_contrast.setAutoDraw(True)
            if START_contrast.status == STARTED:
                # check whether START_contrast has been pressed
                if START_contrast.isClicked:
                    if not START_contrast.wasClicked:
                        START_contrast.timesOn.append(globalClock.getTime()) # store time of first click
                        START_contrast.timesOff.append(globalClock.getTime()) # store time clicked until
                    else:
                        START_contrast.timesOff[-1] = globalClock.getTime() # update time clicked until
                    if not START_contrast.wasClicked:
                        continueRoutine = False  # end routine when START_contrast is clicked
                        None
                    START_contrast.wasClicked = True  # if START_contrast is still clicked next frame, it is not a new click
                else:
                    START_contrast.wasClicked = False  # if START_contrast is clicked next frame, it is a new click
            else:
                START_contrast.wasClicked = False  # if START_contrast is clicked next frame, it is a new click
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Contrast_illusion_INTROComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Contrast_illusion_INTRO" ---
        for thisComponent in Contrast_illusion_INTROComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        sound_4.stop()  # ensure sound has stopped at end of routine
        B.addData('START_contrast.numClicks', START_contrast.numClicks)
        if START_contrast.numClicks:
           B.addData('START_contrast.timesOn', START_contrast.timesOn)
           B.addData('START_contrast.timesOff', START_contrast.timesOff)
        else:
           B.addData('START_contrast.timesOn', "")
           B.addData('START_contrast.timesOff', "")
        # the Routine "Contrast_illusion_INTRO" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        contrast_rep = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('Stimuli/Contrast trials/Contrast_condition_file.xlsx'),
            seed=None, name='contrast_rep')
        thisExp.addLoop(contrast_rep)  # add the loop to the experiment
        thisContrast_rep = contrast_rep.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisContrast_rep.rgb)
        if thisContrast_rep != None:
            for paramName in thisContrast_rep:
                exec('{} = thisContrast_rep[paramName]'.format(paramName))
        
        for thisContrast_rep in contrast_rep:
            currentLoop = contrast_rep
            # abbreviate parameter names if possible (e.g. rgb = thisContrast_rep.rgb)
            if thisContrast_rep != None:
                for paramName in thisContrast_rep:
                    exec('{} = thisContrast_rep[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "TEST_contrast" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            image_cont.setImage(path)
            # setup some python lists for storing info about the mouse_cont
            mouse_cont.x = []
            mouse_cont.y = []
            mouse_cont.leftButton = []
            mouse_cont.midButton = []
            mouse_cont.rightButton = []
            mouse_cont.time = []
            mouse_cont.clicked_name = []
            gotValidClick = False  # until a click is received
            sound_8.setSound('Stimuli/Instructions/CT_short.ogg', secs=10, hamming=True)
            sound_8.setVolume(1.0, log=False)
            # clear any previous roi data
            ROI_LEFT_cont.reset()
            # clear any previous roi data
            ROI_RIGHT_cont.reset()
            key_resp_3.keys = []
            key_resp_3.rt = []
            _key_resp_3_allKeys = []
            # keep track of which components have finished
            TEST_contrastComponents = [image_cont, LEFT_cont, RIGHT_cont, mouse_cont, sound_8, contrast_tracker, ROI_LEFT_cont, ROI_RIGHT_cont, key_resp_3]
            for thisComponent in TEST_contrastComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "TEST_contrast" ---
            while continueRoutine and routineTimer.getTime() < 15.1:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image_cont* updates
                if image_cont.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
                    # keep track of start time/frame for later
                    image_cont.frameNStart = frameN  # exact frame index
                    image_cont.tStart = t  # local t and not account for scr refresh
                    image_cont.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_cont, 'tStartRefresh')  # time at next scr refresh
                    image_cont.setAutoDraw(True)
                if image_cont.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_cont.tStartRefresh + 15-frameTolerance:
                        # keep track of stop time/frame for later
                        image_cont.tStop = t  # not accounting for scr refresh
                        image_cont.frameNStop = frameN  # exact frame index
                        image_cont.setAutoDraw(False)
                
                # *LEFT_cont* updates
                if LEFT_cont.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    LEFT_cont.frameNStart = frameN  # exact frame index
                    LEFT_cont.tStart = t  # local t and not account for scr refresh
                    LEFT_cont.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(LEFT_cont, 'tStartRefresh')  # time at next scr refresh
                    LEFT_cont.setAutoDraw(True)
                if LEFT_cont.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > LEFT_cont.tStartRefresh + 15-frameTolerance:
                        # keep track of stop time/frame for later
                        LEFT_cont.tStop = t  # not accounting for scr refresh
                        LEFT_cont.frameNStop = frameN  # exact frame index
                        LEFT_cont.setAutoDraw(False)
                
                # *RIGHT_cont* updates
                if RIGHT_cont.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    RIGHT_cont.frameNStart = frameN  # exact frame index
                    RIGHT_cont.tStart = t  # local t and not account for scr refresh
                    RIGHT_cont.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(RIGHT_cont, 'tStartRefresh')  # time at next scr refresh
                    RIGHT_cont.setAutoDraw(True)
                if RIGHT_cont.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > RIGHT_cont.tStartRefresh + 15-frameTolerance:
                        # keep track of stop time/frame for later
                        RIGHT_cont.tStop = t  # not accounting for scr refresh
                        RIGHT_cont.frameNStop = frameN  # exact frame index
                        RIGHT_cont.setAutoDraw(False)
                # *mouse_cont* updates
                if mouse_cont.status == NOT_STARTED and t >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    mouse_cont.frameNStart = frameN  # exact frame index
                    mouse_cont.tStart = t  # local t and not account for scr refresh
                    mouse_cont.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse_cont, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.addData('mouse_cont.started', t)
                    mouse_cont.status = STARTED
                    mouse_cont.mouseClock.reset()
                    prevButtonState = mouse_cont.getPressed()  # if button is down already this ISN'T a new click
                if mouse_cont.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > mouse_cont.tStartRefresh + 15-frameTolerance:
                        # keep track of stop time/frame for later
                        mouse_cont.tStop = t  # not accounting for scr refresh
                        mouse_cont.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.addData('mouse_cont.stopped', t)
                        mouse_cont.status = FINISHED
                if mouse_cont.status == STARTED:  # only update if started and not finished!
                    buttons = mouse_cont.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            try:
                                iter([LEFT_cont, RIGHT_cont])
                                clickableList = [LEFT_cont, RIGHT_cont]
                            except:
                                clickableList = [[LEFT_cont, RIGHT_cont]]
                            for obj in clickableList:
                                if obj.contains(mouse_cont):
                                    gotValidClick = True
                                    mouse_cont.clicked_name.append(obj.name)
                            x, y = mouse_cont.getPos()
                            mouse_cont.x.append(x)
                            mouse_cont.y.append(y)
                            buttons = mouse_cont.getPressed()
                            mouse_cont.leftButton.append(buttons[0])
                            mouse_cont.midButton.append(buttons[1])
                            mouse_cont.rightButton.append(buttons[2])
                            mouse_cont.time.append(mouse_cont.mouseClock.getTime())
                            
                            continueRoutine = False  # abort routine on response
                # start/stop sound_8
                if sound_8.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
                    # keep track of start time/frame for later
                    sound_8.frameNStart = frameN  # exact frame index
                    sound_8.tStart = t  # local t and not account for scr refresh
                    sound_8.tStartRefresh = tThisFlipGlobal  # on global time
                    sound_8.play(when=win)  # sync with win flip
                if sound_8.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > sound_8.tStartRefresh + 10-frameTolerance:
                        # keep track of stop time/frame for later
                        sound_8.tStop = t  # not accounting for scr refresh
                        sound_8.frameNStop = frameN  # exact frame index
                        sound_8.stop()
                # *contrast_tracker* updates
                if contrast_tracker.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    contrast_tracker.frameNStart = frameN  # exact frame index
                    contrast_tracker.tStart = t  # local t and not account for scr refresh
                    contrast_tracker.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(contrast_tracker, 'tStartRefresh')  # time at next scr refresh
                    contrast_tracker.status = STARTED
                if contrast_tracker.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > contrast_tracker.tStartRefresh + 15-frameTolerance:
                        # keep track of stop time/frame for later
                        contrast_tracker.tStop = t  # not accounting for scr refresh
                        contrast_tracker.frameNStop = frameN  # exact frame index
                        contrast_tracker.status = FINISHED
                if ROI_LEFT_cont.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    ROI_LEFT_cont.frameNStart = frameN  # exact frame index
                    ROI_LEFT_cont.tStart = t  # local t and not account for scr refresh
                    ROI_LEFT_cont.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ROI_LEFT_cont, 'tStartRefresh')  # time at next scr refresh
                    ROI_LEFT_cont.status = STARTED
                if ROI_LEFT_cont.status == STARTED:
                    # check whether ROI_LEFT_cont has been looked in
                    if ROI_LEFT_cont.isLookedIn:
                        if not ROI_LEFT_cont.wasLookedIn:
                            ROI_LEFT_cont.timesOn.append(ROI_LEFT_cont.clock.getTime()) # store time of first look
                            ROI_LEFT_cont.timesOff.append(ROI_LEFT_cont.clock.getTime()) # store time looked until
                        else:
                            ROI_LEFT_cont.timesOff[-1] = ROI_LEFT_cont.clock.getTime() # update time looked until
                        ROI_LEFT_cont.wasLookedIn = True  # if ROI_LEFT_cont is still looked at next frame, it is not a new look
                    else:
                        if ROI_LEFT_cont.wasLookedIn:
                            ROI_LEFT_cont.timesOff[-1] = ROI_LEFT_cont.clock.getTime() # update time looked until
                        ROI_LEFT_cont.wasLookedIn = False  # if ROI_LEFT_cont is looked at next frame, it is a new look
                else:
                    ROI_LEFT_cont.clock.reset() # keep clock at 0 if roi hasn't started / has finished
                    ROI_LEFT_cont.wasLookedIn = False  # if ROI_LEFT_cont is looked at next frame, it is a new look
                if ROI_LEFT_cont.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ROI_LEFT_cont.tStartRefresh + 15-frameTolerance:
                        # keep track of stop time/frame for later
                        ROI_LEFT_cont.tStop = t  # not accounting for scr refresh
                        ROI_LEFT_cont.frameNStop = frameN  # exact frame index
                        ROI_LEFT_cont.status = FINISHED
                if ROI_RIGHT_cont.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    ROI_RIGHT_cont.frameNStart = frameN  # exact frame index
                    ROI_RIGHT_cont.tStart = t  # local t and not account for scr refresh
                    ROI_RIGHT_cont.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ROI_RIGHT_cont, 'tStartRefresh')  # time at next scr refresh
                    ROI_RIGHT_cont.status = STARTED
                if ROI_RIGHT_cont.status == STARTED:
                    # check whether ROI_RIGHT_cont has been looked in
                    if ROI_RIGHT_cont.isLookedIn:
                        if not ROI_RIGHT_cont.wasLookedIn:
                            ROI_RIGHT_cont.timesOn.append(ROI_RIGHT_cont.clock.getTime()) # store time of first look
                            ROI_RIGHT_cont.timesOff.append(ROI_RIGHT_cont.clock.getTime()) # store time looked until
                        else:
                            ROI_RIGHT_cont.timesOff[-1] = ROI_RIGHT_cont.clock.getTime() # update time looked until
                        ROI_RIGHT_cont.wasLookedIn = True  # if ROI_RIGHT_cont is still looked at next frame, it is not a new look
                    else:
                        if ROI_RIGHT_cont.wasLookedIn:
                            ROI_RIGHT_cont.timesOff[-1] = ROI_RIGHT_cont.clock.getTime() # update time looked until
                        ROI_RIGHT_cont.wasLookedIn = False  # if ROI_RIGHT_cont is looked at next frame, it is a new look
                else:
                    ROI_RIGHT_cont.clock.reset() # keep clock at 0 if roi hasn't started / has finished
                    ROI_RIGHT_cont.wasLookedIn = False  # if ROI_RIGHT_cont is looked at next frame, it is a new look
                if ROI_RIGHT_cont.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ROI_RIGHT_cont.tStartRefresh + 15-frameTolerance:
                        # keep track of stop time/frame for later
                        ROI_RIGHT_cont.tStop = t  # not accounting for scr refresh
                        ROI_RIGHT_cont.frameNStop = frameN  # exact frame index
                        ROI_RIGHT_cont.status = FINISHED
                
                # *key_resp_3* updates
                if key_resp_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_3.frameNStart = frameN  # exact frame index
                    key_resp_3.tStart = t  # local t and not account for scr refresh
                    key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
                    key_resp_3.status = STARTED
                    # keyboard checking is just starting
                    key_resp_3.clock.reset()  # now t=0
                if key_resp_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > key_resp_3.tStartRefresh + 15-frameTolerance:
                        # keep track of stop time/frame for later
                        key_resp_3.tStop = t  # not accounting for scr refresh
                        key_resp_3.frameNStop = frameN  # exact frame index
                        key_resp_3.status = FINISHED
                if key_resp_3.status == STARTED:
                    theseKeys = key_resp_3.getKeys(keyList=['p'], waitRelease=False)
                    _key_resp_3_allKeys.extend(theseKeys)
                    if len(_key_resp_3_allKeys):
                        key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                        key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in TEST_contrastComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "TEST_contrast" ---
            for thisComponent in TEST_contrastComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store data for contrast_rep (TrialHandler)
            contrast_rep.addData('mouse_cont.x', mouse_cont.x)
            contrast_rep.addData('mouse_cont.y', mouse_cont.y)
            contrast_rep.addData('mouse_cont.leftButton', mouse_cont.leftButton)
            contrast_rep.addData('mouse_cont.midButton', mouse_cont.midButton)
            contrast_rep.addData('mouse_cont.rightButton', mouse_cont.rightButton)
            contrast_rep.addData('mouse_cont.time', mouse_cont.time)
            contrast_rep.addData('mouse_cont.clicked_name', mouse_cont.clicked_name)
            sound_8.stop()  # ensure sound has stopped at end of routine
            # make sure the eyetracker recording stops
            if contrast_tracker.status != FINISHED:
                contrast_tracker.status = FINISHED
            contrast_rep.addData('ROI_LEFT_cont.numLooks', ROI_LEFT_cont.numLooks)
            if ROI_LEFT_cont.numLooks:
               contrast_rep.addData('ROI_LEFT_cont.timesOn', ROI_LEFT_cont.timesOn)
               contrast_rep.addData('ROI_LEFT_cont.timesOff', ROI_LEFT_cont.timesOff)
            else:
               contrast_rep.addData('ROI_LEFT_cont.timesOn', "")
               contrast_rep.addData('ROI_LEFT_cont.timesOff', "")
            contrast_rep.addData('ROI_RIGHT_cont.numLooks', ROI_RIGHT_cont.numLooks)
            if ROI_RIGHT_cont.numLooks:
               contrast_rep.addData('ROI_RIGHT_cont.timesOn', ROI_RIGHT_cont.timesOn)
               contrast_rep.addData('ROI_RIGHT_cont.timesOff', ROI_RIGHT_cont.timesOff)
            else:
               contrast_rep.addData('ROI_RIGHT_cont.timesOn', "")
               contrast_rep.addData('ROI_RIGHT_cont.timesOff', "")
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-15.100000)
            
            # --- Prepare to start Routine "pressspace" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            Next_text.reset()
            # setup some python lists for storing info about the Next_mouse
            Next_mouse.clicked_name = []
            gotValidClick = False  # until a click is received
            key_resp_2.keys = []
            key_resp_2.rt = []
            _key_resp_2_allKeys = []
            # keep track of which components have finished
            pressspaceComponents = [Next_text, Next_polygon, Next_mouse, key_resp_2]
            for thisComponent in pressspaceComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "pressspace" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Next_text* updates
                if Next_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Next_text.frameNStart = frameN  # exact frame index
                    Next_text.tStart = t  # local t and not account for scr refresh
                    Next_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Next_text, 'tStartRefresh')  # time at next scr refresh
                    Next_text.setAutoDraw(True)
                
                # *Next_polygon* updates
                if Next_polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Next_polygon.frameNStart = frameN  # exact frame index
                    Next_polygon.tStart = t  # local t and not account for scr refresh
                    Next_polygon.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Next_polygon, 'tStartRefresh')  # time at next scr refresh
                    Next_polygon.setAutoDraw(True)
                # *Next_mouse* updates
                if Next_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Next_mouse.frameNStart = frameN  # exact frame index
                    Next_mouse.tStart = t  # local t and not account for scr refresh
                    Next_mouse.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Next_mouse, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.addData('Next_mouse.started', t)
                    Next_mouse.status = STARTED
                    prevButtonState = Next_mouse.getPressed()  # if button is down already this ISN'T a new click
                if Next_mouse.status == STARTED:  # only update if started and not finished!
                    buttons = Next_mouse.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            try:
                                iter(Next_polygon)
                                clickableList = Next_polygon
                            except:
                                clickableList = [Next_polygon]
                            for obj in clickableList:
                                if obj.contains(Next_mouse):
                                    gotValidClick = True
                                    Next_mouse.clicked_name.append(obj.name)
                            if gotValidClick:  
                                continueRoutine = False  # abort routine on response
                
                # *key_resp_2* updates
                if key_resp_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_2.frameNStart = frameN  # exact frame index
                    key_resp_2.tStart = t  # local t and not account for scr refresh
                    key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                    key_resp_2.status = STARTED
                    # keyboard checking is just starting
                    key_resp_2.clock.reset()  # now t=0
                if key_resp_2.status == STARTED:
                    theseKeys = key_resp_2.getKeys(keyList=['p'], waitRelease=False)
                    _key_resp_2_allKeys.extend(theseKeys)
                    if len(_key_resp_2_allKeys):
                        key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                        key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in pressspaceComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "pressspace" ---
            for thisComponent in pressspaceComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store data for contrast_rep (TrialHandler)
            x, y = Next_mouse.getPos()
            buttons = Next_mouse.getPressed()
            if sum(buttons):
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(Next_polygon)
                    clickableList = Next_polygon
                except:
                    clickableList = [Next_polygon]
                for obj in clickableList:
                    if obj.contains(Next_mouse):
                        gotValidClick = True
                        Next_mouse.clicked_name.append(obj.name)
            contrast_rep.addData('Next_mouse.x', x)
            contrast_rep.addData('Next_mouse.y', y)
            contrast_rep.addData('Next_mouse.leftButton', buttons[0])
            contrast_rep.addData('Next_mouse.midButton', buttons[1])
            contrast_rep.addData('Next_mouse.rightButton', buttons[2])
            if len(Next_mouse.clicked_name):
                contrast_rep.addData('Next_mouse.clicked_name', Next_mouse.clicked_name[0])
            # the Routine "pressspace" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'contrast_rep'
        
        # get names of stimulus parameters
        if contrast_rep.trialList in ([], [None], None):
            params = []
        else:
            params = contrast_rep.trialList[0].keys()
        # save data for this loop
        contrast_rep.saveAsExcel(filename + '.xlsx', sheetName='contrast_rep',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        thisExp.nextEntry()
        
    # completed contrast_repeat repeats of 'B'
    
    # get names of stimulus parameters
    if B.trialList in ([], [None], None):
        params = []
    else:
        params = B.trialList[0].keys()
    # save data for this loop
    B.saveAsExcel(filename + '.xlsx', sheetName='B',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # set up handler to look after randomisation of conditions etc
    C = data.TrialHandler(nReps=ebbing_repeat, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='C')
    thisExp.addLoop(C)  # add the loop to the experiment
    thisC = C.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisC.rgb)
    if thisC != None:
        for paramName in thisC:
            exec('{} = thisC[paramName]'.format(paramName))
    
    for thisC in C:
        currentLoop = C
        # abbreviate parameter names if possible (e.g. rgb = thisC.rgb)
        if thisC != None:
            for paramName in thisC:
                exec('{} = thisC[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "Ebbing_INTRO" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        sound_5.setSound('Stimuli/Instructions/EB_long.ogg', hamming=True)
        sound_5.setVolume(1.0, log=False)
        # keep track of which components have finished
        Ebbing_INTROComponents = [ebbing_intro_text, sound_5, START_ebbing]
        for thisComponent in Ebbing_INTROComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Ebbing_INTRO" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *ebbing_intro_text* updates
            if ebbing_intro_text.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                ebbing_intro_text.frameNStart = frameN  # exact frame index
                ebbing_intro_text.tStart = t  # local t and not account for scr refresh
                ebbing_intro_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ebbing_intro_text, 'tStartRefresh')  # time at next scr refresh
                ebbing_intro_text.setAutoDraw(True)
            # start/stop sound_5
            if sound_5.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                sound_5.frameNStart = frameN  # exact frame index
                sound_5.tStart = t  # local t and not account for scr refresh
                sound_5.tStartRefresh = tThisFlipGlobal  # on global time
                sound_5.play(when=win)  # sync with win flip
            
            # *START_ebbing* updates
            if START_ebbing.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                START_ebbing.frameNStart = frameN  # exact frame index
                START_ebbing.tStart = t  # local t and not account for scr refresh
                START_ebbing.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(START_ebbing, 'tStartRefresh')  # time at next scr refresh
                START_ebbing.setAutoDraw(True)
            if START_ebbing.status == STARTED:
                # check whether START_ebbing has been pressed
                if START_ebbing.isClicked:
                    if not START_ebbing.wasClicked:
                        START_ebbing.timesOn.append(globalClock.getTime()) # store time of first click
                        START_ebbing.timesOff.append(globalClock.getTime()) # store time clicked until
                    else:
                        START_ebbing.timesOff[-1] = globalClock.getTime() # update time clicked until
                    if not START_ebbing.wasClicked:
                        continueRoutine = False  # end routine when START_ebbing is clicked
                        None
                    START_ebbing.wasClicked = True  # if START_ebbing is still clicked next frame, it is not a new click
                else:
                    START_ebbing.wasClicked = False  # if START_ebbing is clicked next frame, it is a new click
            else:
                START_ebbing.wasClicked = False  # if START_ebbing is clicked next frame, it is a new click
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Ebbing_INTROComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Ebbing_INTRO" ---
        for thisComponent in Ebbing_INTROComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        sound_5.stop()  # ensure sound has stopped at end of routine
        C.addData('START_ebbing.numClicks', START_ebbing.numClicks)
        if START_ebbing.numClicks:
           C.addData('START_ebbing.timesOn', START_ebbing.timesOn)
           C.addData('START_ebbing.timesOff', START_ebbing.timesOff)
        else:
           C.addData('START_ebbing.timesOn', "")
           C.addData('START_ebbing.timesOff', "")
        # the Routine "Ebbing_INTRO" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        ebbing_rep = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('Stimuli/Ebbinghaus trials/Ebbinghaus_condition_file.xlsx'),
            seed=None, name='ebbing_rep')
        thisExp.addLoop(ebbing_rep)  # add the loop to the experiment
        thisEbbing_rep = ebbing_rep.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisEbbing_rep.rgb)
        if thisEbbing_rep != None:
            for paramName in thisEbbing_rep:
                exec('{} = thisEbbing_rep[paramName]'.format(paramName))
        
        for thisEbbing_rep in ebbing_rep:
            currentLoop = ebbing_rep
            # abbreviate parameter names if possible (e.g. rgb = thisEbbing_rep.rgb)
            if thisEbbing_rep != None:
                for paramName in thisEbbing_rep:
                    exec('{} = thisEbbing_rep[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "TEST_ebbing" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            image_ebbing.setImage(path)
            # setup some python lists for storing info about the mouse_ebbing
            mouse_ebbing.x = []
            mouse_ebbing.y = []
            mouse_ebbing.leftButton = []
            mouse_ebbing.midButton = []
            mouse_ebbing.rightButton = []
            mouse_ebbing.time = []
            mouse_ebbing.clicked_name = []
            gotValidClick = False  # until a click is received
            sound_9.setSound('Stimuli/Instructions/EB_short.ogg', secs=10, hamming=True)
            sound_9.setVolume(1.0, log=False)
            # clear any previous roi data
            ROI_LEFT_ebbing.reset()
            # clear any previous roi data
            ROI_RIGHT_ebbingroi.reset()
            key_resp_4.keys = []
            key_resp_4.rt = []
            _key_resp_4_allKeys = []
            # keep track of which components have finished
            TEST_ebbingComponents = [RIGHT_ebbing, LEFT_ebbing, image_ebbing, mouse_ebbing, sound_9, ebbing_tracker, ROI_LEFT_ebbing, ROI_RIGHT_ebbingroi, key_resp_4]
            for thisComponent in TEST_ebbingComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "TEST_ebbing" ---
            while continueRoutine and routineTimer.getTime() < 15.1:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *RIGHT_ebbing* updates
                if RIGHT_ebbing.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    RIGHT_ebbing.frameNStart = frameN  # exact frame index
                    RIGHT_ebbing.tStart = t  # local t and not account for scr refresh
                    RIGHT_ebbing.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(RIGHT_ebbing, 'tStartRefresh')  # time at next scr refresh
                    RIGHT_ebbing.setAutoDraw(True)
                if RIGHT_ebbing.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > RIGHT_ebbing.tStartRefresh + 15-frameTolerance:
                        # keep track of stop time/frame for later
                        RIGHT_ebbing.tStop = t  # not accounting for scr refresh
                        RIGHT_ebbing.frameNStop = frameN  # exact frame index
                        RIGHT_ebbing.setAutoDraw(False)
                
                # *LEFT_ebbing* updates
                if LEFT_ebbing.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    LEFT_ebbing.frameNStart = frameN  # exact frame index
                    LEFT_ebbing.tStart = t  # local t and not account for scr refresh
                    LEFT_ebbing.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(LEFT_ebbing, 'tStartRefresh')  # time at next scr refresh
                    LEFT_ebbing.setAutoDraw(True)
                if LEFT_ebbing.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > LEFT_ebbing.tStartRefresh + 15-frameTolerance:
                        # keep track of stop time/frame for later
                        LEFT_ebbing.tStop = t  # not accounting for scr refresh
                        LEFT_ebbing.frameNStop = frameN  # exact frame index
                        LEFT_ebbing.setAutoDraw(False)
                
                # *image_ebbing* updates
                if image_ebbing.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
                    # keep track of start time/frame for later
                    image_ebbing.frameNStart = frameN  # exact frame index
                    image_ebbing.tStart = t  # local t and not account for scr refresh
                    image_ebbing.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_ebbing, 'tStartRefresh')  # time at next scr refresh
                    image_ebbing.setAutoDraw(True)
                if image_ebbing.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_ebbing.tStartRefresh + 15-frameTolerance:
                        # keep track of stop time/frame for later
                        image_ebbing.tStop = t  # not accounting for scr refresh
                        image_ebbing.frameNStop = frameN  # exact frame index
                        image_ebbing.setAutoDraw(False)
                # *mouse_ebbing* updates
                if mouse_ebbing.status == NOT_STARTED and t >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    mouse_ebbing.frameNStart = frameN  # exact frame index
                    mouse_ebbing.tStart = t  # local t and not account for scr refresh
                    mouse_ebbing.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse_ebbing, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.addData('mouse_ebbing.started', t)
                    mouse_ebbing.status = STARTED
                    mouse_ebbing.mouseClock.reset()
                    prevButtonState = mouse_ebbing.getPressed()  # if button is down already this ISN'T a new click
                if mouse_ebbing.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > mouse_ebbing.tStartRefresh + 15-frameTolerance:
                        # keep track of stop time/frame for later
                        mouse_ebbing.tStop = t  # not accounting for scr refresh
                        mouse_ebbing.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.addData('mouse_ebbing.stopped', t)
                        mouse_ebbing.status = FINISHED
                if mouse_ebbing.status == STARTED:  # only update if started and not finished!
                    buttons = mouse_ebbing.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            try:
                                iter([LEFT_ebbing, RIGHT_ebbing])
                                clickableList = [LEFT_ebbing, RIGHT_ebbing]
                            except:
                                clickableList = [[LEFT_ebbing, RIGHT_ebbing]]
                            for obj in clickableList:
                                if obj.contains(mouse_ebbing):
                                    gotValidClick = True
                                    mouse_ebbing.clicked_name.append(obj.name)
                            x, y = mouse_ebbing.getPos()
                            mouse_ebbing.x.append(x)
                            mouse_ebbing.y.append(y)
                            buttons = mouse_ebbing.getPressed()
                            mouse_ebbing.leftButton.append(buttons[0])
                            mouse_ebbing.midButton.append(buttons[1])
                            mouse_ebbing.rightButton.append(buttons[2])
                            mouse_ebbing.time.append(mouse_ebbing.mouseClock.getTime())
                            
                            continueRoutine = False  # abort routine on response
                # start/stop sound_9
                if sound_9.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
                    # keep track of start time/frame for later
                    sound_9.frameNStart = frameN  # exact frame index
                    sound_9.tStart = t  # local t and not account for scr refresh
                    sound_9.tStartRefresh = tThisFlipGlobal  # on global time
                    sound_9.play(when=win)  # sync with win flip
                if sound_9.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > sound_9.tStartRefresh + 10-frameTolerance:
                        # keep track of stop time/frame for later
                        sound_9.tStop = t  # not accounting for scr refresh
                        sound_9.frameNStop = frameN  # exact frame index
                        sound_9.stop()
                # *ebbing_tracker* updates
                if ebbing_tracker.status == NOT_STARTED and t >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    ebbing_tracker.frameNStart = frameN  # exact frame index
                    ebbing_tracker.tStart = t  # local t and not account for scr refresh
                    ebbing_tracker.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ebbing_tracker, 'tStartRefresh')  # time at next scr refresh
                    ebbing_tracker.status = STARTED
                if ebbing_tracker.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ebbing_tracker.tStartRefresh + 15-frameTolerance:
                        # keep track of stop time/frame for later
                        ebbing_tracker.tStop = t  # not accounting for scr refresh
                        ebbing_tracker.frameNStop = frameN  # exact frame index
                        ebbing_tracker.status = FINISHED
                if ROI_LEFT_ebbing.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    ROI_LEFT_ebbing.frameNStart = frameN  # exact frame index
                    ROI_LEFT_ebbing.tStart = t  # local t and not account for scr refresh
                    ROI_LEFT_ebbing.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ROI_LEFT_ebbing, 'tStartRefresh')  # time at next scr refresh
                    ROI_LEFT_ebbing.status = STARTED
                if ROI_LEFT_ebbing.status == STARTED:
                    # check whether ROI_LEFT_ebbing has been looked in
                    if ROI_LEFT_ebbing.isLookedIn:
                        if not ROI_LEFT_ebbing.wasLookedIn:
                            ROI_LEFT_ebbing.timesOn.append(ROI_LEFT_ebbing.clock.getTime()) # store time of first look
                            ROI_LEFT_ebbing.timesOff.append(ROI_LEFT_ebbing.clock.getTime()) # store time looked until
                        else:
                            ROI_LEFT_ebbing.timesOff[-1] = ROI_LEFT_ebbing.clock.getTime() # update time looked until
                        ROI_LEFT_ebbing.wasLookedIn = True  # if ROI_LEFT_ebbing is still looked at next frame, it is not a new look
                    else:
                        if ROI_LEFT_ebbing.wasLookedIn:
                            ROI_LEFT_ebbing.timesOff[-1] = ROI_LEFT_ebbing.clock.getTime() # update time looked until
                        ROI_LEFT_ebbing.wasLookedIn = False  # if ROI_LEFT_ebbing is looked at next frame, it is a new look
                else:
                    ROI_LEFT_ebbing.clock.reset() # keep clock at 0 if roi hasn't started / has finished
                    ROI_LEFT_ebbing.wasLookedIn = False  # if ROI_LEFT_ebbing is looked at next frame, it is a new look
                if ROI_LEFT_ebbing.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ROI_LEFT_ebbing.tStartRefresh + 15-frameTolerance:
                        # keep track of stop time/frame for later
                        ROI_LEFT_ebbing.tStop = t  # not accounting for scr refresh
                        ROI_LEFT_ebbing.frameNStop = frameN  # exact frame index
                        ROI_LEFT_ebbing.status = FINISHED
                if ROI_RIGHT_ebbingroi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    ROI_RIGHT_ebbingroi.frameNStart = frameN  # exact frame index
                    ROI_RIGHT_ebbingroi.tStart = t  # local t and not account for scr refresh
                    ROI_RIGHT_ebbingroi.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ROI_RIGHT_ebbingroi, 'tStartRefresh')  # time at next scr refresh
                    ROI_RIGHT_ebbingroi.status = STARTED
                if ROI_RIGHT_ebbingroi.status == STARTED:
                    # check whether ROI_RIGHT_ebbingroi has been looked in
                    if ROI_RIGHT_ebbingroi.isLookedIn:
                        if not ROI_RIGHT_ebbingroi.wasLookedIn:
                            ROI_RIGHT_ebbingroi.timesOn.append(ROI_RIGHT_ebbingroi.clock.getTime()) # store time of first look
                            ROI_RIGHT_ebbingroi.timesOff.append(ROI_RIGHT_ebbingroi.clock.getTime()) # store time looked until
                        else:
                            ROI_RIGHT_ebbingroi.timesOff[-1] = ROI_RIGHT_ebbingroi.clock.getTime() # update time looked until
                        ROI_RIGHT_ebbingroi.wasLookedIn = True  # if ROI_RIGHT_ebbingroi is still looked at next frame, it is not a new look
                    else:
                        if ROI_RIGHT_ebbingroi.wasLookedIn:
                            ROI_RIGHT_ebbingroi.timesOff[-1] = ROI_RIGHT_ebbingroi.clock.getTime() # update time looked until
                        ROI_RIGHT_ebbingroi.wasLookedIn = False  # if ROI_RIGHT_ebbingroi is looked at next frame, it is a new look
                else:
                    ROI_RIGHT_ebbingroi.clock.reset() # keep clock at 0 if roi hasn't started / has finished
                    ROI_RIGHT_ebbingroi.wasLookedIn = False  # if ROI_RIGHT_ebbingroi is looked at next frame, it is a new look
                if ROI_RIGHT_ebbingroi.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ROI_RIGHT_ebbingroi.tStartRefresh + 15-frameTolerance:
                        # keep track of stop time/frame for later
                        ROI_RIGHT_ebbingroi.tStop = t  # not accounting for scr refresh
                        ROI_RIGHT_ebbingroi.frameNStop = frameN  # exact frame index
                        ROI_RIGHT_ebbingroi.status = FINISHED
                
                # *key_resp_4* updates
                if key_resp_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_4.frameNStart = frameN  # exact frame index
                    key_resp_4.tStart = t  # local t and not account for scr refresh
                    key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
                    key_resp_4.status = STARTED
                    # keyboard checking is just starting
                    key_resp_4.clock.reset()  # now t=0
                if key_resp_4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > key_resp_4.tStartRefresh + 15-frameTolerance:
                        # keep track of stop time/frame for later
                        key_resp_4.tStop = t  # not accounting for scr refresh
                        key_resp_4.frameNStop = frameN  # exact frame index
                        key_resp_4.status = FINISHED
                if key_resp_4.status == STARTED:
                    theseKeys = key_resp_4.getKeys(keyList=['p'], waitRelease=False)
                    _key_resp_4_allKeys.extend(theseKeys)
                    if len(_key_resp_4_allKeys):
                        key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                        key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in TEST_ebbingComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "TEST_ebbing" ---
            for thisComponent in TEST_ebbingComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store data for ebbing_rep (TrialHandler)
            ebbing_rep.addData('mouse_ebbing.x', mouse_ebbing.x)
            ebbing_rep.addData('mouse_ebbing.y', mouse_ebbing.y)
            ebbing_rep.addData('mouse_ebbing.leftButton', mouse_ebbing.leftButton)
            ebbing_rep.addData('mouse_ebbing.midButton', mouse_ebbing.midButton)
            ebbing_rep.addData('mouse_ebbing.rightButton', mouse_ebbing.rightButton)
            ebbing_rep.addData('mouse_ebbing.time', mouse_ebbing.time)
            ebbing_rep.addData('mouse_ebbing.clicked_name', mouse_ebbing.clicked_name)
            sound_9.stop()  # ensure sound has stopped at end of routine
            # make sure the eyetracker recording stops
            if ebbing_tracker.status != FINISHED:
                ebbing_tracker.status = FINISHED
            ebbing_rep.addData('ROI_LEFT_ebbing.numLooks', ROI_LEFT_ebbing.numLooks)
            if ROI_LEFT_ebbing.numLooks:
               ebbing_rep.addData('ROI_LEFT_ebbing.timesOn', ROI_LEFT_ebbing.timesOn)
               ebbing_rep.addData('ROI_LEFT_ebbing.timesOff', ROI_LEFT_ebbing.timesOff)
            else:
               ebbing_rep.addData('ROI_LEFT_ebbing.timesOn', "")
               ebbing_rep.addData('ROI_LEFT_ebbing.timesOff', "")
            ebbing_rep.addData('ROI_RIGHT_ebbingroi.numLooks', ROI_RIGHT_ebbingroi.numLooks)
            if ROI_RIGHT_ebbingroi.numLooks:
               ebbing_rep.addData('ROI_RIGHT_ebbingroi.timesOn', ROI_RIGHT_ebbingroi.timesOn)
               ebbing_rep.addData('ROI_RIGHT_ebbingroi.timesOff', ROI_RIGHT_ebbingroi.timesOff)
            else:
               ebbing_rep.addData('ROI_RIGHT_ebbingroi.timesOn', "")
               ebbing_rep.addData('ROI_RIGHT_ebbingroi.timesOff', "")
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-15.100000)
            
            # --- Prepare to start Routine "pressspace" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            Next_text.reset()
            # setup some python lists for storing info about the Next_mouse
            Next_mouse.clicked_name = []
            gotValidClick = False  # until a click is received
            key_resp_2.keys = []
            key_resp_2.rt = []
            _key_resp_2_allKeys = []
            # keep track of which components have finished
            pressspaceComponents = [Next_text, Next_polygon, Next_mouse, key_resp_2]
            for thisComponent in pressspaceComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "pressspace" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Next_text* updates
                if Next_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Next_text.frameNStart = frameN  # exact frame index
                    Next_text.tStart = t  # local t and not account for scr refresh
                    Next_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Next_text, 'tStartRefresh')  # time at next scr refresh
                    Next_text.setAutoDraw(True)
                
                # *Next_polygon* updates
                if Next_polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Next_polygon.frameNStart = frameN  # exact frame index
                    Next_polygon.tStart = t  # local t and not account for scr refresh
                    Next_polygon.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Next_polygon, 'tStartRefresh')  # time at next scr refresh
                    Next_polygon.setAutoDraw(True)
                # *Next_mouse* updates
                if Next_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Next_mouse.frameNStart = frameN  # exact frame index
                    Next_mouse.tStart = t  # local t and not account for scr refresh
                    Next_mouse.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Next_mouse, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.addData('Next_mouse.started', t)
                    Next_mouse.status = STARTED
                    prevButtonState = Next_mouse.getPressed()  # if button is down already this ISN'T a new click
                if Next_mouse.status == STARTED:  # only update if started and not finished!
                    buttons = Next_mouse.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            try:
                                iter(Next_polygon)
                                clickableList = Next_polygon
                            except:
                                clickableList = [Next_polygon]
                            for obj in clickableList:
                                if obj.contains(Next_mouse):
                                    gotValidClick = True
                                    Next_mouse.clicked_name.append(obj.name)
                            if gotValidClick:  
                                continueRoutine = False  # abort routine on response
                
                # *key_resp_2* updates
                if key_resp_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_2.frameNStart = frameN  # exact frame index
                    key_resp_2.tStart = t  # local t and not account for scr refresh
                    key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                    key_resp_2.status = STARTED
                    # keyboard checking is just starting
                    key_resp_2.clock.reset()  # now t=0
                if key_resp_2.status == STARTED:
                    theseKeys = key_resp_2.getKeys(keyList=['p'], waitRelease=False)
                    _key_resp_2_allKeys.extend(theseKeys)
                    if len(_key_resp_2_allKeys):
                        key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                        key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in pressspaceComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "pressspace" ---
            for thisComponent in pressspaceComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store data for ebbing_rep (TrialHandler)
            x, y = Next_mouse.getPos()
            buttons = Next_mouse.getPressed()
            if sum(buttons):
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(Next_polygon)
                    clickableList = Next_polygon
                except:
                    clickableList = [Next_polygon]
                for obj in clickableList:
                    if obj.contains(Next_mouse):
                        gotValidClick = True
                        Next_mouse.clicked_name.append(obj.name)
            ebbing_rep.addData('Next_mouse.x', x)
            ebbing_rep.addData('Next_mouse.y', y)
            ebbing_rep.addData('Next_mouse.leftButton', buttons[0])
            ebbing_rep.addData('Next_mouse.midButton', buttons[1])
            ebbing_rep.addData('Next_mouse.rightButton', buttons[2])
            if len(Next_mouse.clicked_name):
                ebbing_rep.addData('Next_mouse.clicked_name', Next_mouse.clicked_name[0])
            # the Routine "pressspace" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'ebbing_rep'
        
        # get names of stimulus parameters
        if ebbing_rep.trialList in ([], [None], None):
            params = []
        else:
            params = ebbing_rep.trialList[0].keys()
        # save data for this loop
        ebbing_rep.saveAsExcel(filename + '.xlsx', sheetName='ebbing_rep',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        thisExp.nextEntry()
        
    # completed ebbing_repeat repeats of 'C'
    
    # get names of stimulus parameters
    if C.trialList in ([], [None], None):
        params = []
    else:
        params = C.trialList[0].keys()
    # save data for this loop
    C.saveAsExcel(filename + '.xlsx', sheetName='C',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # set up handler to look after randomisation of conditions etc
    D = data.TrialHandler(nReps=kanizsa_repeat, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='D')
    thisExp.addLoop(D)  # add the loop to the experiment
    thisD = D.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisD.rgb)
    if thisD != None:
        for paramName in thisD:
            exec('{} = thisD[paramName]'.format(paramName))
    
    for thisD in D:
        currentLoop = D
        # abbreviate parameter names if possible (e.g. rgb = thisD.rgb)
        if thisD != None:
            for paramName in thisD:
                exec('{} = thisD[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "Kanizsa_INTRO" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        sound_6.setSound('Stimuli/Instructions/KZS_long.ogg', hamming=True)
        sound_6.setVolume(1.0, log=False)
        # keep track of which components have finished
        Kanizsa_INTROComponents = [kanizsa_intro_text, sound_6, START_KN]
        for thisComponent in Kanizsa_INTROComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Kanizsa_INTRO" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *kanizsa_intro_text* updates
            if kanizsa_intro_text.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                kanizsa_intro_text.frameNStart = frameN  # exact frame index
                kanizsa_intro_text.tStart = t  # local t and not account for scr refresh
                kanizsa_intro_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(kanizsa_intro_text, 'tStartRefresh')  # time at next scr refresh
                kanizsa_intro_text.setAutoDraw(True)
            # start/stop sound_6
            if sound_6.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                sound_6.frameNStart = frameN  # exact frame index
                sound_6.tStart = t  # local t and not account for scr refresh
                sound_6.tStartRefresh = tThisFlipGlobal  # on global time
                sound_6.play(when=win)  # sync with win flip
            
            # *START_KN* updates
            if START_KN.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                START_KN.frameNStart = frameN  # exact frame index
                START_KN.tStart = t  # local t and not account for scr refresh
                START_KN.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(START_KN, 'tStartRefresh')  # time at next scr refresh
                START_KN.setAutoDraw(True)
            if START_KN.status == STARTED:
                # check whether START_KN has been pressed
                if START_KN.isClicked:
                    if not START_KN.wasClicked:
                        START_KN.timesOn.append(globalClock.getTime()) # store time of first click
                        START_KN.timesOff.append(globalClock.getTime()) # store time clicked until
                    else:
                        START_KN.timesOff[-1] = globalClock.getTime() # update time clicked until
                    if not START_KN.wasClicked:
                        continueRoutine = False  # end routine when START_KN is clicked
                        None
                    START_KN.wasClicked = True  # if START_KN is still clicked next frame, it is not a new click
                else:
                    START_KN.wasClicked = False  # if START_KN is clicked next frame, it is a new click
            else:
                START_KN.wasClicked = False  # if START_KN is clicked next frame, it is a new click
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Kanizsa_INTROComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Kanizsa_INTRO" ---
        for thisComponent in Kanizsa_INTROComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        sound_6.stop()  # ensure sound has stopped at end of routine
        D.addData('START_KN.numClicks', START_KN.numClicks)
        if START_KN.numClicks:
           D.addData('START_KN.timesOn', START_KN.timesOn)
           D.addData('START_KN.timesOff', START_KN.timesOff)
        else:
           D.addData('START_KN.timesOn', "")
           D.addData('START_KN.timesOff', "")
        # the Routine "Kanizsa_INTRO" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "trainingKZS" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # setup some python lists for storing info about the mouse_2
        mouse_2.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        trainingKZSComponents = [triangle, threefourth, twofourth, whitesquare, mouse_2]
        for thisComponent in trainingKZSComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trainingKZS" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *triangle* updates
            if triangle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                triangle.frameNStart = frameN  # exact frame index
                triangle.tStart = t  # local t and not account for scr refresh
                triangle.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(triangle, 'tStartRefresh')  # time at next scr refresh
                triangle.setAutoDraw(True)
            
            # *threefourth* updates
            if threefourth.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                threefourth.frameNStart = frameN  # exact frame index
                threefourth.tStart = t  # local t and not account for scr refresh
                threefourth.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(threefourth, 'tStartRefresh')  # time at next scr refresh
                threefourth.setAutoDraw(True)
            
            # *twofourth* updates
            if twofourth.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                twofourth.frameNStart = frameN  # exact frame index
                twofourth.tStart = t  # local t and not account for scr refresh
                twofourth.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(twofourth, 'tStartRefresh')  # time at next scr refresh
                twofourth.setAutoDraw(True)
            
            # *whitesquare* updates
            if whitesquare.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                whitesquare.frameNStart = frameN  # exact frame index
                whitesquare.tStart = t  # local t and not account for scr refresh
                whitesquare.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(whitesquare, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'whitesquare.started')
                whitesquare.setAutoDraw(True)
            # *mouse_2* updates
            if mouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_2.frameNStart = frameN  # exact frame index
                mouse_2.tStart = t  # local t and not account for scr refresh
                mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
                mouse_2.status = STARTED
                mouse_2.mouseClock.reset()
                prevButtonState = mouse_2.getPressed()  # if button is down already this ISN'T a new click
            if mouse_2.status == STARTED:  # only update if started and not finished!
                buttons = mouse_2.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter(whitesquare)
                            clickableList = whitesquare
                        except:
                            clickableList = [whitesquare]
                        for obj in clickableList:
                            if obj.contains(mouse_2):
                                gotValidClick = True
                                mouse_2.clicked_name.append(obj.name)
                        if gotValidClick:  
                            continueRoutine = False  # abort routine on response
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trainingKZSComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trainingKZS" ---
        for thisComponent in trainingKZSComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store data for D (TrialHandler)
        x, y = mouse_2.getPos()
        buttons = mouse_2.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            try:
                iter(whitesquare)
                clickableList = whitesquare
            except:
                clickableList = [whitesquare]
            for obj in clickableList:
                if obj.contains(mouse_2):
                    gotValidClick = True
                    mouse_2.clicked_name.append(obj.name)
        D.addData('mouse_2.x', x)
        D.addData('mouse_2.y', y)
        D.addData('mouse_2.leftButton', buttons[0])
        D.addData('mouse_2.midButton', buttons[1])
        D.addData('mouse_2.rightButton', buttons[2])
        if len(mouse_2.clicked_name):
            D.addData('mouse_2.clicked_name', mouse_2.clicked_name[0])
        # the Routine "trainingKZS" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "trainingKZS_2" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # setup some python lists for storing info about the mouse_3
        mouse_3.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        trainingKZS_2Components = [triangle_2, threefourth_2, twofourth_2, whitesquare_2, mouse_3]
        for thisComponent in trainingKZS_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trainingKZS_2" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *triangle_2* updates
            if triangle_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                triangle_2.frameNStart = frameN  # exact frame index
                triangle_2.tStart = t  # local t and not account for scr refresh
                triangle_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(triangle_2, 'tStartRefresh')  # time at next scr refresh
                triangle_2.setAutoDraw(True)
            
            # *threefourth_2* updates
            if threefourth_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                threefourth_2.frameNStart = frameN  # exact frame index
                threefourth_2.tStart = t  # local t and not account for scr refresh
                threefourth_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(threefourth_2, 'tStartRefresh')  # time at next scr refresh
                threefourth_2.setAutoDraw(True)
            
            # *twofourth_2* updates
            if twofourth_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                twofourth_2.frameNStart = frameN  # exact frame index
                twofourth_2.tStart = t  # local t and not account for scr refresh
                twofourth_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(twofourth_2, 'tStartRefresh')  # time at next scr refresh
                twofourth_2.setAutoDraw(True)
            
            # *whitesquare_2* updates
            if whitesquare_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                whitesquare_2.frameNStart = frameN  # exact frame index
                whitesquare_2.tStart = t  # local t and not account for scr refresh
                whitesquare_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(whitesquare_2, 'tStartRefresh')  # time at next scr refresh
                whitesquare_2.setAutoDraw(True)
            # *mouse_3* updates
            if mouse_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_3.frameNStart = frameN  # exact frame index
                mouse_3.tStart = t  # local t and not account for scr refresh
                mouse_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('mouse_3.started', t)
                mouse_3.status = STARTED
                mouse_3.mouseClock.reset()
                prevButtonState = mouse_3.getPressed()  # if button is down already this ISN'T a new click
            if mouse_3.status == STARTED:  # only update if started and not finished!
                buttons = mouse_3.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter(whitesquare_2)
                            clickableList = whitesquare_2
                        except:
                            clickableList = [whitesquare_2]
                        for obj in clickableList:
                            if obj.contains(mouse_3):
                                gotValidClick = True
                                mouse_3.clicked_name.append(obj.name)
                        if gotValidClick:  
                            continueRoutine = False  # abort routine on response
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trainingKZS_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trainingKZS_2" ---
        for thisComponent in trainingKZS_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store data for D (TrialHandler)
        x, y = mouse_3.getPos()
        buttons = mouse_3.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            try:
                iter(whitesquare_2)
                clickableList = whitesquare_2
            except:
                clickableList = [whitesquare_2]
            for obj in clickableList:
                if obj.contains(mouse_3):
                    gotValidClick = True
                    mouse_3.clicked_name.append(obj.name)
        D.addData('mouse_3.x', x)
        D.addData('mouse_3.y', y)
        D.addData('mouse_3.leftButton', buttons[0])
        D.addData('mouse_3.midButton', buttons[1])
        D.addData('mouse_3.rightButton', buttons[2])
        if len(mouse_3.clicked_name):
            D.addData('mouse_3.clicked_name', mouse_3.clicked_name[0])
        # the Routine "trainingKZS_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        KN_rep = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('Stimuli/Kanizsa trials/KN_condition_file.xlsx'),
            seed=None, name='KN_rep')
        thisExp.addLoop(KN_rep)  # add the loop to the experiment
        thisKN_rep = KN_rep.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisKN_rep.rgb)
        if thisKN_rep != None:
            for paramName in thisKN_rep:
                exec('{} = thisKN_rep[paramName]'.format(paramName))
        
        for thisKN_rep in KN_rep:
            currentLoop = KN_rep
            # abbreviate parameter names if possible (e.g. rgb = thisKN_rep.rgb)
            if thisKN_rep != None:
                for paramName in thisKN_rep:
                    exec('{} = thisKN_rep[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "TEST_knzs" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            image_KN.setImage(path)
            # setup some python lists for storing info about the mouse_KN
            mouse_KN.x = []
            mouse_KN.y = []
            mouse_KN.leftButton = []
            mouse_KN.midButton = []
            mouse_KN.rightButton = []
            mouse_KN.time = []
            mouse_KN.clicked_name = []
            gotValidClick = False  # until a click is received
            sound_11.setSound('Stimuli/Instructions/KZS_short.ogg', secs=10, hamming=True)
            sound_11.setVolume(1.0, log=False)
            # clear any previous roi data
            ROI_LEFT_KN.reset()
            # clear any previous roi data
            ROI_RIGHT_KN.reset()
            key_resp_5.keys = []
            key_resp_5.rt = []
            _key_resp_5_allKeys = []
            # keep track of which components have finished
            TEST_knzsComponents = [image_KN, LEFT_KN, RIGHT_KN, mouse_KN, sound_11, Kanizsa_tracker, ROI_LEFT_KN, ROI_RIGHT_KN, key_resp_5]
            for thisComponent in TEST_knzsComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "TEST_knzs" ---
            while continueRoutine and routineTimer.getTime() < 15.1:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image_KN* updates
                if image_KN.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
                    # keep track of start time/frame for later
                    image_KN.frameNStart = frameN  # exact frame index
                    image_KN.tStart = t  # local t and not account for scr refresh
                    image_KN.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_KN, 'tStartRefresh')  # time at next scr refresh
                    image_KN.setAutoDraw(True)
                if image_KN.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_KN.tStartRefresh + 15-frameTolerance:
                        # keep track of stop time/frame for later
                        image_KN.tStop = t  # not accounting for scr refresh
                        image_KN.frameNStop = frameN  # exact frame index
                        image_KN.setAutoDraw(False)
                
                # *LEFT_KN* updates
                if LEFT_KN.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    LEFT_KN.frameNStart = frameN  # exact frame index
                    LEFT_KN.tStart = t  # local t and not account for scr refresh
                    LEFT_KN.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(LEFT_KN, 'tStartRefresh')  # time at next scr refresh
                    LEFT_KN.setAutoDraw(True)
                if LEFT_KN.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > LEFT_KN.tStartRefresh + 15-frameTolerance:
                        # keep track of stop time/frame for later
                        LEFT_KN.tStop = t  # not accounting for scr refresh
                        LEFT_KN.frameNStop = frameN  # exact frame index
                        LEFT_KN.setAutoDraw(False)
                
                # *RIGHT_KN* updates
                if RIGHT_KN.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    RIGHT_KN.frameNStart = frameN  # exact frame index
                    RIGHT_KN.tStart = t  # local t and not account for scr refresh
                    RIGHT_KN.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(RIGHT_KN, 'tStartRefresh')  # time at next scr refresh
                    RIGHT_KN.setAutoDraw(True)
                if RIGHT_KN.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > RIGHT_KN.tStartRefresh + 15-frameTolerance:
                        # keep track of stop time/frame for later
                        RIGHT_KN.tStop = t  # not accounting for scr refresh
                        RIGHT_KN.frameNStop = frameN  # exact frame index
                        RIGHT_KN.setAutoDraw(False)
                # *mouse_KN* updates
                if mouse_KN.status == NOT_STARTED and t >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    mouse_KN.frameNStart = frameN  # exact frame index
                    mouse_KN.tStart = t  # local t and not account for scr refresh
                    mouse_KN.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse_KN, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.addData('mouse_KN.started', t)
                    mouse_KN.status = STARTED
                    mouse_KN.mouseClock.reset()
                    prevButtonState = mouse_KN.getPressed()  # if button is down already this ISN'T a new click
                if mouse_KN.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > mouse_KN.tStartRefresh + 15-frameTolerance:
                        # keep track of stop time/frame for later
                        mouse_KN.tStop = t  # not accounting for scr refresh
                        mouse_KN.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.addData('mouse_KN.stopped', t)
                        mouse_KN.status = FINISHED
                if mouse_KN.status == STARTED:  # only update if started and not finished!
                    buttons = mouse_KN.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            try:
                                iter([LEFT_MS, RIGHT_MS])
                                clickableList = [LEFT_MS, RIGHT_MS]
                            except:
                                clickableList = [[LEFT_MS, RIGHT_MS]]
                            for obj in clickableList:
                                if obj.contains(mouse_KN):
                                    gotValidClick = True
                                    mouse_KN.clicked_name.append(obj.name)
                            x, y = mouse_KN.getPos()
                            mouse_KN.x.append(x)
                            mouse_KN.y.append(y)
                            buttons = mouse_KN.getPressed()
                            mouse_KN.leftButton.append(buttons[0])
                            mouse_KN.midButton.append(buttons[1])
                            mouse_KN.rightButton.append(buttons[2])
                            mouse_KN.time.append(mouse_KN.mouseClock.getTime())
                            
                            continueRoutine = False  # abort routine on response
                # start/stop sound_11
                if sound_11.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
                    # keep track of start time/frame for later
                    sound_11.frameNStart = frameN  # exact frame index
                    sound_11.tStart = t  # local t and not account for scr refresh
                    sound_11.tStartRefresh = tThisFlipGlobal  # on global time
                    sound_11.play(when=win)  # sync with win flip
                if sound_11.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > sound_11.tStartRefresh + 10-frameTolerance:
                        # keep track of stop time/frame for later
                        sound_11.tStop = t  # not accounting for scr refresh
                        sound_11.frameNStop = frameN  # exact frame index
                        sound_11.stop()
                # *Kanizsa_tracker* updates
                if Kanizsa_tracker.status == NOT_STARTED and t >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    Kanizsa_tracker.frameNStart = frameN  # exact frame index
                    Kanizsa_tracker.tStart = t  # local t and not account for scr refresh
                    Kanizsa_tracker.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Kanizsa_tracker, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.addData('Kanizsa_tracker.started', t)
                    Kanizsa_tracker.status = STARTED
                if Kanizsa_tracker.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Kanizsa_tracker.tStartRefresh + 15-frameTolerance:
                        # keep track of stop time/frame for later
                        Kanizsa_tracker.tStop = t  # not accounting for scr refresh
                        Kanizsa_tracker.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.addData('Kanizsa_tracker.stopped', t)
                        Kanizsa_tracker.status = FINISHED
                if ROI_LEFT_KN.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    ROI_LEFT_KN.frameNStart = frameN  # exact frame index
                    ROI_LEFT_KN.tStart = t  # local t and not account for scr refresh
                    ROI_LEFT_KN.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ROI_LEFT_KN, 'tStartRefresh')  # time at next scr refresh
                    ROI_LEFT_KN.status = STARTED
                if ROI_LEFT_KN.status == STARTED:
                    # check whether ROI_LEFT_KN has been looked in
                    if ROI_LEFT_KN.isLookedIn:
                        if not ROI_LEFT_KN.wasLookedIn:
                            ROI_LEFT_KN.timesOn.append(ROI_LEFT_KN.clock.getTime()) # store time of first look
                            ROI_LEFT_KN.timesOff.append(ROI_LEFT_KN.clock.getTime()) # store time looked until
                        else:
                            ROI_LEFT_KN.timesOff[-1] = ROI_LEFT_KN.clock.getTime() # update time looked until
                        ROI_LEFT_KN.wasLookedIn = True  # if ROI_LEFT_KN is still looked at next frame, it is not a new look
                    else:
                        if ROI_LEFT_KN.wasLookedIn:
                            ROI_LEFT_KN.timesOff[-1] = ROI_LEFT_KN.clock.getTime() # update time looked until
                        ROI_LEFT_KN.wasLookedIn = False  # if ROI_LEFT_KN is looked at next frame, it is a new look
                else:
                    ROI_LEFT_KN.clock.reset() # keep clock at 0 if roi hasn't started / has finished
                    ROI_LEFT_KN.wasLookedIn = False  # if ROI_LEFT_KN is looked at next frame, it is a new look
                if ROI_LEFT_KN.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ROI_LEFT_KN.tStartRefresh + 15-frameTolerance:
                        # keep track of stop time/frame for later
                        ROI_LEFT_KN.tStop = t  # not accounting for scr refresh
                        ROI_LEFT_KN.frameNStop = frameN  # exact frame index
                        ROI_LEFT_KN.status = FINISHED
                if ROI_RIGHT_KN.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    ROI_RIGHT_KN.frameNStart = frameN  # exact frame index
                    ROI_RIGHT_KN.tStart = t  # local t and not account for scr refresh
                    ROI_RIGHT_KN.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ROI_RIGHT_KN, 'tStartRefresh')  # time at next scr refresh
                    ROI_RIGHT_KN.status = STARTED
                if ROI_RIGHT_KN.status == STARTED:
                    # check whether ROI_RIGHT_KN has been looked in
                    if ROI_RIGHT_KN.isLookedIn:
                        if not ROI_RIGHT_KN.wasLookedIn:
                            ROI_RIGHT_KN.timesOn.append(ROI_RIGHT_KN.clock.getTime()) # store time of first look
                            ROI_RIGHT_KN.timesOff.append(ROI_RIGHT_KN.clock.getTime()) # store time looked until
                        else:
                            ROI_RIGHT_KN.timesOff[-1] = ROI_RIGHT_KN.clock.getTime() # update time looked until
                        ROI_RIGHT_KN.wasLookedIn = True  # if ROI_RIGHT_KN is still looked at next frame, it is not a new look
                    else:
                        if ROI_RIGHT_KN.wasLookedIn:
                            ROI_RIGHT_KN.timesOff[-1] = ROI_RIGHT_KN.clock.getTime() # update time looked until
                        ROI_RIGHT_KN.wasLookedIn = False  # if ROI_RIGHT_KN is looked at next frame, it is a new look
                else:
                    ROI_RIGHT_KN.clock.reset() # keep clock at 0 if roi hasn't started / has finished
                    ROI_RIGHT_KN.wasLookedIn = False  # if ROI_RIGHT_KN is looked at next frame, it is a new look
                if ROI_RIGHT_KN.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ROI_RIGHT_KN.tStartRefresh + 15-frameTolerance:
                        # keep track of stop time/frame for later
                        ROI_RIGHT_KN.tStop = t  # not accounting for scr refresh
                        ROI_RIGHT_KN.frameNStop = frameN  # exact frame index
                        ROI_RIGHT_KN.status = FINISHED
                
                # *key_resp_5* updates
                if key_resp_5.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_5.frameNStart = frameN  # exact frame index
                    key_resp_5.tStart = t  # local t and not account for scr refresh
                    key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
                    key_resp_5.status = STARTED
                    # keyboard checking is just starting
                    key_resp_5.clock.reset()  # now t=0
                if key_resp_5.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > key_resp_5.tStartRefresh + 15-frameTolerance:
                        # keep track of stop time/frame for later
                        key_resp_5.tStop = t  # not accounting for scr refresh
                        key_resp_5.frameNStop = frameN  # exact frame index
                        key_resp_5.status = FINISHED
                if key_resp_5.status == STARTED:
                    theseKeys = key_resp_5.getKeys(keyList=['p'], waitRelease=False)
                    _key_resp_5_allKeys.extend(theseKeys)
                    if len(_key_resp_5_allKeys):
                        key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                        key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in TEST_knzsComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "TEST_knzs" ---
            for thisComponent in TEST_knzsComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store data for KN_rep (TrialHandler)
            KN_rep.addData('mouse_KN.x', mouse_KN.x)
            KN_rep.addData('mouse_KN.y', mouse_KN.y)
            KN_rep.addData('mouse_KN.leftButton', mouse_KN.leftButton)
            KN_rep.addData('mouse_KN.midButton', mouse_KN.midButton)
            KN_rep.addData('mouse_KN.rightButton', mouse_KN.rightButton)
            KN_rep.addData('mouse_KN.time', mouse_KN.time)
            KN_rep.addData('mouse_KN.clicked_name', mouse_KN.clicked_name)
            sound_11.stop()  # ensure sound has stopped at end of routine
            # make sure the eyetracker recording stops
            if Kanizsa_tracker.status != FINISHED:
                Kanizsa_tracker.status = FINISHED
            KN_rep.addData('ROI_LEFT_KN.numLooks', ROI_LEFT_KN.numLooks)
            if ROI_LEFT_KN.numLooks:
               KN_rep.addData('ROI_LEFT_KN.timesOn', ROI_LEFT_KN.timesOn)
               KN_rep.addData('ROI_LEFT_KN.timesOff', ROI_LEFT_KN.timesOff)
            else:
               KN_rep.addData('ROI_LEFT_KN.timesOn', "")
               KN_rep.addData('ROI_LEFT_KN.timesOff', "")
            KN_rep.addData('ROI_RIGHT_KN.numLooks', ROI_RIGHT_KN.numLooks)
            if ROI_RIGHT_KN.numLooks:
               KN_rep.addData('ROI_RIGHT_KN.timesOn', ROI_RIGHT_KN.timesOn)
               KN_rep.addData('ROI_RIGHT_KN.timesOff', ROI_RIGHT_KN.timesOff)
            else:
               KN_rep.addData('ROI_RIGHT_KN.timesOn', "")
               KN_rep.addData('ROI_RIGHT_KN.timesOff', "")
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-15.100000)
            
            # --- Prepare to start Routine "pressspace" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            Next_text.reset()
            # setup some python lists for storing info about the Next_mouse
            Next_mouse.clicked_name = []
            gotValidClick = False  # until a click is received
            key_resp_2.keys = []
            key_resp_2.rt = []
            _key_resp_2_allKeys = []
            # keep track of which components have finished
            pressspaceComponents = [Next_text, Next_polygon, Next_mouse, key_resp_2]
            for thisComponent in pressspaceComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "pressspace" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Next_text* updates
                if Next_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Next_text.frameNStart = frameN  # exact frame index
                    Next_text.tStart = t  # local t and not account for scr refresh
                    Next_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Next_text, 'tStartRefresh')  # time at next scr refresh
                    Next_text.setAutoDraw(True)
                
                # *Next_polygon* updates
                if Next_polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Next_polygon.frameNStart = frameN  # exact frame index
                    Next_polygon.tStart = t  # local t and not account for scr refresh
                    Next_polygon.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Next_polygon, 'tStartRefresh')  # time at next scr refresh
                    Next_polygon.setAutoDraw(True)
                # *Next_mouse* updates
                if Next_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Next_mouse.frameNStart = frameN  # exact frame index
                    Next_mouse.tStart = t  # local t and not account for scr refresh
                    Next_mouse.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Next_mouse, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.addData('Next_mouse.started', t)
                    Next_mouse.status = STARTED
                    prevButtonState = Next_mouse.getPressed()  # if button is down already this ISN'T a new click
                if Next_mouse.status == STARTED:  # only update if started and not finished!
                    buttons = Next_mouse.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            try:
                                iter(Next_polygon)
                                clickableList = Next_polygon
                            except:
                                clickableList = [Next_polygon]
                            for obj in clickableList:
                                if obj.contains(Next_mouse):
                                    gotValidClick = True
                                    Next_mouse.clicked_name.append(obj.name)
                            if gotValidClick:  
                                continueRoutine = False  # abort routine on response
                
                # *key_resp_2* updates
                if key_resp_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_2.frameNStart = frameN  # exact frame index
                    key_resp_2.tStart = t  # local t and not account for scr refresh
                    key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                    key_resp_2.status = STARTED
                    # keyboard checking is just starting
                    key_resp_2.clock.reset()  # now t=0
                if key_resp_2.status == STARTED:
                    theseKeys = key_resp_2.getKeys(keyList=['p'], waitRelease=False)
                    _key_resp_2_allKeys.extend(theseKeys)
                    if len(_key_resp_2_allKeys):
                        key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                        key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in pressspaceComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "pressspace" ---
            for thisComponent in pressspaceComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store data for KN_rep (TrialHandler)
            x, y = Next_mouse.getPos()
            buttons = Next_mouse.getPressed()
            if sum(buttons):
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(Next_polygon)
                    clickableList = Next_polygon
                except:
                    clickableList = [Next_polygon]
                for obj in clickableList:
                    if obj.contains(Next_mouse):
                        gotValidClick = True
                        Next_mouse.clicked_name.append(obj.name)
            KN_rep.addData('Next_mouse.x', x)
            KN_rep.addData('Next_mouse.y', y)
            KN_rep.addData('Next_mouse.leftButton', buttons[0])
            KN_rep.addData('Next_mouse.midButton', buttons[1])
            KN_rep.addData('Next_mouse.rightButton', buttons[2])
            if len(Next_mouse.clicked_name):
                KN_rep.addData('Next_mouse.clicked_name', Next_mouse.clicked_name[0])
            # the Routine "pressspace" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'KN_rep'
        
        # get names of stimulus parameters
        if KN_rep.trialList in ([], [None], None):
            params = []
        else:
            params = KN_rep.trialList[0].keys()
        # save data for this loop
        KN_rep.saveAsExcel(filename + '.xlsx', sheetName='KN_rep',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        thisExp.nextEntry()
        
    # completed kanizsa_repeat repeats of 'D'
    
    # get names of stimulus parameters
    if D.trialList in ([], [None], None):
        params = []
    else:
        params = D.trialList[0].keys()
    # save data for this loop
    D.saveAsExcel(filename + '.xlsx', sheetName='D',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # set up handler to look after randomisation of conditions etc
    E = data.TrialHandler(nReps=MS_repeat, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='E')
    thisExp.addLoop(E)  # add the loop to the experiment
    thisE = E.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisE.rgb)
    if thisE != None:
        for paramName in thisE:
            exec('{} = thisE[paramName]'.format(paramName))
    
    for thisE in E:
        currentLoop = E
        # abbreviate parameter names if possible (e.g. rgb = thisE.rgb)
        if thisE != None:
            for paramName in thisE:
                exec('{} = thisE[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "MS_INTRO" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        sound_7.setSound('Stimuli/Instructions/MS_long.ogg', hamming=True)
        sound_7.setVolume(1.0, log=False)
        # keep track of which components have finished
        MS_INTROComponents = [MS_intro_text, sound_7, START_MS]
        for thisComponent in MS_INTROComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "MS_INTRO" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *MS_intro_text* updates
            if MS_intro_text.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                MS_intro_text.frameNStart = frameN  # exact frame index
                MS_intro_text.tStart = t  # local t and not account for scr refresh
                MS_intro_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(MS_intro_text, 'tStartRefresh')  # time at next scr refresh
                MS_intro_text.setAutoDraw(True)
            # start/stop sound_7
            if sound_7.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                sound_7.frameNStart = frameN  # exact frame index
                sound_7.tStart = t  # local t and not account for scr refresh
                sound_7.tStartRefresh = tThisFlipGlobal  # on global time
                sound_7.play(when=win)  # sync with win flip
            
            # *START_MS* updates
            if START_MS.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                START_MS.frameNStart = frameN  # exact frame index
                START_MS.tStart = t  # local t and not account for scr refresh
                START_MS.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(START_MS, 'tStartRefresh')  # time at next scr refresh
                START_MS.setAutoDraw(True)
            if START_MS.status == STARTED:
                # check whether START_MS has been pressed
                if START_MS.isClicked:
                    if not START_MS.wasClicked:
                        START_MS.timesOn.append(globalClock.getTime()) # store time of first click
                        START_MS.timesOff.append(globalClock.getTime()) # store time clicked until
                    else:
                        START_MS.timesOff[-1] = globalClock.getTime() # update time clicked until
                    if not START_MS.wasClicked:
                        continueRoutine = False  # end routine when START_MS is clicked
                        None
                    START_MS.wasClicked = True  # if START_MS is still clicked next frame, it is not a new click
                else:
                    START_MS.wasClicked = False  # if START_MS is clicked next frame, it is a new click
            else:
                START_MS.wasClicked = False  # if START_MS is clicked next frame, it is a new click
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in MS_INTROComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "MS_INTRO" ---
        for thisComponent in MS_INTROComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        sound_7.stop()  # ensure sound has stopped at end of routine
        E.addData('START_MS.numClicks', START_MS.numClicks)
        if START_MS.numClicks:
           E.addData('START_MS.timesOn', START_MS.timesOn)
           E.addData('START_MS.timesOff', START_MS.timesOff)
        else:
           E.addData('START_MS.timesOn', "")
           E.addData('START_MS.timesOff', "")
        # the Routine "MS_INTRO" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        MS_rep = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('Stimuli/Moving snake trials/MS_condition_file.xlsx'),
            seed=None, name='MS_rep')
        thisExp.addLoop(MS_rep)  # add the loop to the experiment
        thisMS_rep = MS_rep.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisMS_rep.rgb)
        if thisMS_rep != None:
            for paramName in thisMS_rep:
                exec('{} = thisMS_rep[paramName]'.format(paramName))
        
        for thisMS_rep in MS_rep:
            currentLoop = MS_rep
            # abbreviate parameter names if possible (e.g. rgb = thisMS_rep.rgb)
            if thisMS_rep != None:
                for paramName in thisMS_rep:
                    exec('{} = thisMS_rep[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "TEST_MS" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            image_MS.setImage(path)
            # setup some python lists for storing info about the mouse_MS
            mouse_MS.x = []
            mouse_MS.y = []
            mouse_MS.leftButton = []
            mouse_MS.midButton = []
            mouse_MS.rightButton = []
            mouse_MS.time = []
            mouse_MS.clicked_name = []
            gotValidClick = False  # until a click is received
            sound_10.setSound('Stimuli/Instructions/MS_short.ogg', secs=10, hamming=True)
            sound_10.setVolume(1.0, log=False)
            # clear any previous roi data
            ROI_LEFT_MS.reset()
            # clear any previous roi data
            ROI_RIGHT_MS.reset()
            key_resp_6.keys = []
            key_resp_6.rt = []
            _key_resp_6_allKeys = []
            # keep track of which components have finished
            TEST_MSComponents = [image_MS, LEFT_MS, RIGHT_MS, mouse_MS, sound_10, MS_tracker, ROI_LEFT_MS, ROI_RIGHT_MS, key_resp_6]
            for thisComponent in TEST_MSComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "TEST_MS" ---
            while continueRoutine and routineTimer.getTime() < 15.1:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image_MS* updates
                if image_MS.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
                    # keep track of start time/frame for later
                    image_MS.frameNStart = frameN  # exact frame index
                    image_MS.tStart = t  # local t and not account for scr refresh
                    image_MS.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_MS, 'tStartRefresh')  # time at next scr refresh
                    image_MS.setAutoDraw(True)
                if image_MS.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_MS.tStartRefresh + 15-frameTolerance:
                        # keep track of stop time/frame for later
                        image_MS.tStop = t  # not accounting for scr refresh
                        image_MS.frameNStop = frameN  # exact frame index
                        image_MS.setAutoDraw(False)
                
                # *LEFT_MS* updates
                if LEFT_MS.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    LEFT_MS.frameNStart = frameN  # exact frame index
                    LEFT_MS.tStart = t  # local t and not account for scr refresh
                    LEFT_MS.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(LEFT_MS, 'tStartRefresh')  # time at next scr refresh
                    LEFT_MS.setAutoDraw(True)
                if LEFT_MS.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > LEFT_MS.tStartRefresh + 15-frameTolerance:
                        # keep track of stop time/frame for later
                        LEFT_MS.tStop = t  # not accounting for scr refresh
                        LEFT_MS.frameNStop = frameN  # exact frame index
                        LEFT_MS.setAutoDraw(False)
                
                # *RIGHT_MS* updates
                if RIGHT_MS.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    RIGHT_MS.frameNStart = frameN  # exact frame index
                    RIGHT_MS.tStart = t  # local t and not account for scr refresh
                    RIGHT_MS.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(RIGHT_MS, 'tStartRefresh')  # time at next scr refresh
                    RIGHT_MS.setAutoDraw(True)
                if RIGHT_MS.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > RIGHT_MS.tStartRefresh + 15-frameTolerance:
                        # keep track of stop time/frame for later
                        RIGHT_MS.tStop = t  # not accounting for scr refresh
                        RIGHT_MS.frameNStop = frameN  # exact frame index
                        RIGHT_MS.setAutoDraw(False)
                # *mouse_MS* updates
                if mouse_MS.status == NOT_STARTED and t >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    mouse_MS.frameNStart = frameN  # exact frame index
                    mouse_MS.tStart = t  # local t and not account for scr refresh
                    mouse_MS.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse_MS, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.addData('mouse_MS.started', t)
                    mouse_MS.status = STARTED
                    mouse_MS.mouseClock.reset()
                    prevButtonState = mouse_MS.getPressed()  # if button is down already this ISN'T a new click
                if mouse_MS.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > mouse_MS.tStartRefresh + 15-frameTolerance:
                        # keep track of stop time/frame for later
                        mouse_MS.tStop = t  # not accounting for scr refresh
                        mouse_MS.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.addData('mouse_MS.stopped', t)
                        mouse_MS.status = FINISHED
                if mouse_MS.status == STARTED:  # only update if started and not finished!
                    buttons = mouse_MS.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            try:
                                iter([LEFT_MS, RIGHT_MS])
                                clickableList = [LEFT_MS, RIGHT_MS]
                            except:
                                clickableList = [[LEFT_MS, RIGHT_MS]]
                            for obj in clickableList:
                                if obj.contains(mouse_MS):
                                    gotValidClick = True
                                    mouse_MS.clicked_name.append(obj.name)
                            x, y = mouse_MS.getPos()
                            mouse_MS.x.append(x)
                            mouse_MS.y.append(y)
                            buttons = mouse_MS.getPressed()
                            mouse_MS.leftButton.append(buttons[0])
                            mouse_MS.midButton.append(buttons[1])
                            mouse_MS.rightButton.append(buttons[2])
                            mouse_MS.time.append(mouse_MS.mouseClock.getTime())
                            
                            continueRoutine = False  # abort routine on response
                # start/stop sound_10
                if sound_10.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
                    # keep track of start time/frame for later
                    sound_10.frameNStart = frameN  # exact frame index
                    sound_10.tStart = t  # local t and not account for scr refresh
                    sound_10.tStartRefresh = tThisFlipGlobal  # on global time
                    sound_10.play(when=win)  # sync with win flip
                if sound_10.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > sound_10.tStartRefresh + 10-frameTolerance:
                        # keep track of stop time/frame for later
                        sound_10.tStop = t  # not accounting for scr refresh
                        sound_10.frameNStop = frameN  # exact frame index
                        sound_10.stop()
                # *MS_tracker* updates
                if MS_tracker.status == NOT_STARTED and t >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    MS_tracker.frameNStart = frameN  # exact frame index
                    MS_tracker.tStart = t  # local t and not account for scr refresh
                    MS_tracker.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(MS_tracker, 'tStartRefresh')  # time at next scr refresh
                    MS_tracker.status = STARTED
                if MS_tracker.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > MS_tracker.tStartRefresh + 15-frameTolerance:
                        # keep track of stop time/frame for later
                        MS_tracker.tStop = t  # not accounting for scr refresh
                        MS_tracker.frameNStop = frameN  # exact frame index
                        MS_tracker.status = FINISHED
                if ROI_LEFT_MS.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    ROI_LEFT_MS.frameNStart = frameN  # exact frame index
                    ROI_LEFT_MS.tStart = t  # local t and not account for scr refresh
                    ROI_LEFT_MS.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ROI_LEFT_MS, 'tStartRefresh')  # time at next scr refresh
                    ROI_LEFT_MS.status = STARTED
                if ROI_LEFT_MS.status == STARTED:
                    # check whether ROI_LEFT_MS has been looked in
                    if ROI_LEFT_MS.isLookedIn:
                        if not ROI_LEFT_MS.wasLookedIn:
                            ROI_LEFT_MS.timesOn.append(ROI_LEFT_MS.clock.getTime()) # store time of first look
                            ROI_LEFT_MS.timesOff.append(ROI_LEFT_MS.clock.getTime()) # store time looked until
                        else:
                            ROI_LEFT_MS.timesOff[-1] = ROI_LEFT_MS.clock.getTime() # update time looked until
                        ROI_LEFT_MS.wasLookedIn = True  # if ROI_LEFT_MS is still looked at next frame, it is not a new look
                    else:
                        if ROI_LEFT_MS.wasLookedIn:
                            ROI_LEFT_MS.timesOff[-1] = ROI_LEFT_MS.clock.getTime() # update time looked until
                        ROI_LEFT_MS.wasLookedIn = False  # if ROI_LEFT_MS is looked at next frame, it is a new look
                else:
                    ROI_LEFT_MS.clock.reset() # keep clock at 0 if roi hasn't started / has finished
                    ROI_LEFT_MS.wasLookedIn = False  # if ROI_LEFT_MS is looked at next frame, it is a new look
                if ROI_LEFT_MS.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ROI_LEFT_MS.tStartRefresh + 15-frameTolerance:
                        # keep track of stop time/frame for later
                        ROI_LEFT_MS.tStop = t  # not accounting for scr refresh
                        ROI_LEFT_MS.frameNStop = frameN  # exact frame index
                        ROI_LEFT_MS.status = FINISHED
                if ROI_RIGHT_MS.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    ROI_RIGHT_MS.frameNStart = frameN  # exact frame index
                    ROI_RIGHT_MS.tStart = t  # local t and not account for scr refresh
                    ROI_RIGHT_MS.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ROI_RIGHT_MS, 'tStartRefresh')  # time at next scr refresh
                    ROI_RIGHT_MS.status = STARTED
                if ROI_RIGHT_MS.status == STARTED:
                    # check whether ROI_RIGHT_MS has been looked in
                    if ROI_RIGHT_MS.isLookedIn:
                        if not ROI_RIGHT_MS.wasLookedIn:
                            ROI_RIGHT_MS.timesOn.append(ROI_RIGHT_MS.clock.getTime()) # store time of first look
                            ROI_RIGHT_MS.timesOff.append(ROI_RIGHT_MS.clock.getTime()) # store time looked until
                        else:
                            ROI_RIGHT_MS.timesOff[-1] = ROI_RIGHT_MS.clock.getTime() # update time looked until
                        ROI_RIGHT_MS.wasLookedIn = True  # if ROI_RIGHT_MS is still looked at next frame, it is not a new look
                    else:
                        if ROI_RIGHT_MS.wasLookedIn:
                            ROI_RIGHT_MS.timesOff[-1] = ROI_RIGHT_MS.clock.getTime() # update time looked until
                        ROI_RIGHT_MS.wasLookedIn = False  # if ROI_RIGHT_MS is looked at next frame, it is a new look
                else:
                    ROI_RIGHT_MS.clock.reset() # keep clock at 0 if roi hasn't started / has finished
                    ROI_RIGHT_MS.wasLookedIn = False  # if ROI_RIGHT_MS is looked at next frame, it is a new look
                if ROI_RIGHT_MS.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ROI_RIGHT_MS.tStartRefresh + 15-frameTolerance:
                        # keep track of stop time/frame for later
                        ROI_RIGHT_MS.tStop = t  # not accounting for scr refresh
                        ROI_RIGHT_MS.frameNStop = frameN  # exact frame index
                        ROI_RIGHT_MS.status = FINISHED
                
                # *key_resp_6* updates
                if key_resp_6.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_6.frameNStart = frameN  # exact frame index
                    key_resp_6.tStart = t  # local t and not account for scr refresh
                    key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
                    key_resp_6.status = STARTED
                    # keyboard checking is just starting
                    key_resp_6.clock.reset()  # now t=0
                if key_resp_6.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > key_resp_6.tStartRefresh + 15-frameTolerance:
                        # keep track of stop time/frame for later
                        key_resp_6.tStop = t  # not accounting for scr refresh
                        key_resp_6.frameNStop = frameN  # exact frame index
                        key_resp_6.status = FINISHED
                if key_resp_6.status == STARTED:
                    theseKeys = key_resp_6.getKeys(keyList=['p'], waitRelease=False)
                    _key_resp_6_allKeys.extend(theseKeys)
                    if len(_key_resp_6_allKeys):
                        key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                        key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in TEST_MSComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "TEST_MS" ---
            for thisComponent in TEST_MSComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store data for MS_rep (TrialHandler)
            MS_rep.addData('mouse_MS.x', mouse_MS.x)
            MS_rep.addData('mouse_MS.y', mouse_MS.y)
            MS_rep.addData('mouse_MS.leftButton', mouse_MS.leftButton)
            MS_rep.addData('mouse_MS.midButton', mouse_MS.midButton)
            MS_rep.addData('mouse_MS.rightButton', mouse_MS.rightButton)
            MS_rep.addData('mouse_MS.time', mouse_MS.time)
            MS_rep.addData('mouse_MS.clicked_name', mouse_MS.clicked_name)
            sound_10.stop()  # ensure sound has stopped at end of routine
            # make sure the eyetracker recording stops
            if MS_tracker.status != FINISHED:
                MS_tracker.status = FINISHED
            MS_rep.addData('ROI_LEFT_MS.numLooks', ROI_LEFT_MS.numLooks)
            if ROI_LEFT_MS.numLooks:
               MS_rep.addData('ROI_LEFT_MS.timesOn', ROI_LEFT_MS.timesOn)
               MS_rep.addData('ROI_LEFT_MS.timesOff', ROI_LEFT_MS.timesOff)
            else:
               MS_rep.addData('ROI_LEFT_MS.timesOn', "")
               MS_rep.addData('ROI_LEFT_MS.timesOff', "")
            MS_rep.addData('ROI_RIGHT_MS.numLooks', ROI_RIGHT_MS.numLooks)
            if ROI_RIGHT_MS.numLooks:
               MS_rep.addData('ROI_RIGHT_MS.timesOn', ROI_RIGHT_MS.timesOn)
               MS_rep.addData('ROI_RIGHT_MS.timesOff', ROI_RIGHT_MS.timesOff)
            else:
               MS_rep.addData('ROI_RIGHT_MS.timesOn', "")
               MS_rep.addData('ROI_RIGHT_MS.timesOff', "")
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-15.100000)
            
            # --- Prepare to start Routine "pressspace" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            Next_text.reset()
            # setup some python lists for storing info about the Next_mouse
            Next_mouse.clicked_name = []
            gotValidClick = False  # until a click is received
            key_resp_2.keys = []
            key_resp_2.rt = []
            _key_resp_2_allKeys = []
            # keep track of which components have finished
            pressspaceComponents = [Next_text, Next_polygon, Next_mouse, key_resp_2]
            for thisComponent in pressspaceComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "pressspace" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Next_text* updates
                if Next_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Next_text.frameNStart = frameN  # exact frame index
                    Next_text.tStart = t  # local t and not account for scr refresh
                    Next_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Next_text, 'tStartRefresh')  # time at next scr refresh
                    Next_text.setAutoDraw(True)
                
                # *Next_polygon* updates
                if Next_polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Next_polygon.frameNStart = frameN  # exact frame index
                    Next_polygon.tStart = t  # local t and not account for scr refresh
                    Next_polygon.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Next_polygon, 'tStartRefresh')  # time at next scr refresh
                    Next_polygon.setAutoDraw(True)
                # *Next_mouse* updates
                if Next_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Next_mouse.frameNStart = frameN  # exact frame index
                    Next_mouse.tStart = t  # local t and not account for scr refresh
                    Next_mouse.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Next_mouse, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.addData('Next_mouse.started', t)
                    Next_mouse.status = STARTED
                    prevButtonState = Next_mouse.getPressed()  # if button is down already this ISN'T a new click
                if Next_mouse.status == STARTED:  # only update if started and not finished!
                    buttons = Next_mouse.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            try:
                                iter(Next_polygon)
                                clickableList = Next_polygon
                            except:
                                clickableList = [Next_polygon]
                            for obj in clickableList:
                                if obj.contains(Next_mouse):
                                    gotValidClick = True
                                    Next_mouse.clicked_name.append(obj.name)
                            if gotValidClick:  
                                continueRoutine = False  # abort routine on response
                
                # *key_resp_2* updates
                if key_resp_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_2.frameNStart = frameN  # exact frame index
                    key_resp_2.tStart = t  # local t and not account for scr refresh
                    key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                    key_resp_2.status = STARTED
                    # keyboard checking is just starting
                    key_resp_2.clock.reset()  # now t=0
                if key_resp_2.status == STARTED:
                    theseKeys = key_resp_2.getKeys(keyList=['p'], waitRelease=False)
                    _key_resp_2_allKeys.extend(theseKeys)
                    if len(_key_resp_2_allKeys):
                        key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                        key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in pressspaceComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "pressspace" ---
            for thisComponent in pressspaceComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store data for MS_rep (TrialHandler)
            x, y = Next_mouse.getPos()
            buttons = Next_mouse.getPressed()
            if sum(buttons):
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(Next_polygon)
                    clickableList = Next_polygon
                except:
                    clickableList = [Next_polygon]
                for obj in clickableList:
                    if obj.contains(Next_mouse):
                        gotValidClick = True
                        Next_mouse.clicked_name.append(obj.name)
            MS_rep.addData('Next_mouse.x', x)
            MS_rep.addData('Next_mouse.y', y)
            MS_rep.addData('Next_mouse.leftButton', buttons[0])
            MS_rep.addData('Next_mouse.midButton', buttons[1])
            MS_rep.addData('Next_mouse.rightButton', buttons[2])
            if len(Next_mouse.clicked_name):
                MS_rep.addData('Next_mouse.clicked_name', Next_mouse.clicked_name[0])
            # the Routine "pressspace" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'MS_rep'
        
        # get names of stimulus parameters
        if MS_rep.trialList in ([], [None], None):
            params = []
        else:
            params = MS_rep.trialList[0].keys()
        # save data for this loop
        MS_rep.saveAsExcel(filename + '.xlsx', sheetName='MS_rep',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        thisExp.nextEntry()
        
    # completed MS_repeat repeats of 'E'
    
    # get names of stimulus parameters
    if E.trialList in ([], [None], None):
        params = []
    else:
        params = E.trialList[0].keys()
    # save data for this loop
    E.saveAsExcel(filename + '.xlsx', sheetName='E',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
# completed 1.0 repeats of 'trials'


# --- Prepare to start Routine "bye" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# setup some python lists for storing info about the mouse
gotValidClick = False  # until a click is received
# keep track of which components have finished
byeComponents = [text_2, mouse]
for thisComponent in byeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "bye" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_2.started')
        text_2.setAutoDraw(True)
    # *mouse* updates
    if mouse.status == NOT_STARTED and t >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        mouse.frameNStart = frameN  # exact frame index
        mouse.tStart = t  # local t and not account for scr refresh
        mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mouse.started', t)
        mouse.status = STARTED
        prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
    if mouse.status == STARTED:  # only update if started and not finished!
        buttons = mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                continueRoutine = False  # abort routine on response    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in byeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "bye" ---
for thisComponent in byeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
x, y = mouse.getPos()
buttons = mouse.getPressed()
thisExp.addData('mouse.x', x)
thisExp.addData('mouse.y', y)
thisExp.addData('mouse.leftButton', buttons[0])
thisExp.addData('mouse.midButton', buttons[1])
thisExp.addData('mouse.rightButton', buttons[2])
thisExp.nextEntry()
# the Routine "bye" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
