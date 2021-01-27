'''
Created on Jan 21, 2021

@author: Fedotov Dmitriy
'''

import random
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

count = 0
while (count < 6):
    f=open(pictures[count], "r")
    contents =f.read()
    print(contents)
    count = count + 1
    
    
    
#for i in pictures:
    
    
    
print("kuku")


