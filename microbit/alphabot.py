from microbit import *
import speech
import random
import radio
import music

# all, and, any, are, bad, bet, big, box, boy, bye, can, car, cat, cup, cut, day, did, dog, dry, eat, eve, fly, for, get, had, has, her, him, his, hot, how, huh, hum, let, lot, man, may, mom, new, not, off, old, one, our, out, pet, put, red, run, saw, say, see, she, sit, some, the, too, top, try, two, use, was, way, who, why, yes, yet, you
words = ['CAT', 'BOY', 'CAR', 'CUP', 'EAT', 'MAN']
pronounciation =  {
    "A": "ay",
    "B": "bee",
    "C" : "see",
    "D": "dee",
    "E": "eee",
    "F": "eff",
    "G": "gee",
    "H" : "aych",
    "I" : "iy",
    "J" : "jay",
    "K" : "kay",
    "L" : "el",
    "M" : "em",
    "N" : "en",
    "O" : "oh" ,
    "P" : "pee",
    "R" : "ar",
    "T" : "tee",
    "U" : "yew",
    "Y" : "why"
    }


count=0

radio.on()

affirmations = ['Well done.', 'Yes, thats right.', 'Very good.', 'Well done Evin. Thats correct.', ' Yay. Thats right.', 'I am so impressed. You spell very well.']
music.set_tempo(bpm=400)

display.show(Image("00000\n"
              "00000\n"
              "00900\n"
              "00000\n"
              "00000"))
sleep(100)

display.show(Image("00000\n"
              "09990\n"
              "09990\n"
              "09990\n"
              "00000"))
sleep(100)
display.show(Image("99999\n"
              "99999\n"
              "99999\n"
              "99999\n"
              "99999"))
music.play(["C7:2"])
sleep(1000)
display.show(Image.HEART)
speech.say('Hi,  Evin. I am alphabot.', speed=70, pitch=100, throat=100, mouth=200)
sleep(1000)
display.show(Image("09990:"
            "90009:"
            "00009:"
            "00990:"
            "00900"))
speech.say('Will you help me power up my space ship?', speed=70, pitch=100, throat=100, mouth=200)
sleep(1000)
display.show(Image.YES)
speech.say('All you need to do is spell some words to fix my sole uh panel', speed=70, pitch=100, throat=100, mouth=200)

sleep(1500)

while True:
    incoming = radio.receive()
    if (incoming == 'next'):
        if (count > 0):
            previousword = words[count - 1]
            randomNum = random.randint(0, len(affirmations) - 1)
            randomAffirmation = affirmations[randomNum]
            display.show(Image("00000:"
            "00000:"
            "00000:"
            "99999:"
            "09990"))
            speech.say(randomAffirmation + '.' + previousword + 'is spelt.' ,speed=80, pitch=100, throat=100, mouth=200)
            for i in range( len(word)):
                speech.say(pronounciation[previousword[i]],speed=120, pitch=100, throat=100, mouth=200)
                display.show(previousword[i])
                sleep(1000)
            sleep(1500)

        if (count < len(words)):
            display.clear();
            speech.say('Can you spell',speed=70, pitch=100, throat=100, mouth=200)
            sleep(1000)
            word = words[count]
            speech.say(word,speed=200, pitch=100, throat=100, mouth=200)
            sleep(1000)
            count+=1
        else:
            speech.say('We have run out of words.',speed=70, pitch=100, throat=100, mouth=200)
            sleep(500)
            speech.say('Please try again some time to help me get back home.',speed=70, pitch=100, throat=100, mouth=200)
            sleep(500)
            speech.say('Thank for trying to help me Evin.',speed=70, pitch=100, throat=100, mouth=200)
            sleep(800)
            speech.say('Bye bye',speed=70, pitch=100, throat=100, mouth=200)
