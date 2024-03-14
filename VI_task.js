/************** 
 * Pilot Test *
 **************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2022.2.4.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'Pilot';  // from the Builder filename that created this script
let expInfo = {
    'participant': '',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([1.0, 1.0, 1.0]),
  units: 'height',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(helloRoutineBegin());
flowScheduler.add(helloRoutineEachFrame());
flowScheduler.add(helloRoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(byeRoutineBegin());
flowScheduler.add(byeRoutineEachFrame());
flowScheduler.add(byeRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'Stimuli/Ebbinghaus trials/100b_99b_R.png', 'path': 'Stimuli/Ebbinghaus trials/100b_99b_R.png'},
    {'name': 'Stimuli/Kanizsa trials/Kanizsa 50b.png', 'path': 'Stimuli/Kanizsa trials/Kanizsa 50b.png'},
    {'name': 'Stimuli/Instructions/ML_short.ogg', 'path': 'Stimuli/Instructions/ML_short.ogg'},
    {'name': 'Stimuli/Training/triang.png', 'path': 'Stimuli/Training/triang.png'},
    {'name': 'Stimuli/Contrast trials/DD_45_55_R.png', 'path': 'Stimuli/Contrast trials/DD_45_55_R.png'},
    {'name': 'Stimuli/Instructions/CT_short.ogg', 'path': 'Stimuli/Instructions/CT_short.ogg'},
    {'name': 'Stimuli/Müller-Lyer trials/100ow_85ow.png', 'path': 'Stimuli/Müller-Lyer trials/100ow_85ow.png'},
    {'name': 'Stimuli/randomblock.xlsx', 'path': 'Stimuli/randomblock.xlsx'},
    {'name': 'Stimuli/Ebbinghaus trials/100s_99s.png', 'path': 'Stimuli/Ebbinghaus trials/100s_99s.png'},
    {'name': 'Stimuli/Kanizsa trials/Kanizsa 50e_R.png', 'path': 'Stimuli/Kanizsa trials/Kanizsa 50e_R.png'},
    {'name': 'Stimuli/Kanizsa trials/Kanizsa 10d.png', 'path': 'Stimuli/Kanizsa trials/Kanizsa 10d.png'},
    {'name': 'Stimuli/Training/whitesquare3p4.png', 'path': 'Stimuli/Training/whitesquare3p4.png'},
    {'name': 'Stimuli/Müller-Lyer trials/100iw_70ow.png', 'path': 'Stimuli/Müller-Lyer trials/100iw_70ow.png'},
    {'name': 'Stimuli/Moving snake trials/moving snake 2_5_mirror.png', 'path': 'Stimuli/Moving snake trials/moving snake 2_5_mirror.png'},
    {'name': 'Stimuli/Contrast trials/DD_50_51.png', 'path': 'Stimuli/Contrast trials/DD_50_51.png'},
    {'name': 'Stimuli/Kanizsa trials/Kanizsa 20e.png', 'path': 'Stimuli/Kanizsa trials/Kanizsa 20e.png'},
    {'name': 'Stimuli/Müller-Lyer trials/100iw_70iw_R.png', 'path': 'Stimuli/Müller-Lyer trials/100iw_70iw_R.png'},
    {'name': 'Stimuli/Moving snake trials/moving snake 3_5_mirror.png', 'path': 'Stimuli/Moving snake trials/moving snake 3_5_mirror.png'},
    {'name': 'Stimuli/Moving snake trials/moving snake 3_4.png', 'path': 'Stimuli/Moving snake trials/moving snake 3_4.png'},
    {'name': 'Stimuli/Contrast trials/D49_L51.png', 'path': 'Stimuli/Contrast trials/D49_L51.png'},
    {'name': 'Stimuli/Moving snake trials/moving snake 1_5.png', 'path': 'Stimuli/Moving snake trials/moving snake 1_5.png'},
    {'name': 'Stimuli/Müller-Lyer trials/100ow_95ow.png', 'path': 'Stimuli/Müller-Lyer trials/100ow_95ow.png'},
    {'name': 'Stimuli/Contrast trials/D48_L52_R.png', 'path': 'Stimuli/Contrast trials/D48_L52_R.png'},
    {'name': 'Stimuli/Ebbinghaus trials/100s_70b_R.png', 'path': 'Stimuli/Ebbinghaus trials/100s_70b_R.png'},
    {'name': 'Stimuli/Müller-Lyer trials/100ow_70iw_R.png', 'path': 'Stimuli/Müller-Lyer trials/100ow_70iw_R.png'},
    {'name': 'Stimuli/Moving snake trials/MS_condition_file .xlsx', 'path': 'Stimuli/Moving snake trials/MS_condition_file .xlsx'},
    {'name': 'Stimuli/Müller-Lyer trials/100ow_80ow.png', 'path': 'Stimuli/Müller-Lyer trials/100ow_80ow.png'},
    {'name': 'Stimuli/Müller-Lyer trials/100ow_90iw_R.png', 'path': 'Stimuli/Müller-Lyer trials/100ow_90iw_R.png'},
    {'name': 'Stimuli/Müller-Lyer trials/100iw_80ow.png', 'path': 'Stimuli/Müller-Lyer trials/100iw_80ow.png'},
    {'name': 'Stimuli/Müller-Lyer trials/100iw_99ow.png', 'path': 'Stimuli/Müller-Lyer trials/100iw_99ow.png'},
    {'name': 'Stimuli/Ebbinghaus trials/100b_70s.png', 'path': 'Stimuli/Ebbinghaus trials/100b_70s.png'},
    {'name': 'Stimuli/Contrast trials/DD_47_53_R.png', 'path': 'Stimuli/Contrast trials/DD_47_53_R.png'},
    {'name': 'Stimuli/Instructions/CT_long.ogg', 'path': 'Stimuli/Instructions/CT_long.ogg'},
    {'name': 'Stimuli/Contrast trials/DD_47_53.png', 'path': 'Stimuli/Contrast trials/DD_47_53.png'},
    {'name': 'Stimuli/Müller-Lyer trials/100iw_80iw_R.png', 'path': 'Stimuli/Müller-Lyer trials/100iw_80iw_R.png'},
    {'name': 'Stimuli/Training/whitesquare2p4.png', 'path': 'Stimuli/Training/whitesquare2p4.png'},
    {'name': 'Stimuli/Contrast trials/DD_49_51_R.png', 'path': 'Stimuli/Contrast trials/DD_49_51_R.png'},
    {'name': 'Stimuli/Ebbinghaus trials/100b_85s.png', 'path': 'Stimuli/Ebbinghaus trials/100b_85s.png'},
    {'name': 'Stimuli/Müller-Lyer trials/100ow_95iw_R.png', 'path': 'Stimuli/Müller-Lyer trials/100ow_95iw_R.png'},
    {'name': 'Stimuli/Kanizsa trials/Kanizsa 10b.png', 'path': 'Stimuli/Kanizsa trials/Kanizsa 10b.png'},
    {'name': 'Stimuli/Müller-Lyer trials/100iw_85ow.png', 'path': 'Stimuli/Müller-Lyer trials/100iw_85ow.png'},
    {'name': 'Stimuli/Kanizsa trials/Kanizsa 20b_R.png', 'path': 'Stimuli/Kanizsa trials/Kanizsa 20b_R.png'},
    {'name': 'Stimuli/Kanizsa trials/Kanizsa 10a_R.png', 'path': 'Stimuli/Kanizsa trials/Kanizsa 10a_R.png'},
    {'name': 'Stimuli/Ebbinghaus trials/100b_90s.png', 'path': 'Stimuli/Ebbinghaus trials/100b_90s.png'},
    {'name': 'Stimuli/Ebbinghaus trials/100s_85s.png', 'path': 'Stimuli/Ebbinghaus trials/100s_85s.png'},
    {'name': 'Stimuli/Moving snake trials/moving snake 1_3.png', 'path': 'Stimuli/Moving snake trials/moving snake 1_3.png'},
    {'name': 'Stimuli/Moving snake trials/moving snake 1_4_mirror.png', 'path': 'Stimuli/Moving snake trials/moving snake 1_4_mirror.png'},
    {'name': 'Stimuli/Kanizsa trials/Kanizsa 50a_R.png', 'path': 'Stimuli/Kanizsa trials/Kanizsa 50a_R.png'},
    {'name': 'Stimuli/Moving snake trials/moving snake 2_4.png', 'path': 'Stimuli/Moving snake trials/moving snake 2_4.png'},
    {'name': 'Stimuli/Kanizsa trials/Kanizsa 40a.png', 'path': 'Stimuli/Kanizsa trials/Kanizsa 40a.png'},
    {'name': 'Stimuli/Contrast trials/DD_45_55.png', 'path': 'Stimuli/Contrast trials/DD_45_55.png'},
    {'name': 'Stimuli/Ebbinghaus trials/100b_95b_R.png', 'path': 'Stimuli/Ebbinghaus trials/100b_95b_R.png'},
    {'name': 'Stimuli/Kanizsa trials/Kanizsa 10c_R.png', 'path': 'Stimuli/Kanizsa trials/Kanizsa 10c_R.png'},
    {'name': 'Stimuli/Kanizsa trials/Kanizsa 30c_R.png', 'path': 'Stimuli/Kanizsa trials/Kanizsa 30c_R.png'},
    {'name': 'Stimuli/Instructions/EB_short.ogg', 'path': 'Stimuli/Instructions/EB_short.ogg'},
    {'name': 'Stimuli/Müller-Lyer trials/ML_condition_file.xlsx', 'path': 'Stimuli/Müller-Lyer trials/ML_condition_file.xlsx'},
    {'name': 'Stimuli/Instructions/KZS_short.ogg', 'path': 'Stimuli/Instructions/KZS_short.ogg'},
    {'name': 'Stimuli/Ebbinghaus trials/100s_95b_R.png', 'path': 'Stimuli/Ebbinghaus trials/100s_95b_R.png'},
    {'name': 'Stimuli/Contrast trials/D47_L53_R.png', 'path': 'Stimuli/Contrast trials/D47_L53_R.png'},
    {'name': 'Stimuli/Moving snake trials/moving snake 4_5.png', 'path': 'Stimuli/Moving snake trials/moving snake 4_5.png'},
    {'name': 'Stimuli/Contrast trials/D50_L51_R.png', 'path': 'Stimuli/Contrast trials/D50_L51_R.png'},
    {'name': 'Stimuli/Müller-Lyer trials/100iw_90iw_R.png', 'path': 'Stimuli/Müller-Lyer trials/100iw_90iw_R.png'},
    {'name': 'Stimuli/Kanizsa trials/Kanizsa 30b.png', 'path': 'Stimuli/Kanizsa trials/Kanizsa 30b.png'},
    {'name': 'Stimuli/Training/whitesquare.png', 'path': 'Stimuli/Training/whitesquare.png'},
    {'name': 'Stimuli/Ebbinghaus trials/100s_80s.png', 'path': 'Stimuli/Ebbinghaus trials/100s_80s.png'},
    {'name': 'Stimuli/Ebbinghaus trials/100s_80b_R.png', 'path': 'Stimuli/Ebbinghaus trials/100s_80b_R.png'},
    {'name': 'Stimuli/Contrast trials/D45_L55.png', 'path': 'Stimuli/Contrast trials/D45_L55.png'},
    {'name': 'Stimuli/Ebbinghaus trials/100b_95s.png', 'path': 'Stimuli/Ebbinghaus trials/100b_95s.png'},
    {'name': 'Stimuli/Contrast trials/DD_49_51.png', 'path': 'Stimuli/Contrast trials/DD_49_51.png'},
    {'name': 'Stimuli/Ebbinghaus trials/100s_90b_R.png', 'path': 'Stimuli/Ebbinghaus trials/100s_90b_R.png'},
    {'name': 'Stimuli/Ebbinghaus trials/100s_95s.png', 'path': 'Stimuli/Ebbinghaus trials/100s_95s.png'},
    {'name': 'Stimuli/Müller-Lyer trials/100ow_99ow.png', 'path': 'Stimuli/Müller-Lyer trials/100ow_99ow.png'},
    {'name': 'Stimuli/Kanizsa trials/Kanizsa 20d_R.png', 'path': 'Stimuli/Kanizsa trials/Kanizsa 20d_R.png'},
    {'name': 'Stimuli/Contrast trials/D49_L51_R.png', 'path': 'Stimuli/Contrast trials/D49_L51_R.png'},
    {'name': 'Stimuli/Kanizsa trials/Kanizsa 40b_R.png', 'path': 'Stimuli/Kanizsa trials/Kanizsa 40b_R.png'},
    {'name': 'Stimuli/Ebbinghaus trials/100b_99s.png', 'path': 'Stimuli/Ebbinghaus trials/100b_99s.png'},
    {'name': 'Stimuli/Kanizsa trials/Kanizsa 50d.png', 'path': 'Stimuli/Kanizsa trials/Kanizsa 50d.png'},
    {'name': 'Stimuli/Instructions/EB_long.ogg', 'path': 'Stimuli/Instructions/EB_long.ogg'},
    {'name': 'Stimuli/Kanizsa trials/Kanizsa 40c.png', 'path': 'Stimuli/Kanizsa trials/Kanizsa 40c.png'},
    {'name': 'Stimuli/Müller-Lyer trials/100ow_70ow.png', 'path': 'Stimuli/Müller-Lyer trials/100ow_70ow.png'},
    {'name': 'Stimuli/Müller-Lyer trials/100ow_90ow.png', 'path': 'Stimuli/Müller-Lyer trials/100ow_90ow.png'},
    {'name': 'Stimuli/Müller-Lyer trials/100ow_99iw_R.png', 'path': 'Stimuli/Müller-Lyer trials/100ow_99iw_R.png'},
    {'name': 'Stimuli/Contrast trials/DD_48_52.png', 'path': 'Stimuli/Contrast trials/DD_48_52.png'},
    {'name': 'Stimuli/Müller-Lyer trials/100iw_85iw_R.png', 'path': 'Stimuli/Müller-Lyer trials/100iw_85iw_R.png'},
    {'name': 'Stimuli/Ebbinghaus trials/100b_70b_R.png', 'path': 'Stimuli/Ebbinghaus trials/100b_70b_R.png'},
    {'name': 'Stimuli/Müller-Lyer trials/100iw_95ow.png', 'path': 'Stimuli/Müller-Lyer trials/100iw_95ow.png'},
    {'name': 'Stimuli/Contrast trials/Contrast_condition_file.xlsx', 'path': 'Stimuli/Contrast trials/Contrast_condition_file.xlsx'},
    {'name': 'Stimuli/Ebbinghaus trials/Ebbinghaus_condition_file.xlsx', 'path': 'Stimuli/Ebbinghaus trials/Ebbinghaus_condition_file.xlsx'},
    {'name': 'Stimuli/Kanizsa trials/Kanizsa 40e.png', 'path': 'Stimuli/Kanizsa trials/Kanizsa 40e.png'},
    {'name': 'Stimuli/Kanizsa trials/Kanizsa 20c.png', 'path': 'Stimuli/Kanizsa trials/Kanizsa 20c.png'},
    {'name': 'Stimuli/Kanizsa trials/Kanizsa 30e_R.png', 'path': 'Stimuli/Kanizsa trials/Kanizsa 30e_R.png'},
    {'name': 'Stimuli/Ebbinghaus trials/100s_99b_R.png', 'path': 'Stimuli/Ebbinghaus trials/100s_99b_R.png'},
    {'name': 'Stimuli/Müller-Lyer trials/100iw_95iw_R.png', 'path': 'Stimuli/Müller-Lyer trials/100iw_95iw_R.png'},
    {'name': 'Stimuli/Ebbinghaus trials/100b_85b_R.png', 'path': 'Stimuli/Ebbinghaus trials/100b_85b_R.png'},
    {'name': 'Stimuli/Müller-Lyer trials/100ow_85iw_R.png', 'path': 'Stimuli/Müller-Lyer trials/100ow_85iw_R.png'},
    {'name': 'Stimuli/Ebbinghaus trials/100s_70s.png', 'path': 'Stimuli/Ebbinghaus trials/100s_70s.png'},
    {'name': 'Stimuli/Müller-Lyer trials/100ow_80iw_R.png', 'path': 'Stimuli/Müller-Lyer trials/100ow_80iw_R.png'},
    {'name': 'Stimuli/Contrast trials/D47_L53.png', 'path': 'Stimuli/Contrast trials/D47_L53.png'},
    {'name': 'Stimuli/Contrast trials/DD_48_52_R.png', 'path': 'Stimuli/Contrast trials/DD_48_52_R.png'},
    {'name': 'Stimuli/Instructions/ML_long.ogg', 'path': 'Stimuli/Instructions/ML_long.ogg'},
    {'name': 'Stimuli/Contrast trials/DD_50_51_R.png', 'path': 'Stimuli/Contrast trials/DD_50_51_R.png'},
    {'name': 'Stimuli/Kanizsa trials/KN_condition_file.xlsx', 'path': 'Stimuli/Kanizsa trials/KN_condition_file.xlsx'},
    {'name': 'Stimuli/Ebbinghaus trials/100s_90s.png', 'path': 'Stimuli/Ebbinghaus trials/100s_90s.png'},
    {'name': 'Stimuli/Kanizsa trials/Kanizsa 40d_R.png', 'path': 'Stimuli/Kanizsa trials/Kanizsa 40d_R.png'},
    {'name': 'Stimuli/Contrast trials/D48_L52.png', 'path': 'Stimuli/Contrast trials/D48_L52.png'},
    {'name': 'Stimuli/Instructions/KZS_long.ogg', 'path': 'Stimuli/Instructions/KZS_long.ogg'},
    {'name': 'Stimuli/Instructions/MS_short.ogg', 'path': 'Stimuli/Instructions/MS_short.ogg'},
    {'name': 'Stimuli/Ebbinghaus trials/100b_80s.png', 'path': 'Stimuli/Ebbinghaus trials/100b_80s.png'},
    {'name': 'Stimuli/Instructions/Instrucción inicial2.ogg', 'path': 'Stimuli/Instructions/Instrucción inicial2.ogg'},
    {'name': 'Stimuli/Ebbinghaus trials/100b_90b_R.png', 'path': 'Stimuli/Ebbinghaus trials/100b_90b_R.png'},
    {'name': 'Stimuli/Moving snake trials/moving snake 1_2_mirror.png', 'path': 'Stimuli/Moving snake trials/moving snake 1_2_mirror.png'},
    {'name': 'Stimuli/Ebbinghaus trials/100b_80b_R.png', 'path': 'Stimuli/Ebbinghaus trials/100b_80b_R.png'},
    {'name': 'Stimuli/Müller-Lyer trials/100iw_90ow.png', 'path': 'Stimuli/Müller-Lyer trials/100iw_90ow.png'},
    {'name': 'Stimuli/Kanizsa trials/Kanizsa 30d.png', 'path': 'Stimuli/Kanizsa trials/Kanizsa 30d.png'},
    {'name': 'Stimuli/Kanizsa trials/Kanizsa 20a.png', 'path': 'Stimuli/Kanizsa trials/Kanizsa 20a.png'},
    {'name': 'Stimuli/Müller-Lyer trials/100iw_99iw_R.png', 'path': 'Stimuli/Müller-Lyer trials/100iw_99iw_R.png'},
    {'name': 'Stimuli/Contrast trials/D45_L55_R.png', 'path': 'Stimuli/Contrast trials/D45_L55_R.png'},
    {'name': 'Stimuli/Kanizsa trials/Kanizsa 50c_R.png', 'path': 'Stimuli/Kanizsa trials/Kanizsa 50c_R.png'},
    {'name': 'Stimuli/Moving snake trials/moving snake 2_3_mirror.png', 'path': 'Stimuli/Moving snake trials/moving snake 2_3_mirror.png'},
    {'name': 'Stimuli/Ebbinghaus trials/100s_85b_R.png', 'path': 'Stimuli/Ebbinghaus trials/100s_85b_R.png'},
    {'name': 'Stimuli/Kanizsa trials/Kanizsa 30a_R.png', 'path': 'Stimuli/Kanizsa trials/Kanizsa 30a_R.png'},
    {'name': 'Stimuli/Instructions/MS_long.ogg', 'path': 'Stimuli/Instructions/MS_long.ogg'},
    {'name': 'Stimuli/Kanizsa trials/Kanizsa 10e_R.png', 'path': 'Stimuli/Kanizsa trials/Kanizsa 10e_R.png'},
    {'name': 'Stimuli/Contrast trials/D50_L51.png', 'path': 'Stimuli/Contrast trials/D50_L51.png'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2022.2.4';
  expInfo['OS'] = window.navigator.platform;

  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var helloClock;
var text;
var buttonhello;
var sound_1;
var ML_INTROClock;
var ml_intro_text;
var sound_2;
var START_ML;
var TEST_MLClock;
var image_ML;
var LEFT_ML;
var RIGHT_ML;
var mouse_ML;
var sound_3;
var key_resp;
var pressspaceClock;
var Next_text;
var Next_polygon;
var Next_mouse;
var key_resp_2;
var Contrast_illusion_INTROClock;
var contrast_intro_text;
var sound_4;
var START_contrast;
var TEST_contrastClock;
var image_cont;
var LEFT_cont;
var RIGHT_cont;
var mouse_cont;
var sound_8;
var key_resp_3;
var Ebbing_INTROClock;
var ebbing_intro_text;
var sound_5;
var START_ebbing;
var TEST_ebbingClock;
var RIGHT_ebbing;
var LEFT_ebbing;
var image_ebbing;
var mouse_ebbing;
var sound_9;
var key_resp_4;
var Kanizsa_INTROClock;
var kanizsa_intro_text;
var sound_6;
var START_KN;
var trainingKZSClock;
var triangle;
var threefourth;
var twofourth;
var whitesquare;
var mouse_2;
var trainingKZS_2Clock;
var triangle_2;
var threefourth_2;
var twofourth_2;
var whitesquare_2;
var mouse_3;
var TEST_knzsClock;
var image_KN;
var LEFT_KN;
var RIGHT_KN;
var mouse_KN;
var sound_11;
var key_resp_5;
var MS_INTROClock;
var MS_intro_text;
var sound_7;
var START_MS;
var TEST_MSClock;
var image_MS;
var LEFT_MS;
var RIGHT_MS;
var mouse_MS;
var sound_10;
var key_resp_6;
var byeClock;
var text_2;
var mouse;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "hello"
  helloClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'A continuación, te presentaremos dos imágenes, \nuna del lado derecho y una del lado izquierdo. \nDebes elegir la imagen que mejor cumpla lo que la \ninstrucción te indicará. \nEscucha con atención cada instrucción y trata de \nresponder tan rápido como puedas.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.25], height: 0.06,  wrapWidth: 10.0, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 0.4902), (- 0.1765), 0.7647]),  opacity: undefined,
    depth: 0.0 
  });
  
  buttonhello = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'buttonhello',
    text: 'INICIAR',
    fillColor: 'orangered',
    borderColor: [(- 1.0), (- 1.0), (- 1.0)],
    color: 'white',
    colorSpace: 'rgb',
    pos: [0, (- 0.25)],
    letterHeight: 0.08,
    size: [0.4, 0.2]
  });
  buttonhello.clock = new util.Clock();
  
  sound_1 = new sound.Sound({
    win: psychoJS.window,
    value: 'Stimuli/Instructions/Instrucción inicial2.ogg',
    secs: (- 1),
    });
  sound_1.setVolume(1.0);
  // Initialize components for Routine "ML_INTRO"
  ML_INTROClock = new util.Clock();
  ml_intro_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'ml_intro_text',
    text: '\nElige la línea horizontal que te parezca \n¡MÁS LARGA!',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.2], height: 0.1,  wrapWidth: 20.0, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 0.4902), (- 0.1765), 0.7647]),  opacity: undefined,
    depth: 0.0 
  });
  
  sound_2 = new sound.Sound({
    win: psychoJS.window,
    value: 'Stimuli/Instructions/ML_long.ogg',
    secs: (- 1),
    });
  sound_2.setVolume(1.0);
  START_ML = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'START_ML',
    text: 'INICIAR',
    fillColor: [1.0, (- 0.4588), (- 1.0)],
    borderColor: [(- 1.0), (- 1.0), (- 1.0)],
    color: [1.0, 1.0, 1.0],
    colorSpace: 'rgb',
    pos: [0, (- 0.3)],
    letterHeight: 0.05,
    size: [0.3, 0.15]
  });
  START_ML.clock = new util.Clock();
  
  // Initialize components for Routine "TEST_ML"
  TEST_MLClock = new util.Clock();
  image_ML = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_ML', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : undefined,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  LEFT_ML = new visual.Rect ({
    win: psychoJS.window, name: 'LEFT_ML', 
    width: [0.86, 0.95][0], height: [0.86, 0.95][1],
    ori: 0.0, pos: [(- 0.44), 0],
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color(undefined),
    fillColor: new util.Color(undefined),
    opacity: 0.0, depth: -1, interpolate: true,
  });
  
  RIGHT_ML = new visual.Rect ({
    win: psychoJS.window, name: 'RIGHT_ML', 
    width: [0.86, 0.95][0], height: [0.86, 0.95][1],
    ori: 0.0, pos: [0.44, 0],
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color(undefined),
    fillColor: new util.Color(undefined),
    opacity: 0.0, depth: -2, interpolate: true,
  });
  
  mouse_ML = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_ML.mouseClock = new util.Clock();
  sound_3 = new sound.Sound({
    win: psychoJS.window,
    value: 'Stimuli/Instructions/ML_short.ogg',
    secs: (- 1),
    });
  sound_3.setVolume(1.0);
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "pressspace"
  pressspaceClock = new util.Clock();
  Next_text = new visual.TextBox({
    win: psychoJS.window,
    name: 'Next_text',
    text: 'Para ver la siguiente imagen\nPresione EN EL CIRCULO ROJO',
    font: 'Calibri',
    pos: [0, 0.3], letterHeight: 0.06,
    size: [null, null],  units: undefined, 
    color: [(- 1.0), (- 1.0), 1.0], colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: 0.0 
  });
  
  Next_polygon = new visual.Polygon({
    win: psychoJS.window, name: 'Next_polygon', 
    edges: 100, size:[0.15, 0.15],
    ori: 0.0, pos: [0, (- 0.2)],
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('black'),
    fillColor: new util.Color([1.0, (- 0.4588), (- 1.0)]),
    opacity: undefined, depth: -1, interpolate: true,
  });
  
  Next_mouse = new core.Mouse({
    win: psychoJS.window,
  });
  Next_mouse.mouseClock = new util.Clock();
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Contrast_illusion_INTRO"
  Contrast_illusion_INTROClock = new util.Clock();
  contrast_intro_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'contrast_intro_text',
    text: '\nElige el círculo que te parezca  \nMÁS OSCURO!\n',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.2], height: 0.1,  wrapWidth: 20.0, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('royalblue'),  opacity: undefined,
    depth: 0.0 
  });
  
  sound_4 = new sound.Sound({
    win: psychoJS.window,
    value: 'Stimuli/Instructions/CT_long.ogg',
    secs: (- 1),
    });
  sound_4.setVolume(1.0);
  START_contrast = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'START_contrast',
    text: 'INICIAR',
    fillColor: 'orangered',
    borderColor: 'black',
    color: 'white',
    colorSpace: 'rgb',
    pos: [0, (- 0.3)],
    letterHeight: 0.05,
    size: [0.3, 0.15]
  });
  START_contrast.clock = new util.Clock();
  
  // Initialize components for Routine "TEST_contrast"
  TEST_contrastClock = new util.Clock();
  image_cont = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_cont', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : undefined,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  LEFT_cont = new visual.Rect ({
    win: psychoJS.window, name: 'LEFT_cont', 
    width: [0.86, 0.95][0], height: [0.86, 0.95][1],
    ori: 0.0, pos: [(- 0.44), 0],
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color(undefined),
    fillColor: new util.Color(undefined),
    opacity: 0.0, depth: -1, interpolate: true,
  });
  
  RIGHT_cont = new visual.Rect ({
    win: psychoJS.window, name: 'RIGHT_cont', 
    width: [0.86, 0.95][0], height: [0.86, 0.95][1],
    ori: 0.0, pos: [0.44, 0],
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color(undefined),
    fillColor: new util.Color(undefined),
    opacity: 0.0, depth: -2, interpolate: true,
  });
  
  mouse_cont = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_cont.mouseClock = new util.Clock();
  sound_8 = new sound.Sound({
    win: psychoJS.window,
    value: 'Stimuli/Instructions/CT_short.ogg',
    secs: (- 1),
    });
  sound_8.setVolume(1.0);
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Ebbing_INTRO"
  Ebbing_INTROClock = new util.Clock();
  ebbing_intro_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'ebbing_intro_text',
    text: '\nElige el círculo naranja que te parezca \n¡MÁS GRANDE!\n',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.2], height: 0.1,  wrapWidth: 20.0, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('royalblue'),  opacity: undefined,
    depth: 0.0 
  });
  
  sound_5 = new sound.Sound({
    win: psychoJS.window,
    value: 'Stimuli/Instructions/EB_long.ogg',
    secs: (- 1),
    });
  sound_5.setVolume(1.0);
  START_ebbing = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'START_ebbing',
    text: 'INICIAR',
    fillColor: 'orangered',
    borderColor: 'black',
    color: 'white',
    colorSpace: 'rgb',
    pos: [0, (- 0.3)],
    letterHeight: 0.05,
    size: [0.3, 0.15]
  });
  START_ebbing.clock = new util.Clock();
  
  // Initialize components for Routine "TEST_ebbing"
  TEST_ebbingClock = new util.Clock();
  RIGHT_ebbing = new visual.Rect ({
    win: psychoJS.window, name: 'RIGHT_ebbing', 
    width: [0.86, 0.95][0], height: [0.86, 0.95][1],
    ori: 0.0, pos: [0.44, 0],
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    fillColor: new util.Color(undefined),
    opacity: 0.0, depth: 0, interpolate: true,
  });
  
  LEFT_ebbing = new visual.Rect ({
    win: psychoJS.window, name: 'LEFT_ebbing', 
    width: [0.86, 0.95][0], height: [0.86, 0.95][1],
    ori: 0.0, pos: [(- 0.44), 0],
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    fillColor: new util.Color(undefined),
    opacity: 0.0, depth: -1, interpolate: true,
  });
  
  image_ebbing = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_ebbing', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : undefined,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  mouse_ebbing = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_ebbing.mouseClock = new util.Clock();
  sound_9 = new sound.Sound({
    win: psychoJS.window,
    value: 'Stimuli/Instructions/EB_short.ogg',
    secs: (- 1),
    });
  sound_9.setVolume(1.0);
  key_resp_4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Kanizsa_INTRO"
  Kanizsa_INTROClock = new util.Clock();
  kanizsa_intro_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'kanizsa_intro_text',
    text: '\nElige el lado con el\n¡CUADRADO BLANCO!',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.2], height: 0.1,  wrapWidth: 20.0, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('royalblue'),  opacity: undefined,
    depth: 0.0 
  });
  
  sound_6 = new sound.Sound({
    win: psychoJS.window,
    value: 'Stimuli/Instructions/KZS_long.ogg',
    secs: (- 1),
    });
  sound_6.setVolume(1.0);
  START_KN = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'START_KN',
    text: 'INICIAR',
    fillColor: 'orangered',
    borderColor: 'black',
    color: 'white',
    colorSpace: 'rgb',
    pos: [0, (- 0.3)],
    letterHeight: 0.05,
    size: [0.3, 0.15]
  });
  START_KN.clock = new util.Clock();
  
  // Initialize components for Routine "trainingKZS"
  trainingKZSClock = new util.Clock();
  triangle = new visual.ImageStim({
    win : psychoJS.window,
    name : 'triangle', units : undefined, 
    image : 'Stimuli/Training/triang.png', mask : undefined,
    ori : 0.0, pos : [(- 0.5), 0.25], size : [0.4, 0.4],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  threefourth = new visual.ImageStim({
    win : psychoJS.window,
    name : 'threefourth', units : undefined, 
    image : 'Stimuli/Training/whitesquare3p4.png', mask : undefined,
    ori : 0.0, pos : [0.3, 0.25], size : [0.3, 0.3],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  twofourth = new visual.ImageStim({
    win : psychoJS.window,
    name : 'twofourth', units : undefined, 
    image : 'Stimuli/Training/whitesquare2p4.png', mask : undefined,
    ori : 0.0, pos : [(- 0.3), (- 0.25)], size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  whitesquare = new visual.ImageStim({
    win : psychoJS.window,
    name : 'whitesquare', units : undefined, 
    image : 'Stimuli/Training/whitesquare.png', mask : undefined,
    ori : 0.0, pos : [0.5, (- 0.15)], size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  mouse_2 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_2.mouseClock = new util.Clock();
  // Initialize components for Routine "trainingKZS_2"
  trainingKZS_2Clock = new util.Clock();
  triangle_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'triangle_2', units : undefined, 
    image : 'Stimuli/Training/triang.png', mask : undefined,
    ori : 23.0, pos : [(- 0.3), (- 0.25)], size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  threefourth_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'threefourth_2', units : undefined, 
    image : 'Stimuli/Training/whitesquare3p4.png', mask : undefined,
    ori : 350.0, pos : [0.5, (- 0.15)], size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  twofourth_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'twofourth_2', units : undefined, 
    image : 'Stimuli/Training/whitesquare2p4.png', mask : undefined,
    ori : 0.0, pos : [0.3, 0.25], size : [0.3, 0.3],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  whitesquare_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'whitesquare_2', units : undefined, 
    image : 'Stimuli/Training/whitesquare.png', mask : undefined,
    ori : 45.0, pos : [(- 0.5), 0.25], size : [0.4, 0.4],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  mouse_3 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_3.mouseClock = new util.Clock();
  // Initialize components for Routine "TEST_knzs"
  TEST_knzsClock = new util.Clock();
  image_KN = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_KN', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : undefined,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  LEFT_KN = new visual.Rect ({
    win: psychoJS.window, name: 'LEFT_KN', 
    width: [0.86, 0.95][0], height: [0.86, 0.95][1],
    ori: 0.0, pos: [(- 0.44), 0],
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color(undefined),
    fillColor: new util.Color(undefined),
    opacity: 0.0, depth: -1, interpolate: true,
  });
  
  RIGHT_KN = new visual.Rect ({
    win: psychoJS.window, name: 'RIGHT_KN', 
    width: [0.86, 0.95][0], height: [0.86, 0.95][1],
    ori: 0.0, pos: [0.44, 0],
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color(undefined),
    fillColor: new util.Color(undefined),
    opacity: 0.0, depth: -2, interpolate: true,
  });
  
  mouse_KN = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_KN.mouseClock = new util.Clock();
  sound_11 = new sound.Sound({
    win: psychoJS.window,
    value: 'Stimuli/Instructions/KZS_short.ogg',
    secs: (- 1),
    });
  sound_11.setVolume(1.0);
  key_resp_5 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "MS_INTRO"
  MS_INTROClock = new util.Clock();
  MS_intro_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'MS_intro_text',
    text: '\nElige aquella en la que notas \n¡MAYOR MOVIMIENTO!\n',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.2], height: 0.1,  wrapWidth: 20.0, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('royalblue'),  opacity: undefined,
    depth: 0.0 
  });
  
  sound_7 = new sound.Sound({
    win: psychoJS.window,
    value: 'Stimuli/Instructions/MS_long.ogg',
    secs: (- 1),
    });
  sound_7.setVolume(1.0);
  START_MS = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'START_MS',
    text: 'INICIAR',
    fillColor: 'orangered',
    borderColor: 'black',
    color: 'white',
    colorSpace: 'rgb',
    pos: [0, (- 0.3)],
    letterHeight: 0.05,
    size: [0.3, 0.15]
  });
  START_MS.clock = new util.Clock();
  
  // Initialize components for Routine "TEST_MS"
  TEST_MSClock = new util.Clock();
  image_MS = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_MS', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : undefined,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  LEFT_MS = new visual.Rect ({
    win: psychoJS.window, name: 'LEFT_MS', 
    width: [0.86, 0.95][0], height: [0.86, 0.95][1],
    ori: 0.0, pos: [(- 0.44), 0],
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color(undefined),
    fillColor: new util.Color(undefined),
    opacity: 0.0, depth: -1, interpolate: true,
  });
  
  RIGHT_MS = new visual.Rect ({
    win: psychoJS.window, name: 'RIGHT_MS', 
    width: [0.86, 0.95][0], height: [0.86, 0.95][1],
    ori: 0.0, pos: [0.44, 0],
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color(undefined),
    fillColor: new util.Color(undefined),
    opacity: 0.0, depth: -2, interpolate: true,
  });
  
  mouse_MS = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_MS.mouseClock = new util.Clock();
  sound_10 = new sound.Sound({
    win: psychoJS.window,
    value: 'Stimuli/Instructions/MS_short.ogg',
    secs: (- 1),
    });
  sound_10.setVolume(1.0);
  key_resp_6 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "bye"
  byeClock = new util.Clock();
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: '¡GRACIAS!',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.2,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 0.4902), (- 0.1765), 0.7647]),  opacity: undefined,
    depth: 0.0 
  });
  
  mouse = new core.Mouse({
    win: psychoJS.window,
  });
  mouse.mouseClock = new util.Clock();
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var helloComponents;
function helloRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'hello' ---
    t = 0;
    helloClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    sound_1.setVolume(1.0);
    // keep track of which components have finished
    helloComponents = [];
    helloComponents.push(text);
    helloComponents.push(buttonhello);
    helloComponents.push(sound_1);
    
    for (const thisComponent of helloComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function helloRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'hello' ---
    // get current time
    t = helloClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    
    // *buttonhello* updates
    if (t >= 0 && buttonhello.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      buttonhello.tStart = t;  // (not accounting for frame time here)
      buttonhello.frameNStart = frameN;  // exact frame index
      
      buttonhello.setAutoDraw(true);
    }

    if (buttonhello.status === PsychoJS.Status.STARTED) {
      // check whether buttonhello has been pressed
      if (buttonhello.isClicked) {
        if (!buttonhello.wasClicked) {
          // store time of first click
          buttonhello.timesOn.push(buttonhello.clock.getTime());
          buttonhello.numClicks += 1;
          // store time clicked until
          buttonhello.timesOff.push(buttonhello.clock.getTime());
        } else {
          // update time clicked until;
          buttonhello.timesOff[buttonhello.timesOff.length - 1] = buttonhello.clock.getTime();
        }
        if (!buttonhello.wasClicked) {
          // end routine when buttonhello is clicked
          continueRoutine = false;
        }
        // if buttonhello is still clicked next frame, it is not a new click
        buttonhello.wasClicked = true;
      } else {
        // if buttonhello is clicked next frame, it is a new click
        buttonhello.wasClicked = false;
      }
    } else {
      // keep clock at 0 if buttonhello hasn't started / has finished
      buttonhello.clock.reset();
      // if buttonhello is clicked next frame, it is a new click
      buttonhello.wasClicked = false;
    }
    // start/stop sound_1
    if (t >= 0.0 && sound_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sound_1.tStart = t;  // (not accounting for frame time here)
      sound_1.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ sound_1.play(); });  // screen flip
      sound_1.status = PsychoJS.Status.STARTED;
    }
    if (t >= (sound_1.getDuration() + sound_1.tStart)     && sound_1.status === PsychoJS.Status.STARTED) {
      sound_1.stop();  // stop the sound (if longer than duration)
      sound_1.status = PsychoJS.Status.FINISHED;
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of helloComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function helloRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'hello' ---
    for (const thisComponent of helloComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('buttonhello.numClicks', buttonhello.numClicks);
    psychoJS.experiment.addData('buttonhello.timesOn', buttonhello.timesOn);
    psychoJS.experiment.addData('buttonhello.timesOff', buttonhello.timesOff);
    sound_1.stop();  // ensure sound has stopped at end of routine
    // the Routine "hello" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var trials;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'Stimuli/randomblock.xlsx',
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial of trials) {
      snapshot = trials.getSnapshot();
      trialsLoopScheduler.add(importConditions(snapshot));
      const ALoopScheduler = new Scheduler(psychoJS);
      trialsLoopScheduler.add(ALoopBegin(ALoopScheduler, snapshot));
      trialsLoopScheduler.add(ALoopScheduler);
      trialsLoopScheduler.add(ALoopEnd);
      const BLoopScheduler = new Scheduler(psychoJS);
      trialsLoopScheduler.add(BLoopBegin(BLoopScheduler, snapshot));
      trialsLoopScheduler.add(BLoopScheduler);
      trialsLoopScheduler.add(BLoopEnd);
      const CLoopScheduler = new Scheduler(psychoJS);
      trialsLoopScheduler.add(CLoopBegin(CLoopScheduler, snapshot));
      trialsLoopScheduler.add(CLoopScheduler);
      trialsLoopScheduler.add(CLoopEnd);
      const DLoopScheduler = new Scheduler(psychoJS);
      trialsLoopScheduler.add(DLoopBegin(DLoopScheduler, snapshot));
      trialsLoopScheduler.add(DLoopScheduler);
      trialsLoopScheduler.add(DLoopEnd);
      const ELoopScheduler = new Scheduler(psychoJS);
      trialsLoopScheduler.add(ELoopBegin(ELoopScheduler, snapshot));
      trialsLoopScheduler.add(ELoopScheduler);
      trialsLoopScheduler.add(ELoopEnd);
      trialsLoopScheduler.add(trialsLoopEndIteration(trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var A;
function ALoopBegin(ALoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    A = new TrialHandler({
      psychoJS: psychoJS,
      nReps: ML_repeat, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'A'
    });
    psychoJS.experiment.addLoop(A); // add the loop to the experiment
    currentLoop = A;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisA of A) {
      snapshot = A.getSnapshot();
      ALoopScheduler.add(importConditions(snapshot));
      ALoopScheduler.add(ML_INTRORoutineBegin(snapshot));
      ALoopScheduler.add(ML_INTRORoutineEachFrame());
      ALoopScheduler.add(ML_INTRORoutineEnd(snapshot));
      const ML_repLoopScheduler = new Scheduler(psychoJS);
      ALoopScheduler.add(ML_repLoopBegin(ML_repLoopScheduler, snapshot));
      ALoopScheduler.add(ML_repLoopScheduler);
      ALoopScheduler.add(ML_repLoopEnd);
      ALoopScheduler.add(ALoopEndIteration(ALoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var ML_rep;
function ML_repLoopBegin(ML_repLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    ML_rep = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'Stimuli/Müller-Lyer trials/ML_condition_file.xlsx',
      seed: undefined, name: 'ML_rep'
    });
    psychoJS.experiment.addLoop(ML_rep); // add the loop to the experiment
    currentLoop = ML_rep;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisML_rep of ML_rep) {
      snapshot = ML_rep.getSnapshot();
      ML_repLoopScheduler.add(importConditions(snapshot));
      ML_repLoopScheduler.add(TEST_MLRoutineBegin(snapshot));
      ML_repLoopScheduler.add(TEST_MLRoutineEachFrame());
      ML_repLoopScheduler.add(TEST_MLRoutineEnd(snapshot));
      ML_repLoopScheduler.add(pressspaceRoutineBegin(snapshot));
      ML_repLoopScheduler.add(pressspaceRoutineEachFrame());
      ML_repLoopScheduler.add(pressspaceRoutineEnd(snapshot));
      ML_repLoopScheduler.add(ML_repLoopEndIteration(ML_repLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function ML_repLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(ML_rep);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function ML_repLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function ALoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(A);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function ALoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var B;
function BLoopBegin(BLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    B = new TrialHandler({
      psychoJS: psychoJS,
      nReps: contrast_repeat, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'B'
    });
    psychoJS.experiment.addLoop(B); // add the loop to the experiment
    currentLoop = B;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisB of B) {
      snapshot = B.getSnapshot();
      BLoopScheduler.add(importConditions(snapshot));
      BLoopScheduler.add(Contrast_illusion_INTRORoutineBegin(snapshot));
      BLoopScheduler.add(Contrast_illusion_INTRORoutineEachFrame());
      BLoopScheduler.add(Contrast_illusion_INTRORoutineEnd(snapshot));
      const contrast_repLoopScheduler = new Scheduler(psychoJS);
      BLoopScheduler.add(contrast_repLoopBegin(contrast_repLoopScheduler, snapshot));
      BLoopScheduler.add(contrast_repLoopScheduler);
      BLoopScheduler.add(contrast_repLoopEnd);
      BLoopScheduler.add(BLoopEndIteration(BLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var contrast_rep;
function contrast_repLoopBegin(contrast_repLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    contrast_rep = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'Stimuli/Contrast trials/Contrast_condition_file.xlsx',
      seed: undefined, name: 'contrast_rep'
    });
    psychoJS.experiment.addLoop(contrast_rep); // add the loop to the experiment
    currentLoop = contrast_rep;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisContrast_rep of contrast_rep) {
      snapshot = contrast_rep.getSnapshot();
      contrast_repLoopScheduler.add(importConditions(snapshot));
      contrast_repLoopScheduler.add(TEST_contrastRoutineBegin(snapshot));
      contrast_repLoopScheduler.add(TEST_contrastRoutineEachFrame());
      contrast_repLoopScheduler.add(TEST_contrastRoutineEnd(snapshot));
      contrast_repLoopScheduler.add(pressspaceRoutineBegin(snapshot));
      contrast_repLoopScheduler.add(pressspaceRoutineEachFrame());
      contrast_repLoopScheduler.add(pressspaceRoutineEnd(snapshot));
      contrast_repLoopScheduler.add(contrast_repLoopEndIteration(contrast_repLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function contrast_repLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(contrast_rep);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function contrast_repLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function BLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(B);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function BLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var C;
function CLoopBegin(CLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    C = new TrialHandler({
      psychoJS: psychoJS,
      nReps: ebbing_repeat, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'C'
    });
    psychoJS.experiment.addLoop(C); // add the loop to the experiment
    currentLoop = C;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisC of C) {
      snapshot = C.getSnapshot();
      CLoopScheduler.add(importConditions(snapshot));
      CLoopScheduler.add(Ebbing_INTRORoutineBegin(snapshot));
      CLoopScheduler.add(Ebbing_INTRORoutineEachFrame());
      CLoopScheduler.add(Ebbing_INTRORoutineEnd(snapshot));
      const ebbing_repLoopScheduler = new Scheduler(psychoJS);
      CLoopScheduler.add(ebbing_repLoopBegin(ebbing_repLoopScheduler, snapshot));
      CLoopScheduler.add(ebbing_repLoopScheduler);
      CLoopScheduler.add(ebbing_repLoopEnd);
      CLoopScheduler.add(CLoopEndIteration(CLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var ebbing_rep;
function ebbing_repLoopBegin(ebbing_repLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    ebbing_rep = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'Stimuli/Ebbinghaus trials/Ebbinghaus_condition_file.xlsx',
      seed: undefined, name: 'ebbing_rep'
    });
    psychoJS.experiment.addLoop(ebbing_rep); // add the loop to the experiment
    currentLoop = ebbing_rep;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisEbbing_rep of ebbing_rep) {
      snapshot = ebbing_rep.getSnapshot();
      ebbing_repLoopScheduler.add(importConditions(snapshot));
      ebbing_repLoopScheduler.add(TEST_ebbingRoutineBegin(snapshot));
      ebbing_repLoopScheduler.add(TEST_ebbingRoutineEachFrame());
      ebbing_repLoopScheduler.add(TEST_ebbingRoutineEnd(snapshot));
      ebbing_repLoopScheduler.add(pressspaceRoutineBegin(snapshot));
      ebbing_repLoopScheduler.add(pressspaceRoutineEachFrame());
      ebbing_repLoopScheduler.add(pressspaceRoutineEnd(snapshot));
      ebbing_repLoopScheduler.add(ebbing_repLoopEndIteration(ebbing_repLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function ebbing_repLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(ebbing_rep);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function ebbing_repLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function CLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(C);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function CLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var D;
function DLoopBegin(DLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    D = new TrialHandler({
      psychoJS: psychoJS,
      nReps: kanizsa_repeat, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'D'
    });
    psychoJS.experiment.addLoop(D); // add the loop to the experiment
    currentLoop = D;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisD of D) {
      snapshot = D.getSnapshot();
      DLoopScheduler.add(importConditions(snapshot));
      DLoopScheduler.add(Kanizsa_INTRORoutineBegin(snapshot));
      DLoopScheduler.add(Kanizsa_INTRORoutineEachFrame());
      DLoopScheduler.add(Kanizsa_INTRORoutineEnd(snapshot));
      DLoopScheduler.add(trainingKZSRoutineBegin(snapshot));
      DLoopScheduler.add(trainingKZSRoutineEachFrame());
      DLoopScheduler.add(trainingKZSRoutineEnd(snapshot));
      DLoopScheduler.add(trainingKZS_2RoutineBegin(snapshot));
      DLoopScheduler.add(trainingKZS_2RoutineEachFrame());
      DLoopScheduler.add(trainingKZS_2RoutineEnd(snapshot));
      const KN_repLoopScheduler = new Scheduler(psychoJS);
      DLoopScheduler.add(KN_repLoopBegin(KN_repLoopScheduler, snapshot));
      DLoopScheduler.add(KN_repLoopScheduler);
      DLoopScheduler.add(KN_repLoopEnd);
      DLoopScheduler.add(DLoopEndIteration(DLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var KN_rep;
function KN_repLoopBegin(KN_repLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    KN_rep = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'Stimuli/Kanizsa trials/KN_condition_file.xlsx',
      seed: undefined, name: 'KN_rep'
    });
    psychoJS.experiment.addLoop(KN_rep); // add the loop to the experiment
    currentLoop = KN_rep;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisKN_rep of KN_rep) {
      snapshot = KN_rep.getSnapshot();
      KN_repLoopScheduler.add(importConditions(snapshot));
      KN_repLoopScheduler.add(TEST_knzsRoutineBegin(snapshot));
      KN_repLoopScheduler.add(TEST_knzsRoutineEachFrame());
      KN_repLoopScheduler.add(TEST_knzsRoutineEnd(snapshot));
      KN_repLoopScheduler.add(pressspaceRoutineBegin(snapshot));
      KN_repLoopScheduler.add(pressspaceRoutineEachFrame());
      KN_repLoopScheduler.add(pressspaceRoutineEnd(snapshot));
      KN_repLoopScheduler.add(KN_repLoopEndIteration(KN_repLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function KN_repLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(KN_rep);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function KN_repLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function DLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(D);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function DLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var E;
function ELoopBegin(ELoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    E = new TrialHandler({
      psychoJS: psychoJS,
      nReps: MS_repeat, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'E'
    });
    psychoJS.experiment.addLoop(E); // add the loop to the experiment
    currentLoop = E;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisE of E) {
      snapshot = E.getSnapshot();
      ELoopScheduler.add(importConditions(snapshot));
      ELoopScheduler.add(MS_INTRORoutineBegin(snapshot));
      ELoopScheduler.add(MS_INTRORoutineEachFrame());
      ELoopScheduler.add(MS_INTRORoutineEnd(snapshot));
      const MS_repLoopScheduler = new Scheduler(psychoJS);
      ELoopScheduler.add(MS_repLoopBegin(MS_repLoopScheduler, snapshot));
      ELoopScheduler.add(MS_repLoopScheduler);
      ELoopScheduler.add(MS_repLoopEnd);
      ELoopScheduler.add(ELoopEndIteration(ELoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var MS_rep;
function MS_repLoopBegin(MS_repLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    MS_rep = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'Stimuli/Moving snake trials/MS_condition_file .xlsx',
      seed: undefined, name: 'MS_rep'
    });
    psychoJS.experiment.addLoop(MS_rep); // add the loop to the experiment
    currentLoop = MS_rep;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisMS_rep of MS_rep) {
      snapshot = MS_rep.getSnapshot();
      MS_repLoopScheduler.add(importConditions(snapshot));
      MS_repLoopScheduler.add(TEST_MSRoutineBegin(snapshot));
      MS_repLoopScheduler.add(TEST_MSRoutineEachFrame());
      MS_repLoopScheduler.add(TEST_MSRoutineEnd(snapshot));
      MS_repLoopScheduler.add(pressspaceRoutineBegin(snapshot));
      MS_repLoopScheduler.add(pressspaceRoutineEachFrame());
      MS_repLoopScheduler.add(pressspaceRoutineEnd(snapshot));
      MS_repLoopScheduler.add(MS_repLoopEndIteration(MS_repLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function MS_repLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(MS_rep);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function MS_repLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function ELoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(E);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function ELoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var ML_INTROComponents;
function ML_INTRORoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'ML_INTRO' ---
    t = 0;
    ML_INTROClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    sound_2.setVolume(1.0);
    // keep track of which components have finished
    ML_INTROComponents = [];
    ML_INTROComponents.push(ml_intro_text);
    ML_INTROComponents.push(sound_2);
    ML_INTROComponents.push(START_ML);
    
    for (const thisComponent of ML_INTROComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function ML_INTRORoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'ML_INTRO' ---
    // get current time
    t = ML_INTROClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *ml_intro_text* updates
    if (t >= 1 && ml_intro_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ml_intro_text.tStart = t;  // (not accounting for frame time here)
      ml_intro_text.frameNStart = frameN;  // exact frame index
      
      ml_intro_text.setAutoDraw(true);
    }

    // start/stop sound_2
    if (t >= 1 && sound_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sound_2.tStart = t;  // (not accounting for frame time here)
      sound_2.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ sound_2.play(); });  // screen flip
      sound_2.status = PsychoJS.Status.STARTED;
    }
    if (t >= (sound_2.getDuration() + sound_2.tStart)     && sound_2.status === PsychoJS.Status.STARTED) {
      sound_2.stop();  // stop the sound (if longer than duration)
      sound_2.status = PsychoJS.Status.FINISHED;
    }
    
    // *START_ML* updates
    if (t >= 1 && START_ML.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      START_ML.tStart = t;  // (not accounting for frame time here)
      START_ML.frameNStart = frameN;  // exact frame index
      
      START_ML.setAutoDraw(true);
    }

    if (START_ML.status === PsychoJS.Status.STARTED) {
      // check whether START_ML has been pressed
      if (START_ML.isClicked) {
        if (!START_ML.wasClicked) {
          // store time of first click
          START_ML.timesOn.push(START_ML.clock.getTime());
          START_ML.numClicks += 1;
          // store time clicked until
          START_ML.timesOff.push(START_ML.clock.getTime());
        } else {
          // update time clicked until;
          START_ML.timesOff[START_ML.timesOff.length - 1] = START_ML.clock.getTime();
        }
        if (!START_ML.wasClicked) {
          // end routine when START_ML is clicked
          continueRoutine = false;
        }
        // if START_ML is still clicked next frame, it is not a new click
        START_ML.wasClicked = true;
      } else {
        // if START_ML is clicked next frame, it is a new click
        START_ML.wasClicked = false;
      }
    } else {
      // keep clock at 0 if START_ML hasn't started / has finished
      START_ML.clock.reset();
      // if START_ML is clicked next frame, it is a new click
      START_ML.wasClicked = false;
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ML_INTROComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ML_INTRORoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'ML_INTRO' ---
    for (const thisComponent of ML_INTROComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    sound_2.stop();  // ensure sound has stopped at end of routine
    psychoJS.experiment.addData('START_ML.numClicks', START_ML.numClicks);
    psychoJS.experiment.addData('START_ML.timesOn', START_ML.timesOn);
    psychoJS.experiment.addData('START_ML.timesOff', START_ML.timesOff);
    // the Routine "ML_INTRO" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var gotValidClick;
var _key_resp_allKeys;
var TEST_MLComponents;
function TEST_MLRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'TEST_ML' ---
    t = 0;
    TEST_MLClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(15.100000);
    // update component parameters for each repeat
    image_ML.setImage(path);
    // setup some python lists for storing info about the mouse_ML
    // current position of the mouse:
    mouse_ML.x = [];
    mouse_ML.y = [];
    mouse_ML.leftButton = [];
    mouse_ML.midButton = [];
    mouse_ML.rightButton = [];
    mouse_ML.time = [];
    mouse_ML.clicked_name = [];
    gotValidClick = false; // until a click is received
    sound_3.secs=10;
    sound_3.setVolume(1.0);
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    TEST_MLComponents = [];
    TEST_MLComponents.push(image_ML);
    TEST_MLComponents.push(LEFT_ML);
    TEST_MLComponents.push(RIGHT_ML);
    TEST_MLComponents.push(mouse_ML);
    TEST_MLComponents.push(sound_3);
    TEST_MLComponents.push(key_resp);
    
    for (const thisComponent of TEST_MLComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
var prevButtonState;
var _mouseButtons;
var _mouseXYs;
function TEST_MLRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'TEST_ML' ---
    // get current time
    t = TEST_MLClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_ML* updates
    if (t >= 0.1 && image_ML.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_ML.tStart = t;  // (not accounting for frame time here)
      image_ML.frameNStart = frameN;  // exact frame index
      
      image_ML.setAutoDraw(true);
    }

    frameRemains = 0.1 + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_ML.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_ML.setAutoDraw(false);
    }
    
    // *LEFT_ML* updates
    if (t >= 0 && LEFT_ML.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      LEFT_ML.tStart = t;  // (not accounting for frame time here)
      LEFT_ML.frameNStart = frameN;  // exact frame index
      
      LEFT_ML.setAutoDraw(true);
    }

    frameRemains = 0 + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (LEFT_ML.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      LEFT_ML.setAutoDraw(false);
    }
    
    // *RIGHT_ML* updates
    if (t >= 0 && RIGHT_ML.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      RIGHT_ML.tStart = t;  // (not accounting for frame time here)
      RIGHT_ML.frameNStart = frameN;  // exact frame index
      
      RIGHT_ML.setAutoDraw(true);
    }

    frameRemains = 0 + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (RIGHT_ML.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      RIGHT_ML.setAutoDraw(false);
    }
    // *mouse_ML* updates
    if (t >= 0 && mouse_ML.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_ML.tStart = t;  // (not accounting for frame time here)
      mouse_ML.frameNStart = frameN;  // exact frame index
      
      mouse_ML.status = PsychoJS.Status.STARTED;
      mouse_ML.mouseClock.reset();
      prevButtonState = mouse_ML.getPressed();  // if button is down already this ISN'T a new click
      }
    frameRemains = 0 + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (mouse_ML.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      mouse_ML.status = PsychoJS.Status.FINISHED;
  }
    if (mouse_ML.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_ML.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [LEFT_ML, RIGHT_ML]) {
            if (obj.contains(mouse_ML)) {
              gotValidClick = true;
              mouse_ML.clicked_name.push(obj.name)
            }
          }
          _mouseXYs = mouse_ML.getPos();
          mouse_ML.x.push(_mouseXYs[0]);
          mouse_ML.y.push(_mouseXYs[1]);
          mouse_ML.leftButton.push(_mouseButtons[0]);
          mouse_ML.midButton.push(_mouseButtons[1]);
          mouse_ML.rightButton.push(_mouseButtons[2]);
          mouse_ML.time.push(mouse_ML.mouseClock.getTime());
          // abort routine on response
          continueRoutine = false;
        }
      }
    }
    // start/stop sound_3
    if (t >= 5 && sound_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sound_3.tStart = t;  // (not accounting for frame time here)
      sound_3.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ sound_3.play(); });  // screen flip
      sound_3.status = PsychoJS.Status.STARTED;
    }
    frameRemains = 5 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (sound_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      if (10 > 0.5) {
        sound_3.stop();  // stop the sound (if longer than duration)
      }
      sound_3.status = PsychoJS.Status.FINISHED;
    }
    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      key_resp.clock.reset();
      key_resp.start();
    }

    frameRemains = 0.0 + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp.status = PsychoJS.Status.FINISHED;
  }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['p'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of TEST_MLComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function TEST_MLRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'TEST_ML' ---
    for (const thisComponent of TEST_MLComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for psychoJS.experiment (ExperimentHandler)
    if (mouse_ML.x) {  psychoJS.experiment.addData('mouse_ML.x', mouse_ML.x[0])};
    if (mouse_ML.y) {  psychoJS.experiment.addData('mouse_ML.y', mouse_ML.y[0])};
    if (mouse_ML.leftButton) {  psychoJS.experiment.addData('mouse_ML.leftButton', mouse_ML.leftButton[0])};
    if (mouse_ML.midButton) {  psychoJS.experiment.addData('mouse_ML.midButton', mouse_ML.midButton[0])};
    if (mouse_ML.rightButton) {  psychoJS.experiment.addData('mouse_ML.rightButton', mouse_ML.rightButton[0])};
    if (mouse_ML.time) {  psychoJS.experiment.addData('mouse_ML.time', mouse_ML.time[0])};
    if (mouse_ML.clicked_name) {  psychoJS.experiment.addData('mouse_ML.clicked_name', mouse_ML.clicked_name[0])};
    
    sound_3.stop();  // ensure sound has stopped at end of routine
    key_resp.stop();
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_2_allKeys;
var pressspaceComponents;
function pressspaceRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'pressspace' ---
    t = 0;
    pressspaceClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // setup some python lists for storing info about the Next_mouse
    Next_mouse.clicked_name = [];
    gotValidClick = false; // until a click is received
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    // keep track of which components have finished
    pressspaceComponents = [];
    pressspaceComponents.push(Next_text);
    pressspaceComponents.push(Next_polygon);
    pressspaceComponents.push(Next_mouse);
    pressspaceComponents.push(key_resp_2);
    
    for (const thisComponent of pressspaceComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function pressspaceRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'pressspace' ---
    // get current time
    t = pressspaceClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Next_text* updates
    if (t >= 0.0 && Next_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Next_text.tStart = t;  // (not accounting for frame time here)
      Next_text.frameNStart = frameN;  // exact frame index
      
      Next_text.setAutoDraw(true);
    }

    
    // *Next_polygon* updates
    if (t >= 0.0 && Next_polygon.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Next_polygon.tStart = t;  // (not accounting for frame time here)
      Next_polygon.frameNStart = frameN;  // exact frame index
      
      Next_polygon.setAutoDraw(true);
    }

    // *Next_mouse* updates
    if (t >= 0.0 && Next_mouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Next_mouse.tStart = t;  // (not accounting for frame time here)
      Next_mouse.frameNStart = frameN;  // exact frame index
      
      Next_mouse.status = PsychoJS.Status.STARTED;
      prevButtonState = Next_mouse.getPressed();  // if button is down already this ISN'T a new click
      }
    if (Next_mouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = Next_mouse.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [Next_polygon]) {
            if (obj.contains(Next_mouse)) {
              gotValidClick = true;
              Next_mouse.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *key_resp_2* updates
    if (t >= 0.0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      key_resp_2.clock.reset();
      key_resp_2.start();
    }

    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['p'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of pressspaceComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function pressspaceRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'pressspace' ---
    for (const thisComponent of pressspaceComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for psychoJS.experiment (ExperimentHandler)
    _mouseXYs = Next_mouse.getPos();
    _mouseButtons = Next_mouse.getPressed();
    psychoJS.experiment.addData('Next_mouse.x', _mouseXYs[0]);
    psychoJS.experiment.addData('Next_mouse.y', _mouseXYs[1]);
    psychoJS.experiment.addData('Next_mouse.leftButton', _mouseButtons[0]);
    psychoJS.experiment.addData('Next_mouse.midButton', _mouseButtons[1]);
    psychoJS.experiment.addData('Next_mouse.rightButton', _mouseButtons[2]);
    if (Next_mouse.clicked_name.length > 0) {
      psychoJS.experiment.addData('Next_mouse.clicked_name', Next_mouse.clicked_name[0]);}
    key_resp_2.stop();
    // the Routine "pressspace" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Contrast_illusion_INTROComponents;
function Contrast_illusion_INTRORoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Contrast_illusion_INTRO' ---
    t = 0;
    Contrast_illusion_INTROClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    sound_4.setVolume(1.0);
    // keep track of which components have finished
    Contrast_illusion_INTROComponents = [];
    Contrast_illusion_INTROComponents.push(contrast_intro_text);
    Contrast_illusion_INTROComponents.push(sound_4);
    Contrast_illusion_INTROComponents.push(START_contrast);
    
    for (const thisComponent of Contrast_illusion_INTROComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Contrast_illusion_INTRORoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Contrast_illusion_INTRO' ---
    // get current time
    t = Contrast_illusion_INTROClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *contrast_intro_text* updates
    if (t >= 1 && contrast_intro_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      contrast_intro_text.tStart = t;  // (not accounting for frame time here)
      contrast_intro_text.frameNStart = frameN;  // exact frame index
      
      contrast_intro_text.setAutoDraw(true);
    }

    // start/stop sound_4
    if (t >= 1 && sound_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sound_4.tStart = t;  // (not accounting for frame time here)
      sound_4.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ sound_4.play(); });  // screen flip
      sound_4.status = PsychoJS.Status.STARTED;
    }
    if (t >= (sound_4.getDuration() + sound_4.tStart)     && sound_4.status === PsychoJS.Status.STARTED) {
      sound_4.stop();  // stop the sound (if longer than duration)
      sound_4.status = PsychoJS.Status.FINISHED;
    }
    
    // *START_contrast* updates
    if (t >= 1 && START_contrast.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      START_contrast.tStart = t;  // (not accounting for frame time here)
      START_contrast.frameNStart = frameN;  // exact frame index
      
      START_contrast.setAutoDraw(true);
    }

    if (START_contrast.status === PsychoJS.Status.STARTED) {
      // check whether START_contrast has been pressed
      if (START_contrast.isClicked) {
        if (!START_contrast.wasClicked) {
          // store time of first click
          START_contrast.timesOn.push(START_contrast.clock.getTime());
          START_contrast.numClicks += 1;
          // store time clicked until
          START_contrast.timesOff.push(START_contrast.clock.getTime());
        } else {
          // update time clicked until;
          START_contrast.timesOff[START_contrast.timesOff.length - 1] = START_contrast.clock.getTime();
        }
        if (!START_contrast.wasClicked) {
          // end routine when START_contrast is clicked
          continueRoutine = false;
        }
        // if START_contrast is still clicked next frame, it is not a new click
        START_contrast.wasClicked = true;
      } else {
        // if START_contrast is clicked next frame, it is a new click
        START_contrast.wasClicked = false;
      }
    } else {
      // keep clock at 0 if START_contrast hasn't started / has finished
      START_contrast.clock.reset();
      // if START_contrast is clicked next frame, it is a new click
      START_contrast.wasClicked = false;
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Contrast_illusion_INTROComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Contrast_illusion_INTRORoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Contrast_illusion_INTRO' ---
    for (const thisComponent of Contrast_illusion_INTROComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    sound_4.stop();  // ensure sound has stopped at end of routine
    psychoJS.experiment.addData('START_contrast.numClicks', START_contrast.numClicks);
    psychoJS.experiment.addData('START_contrast.timesOn', START_contrast.timesOn);
    psychoJS.experiment.addData('START_contrast.timesOff', START_contrast.timesOff);
    // the Routine "Contrast_illusion_INTRO" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_3_allKeys;
var TEST_contrastComponents;
function TEST_contrastRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'TEST_contrast' ---
    t = 0;
    TEST_contrastClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(15.100000);
    // update component parameters for each repeat
    image_cont.setImage(path);
    // setup some python lists for storing info about the mouse_cont
    // current position of the mouse:
    mouse_cont.x = [];
    mouse_cont.y = [];
    mouse_cont.leftButton = [];
    mouse_cont.midButton = [];
    mouse_cont.rightButton = [];
    mouse_cont.time = [];
    mouse_cont.clicked_name = [];
    gotValidClick = false; // until a click is received
    sound_8.secs=10;
    sound_8.setVolume(1.0);
    key_resp_3.keys = undefined;
    key_resp_3.rt = undefined;
    _key_resp_3_allKeys = [];
    // keep track of which components have finished
    TEST_contrastComponents = [];
    TEST_contrastComponents.push(image_cont);
    TEST_contrastComponents.push(LEFT_cont);
    TEST_contrastComponents.push(RIGHT_cont);
    TEST_contrastComponents.push(mouse_cont);
    TEST_contrastComponents.push(sound_8);
    TEST_contrastComponents.push(key_resp_3);
    
    for (const thisComponent of TEST_contrastComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function TEST_contrastRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'TEST_contrast' ---
    // get current time
    t = TEST_contrastClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_cont* updates
    if (t >= 0.1 && image_cont.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_cont.tStart = t;  // (not accounting for frame time here)
      image_cont.frameNStart = frameN;  // exact frame index
      
      image_cont.setAutoDraw(true);
    }

    frameRemains = 0.1 + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_cont.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_cont.setAutoDraw(false);
    }
    
    // *LEFT_cont* updates
    if (t >= 0 && LEFT_cont.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      LEFT_cont.tStart = t;  // (not accounting for frame time here)
      LEFT_cont.frameNStart = frameN;  // exact frame index
      
      LEFT_cont.setAutoDraw(true);
    }

    frameRemains = 0 + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (LEFT_cont.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      LEFT_cont.setAutoDraw(false);
    }
    
    // *RIGHT_cont* updates
    if (t >= 0 && RIGHT_cont.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      RIGHT_cont.tStart = t;  // (not accounting for frame time here)
      RIGHT_cont.frameNStart = frameN;  // exact frame index
      
      RIGHT_cont.setAutoDraw(true);
    }

    frameRemains = 0 + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (RIGHT_cont.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      RIGHT_cont.setAutoDraw(false);
    }
    // *mouse_cont* updates
    if (t >= 0 && mouse_cont.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_cont.tStart = t;  // (not accounting for frame time here)
      mouse_cont.frameNStart = frameN;  // exact frame index
      
      mouse_cont.status = PsychoJS.Status.STARTED;
      mouse_cont.mouseClock.reset();
      prevButtonState = mouse_cont.getPressed();  // if button is down already this ISN'T a new click
      }
    frameRemains = 0 + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (mouse_cont.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      mouse_cont.status = PsychoJS.Status.FINISHED;
  }
    if (mouse_cont.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_cont.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [LEFT_cont, RIGHT_cont]) {
            if (obj.contains(mouse_cont)) {
              gotValidClick = true;
              mouse_cont.clicked_name.push(obj.name)
            }
          }
          _mouseXYs = mouse_cont.getPos();
          mouse_cont.x.push(_mouseXYs[0]);
          mouse_cont.y.push(_mouseXYs[1]);
          mouse_cont.leftButton.push(_mouseButtons[0]);
          mouse_cont.midButton.push(_mouseButtons[1]);
          mouse_cont.rightButton.push(_mouseButtons[2]);
          mouse_cont.time.push(mouse_cont.mouseClock.getTime());
          // abort routine on response
          continueRoutine = false;
        }
      }
    }
    // start/stop sound_8
    if (t >= 5 && sound_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sound_8.tStart = t;  // (not accounting for frame time here)
      sound_8.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ sound_8.play(); });  // screen flip
      sound_8.status = PsychoJS.Status.STARTED;
    }
    frameRemains = 5 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (sound_8.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      if (10 > 0.5) {
        sound_8.stop();  // stop the sound (if longer than duration)
      }
      sound_8.status = PsychoJS.Status.FINISHED;
    }
    
    // *key_resp_3* updates
    if (t >= 0.0 && key_resp_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_3.tStart = t;  // (not accounting for frame time here)
      key_resp_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      key_resp_3.clock.reset();
      key_resp_3.start();
    }

    frameRemains = 0.0 + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_resp_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp_3.status = PsychoJS.Status.FINISHED;
  }

    if (key_resp_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_3.getKeys({keyList: ['p'], waitRelease: false});
      _key_resp_3_allKeys = _key_resp_3_allKeys.concat(theseKeys);
      if (_key_resp_3_allKeys.length > 0) {
        key_resp_3.keys = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].name;  // just the last key pressed
        key_resp_3.rt = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of TEST_contrastComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function TEST_contrastRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'TEST_contrast' ---
    for (const thisComponent of TEST_contrastComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for psychoJS.experiment (ExperimentHandler)
    if (mouse_cont.x) {  psychoJS.experiment.addData('mouse_cont.x', mouse_cont.x[0])};
    if (mouse_cont.y) {  psychoJS.experiment.addData('mouse_cont.y', mouse_cont.y[0])};
    if (mouse_cont.leftButton) {  psychoJS.experiment.addData('mouse_cont.leftButton', mouse_cont.leftButton[0])};
    if (mouse_cont.midButton) {  psychoJS.experiment.addData('mouse_cont.midButton', mouse_cont.midButton[0])};
    if (mouse_cont.rightButton) {  psychoJS.experiment.addData('mouse_cont.rightButton', mouse_cont.rightButton[0])};
    if (mouse_cont.time) {  psychoJS.experiment.addData('mouse_cont.time', mouse_cont.time[0])};
    if (mouse_cont.clicked_name) {  psychoJS.experiment.addData('mouse_cont.clicked_name', mouse_cont.clicked_name[0])};
    
    sound_8.stop();  // ensure sound has stopped at end of routine
    key_resp_3.stop();
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Ebbing_INTROComponents;
function Ebbing_INTRORoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Ebbing_INTRO' ---
    t = 0;
    Ebbing_INTROClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    sound_5.setVolume(1.0);
    // keep track of which components have finished
    Ebbing_INTROComponents = [];
    Ebbing_INTROComponents.push(ebbing_intro_text);
    Ebbing_INTROComponents.push(sound_5);
    Ebbing_INTROComponents.push(START_ebbing);
    
    for (const thisComponent of Ebbing_INTROComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Ebbing_INTRORoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Ebbing_INTRO' ---
    // get current time
    t = Ebbing_INTROClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *ebbing_intro_text* updates
    if (t >= 1 && ebbing_intro_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ebbing_intro_text.tStart = t;  // (not accounting for frame time here)
      ebbing_intro_text.frameNStart = frameN;  // exact frame index
      
      ebbing_intro_text.setAutoDraw(true);
    }

    // start/stop sound_5
    if (t >= 1 && sound_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sound_5.tStart = t;  // (not accounting for frame time here)
      sound_5.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ sound_5.play(); });  // screen flip
      sound_5.status = PsychoJS.Status.STARTED;
    }
    if (t >= (sound_5.getDuration() + sound_5.tStart)     && sound_5.status === PsychoJS.Status.STARTED) {
      sound_5.stop();  // stop the sound (if longer than duration)
      sound_5.status = PsychoJS.Status.FINISHED;
    }
    
    // *START_ebbing* updates
    if (t >= 1 && START_ebbing.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      START_ebbing.tStart = t;  // (not accounting for frame time here)
      START_ebbing.frameNStart = frameN;  // exact frame index
      
      START_ebbing.setAutoDraw(true);
    }

    if (START_ebbing.status === PsychoJS.Status.STARTED) {
      // check whether START_ebbing has been pressed
      if (START_ebbing.isClicked) {
        if (!START_ebbing.wasClicked) {
          // store time of first click
          START_ebbing.timesOn.push(START_ebbing.clock.getTime());
          START_ebbing.numClicks += 1;
          // store time clicked until
          START_ebbing.timesOff.push(START_ebbing.clock.getTime());
        } else {
          // update time clicked until;
          START_ebbing.timesOff[START_ebbing.timesOff.length - 1] = START_ebbing.clock.getTime();
        }
        if (!START_ebbing.wasClicked) {
          // end routine when START_ebbing is clicked
          continueRoutine = false;
        }
        // if START_ebbing is still clicked next frame, it is not a new click
        START_ebbing.wasClicked = true;
      } else {
        // if START_ebbing is clicked next frame, it is a new click
        START_ebbing.wasClicked = false;
      }
    } else {
      // keep clock at 0 if START_ebbing hasn't started / has finished
      START_ebbing.clock.reset();
      // if START_ebbing is clicked next frame, it is a new click
      START_ebbing.wasClicked = false;
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Ebbing_INTROComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Ebbing_INTRORoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Ebbing_INTRO' ---
    for (const thisComponent of Ebbing_INTROComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    sound_5.stop();  // ensure sound has stopped at end of routine
    psychoJS.experiment.addData('START_ebbing.numClicks', START_ebbing.numClicks);
    psychoJS.experiment.addData('START_ebbing.timesOn', START_ebbing.timesOn);
    psychoJS.experiment.addData('START_ebbing.timesOff', START_ebbing.timesOff);
    // the Routine "Ebbing_INTRO" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_4_allKeys;
var TEST_ebbingComponents;
function TEST_ebbingRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'TEST_ebbing' ---
    t = 0;
    TEST_ebbingClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(15.100000);
    // update component parameters for each repeat
    image_ebbing.setImage(path);
    // setup some python lists for storing info about the mouse_ebbing
    // current position of the mouse:
    mouse_ebbing.x = [];
    mouse_ebbing.y = [];
    mouse_ebbing.leftButton = [];
    mouse_ebbing.midButton = [];
    mouse_ebbing.rightButton = [];
    mouse_ebbing.time = [];
    mouse_ebbing.clicked_name = [];
    gotValidClick = false; // until a click is received
    sound_9.secs=10;
    sound_9.setVolume(1.0);
    key_resp_4.keys = undefined;
    key_resp_4.rt = undefined;
    _key_resp_4_allKeys = [];
    // keep track of which components have finished
    TEST_ebbingComponents = [];
    TEST_ebbingComponents.push(RIGHT_ebbing);
    TEST_ebbingComponents.push(LEFT_ebbing);
    TEST_ebbingComponents.push(image_ebbing);
    TEST_ebbingComponents.push(mouse_ebbing);
    TEST_ebbingComponents.push(sound_9);
    TEST_ebbingComponents.push(key_resp_4);
    
    for (const thisComponent of TEST_ebbingComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function TEST_ebbingRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'TEST_ebbing' ---
    // get current time
    t = TEST_ebbingClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *RIGHT_ebbing* updates
    if (t >= 0 && RIGHT_ebbing.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      RIGHT_ebbing.tStart = t;  // (not accounting for frame time here)
      RIGHT_ebbing.frameNStart = frameN;  // exact frame index
      
      RIGHT_ebbing.setAutoDraw(true);
    }

    frameRemains = 0 + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (RIGHT_ebbing.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      RIGHT_ebbing.setAutoDraw(false);
    }
    
    // *LEFT_ebbing* updates
    if (t >= 0 && LEFT_ebbing.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      LEFT_ebbing.tStart = t;  // (not accounting for frame time here)
      LEFT_ebbing.frameNStart = frameN;  // exact frame index
      
      LEFT_ebbing.setAutoDraw(true);
    }

    frameRemains = 0 + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (LEFT_ebbing.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      LEFT_ebbing.setAutoDraw(false);
    }
    
    // *image_ebbing* updates
    if (t >= 0.1 && image_ebbing.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_ebbing.tStart = t;  // (not accounting for frame time here)
      image_ebbing.frameNStart = frameN;  // exact frame index
      
      image_ebbing.setAutoDraw(true);
    }

    frameRemains = 0.1 + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_ebbing.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_ebbing.setAutoDraw(false);
    }
    // *mouse_ebbing* updates
    if (t >= 0 && mouse_ebbing.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_ebbing.tStart = t;  // (not accounting for frame time here)
      mouse_ebbing.frameNStart = frameN;  // exact frame index
      
      mouse_ebbing.status = PsychoJS.Status.STARTED;
      mouse_ebbing.mouseClock.reset();
      prevButtonState = mouse_ebbing.getPressed();  // if button is down already this ISN'T a new click
      }
    frameRemains = 0 + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (mouse_ebbing.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      mouse_ebbing.status = PsychoJS.Status.FINISHED;
  }
    if (mouse_ebbing.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_ebbing.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [LEFT_ebbing, RIGHT_ebbing]) {
            if (obj.contains(mouse_ebbing)) {
              gotValidClick = true;
              mouse_ebbing.clicked_name.push(obj.name)
            }
          }
          _mouseXYs = mouse_ebbing.getPos();
          mouse_ebbing.x.push(_mouseXYs[0]);
          mouse_ebbing.y.push(_mouseXYs[1]);
          mouse_ebbing.leftButton.push(_mouseButtons[0]);
          mouse_ebbing.midButton.push(_mouseButtons[1]);
          mouse_ebbing.rightButton.push(_mouseButtons[2]);
          mouse_ebbing.time.push(mouse_ebbing.mouseClock.getTime());
          // abort routine on response
          continueRoutine = false;
        }
      }
    }
    // start/stop sound_9
    if (t >= 5 && sound_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sound_9.tStart = t;  // (not accounting for frame time here)
      sound_9.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ sound_9.play(); });  // screen flip
      sound_9.status = PsychoJS.Status.STARTED;
    }
    frameRemains = 5 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (sound_9.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      if (10 > 0.5) {
        sound_9.stop();  // stop the sound (if longer than duration)
      }
      sound_9.status = PsychoJS.Status.FINISHED;
    }
    
    // *key_resp_4* updates
    if (t >= 0.0 && key_resp_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_4.tStart = t;  // (not accounting for frame time here)
      key_resp_4.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      key_resp_4.clock.reset();
      key_resp_4.start();
    }

    frameRemains = 0.0 + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_resp_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp_4.status = PsychoJS.Status.FINISHED;
  }

    if (key_resp_4.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_4.getKeys({keyList: ['p'], waitRelease: false});
      _key_resp_4_allKeys = _key_resp_4_allKeys.concat(theseKeys);
      if (_key_resp_4_allKeys.length > 0) {
        key_resp_4.keys = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].name;  // just the last key pressed
        key_resp_4.rt = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of TEST_ebbingComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function TEST_ebbingRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'TEST_ebbing' ---
    for (const thisComponent of TEST_ebbingComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for psychoJS.experiment (ExperimentHandler)
    if (mouse_ebbing.x) {  psychoJS.experiment.addData('mouse_ebbing.x', mouse_ebbing.x[0])};
    if (mouse_ebbing.y) {  psychoJS.experiment.addData('mouse_ebbing.y', mouse_ebbing.y[0])};
    if (mouse_ebbing.leftButton) {  psychoJS.experiment.addData('mouse_ebbing.leftButton', mouse_ebbing.leftButton[0])};
    if (mouse_ebbing.midButton) {  psychoJS.experiment.addData('mouse_ebbing.midButton', mouse_ebbing.midButton[0])};
    if (mouse_ebbing.rightButton) {  psychoJS.experiment.addData('mouse_ebbing.rightButton', mouse_ebbing.rightButton[0])};
    if (mouse_ebbing.time) {  psychoJS.experiment.addData('mouse_ebbing.time', mouse_ebbing.time[0])};
    if (mouse_ebbing.clicked_name) {  psychoJS.experiment.addData('mouse_ebbing.clicked_name', mouse_ebbing.clicked_name[0])};
    
    sound_9.stop();  // ensure sound has stopped at end of routine
    key_resp_4.stop();
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Kanizsa_INTROComponents;
function Kanizsa_INTRORoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Kanizsa_INTRO' ---
    t = 0;
    Kanizsa_INTROClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    sound_6.setVolume(1.0);
    // keep track of which components have finished
    Kanizsa_INTROComponents = [];
    Kanizsa_INTROComponents.push(kanizsa_intro_text);
    Kanizsa_INTROComponents.push(sound_6);
    Kanizsa_INTROComponents.push(START_KN);
    
    for (const thisComponent of Kanizsa_INTROComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Kanizsa_INTRORoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Kanizsa_INTRO' ---
    // get current time
    t = Kanizsa_INTROClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *kanizsa_intro_text* updates
    if (t >= 1 && kanizsa_intro_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      kanizsa_intro_text.tStart = t;  // (not accounting for frame time here)
      kanizsa_intro_text.frameNStart = frameN;  // exact frame index
      
      kanizsa_intro_text.setAutoDraw(true);
    }

    // start/stop sound_6
    if (t >= 1 && sound_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sound_6.tStart = t;  // (not accounting for frame time here)
      sound_6.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ sound_6.play(); });  // screen flip
      sound_6.status = PsychoJS.Status.STARTED;
    }
    if (t >= (sound_6.getDuration() + sound_6.tStart)     && sound_6.status === PsychoJS.Status.STARTED) {
      sound_6.stop();  // stop the sound (if longer than duration)
      sound_6.status = PsychoJS.Status.FINISHED;
    }
    
    // *START_KN* updates
    if (t >= 1 && START_KN.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      START_KN.tStart = t;  // (not accounting for frame time here)
      START_KN.frameNStart = frameN;  // exact frame index
      
      START_KN.setAutoDraw(true);
    }

    if (START_KN.status === PsychoJS.Status.STARTED) {
      // check whether START_KN has been pressed
      if (START_KN.isClicked) {
        if (!START_KN.wasClicked) {
          // store time of first click
          START_KN.timesOn.push(START_KN.clock.getTime());
          START_KN.numClicks += 1;
          // store time clicked until
          START_KN.timesOff.push(START_KN.clock.getTime());
        } else {
          // update time clicked until;
          START_KN.timesOff[START_KN.timesOff.length - 1] = START_KN.clock.getTime();
        }
        if (!START_KN.wasClicked) {
          // end routine when START_KN is clicked
          continueRoutine = false;
        }
        // if START_KN is still clicked next frame, it is not a new click
        START_KN.wasClicked = true;
      } else {
        // if START_KN is clicked next frame, it is a new click
        START_KN.wasClicked = false;
      }
    } else {
      // keep clock at 0 if START_KN hasn't started / has finished
      START_KN.clock.reset();
      // if START_KN is clicked next frame, it is a new click
      START_KN.wasClicked = false;
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Kanizsa_INTROComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Kanizsa_INTRORoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Kanizsa_INTRO' ---
    for (const thisComponent of Kanizsa_INTROComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    sound_6.stop();  // ensure sound has stopped at end of routine
    psychoJS.experiment.addData('START_KN.numClicks', START_KN.numClicks);
    psychoJS.experiment.addData('START_KN.timesOn', START_KN.timesOn);
    psychoJS.experiment.addData('START_KN.timesOff', START_KN.timesOff);
    // the Routine "Kanizsa_INTRO" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var trainingKZSComponents;
function trainingKZSRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trainingKZS' ---
    t = 0;
    trainingKZSClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_2
    mouse_2.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    trainingKZSComponents = [];
    trainingKZSComponents.push(triangle);
    trainingKZSComponents.push(threefourth);
    trainingKZSComponents.push(twofourth);
    trainingKZSComponents.push(whitesquare);
    trainingKZSComponents.push(mouse_2);
    
    for (const thisComponent of trainingKZSComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function trainingKZSRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trainingKZS' ---
    // get current time
    t = trainingKZSClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *triangle* updates
    if (t >= 0.0 && triangle.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      triangle.tStart = t;  // (not accounting for frame time here)
      triangle.frameNStart = frameN;  // exact frame index
      
      triangle.setAutoDraw(true);
    }

    
    // *threefourth* updates
    if (t >= 0.0 && threefourth.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      threefourth.tStart = t;  // (not accounting for frame time here)
      threefourth.frameNStart = frameN;  // exact frame index
      
      threefourth.setAutoDraw(true);
    }

    
    // *twofourth* updates
    if (t >= 0.0 && twofourth.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      twofourth.tStart = t;  // (not accounting for frame time here)
      twofourth.frameNStart = frameN;  // exact frame index
      
      twofourth.setAutoDraw(true);
    }

    
    // *whitesquare* updates
    if (t >= 0.0 && whitesquare.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      whitesquare.tStart = t;  // (not accounting for frame time here)
      whitesquare.frameNStart = frameN;  // exact frame index
      
      whitesquare.setAutoDraw(true);
    }

    // *mouse_2* updates
    if (t >= 0.0 && mouse_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_2.tStart = t;  // (not accounting for frame time here)
      mouse_2.frameNStart = frameN;  // exact frame index
      
      mouse_2.status = PsychoJS.Status.STARTED;
      mouse_2.mouseClock.reset();
      prevButtonState = mouse_2.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_2.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_2.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [whitesquare]) {
            if (obj.contains(mouse_2)) {
              gotValidClick = true;
              mouse_2.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of trainingKZSComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trainingKZSRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trainingKZS' ---
    for (const thisComponent of trainingKZSComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for psychoJS.experiment (ExperimentHandler)
    _mouseXYs = mouse_2.getPos();
    _mouseButtons = mouse_2.getPressed();
    psychoJS.experiment.addData('mouse_2.x', _mouseXYs[0]);
    psychoJS.experiment.addData('mouse_2.y', _mouseXYs[1]);
    psychoJS.experiment.addData('mouse_2.leftButton', _mouseButtons[0]);
    psychoJS.experiment.addData('mouse_2.midButton', _mouseButtons[1]);
    psychoJS.experiment.addData('mouse_2.rightButton', _mouseButtons[2]);
    if (mouse_2.clicked_name.length > 0) {
      psychoJS.experiment.addData('mouse_2.clicked_name', mouse_2.clicked_name[0]);}
    // the Routine "trainingKZS" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var trainingKZS_2Components;
function trainingKZS_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trainingKZS_2' ---
    t = 0;
    trainingKZS_2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_3
    mouse_3.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    trainingKZS_2Components = [];
    trainingKZS_2Components.push(triangle_2);
    trainingKZS_2Components.push(threefourth_2);
    trainingKZS_2Components.push(twofourth_2);
    trainingKZS_2Components.push(whitesquare_2);
    trainingKZS_2Components.push(mouse_3);
    
    for (const thisComponent of trainingKZS_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function trainingKZS_2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trainingKZS_2' ---
    // get current time
    t = trainingKZS_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *triangle_2* updates
    if (t >= 0.0 && triangle_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      triangle_2.tStart = t;  // (not accounting for frame time here)
      triangle_2.frameNStart = frameN;  // exact frame index
      
      triangle_2.setAutoDraw(true);
    }

    
    // *threefourth_2* updates
    if (t >= 0.0 && threefourth_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      threefourth_2.tStart = t;  // (not accounting for frame time here)
      threefourth_2.frameNStart = frameN;  // exact frame index
      
      threefourth_2.setAutoDraw(true);
    }

    
    // *twofourth_2* updates
    if (t >= 0.0 && twofourth_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      twofourth_2.tStart = t;  // (not accounting for frame time here)
      twofourth_2.frameNStart = frameN;  // exact frame index
      
      twofourth_2.setAutoDraw(true);
    }

    
    // *whitesquare_2* updates
    if (t >= 0.0 && whitesquare_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      whitesquare_2.tStart = t;  // (not accounting for frame time here)
      whitesquare_2.frameNStart = frameN;  // exact frame index
      
      whitesquare_2.setAutoDraw(true);
    }

    // *mouse_3* updates
    if (t >= 0.0 && mouse_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_3.tStart = t;  // (not accounting for frame time here)
      mouse_3.frameNStart = frameN;  // exact frame index
      
      mouse_3.status = PsychoJS.Status.STARTED;
      mouse_3.mouseClock.reset();
      prevButtonState = mouse_3.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_3.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_3.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [whitesquare_2]) {
            if (obj.contains(mouse_3)) {
              gotValidClick = true;
              mouse_3.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of trainingKZS_2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trainingKZS_2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trainingKZS_2' ---
    for (const thisComponent of trainingKZS_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for psychoJS.experiment (ExperimentHandler)
    _mouseXYs = mouse_3.getPos();
    _mouseButtons = mouse_3.getPressed();
    psychoJS.experiment.addData('mouse_3.x', _mouseXYs[0]);
    psychoJS.experiment.addData('mouse_3.y', _mouseXYs[1]);
    psychoJS.experiment.addData('mouse_3.leftButton', _mouseButtons[0]);
    psychoJS.experiment.addData('mouse_3.midButton', _mouseButtons[1]);
    psychoJS.experiment.addData('mouse_3.rightButton', _mouseButtons[2]);
    if (mouse_3.clicked_name.length > 0) {
      psychoJS.experiment.addData('mouse_3.clicked_name', mouse_3.clicked_name[0]);}
    // the Routine "trainingKZS_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_5_allKeys;
var TEST_knzsComponents;
function TEST_knzsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'TEST_knzs' ---
    t = 0;
    TEST_knzsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(15.100000);
    // update component parameters for each repeat
    image_KN.setImage(path);
    // setup some python lists for storing info about the mouse_KN
    // current position of the mouse:
    mouse_KN.x = [];
    mouse_KN.y = [];
    mouse_KN.leftButton = [];
    mouse_KN.midButton = [];
    mouse_KN.rightButton = [];
    mouse_KN.time = [];
    mouse_KN.clicked_name = [];
    gotValidClick = false; // until a click is received
    sound_11.secs=10;
    sound_11.setVolume(1.0);
    key_resp_5.keys = undefined;
    key_resp_5.rt = undefined;
    _key_resp_5_allKeys = [];
    // keep track of which components have finished
    TEST_knzsComponents = [];
    TEST_knzsComponents.push(image_KN);
    TEST_knzsComponents.push(LEFT_KN);
    TEST_knzsComponents.push(RIGHT_KN);
    TEST_knzsComponents.push(mouse_KN);
    TEST_knzsComponents.push(sound_11);
    TEST_knzsComponents.push(key_resp_5);
    
    for (const thisComponent of TEST_knzsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function TEST_knzsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'TEST_knzs' ---
    // get current time
    t = TEST_knzsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_KN* updates
    if (t >= 0.1 && image_KN.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_KN.tStart = t;  // (not accounting for frame time here)
      image_KN.frameNStart = frameN;  // exact frame index
      
      image_KN.setAutoDraw(true);
    }

    frameRemains = 0.1 + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_KN.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_KN.setAutoDraw(false);
    }
    
    // *LEFT_KN* updates
    if (t >= 0 && LEFT_KN.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      LEFT_KN.tStart = t;  // (not accounting for frame time here)
      LEFT_KN.frameNStart = frameN;  // exact frame index
      
      LEFT_KN.setAutoDraw(true);
    }

    frameRemains = 0 + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (LEFT_KN.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      LEFT_KN.setAutoDraw(false);
    }
    
    // *RIGHT_KN* updates
    if (t >= 0 && RIGHT_KN.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      RIGHT_KN.tStart = t;  // (not accounting for frame time here)
      RIGHT_KN.frameNStart = frameN;  // exact frame index
      
      RIGHT_KN.setAutoDraw(true);
    }

    frameRemains = 0 + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (RIGHT_KN.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      RIGHT_KN.setAutoDraw(false);
    }
    // *mouse_KN* updates
    if (t >= 0 && mouse_KN.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_KN.tStart = t;  // (not accounting for frame time here)
      mouse_KN.frameNStart = frameN;  // exact frame index
      
      mouse_KN.status = PsychoJS.Status.STARTED;
      mouse_KN.mouseClock.reset();
      prevButtonState = mouse_KN.getPressed();  // if button is down already this ISN'T a new click
      }
    frameRemains = 0 + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (mouse_KN.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      mouse_KN.status = PsychoJS.Status.FINISHED;
  }
    if (mouse_KN.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_KN.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [LEFT_MS, RIGHT_MS]) {
            if (obj.contains(mouse_KN)) {
              gotValidClick = true;
              mouse_KN.clicked_name.push(obj.name)
            }
          }
          _mouseXYs = mouse_KN.getPos();
          mouse_KN.x.push(_mouseXYs[0]);
          mouse_KN.y.push(_mouseXYs[1]);
          mouse_KN.leftButton.push(_mouseButtons[0]);
          mouse_KN.midButton.push(_mouseButtons[1]);
          mouse_KN.rightButton.push(_mouseButtons[2]);
          mouse_KN.time.push(mouse_KN.mouseClock.getTime());
          // abort routine on response
          continueRoutine = false;
        }
      }
    }
    // start/stop sound_11
    if (t >= 5 && sound_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sound_11.tStart = t;  // (not accounting for frame time here)
      sound_11.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ sound_11.play(); });  // screen flip
      sound_11.status = PsychoJS.Status.STARTED;
    }
    frameRemains = 5 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (sound_11.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      if (10 > 0.5) {
        sound_11.stop();  // stop the sound (if longer than duration)
      }
      sound_11.status = PsychoJS.Status.FINISHED;
    }
    
    // *key_resp_5* updates
    if (t >= 0.0 && key_resp_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_5.tStart = t;  // (not accounting for frame time here)
      key_resp_5.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      key_resp_5.clock.reset();
      key_resp_5.start();
    }

    frameRemains = 0.0 + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_resp_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp_5.status = PsychoJS.Status.FINISHED;
  }

    if (key_resp_5.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_5.getKeys({keyList: ['p'], waitRelease: false});
      _key_resp_5_allKeys = _key_resp_5_allKeys.concat(theseKeys);
      if (_key_resp_5_allKeys.length > 0) {
        key_resp_5.keys = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].name;  // just the last key pressed
        key_resp_5.rt = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of TEST_knzsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function TEST_knzsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'TEST_knzs' ---
    for (const thisComponent of TEST_knzsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for psychoJS.experiment (ExperimentHandler)
    if (mouse_KN.x) {  psychoJS.experiment.addData('mouse_KN.x', mouse_KN.x[0])};
    if (mouse_KN.y) {  psychoJS.experiment.addData('mouse_KN.y', mouse_KN.y[0])};
    if (mouse_KN.leftButton) {  psychoJS.experiment.addData('mouse_KN.leftButton', mouse_KN.leftButton[0])};
    if (mouse_KN.midButton) {  psychoJS.experiment.addData('mouse_KN.midButton', mouse_KN.midButton[0])};
    if (mouse_KN.rightButton) {  psychoJS.experiment.addData('mouse_KN.rightButton', mouse_KN.rightButton[0])};
    if (mouse_KN.time) {  psychoJS.experiment.addData('mouse_KN.time', mouse_KN.time[0])};
    if (mouse_KN.clicked_name) {  psychoJS.experiment.addData('mouse_KN.clicked_name', mouse_KN.clicked_name[0])};
    
    sound_11.stop();  // ensure sound has stopped at end of routine
    key_resp_5.stop();
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var MS_INTROComponents;
function MS_INTRORoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'MS_INTRO' ---
    t = 0;
    MS_INTROClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    sound_7.setVolume(1.0);
    // keep track of which components have finished
    MS_INTROComponents = [];
    MS_INTROComponents.push(MS_intro_text);
    MS_INTROComponents.push(sound_7);
    MS_INTROComponents.push(START_MS);
    
    for (const thisComponent of MS_INTROComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function MS_INTRORoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'MS_INTRO' ---
    // get current time
    t = MS_INTROClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *MS_intro_text* updates
    if (t >= 1 && MS_intro_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      MS_intro_text.tStart = t;  // (not accounting for frame time here)
      MS_intro_text.frameNStart = frameN;  // exact frame index
      
      MS_intro_text.setAutoDraw(true);
    }

    // start/stop sound_7
    if (t >= 1 && sound_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sound_7.tStart = t;  // (not accounting for frame time here)
      sound_7.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ sound_7.play(); });  // screen flip
      sound_7.status = PsychoJS.Status.STARTED;
    }
    if (t >= (sound_7.getDuration() + sound_7.tStart)     && sound_7.status === PsychoJS.Status.STARTED) {
      sound_7.stop();  // stop the sound (if longer than duration)
      sound_7.status = PsychoJS.Status.FINISHED;
    }
    
    // *START_MS* updates
    if (t >= 1 && START_MS.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      START_MS.tStart = t;  // (not accounting for frame time here)
      START_MS.frameNStart = frameN;  // exact frame index
      
      START_MS.setAutoDraw(true);
    }

    if (START_MS.status === PsychoJS.Status.STARTED) {
      // check whether START_MS has been pressed
      if (START_MS.isClicked) {
        if (!START_MS.wasClicked) {
          // store time of first click
          START_MS.timesOn.push(START_MS.clock.getTime());
          START_MS.numClicks += 1;
          // store time clicked until
          START_MS.timesOff.push(START_MS.clock.getTime());
        } else {
          // update time clicked until;
          START_MS.timesOff[START_MS.timesOff.length - 1] = START_MS.clock.getTime();
        }
        if (!START_MS.wasClicked) {
          // end routine when START_MS is clicked
          continueRoutine = false;
        }
        // if START_MS is still clicked next frame, it is not a new click
        START_MS.wasClicked = true;
      } else {
        // if START_MS is clicked next frame, it is a new click
        START_MS.wasClicked = false;
      }
    } else {
      // keep clock at 0 if START_MS hasn't started / has finished
      START_MS.clock.reset();
      // if START_MS is clicked next frame, it is a new click
      START_MS.wasClicked = false;
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of MS_INTROComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function MS_INTRORoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'MS_INTRO' ---
    for (const thisComponent of MS_INTROComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    sound_7.stop();  // ensure sound has stopped at end of routine
    psychoJS.experiment.addData('START_MS.numClicks', START_MS.numClicks);
    psychoJS.experiment.addData('START_MS.timesOn', START_MS.timesOn);
    psychoJS.experiment.addData('START_MS.timesOff', START_MS.timesOff);
    // the Routine "MS_INTRO" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_6_allKeys;
var TEST_MSComponents;
function TEST_MSRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'TEST_MS' ---
    t = 0;
    TEST_MSClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(15.100000);
    // update component parameters for each repeat
    image_MS.setImage(path);
    // setup some python lists for storing info about the mouse_MS
    // current position of the mouse:
    mouse_MS.x = [];
    mouse_MS.y = [];
    mouse_MS.leftButton = [];
    mouse_MS.midButton = [];
    mouse_MS.rightButton = [];
    mouse_MS.time = [];
    mouse_MS.clicked_name = [];
    gotValidClick = false; // until a click is received
    sound_10.secs=10;
    sound_10.setVolume(1.0);
    key_resp_6.keys = undefined;
    key_resp_6.rt = undefined;
    _key_resp_6_allKeys = [];
    // keep track of which components have finished
    TEST_MSComponents = [];
    TEST_MSComponents.push(image_MS);
    TEST_MSComponents.push(LEFT_MS);
    TEST_MSComponents.push(RIGHT_MS);
    TEST_MSComponents.push(mouse_MS);
    TEST_MSComponents.push(sound_10);
    TEST_MSComponents.push(key_resp_6);
    
    for (const thisComponent of TEST_MSComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function TEST_MSRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'TEST_MS' ---
    // get current time
    t = TEST_MSClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_MS* updates
    if (t >= 0.1 && image_MS.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_MS.tStart = t;  // (not accounting for frame time here)
      image_MS.frameNStart = frameN;  // exact frame index
      
      image_MS.setAutoDraw(true);
    }

    frameRemains = 0.1 + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_MS.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_MS.setAutoDraw(false);
    }
    
    // *LEFT_MS* updates
    if (t >= 0 && LEFT_MS.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      LEFT_MS.tStart = t;  // (not accounting for frame time here)
      LEFT_MS.frameNStart = frameN;  // exact frame index
      
      LEFT_MS.setAutoDraw(true);
    }

    frameRemains = 0 + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (LEFT_MS.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      LEFT_MS.setAutoDraw(false);
    }
    
    // *RIGHT_MS* updates
    if (t >= 0 && RIGHT_MS.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      RIGHT_MS.tStart = t;  // (not accounting for frame time here)
      RIGHT_MS.frameNStart = frameN;  // exact frame index
      
      RIGHT_MS.setAutoDraw(true);
    }

    frameRemains = 0 + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (RIGHT_MS.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      RIGHT_MS.setAutoDraw(false);
    }
    // *mouse_MS* updates
    if (t >= 0 && mouse_MS.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_MS.tStart = t;  // (not accounting for frame time here)
      mouse_MS.frameNStart = frameN;  // exact frame index
      
      mouse_MS.status = PsychoJS.Status.STARTED;
      mouse_MS.mouseClock.reset();
      prevButtonState = mouse_MS.getPressed();  // if button is down already this ISN'T a new click
      }
    frameRemains = 0 + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (mouse_MS.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      mouse_MS.status = PsychoJS.Status.FINISHED;
  }
    if (mouse_MS.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_MS.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [LEFT_MS, RIGHT_MS]) {
            if (obj.contains(mouse_MS)) {
              gotValidClick = true;
              mouse_MS.clicked_name.push(obj.name)
            }
          }
          _mouseXYs = mouse_MS.getPos();
          mouse_MS.x.push(_mouseXYs[0]);
          mouse_MS.y.push(_mouseXYs[1]);
          mouse_MS.leftButton.push(_mouseButtons[0]);
          mouse_MS.midButton.push(_mouseButtons[1]);
          mouse_MS.rightButton.push(_mouseButtons[2]);
          mouse_MS.time.push(mouse_MS.mouseClock.getTime());
          // abort routine on response
          continueRoutine = false;
        }
      }
    }
    // start/stop sound_10
    if (t >= 5 && sound_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sound_10.tStart = t;  // (not accounting for frame time here)
      sound_10.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ sound_10.play(); });  // screen flip
      sound_10.status = PsychoJS.Status.STARTED;
    }
    frameRemains = 5 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (sound_10.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      if (10 > 0.5) {
        sound_10.stop();  // stop the sound (if longer than duration)
      }
      sound_10.status = PsychoJS.Status.FINISHED;
    }
    
    // *key_resp_6* updates
    if (t >= 0.0 && key_resp_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_6.tStart = t;  // (not accounting for frame time here)
      key_resp_6.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      key_resp_6.clock.reset();
      key_resp_6.start();
    }

    frameRemains = 0.0 + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_resp_6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp_6.status = PsychoJS.Status.FINISHED;
  }

    if (key_resp_6.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_6.getKeys({keyList: ['p'], waitRelease: false});
      _key_resp_6_allKeys = _key_resp_6_allKeys.concat(theseKeys);
      if (_key_resp_6_allKeys.length > 0) {
        key_resp_6.keys = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].name;  // just the last key pressed
        key_resp_6.rt = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of TEST_MSComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function TEST_MSRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'TEST_MS' ---
    for (const thisComponent of TEST_MSComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for psychoJS.experiment (ExperimentHandler)
    if (mouse_MS.x) {  psychoJS.experiment.addData('mouse_MS.x', mouse_MS.x[0])};
    if (mouse_MS.y) {  psychoJS.experiment.addData('mouse_MS.y', mouse_MS.y[0])};
    if (mouse_MS.leftButton) {  psychoJS.experiment.addData('mouse_MS.leftButton', mouse_MS.leftButton[0])};
    if (mouse_MS.midButton) {  psychoJS.experiment.addData('mouse_MS.midButton', mouse_MS.midButton[0])};
    if (mouse_MS.rightButton) {  psychoJS.experiment.addData('mouse_MS.rightButton', mouse_MS.rightButton[0])};
    if (mouse_MS.time) {  psychoJS.experiment.addData('mouse_MS.time', mouse_MS.time[0])};
    if (mouse_MS.clicked_name) {  psychoJS.experiment.addData('mouse_MS.clicked_name', mouse_MS.clicked_name[0])};
    
    sound_10.stop();  // ensure sound has stopped at end of routine
    key_resp_6.stop();
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var byeComponents;
function byeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'bye' ---
    t = 0;
    byeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    byeComponents = [];
    byeComponents.push(text_2);
    byeComponents.push(mouse);
    
    for (const thisComponent of byeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function byeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'bye' ---
    // get current time
    t = byeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_2* updates
    if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }

    // *mouse* updates
    if (t >= 0.5 && mouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse.tStart = t;  // (not accounting for frame time here)
      mouse.frameNStart = frameN;  // exact frame index
      
      mouse.status = PsychoJS.Status.STARTED;
      prevButtonState = mouse.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // abort routine on response
          continueRoutine = false;
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of byeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function byeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'bye' ---
    for (const thisComponent of byeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for psychoJS.experiment (ExperimentHandler)
    _mouseXYs = mouse.getPos();
    _mouseButtons = mouse.getPressed();
    psychoJS.experiment.addData('mouse.x', _mouseXYs[0]);
    psychoJS.experiment.addData('mouse.y', _mouseXYs[1]);
    psychoJS.experiment.addData('mouse.leftButton', _mouseButtons[0]);
    psychoJS.experiment.addData('mouse.midButton', _mouseButtons[1]);
    psychoJS.experiment.addData('mouse.rightButton', _mouseButtons[2]);
    // the Routine "bye" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
