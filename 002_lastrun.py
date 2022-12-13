#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.7),
    on 11月 15, 2019, at 12:53
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.0.7'
expName = '001'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
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
    originPath='D:\\experiment_set_for_handai\\002_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "inst"
instClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='この実験は，人の顔に対する印象がどのような要因によって決まるかを調べるものです．\nお答えいただいたデータは，すべて匿名で処理され，個人が特定されることはありません．\n正しい回答はありませんので，自分の直感に従って，ありのままにお答えください．',
    font='Arial',
    units='pix', pos=(0, 0), height=20, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "practice_instruction"
practice_instructionClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='画面に顔画像が表示されますので，その都度5段階で「かわいさ」を評価してください．評価の選択はマウスで行ってください．\n\u3000全部で60回評価していただきます．ただし最初の10回は練習です．\n個人差はありますが，全部で15分以内に終わります．\n途中から画像の表示に時間がかかることありますが，コンピュータでの計算に時間がかかっているためです．\n表示が遅い場合はそのままお待ち下さい． \n\nSpaceキーを押すと始まります。',
    font='Arial',
    units='pix', pos=(0, 0), height=20, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
import csv
from numpy import random
from ego.stimulation.face import random_gallery, ucb_gallery

Path = 'image_data/000/000.bmp'

practice_count_num = 1
PRACTICE_NUM = 10
practice_most_gallery = []
practice_result = []

count_num= -PRACTICE_NUM + 1
LOOP_NUM = 60
RANDOM_NUM = 30

response = []
result = []
result_index = []
start = 0.2
end = 0.2
image_1 = visual.ImageStim(
    win=win,
    name='image_1', units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(600, 600),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text_1 = visual.TextStim(win=win, name='text_1',
    text='default text',
    font='Arial',
    units='pix', pos=(-150, 350), height=32, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
ISI = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
slider = visual.Slider(win=win, name='slider',
    size=(0.5, 0.05), pos=(0, -0.7),
    labels=[1,2,3,4,5], ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating', 'triangleMarker'],
    color='LightGray', font='HelveticaBold',
    flip=False)
text_3 = visual.TextStim(win=win, name='text_3',
    text='非常にかわいい',
    font='Arial',
    units='pix', pos=(800, -390), height=18, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
text_4 = visual.TextStim(win=win, name='text_4',
    text='全くかわいくない',
    font='Arial',
    units='pix', pos=(60, -390), height=18, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
image = visual.ImageStim(
    win=win,
    name='image', units='pix', 
    image='koushinchu.png', mask=None,
    ori=0, pos=(0, 0), size=(1500, 1000),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)

# Initialize components for Routine "instruction"
instructionClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Spaceキーを押すと始まります．',
    font='Arial',
    units='pix', pos=(0, 0), height=18, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
import csv
from numpy import random
from ego.stimulation.face import random_gallery, ucb_gallery

Path = 'image_data/000/000.bmp'

practice_count_num = 1
PRACTICE_NUM = 10
practice_most_gallery = []
practice_result = []

count_num= -PRACTICE_NUM + 1
LOOP_NUM = 60
RANDOM_NUM = 30

response = []
result = []
result_index = []
start = 0.2
end = 0.2
image_1 = visual.ImageStim(
    win=win,
    name='image_1', units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(600, 600),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text_1 = visual.TextStim(win=win, name='text_1',
    text='default text',
    font='Arial',
    units='pix', pos=(-150, 350), height=32, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
ISI = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
slider = visual.Slider(win=win, name='slider',
    size=(0.5, 0.05), pos=(0, -0.7),
    labels=[1,2,3,4,5], ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating', 'triangleMarker'],
    color='LightGray', font='HelveticaBold',
    flip=False)
text_3 = visual.TextStim(win=win, name='text_3',
    text='非常にかわいい',
    font='Arial',
    units='pix', pos=(800, -390), height=18, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
text_4 = visual.TextStim(win=win, name='text_4',
    text='全くかわいくない',
    font='Arial',
    units='pix', pos=(60, -390), height=18, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
image = visual.ImageStim(
    win=win,
    name='image', units='pix', 
    image='koushinchu.png', mask=None,
    ori=0, pos=(0, 0), size=(1500, 1000),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "inst"-------
t = 0
instClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(6.000000)
# update component parameters for each repeat
# keep track of which components have finished
instComponents = [text_5]
for thisComponent in instComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "inst"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = instClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_5* updates
    if t >= 0.0 and text_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_5.tStart = t
        text_5.frameNStart = frameN  # exact frame index
        text_5.setAutoDraw(True)
    frameRemains = 0.0 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_5.status == STARTED and t >= frameRemains:
        text_5.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "inst"-------
for thisComponent in instComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "practice_instruction"-------
t = 0
practice_instructionClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse()
# keep track of which components have finished
practice_instructionComponents = [text, key_resp_3]
for thisComponent in practice_instructionComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "practice_instruction"-------
while continueRoutine:
    # get current time
    t = practice_instructionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    
    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practice_instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practice_instruction"-------
for thisComponent in practice_instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "practice_instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practices = data.TrialHandler(nReps=PRACTICE_NUM, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='practices')
thisExp.addLoop(practices)  # add the loop to the experiment
thisPractice = practices.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
if thisPractice != None:
    for paramName in thisPractice:
        exec('{} = thisPractice[paramName]'.format(paramName))

for thisPractice in practices:
    currentLoop = practices
    # abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
    if thisPractice != None:
        for paramName in thisPractice:
            exec('{} = thisPractice[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    if practice_count_num <= PRACTICE_NUM:
        gallery, index = random_gallery()
        if index[0] <= 9:
            index[0] = '00' + str(index[0])
        elif index[0] <= 99:
            index[0] = '0' + str(index[0])
        else:
            index[0] = str(index[0])
    
        if index[1] <= 9:
            index[1] = '00' + str(index[1])
        elif index[1] <= 99:
            index[1] = '0' + str(index[1])
        else:
            index[1] = str(index[1])
    
        if index[2] <= 9:
            index[2] = '00' + str(index[2])
        elif index[2] <= 99:
            index[2] = '0' + str(index[2])
        else:
            index[2] = str(index[2])
    
        Path = 'image_data/' + index[0] + '/' + index[1] + '/' + index[2] +'.bmp'
        end = 1.0
    elif count_num <= RANDOM_NUM:
        gallery, index = random_gallery()
        result.append(gallery)
        if index[0] <= 9:
            index[0] = '00' + str(index[0])
        elif index[0] <= 99:
            index[0] = '0' + str(index[0])
        else:
            index[0] = str(index[0])
    
        if index[1] <= 9:
            index[1] = '00' + str(index[1])
        elif index[1] <= 99:
            index[1] = '0' + str(index[1])
        else:
            index[1] = str(index[1])
    
        if index[2] <= 9:
            index[2] = '00' + str(index[2])
        elif index[2] <= 99:
            index[2] = '0' + str(index[2])
        else:
            index[2] = str(index[2])
    
        Path = 'image_data/' + index[0] + '/' + index[1] + '/' + index[2] +'.bmp'
        result_index.append(index)
        end = 1.0
    else:
        gallery, index = ucb_gallery(result, response)
        result.append(gallery)
    
        if index[0] <= 9:
            index[0] = '00' + str(index[0])
        elif index[0] <= 99:
            index[0] = '0' + str(index[0])
        else:
            index[0] = str(index[0])
    
        if index[1] <= 9:
            index[1] = '00' + str(index[1])
        elif index[1] <= 99:
            index[1] = '0' + str(index[1])
        else:
            index[1] = str(index[1])
    
        if index[2] <= 9:
            index[2] = '00' + str(index[2])
        elif index[2] <= 99:
            index[2] = '0' + str(index[2])
        else:
            index[2] = str(index[2])
    
        Path = 'image_data/' + index[0] + '/' + index[1] + '/' + index[2] +'.bmp'
        result_index.append(index)
        start = 0.0
        end = 1.5
    if practice_count_num <= PRACTICE_NUM:
        pass
    elif count_num <= LOOP_NUM:
        response.append(slider.getRating())
    else:
        pass
    text_1.setText(count_num)
    slider.reset()
    # keep track of which components have finished
    trialComponents = [image_1, text_1, ISI, slider, text_3, text_4, image]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_1* updates
        if t >= 0.2 and image_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_1.tStart = t
            image_1.frameNStart = frameN  # exact frame index
            image_1.setAutoDraw(True)
        
        # *text_1* updates
        if t >= 0.2 and text_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_1.tStart = t
            text_1.frameNStart = frameN  # exact frame index
            text_1.setAutoDraw(True)
        
        # *slider* updates
        if t >= 0.2 and slider.status == NOT_STARTED:
            # keep track of start time/frame for later
            slider.tStart = t
            slider.frameNStart = frameN  # exact frame index
            slider.setAutoDraw(True)
        
        # Check slider for response to end routine
        if slider.getRating() is not None and slider.status == STARTED:
            continueRoutine = False
        
        # *text_3* updates
        if t >= 0.2 and text_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_3.tStart = t
            text_3.frameNStart = frameN  # exact frame index
            text_3.setAutoDraw(True)
        
        # *text_4* updates
        if t >= 0.2 and text_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_4.tStart = t
            text_4.frameNStart = frameN  # exact frame index
            text_4.setAutoDraw(True)
        
        # *image* updates
        if (slider.rt != 0) and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        if image.status == STARTED and t >= (image.tStart + end):
            image.setAutoDraw(False)
        # *ISI* period
        if t >= 0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(0.2)
        elif ISI.status == STARTED:  # one frame should pass before updating params and completing
            # updating other components during *ISI*
            image_1.setImage(Path)
            # component updates done
            ISI.complete()  # finish the static period
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice_count_num += 1
    count_num += 1
    practices.addData('slider.response', slider.getRating())
    practices.addData('slider.rt', slider.getRT())
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed PRACTICE_NUM repeats of 'practices'


# ------Prepare to start Routine "instruction"-------
t = 0
instructionClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()
# keep track of which components have finished
instructionComponents = [text_2, key_resp_2]
for thisComponent in instructionComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instruction"-------
while continueRoutine:
    # get current time
    t = instructionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction"-------
for thisComponent in instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=LOOP_NUM, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
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
    
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    if practice_count_num <= PRACTICE_NUM:
        gallery, index = random_gallery()
        if index[0] <= 9:
            index[0] = '00' + str(index[0])
        elif index[0] <= 99:
            index[0] = '0' + str(index[0])
        else:
            index[0] = str(index[0])
    
        if index[1] <= 9:
            index[1] = '00' + str(index[1])
        elif index[1] <= 99:
            index[1] = '0' + str(index[1])
        else:
            index[1] = str(index[1])
    
        if index[2] <= 9:
            index[2] = '00' + str(index[2])
        elif index[2] <= 99:
            index[2] = '0' + str(index[2])
        else:
            index[2] = str(index[2])
    
        Path = 'image_data/' + index[0] + '/' + index[1] + '/' + index[2] +'.bmp'
        end = 1.0
    elif count_num <= RANDOM_NUM:
        gallery, index = random_gallery()
        result.append(gallery)
        if index[0] <= 9:
            index[0] = '00' + str(index[0])
        elif index[0] <= 99:
            index[0] = '0' + str(index[0])
        else:
            index[0] = str(index[0])
    
        if index[1] <= 9:
            index[1] = '00' + str(index[1])
        elif index[1] <= 99:
            index[1] = '0' + str(index[1])
        else:
            index[1] = str(index[1])
    
        if index[2] <= 9:
            index[2] = '00' + str(index[2])
        elif index[2] <= 99:
            index[2] = '0' + str(index[2])
        else:
            index[2] = str(index[2])
    
        Path = 'image_data/' + index[0] + '/' + index[1] + '/' + index[2] +'.bmp'
        result_index.append(index)
        end = 1.0
    else:
        gallery, index = ucb_gallery(result, response)
        result.append(gallery)
    
        if index[0] <= 9:
            index[0] = '00' + str(index[0])
        elif index[0] <= 99:
            index[0] = '0' + str(index[0])
        else:
            index[0] = str(index[0])
    
        if index[1] <= 9:
            index[1] = '00' + str(index[1])
        elif index[1] <= 99:
            index[1] = '0' + str(index[1])
        else:
            index[1] = str(index[1])
    
        if index[2] <= 9:
            index[2] = '00' + str(index[2])
        elif index[2] <= 99:
            index[2] = '0' + str(index[2])
        else:
            index[2] = str(index[2])
    
        Path = 'image_data/' + index[0] + '/' + index[1] + '/' + index[2] +'.bmp'
        result_index.append(index)
        start = 0.0
        end = 1.5
    if practice_count_num <= PRACTICE_NUM:
        pass
    elif count_num <= LOOP_NUM:
        response.append(slider.getRating())
    else:
        pass
    text_1.setText(count_num)
    slider.reset()
    # keep track of which components have finished
    trialComponents = [image_1, text_1, ISI, slider, text_3, text_4, image]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_1* updates
        if t >= 0.2 and image_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_1.tStart = t
            image_1.frameNStart = frameN  # exact frame index
            image_1.setAutoDraw(True)
        
        # *text_1* updates
        if t >= 0.2 and text_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_1.tStart = t
            text_1.frameNStart = frameN  # exact frame index
            text_1.setAutoDraw(True)
        
        # *slider* updates
        if t >= 0.2 and slider.status == NOT_STARTED:
            # keep track of start time/frame for later
            slider.tStart = t
            slider.frameNStart = frameN  # exact frame index
            slider.setAutoDraw(True)
        
        # Check slider for response to end routine
        if slider.getRating() is not None and slider.status == STARTED:
            continueRoutine = False
        
        # *text_3* updates
        if t >= 0.2 and text_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_3.tStart = t
            text_3.frameNStart = frameN  # exact frame index
            text_3.setAutoDraw(True)
        
        # *text_4* updates
        if t >= 0.2 and text_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_4.tStart = t
            text_4.frameNStart = frameN  # exact frame index
            text_4.setAutoDraw(True)
        
        # *image* updates
        if (slider.rt != 0) and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        if image.status == STARTED and t >= (image.tStart + end):
            image.setAutoDraw(False)
        # *ISI* period
        if t >= 0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(0.2)
        elif ISI.status == STARTED:  # one frame should pass before updating params and completing
            # updating other components during *ISI*
            image_1.setImage(Path)
            # component updates done
            ISI.complete()  # finish the static period
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice_count_num += 1
    count_num += 1
    trials.addData('slider.response', slider.getRating())
    trials.addData('slider.rt', slider.getRT())
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed LOOP_NUM repeats of 'trials'

with open(filename + '_result.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(result)
f.close()

with open(filename + '_response.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(response)
f.close()

with open(filename + '_result_index.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(result_index)
f.close()
with open(filename + '_result.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(result)
f.close()

with open(filename + '_response.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(response)
f.close()

with open(filename + '_result_index.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(result_index)
f.close()
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
