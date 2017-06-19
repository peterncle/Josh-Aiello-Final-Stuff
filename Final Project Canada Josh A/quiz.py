        #The Great Canadian Quiz program by Josh Aiello
        #this is a trivia word game

#imports modules

from random import shuffle  #to shuffle quiz questions
import sys      #system commands
import os       #for operating system commands
import pygame   #for graphics
import winsound #for sound effects
import time     #for time commands


os.system('cls') #clear screen

#tuples for each level of the game, each tuple follows question answer format.
quesAns1 = [
    ('What city is the Capital of Canada? ', 'ottawa'),
    ('Which province does the city Mississauga reside in? ', 'ontario'),
    ('How many territories does Canada have in total? ', '3'),
    ('What do the letters CBC stand for? ', 'canadian broadcasting corporation'),
    ('What is Canada\'s only official bilingual province?', 'new brunswick'),
    ('What major sporting event was held in Canada in 2010?', 'winter olympics'),
    ('When does Canada celebrate its national day?', 'july 1'),
    ('What is the capital of Ontario?', 'toronto'),
    ('What province has the biggest french population?', 'quebec'),
    ('Victoria is the capital of which province?', 'british columbia') 
]
quesAns2 = [
    ('Who became the twenty third Prime Minister of Canada? ', 'justin trudeau'),
    ('Paul Henderson scored the winning goal for Canada in the Canada-Soviet Summit Series in hockey. In what year was this goal, often referred to as "the goal heard around the world," scored? ', '1972'),
    ('What is Canada\'s national summer sport? ', 'lacrosse'),
    ('How many oceans border Canada?', '3'),
    ('What does RCMP stand for?', 'royal canadian mounted police'),
    ('What is the capital of Saskatchewan?', 'regina'),
    ('Name the world-famous waterfall in Ontario?', 'niagara falls'),
    ('What province produces the most oil?', 'alberta'),
    ('What is the only canadian city that is south of U.S.A.?', 'windsor'),
    ('True or False: Canada is the worlds second largest country by land mass?', 'true')
]
quesAns3 = [
    ('Government-funded medical care was introduced in Canada in 1962. In which province was it first introduced? ', 'saskatchewan'),
    ('When did "O, Canada" officially become the national anthem? ', '1980'),
    ('Which Canadian province is the largest in terms of land mass? ', 'ontario'),
    ('Whose face is on the Canadian hundred-dollar bill?', 'robert borden'),
    ('What is the population of Canada?', '32 million'),
    ('Somebody gave you a toonie, three quarters, a nickel, two dimes and a penny. How much money did they give you?', '3.01'),
    ('What year did Canada become a country?', '1867'),
    ('There are two governing bodies in Parliament. Name them.', 'the house of commons and the senate'),
    ('Which province outside of Quebec contains the most people who speak French at home?', 'ontario'),
    ('What is Canada\'s highest mountain?', 'mount logan')
]

#high score file. open the file and check the highscore
file = open("highscore.txt","r")

for line in file:
#split the line into an array called "fields" using the ";" as a separator:
    fields = line.split(";")
    #and let's extract the data:
    info1 = fields[0]
    info2 = fields[1]
    info3 = (int(fields[1]))
    
file.close()

from pygame.locals import * #load pygame commands
pygame.init()
screen = pygame.display.set_mode((1920,1080),FULLSCREEN)  #set screen size


#load images
background = pygame.image.load('background.jpg').convert()
image = pygame.image.load('image.png')
scroll = 0 #set counter for intro screen
pygame.mixer.music.load('o_canada.mp3') #Canada anthem sound
pygame.mixer.music.play(1)

#counter for intro screen. with images, sound effects and score.
while scroll<700:
    screen.blit(background, (0,0))
    screen.blit(image, (scroll,540))
    font = pygame.font.SysFont("calibri", 72) #defines font
    text = font.render(info1 + " has a high score of " + info2, True, (0,0,0)) #creates text object ready for blit
    screen.blit(text, (800,800)) #blits text object to screen    
    pygame.display.update()
    scroll = scroll + 1          
    
pygame.quit() #done with intro screen, quit pygame, enter console

os.system('mode con: cols=1920 lines=1080')  #set up console screen

#define exit screen
def lastscreen():
    os.system('cls')
    print ('Game Over')
    print ()
    print ('                     999999999999')
    print ('                    99          99')
    print ('      99999       99              99')
    print ('     9     9    99     99    99     99')
    print ('     9     9   99      99    99       99')
    print ('     9    9  99        99    99        99')
    print ('      9   9   9                         99')
    print ('    999999999999                        99')
    print ('   9            9 99             99     99')
    print ('  99            9  99            99     99')
    print (' 99   99999999999    99        99       99')
    print (' 9               9     9999999         99')
    print (' 99              9                    99')
    print ('  9   999999999999                   99')
    print ('  99           9  99                99')
    print ('   999999999999     99            99')
    print ('                       99999999999')
    
    
    print ()
    print ('Thanks for playing')    
    print ('You got %d right and %d wrong' % (NumRightAnswers1 + NumRightAnswers2 + NumRightAnswers3, NumWrong1 + NumWrong2 + NumWrong3))
    NumRight = NumRightAnswers1 + NumRightAnswers2 + NumRightAnswers3 #display record score if high score
    if NumRight > info3:
        print()
        print(player_name + ' HAS THE NEW HIGH SCORE!!!!')
        print
        file = open("highscore.txt", "w")
        file.writelines([player_name + ';' + str (NumRight)])
        file.close()
    time.sleep(2)

#instruction screen    
print ('WELCOME TO THE GREAT CANADIAN QUIZ')
print ('')
print ('THERE ARE 3 ROUNDS')
print ('')
print ('YOU MUST CORRECTLY ANSWER 4 QUESTIONS TO PROCEED TO THE NEXT ROUND')
print ('')
print ('GET 2 WRONG IN ANY ROUND AND YOUR OUT')
print ('')
print ('CAPITALIZATION OF WORDS DOES NOT MATTER; HOWEVER SPELLING COUNTS')
print ('')
print ('')
print ('GOOD LUCK')

input("Press Enter to continue...")
os.system('cls')

#set variables to record right and wrong answers
NumRightAnswers1 = 0 
NumRightAnswers2 = 0 
NumRightAnswers3 = 0 
NumWrong1 = 0
NumWrong2 = 0
NumWrong3 = 0

#shuffle tuples
shuffle(quesAns1)
shuffle(quesAns2)
shuffle(quesAns3)

#sound effects
correct1 = "Applause.wav"
wrong1 = "Wrong.wav"

#get username
print()
print()
player_name = input ('Please Enter Your Name: ')
print ('Thank you ' + player_name + '.  Enjoy the game')
print()
print()

#loop for asking questions in level 1,2,3
for question, rightAnswer in quesAns1:
    answer = input(question + ' ') 
    if answer.lower() == rightAnswer:    #checking for right and wrong answers
        print('Correct!')
        winsound.PlaySound(correct1, winsound.SND_FILENAME|winsound.SND_ASYNC) #sound effect
        # wait one and a half seconds
        time.sleep(1.5)
        print ()
        NumRightAnswers1 += 1 
        
        #level 1
        if NumRightAnswers1 == 4:
            os.system('cls')
            print ()
            print ('You are a true CANADIAN and you get to play the next level')
            print ()
            for question, rightAnswer in quesAns2:
                answer = input(question + ' ')
                if answer.lower() == rightAnswer:
                    print('Correct!')
                    winsound.PlaySound(correct1, winsound.SND_FILENAME|winsound.SND_ASYNC)
                    # wait one and a half seconds
                    time.sleep(1.5)                   
                    print ()
                    NumRightAnswers2 += 1
                    
                    #level 2
                    if NumRightAnswers2 == 4:
                        os.system('cls')
                        print ()
                        print ('You are a true CANADIAN PATRIOT and you get to play the last level')
                        winsound.PlaySound(correct1, winsound.SND_FILENAME|winsound.SND_ASYNC)
                        # wait one and a half seconds
                        time.sleep(1.5)                            
                        print ()    
                        
                        #level 3
                        for question, rightAnswer in quesAns3:
                            answer = input(question + ' ')
                            if answer.lower() == rightAnswer:
                                print('Correct!')
                                winsound.PlaySound(correct1, winsound.SND_FILENAME|winsound.SND_ASYNC)
                                # wait one and a half seconds
                                time.sleep(1.5)                                       
                                NumRightAnswers3 += 1
                                if NumRightAnswers3 == 4:
                                    os.system('cls')
                                    print ()
                                    print ('You are a FUTURE CANADIAN PRIME MINISTER in the making!!!!!')
                                    winsound.PlaySound(correct1, winsound.SND_FILENAME|winsound.SND_ASYNC)
                                    # wait one and a half seconds
                                    time.sleep(1.5)                                           
                                    lastscreen()
                                    sys.exit(0)                                       
                            else:
                                NumWrong3 += 1
                                print ('Wrong Answer!!!')
                                winsound.PlaySound(wrong1, winsound.SND_FILENAME|winsound.SND_ASYNC)
                                # wait one and a half seconds
                                time.sleep(1.5)                                       
                                if NumWrong3 == 2:
                                    lastscreen()
                                    sys.exit(0)                    
                else:
                    NumWrong2 += 1
                    print ('Wrong Answer!!!')
                    winsound.PlaySound(wrong1, winsound.SND_FILENAME|winsound.SND_ASYNC)
                    # wait one and a half seconds
                    time.sleep(1.5)                   
                    if NumWrong2 == 2:
                        lastscreen()
                        sys.exit(0)                    
               
    else:
        NumWrong1 += 1
        print ('Wrong Answer!!!')
        winsound.PlaySound(wrong1, winsound.SND_FILENAME|winsound.SND_ASYNC)
        # wait one and a half seconds
        time.sleep(1.5)         
        if NumWrong1 == 2:
            winsound.PlaySound(wrong1, winsound.SND_FILENAME|winsound.SND_ASYNC)
            # wait one and a half seconds
            time.sleep(1.5)
            lastscreen()
            sys.exit(0)
