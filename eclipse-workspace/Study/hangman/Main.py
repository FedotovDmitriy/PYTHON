'''
Created on Jan 21, 2021

@author: Fedotov Dmitriy
'''

import random
from xmlrpc.client import Boolean
from pickle import FALSE
print("""
    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \\
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                       |___/
""")
print(random.randint(5,10))
#pictIntro = PictureObj.PictureObject()
#pictIntro.getIntro()
pictures = ["picture_1","picture_2","picture_3","picture_4","picture_5","picture_6","picture_7"]
name = input("Input your name : ")
flag = True
inputType = "Please enter character , "
while (flag):
    wordInput = input(inputType + "\nGuess a letter:  ")
    if len(wordInput) == 1: #Strictly speaking, this is not really required. 
            if wordInput.isalpha() == True:
                inputType = 'a letter'
                flag = False
            else:
                inputType = 'a special character'
    else:
            inputLength = len(wordInput)
            if wordInput.isalpha() == True:
                inputType = 'a character string of length ' + str(inputLength)
            elif wordInput.isalnum() == True:
                inputType = 'an alphanumeric string of length ' + str(inputLength)
            else:
                inputType = 'a string of length ' + str(inputLength) + ' with at least one special character'


    
print(wordInput)

count = 0
while (count < 6):
    f=open(pictures[count], "r")
    contents =f.read()
    print(contents)
    count = count + 1
    
    
    
#for i in pictures:
    
    
    
print("kuku")



