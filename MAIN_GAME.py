import enchant
import random
import string
import itertools
import time
import pyglet

#print(n)

oops=pyglet.media.load('Sad_Trombone.wav',streaming=False)
wins=pyglet.media.load('win.wav',streaming=False)

old_words = []
letters = []
d = enchant.Dict("en_US")
g = int(input('1 to play, 2 to quit\n'))
score = 0
vowels = ['a','e','i','o','u']
multiplier = 1



def get_letters():
     global multiplier
     multiplier = 1
     n = random.randint(4,8)
     for _ in itertools.repeat(None, n):
          letters = [random.choice(string.ascii_lowercase)]
          print((letters), sep='', end=' ', flush=True)
     print([random.choice(vowels)])
     letters = [letters+[random.choice(vowels)]]
     
def check_letters():
     for i in x:
          if i in letters:
               is_word()
          else:
               print('Wrong')
               break
               
def is_word():
    if d.check(x) == True:
         wins.play()
         global score
         global multiplier
         score = score + 1*multiplier
         multiplier += 1
         print('Score =' ,score)
         global old_words
         old_words=old_words+[x]
         print(old_words)
         
    else:
         print('Wrong')
         oops.play()
def end ():
    print('Τέλος παιχνιδιού')
    

def outoftime():
    print('Τέλος χρόνου')
    end()

     
if g == 1:
     get_letters()
if g==2:
     end()

     
start=time.time()    
while time.time() - start < 60:
    x = input("\n")
    
    if  x != '':
         if x in old_words: 
              print('Την έχεις πει ήδη')
         else:
              is_word()

    else:
        get_letters()
        check_letters()
        for i in old_words:
             old_words.remove(i)
             
        
outoftime()

        
