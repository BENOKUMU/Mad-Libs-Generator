#Mad libs generator using Tkinter
#It is usually a game played by kids.
# in this project the user has to first pick a story by titleof the story.
# Then the user has to enter specific words like
# nouns, verb,adverb, food, adjective, etc, according to the requirements, and then the story will be generated

# Importing Tkinter(GUI Python Library)
from tkinter import *

#Create a display Window
root = Tk()
root.geometry( '300x300' )
root.title('Benjamin-MadLibsGenerator')
Label(root, text = 'MadLibsGenerator \n Have Fun!', font = 'arial 20 bold').pack()
Label(root, text = 'Click Any One: ', font = 'arial 15 bold').place(x=40, y=80)

#Define functions
def madlib1():
    animals = input('enter a animal name: ')
    profession = input('enter a proffession name: ')
    cloth = input('enter a piece of clothe: ')
    things = input('enter a thing name: ')
    name= input('enter a name: ')
    place = input('enter a place name: ')
    verb = input('enter a verb in ing form: ')
    food = input('food name: ')
    print('say ' + food + ', the photographer said as the camera flashed! '
          + name + ' and I had gone to get our photos taken on my birthday. '
        'The first photo we really wanted was a picture of us dressed as ' + animals +
          ' pretending to be a ' + profession +
          '. When we saw the second photo, it was exactly what I wanted, we both looked like ' + things +
          ' wearing ' + cloth + ' and ' + verb + '-- exactly what I had in mind.')

def madlib2():
    adjective = input('enter adjectives: ')
    color = input('enter a color name : ')
    thing = input('enter a thing name :')
    place = input('enter a place name : ')
    person = input('enter a person name : ')
    adjactive1 = input('enter a adjactive : ')
    insect = input('enter a insect name : ')
    food = input('enter a food name : ')
    verb = input('enter a verb name : ')
    print(
        'Last night I dreamed I was a ' + adjective +
        ' butterfly with ' + color + ' splocthes that looked like ' + thing +
        ' .I flew to ' + place + ' with my bestfriend and ' + person + ' who was a ' + adjactive1 + ' ' + insect +
        ' .We ate some ' + food + ' when we got there and then decided to ' + verb + ' and the dream ended when I said-- lets ' + verb + '.')


def madlib3():
    person = input('enter person name: ')
    color = input('enter color : ')
    foods = input('enter food name : ')
    adjective = input('enter aa adjective name: ')
    thing = input('enter a thing name : ')
    place = input('enter place : ')
    verb = input('enter verb : ')
    adverb = input('enter adverb : ')
    food = input('enter food name: ')
    things = input('enter a thing name : ')

    print(
        'Today we picked apple from ' + person +
        "'s Orchard. I had no idea there were so many different varieties of apples. I ate " + color +
        ' apples straight off the tree that tested like ' + foods +
        '. Then there was a ' + adjective + ' apple that looked like a ' + thing +
        '.When our bag were full, we went on a free hay ride to ' + place +
        ' and back. It ended at a hay pile where we got to ' + verb + ' ' + adverb +
        '. I can hardly wait to get home and cook with the apples. We are going to make appple ' + food + ' and ' + things + ' pies!.')

#Define Buttons
Button(root, text= 'The Photographer', font ='arial 15', command= madlib1, bg = 'ghost white').place(x=60, y=120)
Button(root, text= 'apple and apple', font ='arial 15', command = madlib3 , bg = 'ghost white').place(x=70, y=180)
Button(root, text= 'The Butterfly', font ='arial 15', command = madlib2, bg = 'ghost white').place(x=80, y=240)

root.mainloop()


