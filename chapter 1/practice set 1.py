# Problem 1:- print twinkle twinkle poem.

print('''Twinkle,twinkle,little star,
            how i wonder what you are,
           up above the world so high,
           like a diamond in the sky.''')

#Problem 3:- install module as your interest.

import pyttsx3
engine = pyttsx3.init()
engine.say('''Twinkle,twinkle,little star,
            how i wonder what you are,
           up above the world so high,
           like a diamond in the sky.''')
engine.runAndWait()

#Problem 4,5:- os for print directory contents and label comments on line.


import os

#Specify the directory you want to list
directory_path = '/'

#list all directories in specified path
contents = os.listdir(directory_path)

#print each diractory name
print(contents)