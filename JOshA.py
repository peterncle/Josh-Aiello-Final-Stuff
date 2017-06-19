from earsketch import *
 
init()
setTempo(120) 
music1=RD_POP_ARPBASS_4
music2=YG_FUNK_BRASS_2
music3=HIPHOP_BASSSUB_002
music4=ELECTRO_ANALOGUE_BASS_001
music5=ELECTRO_ANALOGUE_LEAD_013
music6=EIGHT_BIT_ATARI_LEAD_001
music7=YG_NEW_FUNK_ELECTRIC_PIANO_1
music8=EIGHT_BIT_ANALOG_DRUM_LOOP_018
music9=RD_POP_MAINBEAT_9
music10=RD_POP_PADCHORD_2
music11=RD_EDM_ANALOGPLUCK_1

makeBeat(HIPHOP_SOLOMOOGLEAD_001, 3, 4, "0++-0---0+++0---");


fitMedia(music1,1,1,9)
fitMedia(music2,2,3,9)
fitMedia(music3,3,8,20)
fitMedia(music4,2,10,15)
fitMedia(music5,1,15,20)
fitMedia(music6,2,20,25)
fitMedia(music7,1,25,35)
fitMedia(music8,3,30,35)
fitMedia(music9,2,35,40)
fitMedia(music10,1,40,50)
fitMedia(music11,3,45,50)

setEffect(3, VOLUME, GAIN, -40, 1, 5, 5)


finish()