import pyautogui
# PyAutoGUI is a cross-platform GUI automation Python module for human beings. Used to programmatically control the mouse & keyboard.

import os
# This module provides a portable way of using operating system dependent functionality

os.getenv
# Return the value of the environment variable key as a string if it exists, or default if it doesn’t.

from os import listdir
# Return a list containing the names of the entries in the directory given by path. The list is in arbitrary order, and does not include the special entries
from src.layers.presentation.display import display_sort_stack, display_txt_files


print('Press Ctrl-C to quit.')
try:
    varF1 = open("/Volumes/AlvaroJS/academlo/algoritmos/proyectoFinal/python_algorithms/buckets/f1.txt","w")
    varF2 = open("/Volumes/AlvaroJS/academlo/algoritmos/proyectoFinal/python_algorithms/buckets/f2.txt","w")
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)        
        varF1.write(str(x)) 
        varF1.write('\n') 
        varF2.write(str(y)) 
        varF2.write('\n') 
    varF1.close() 
    varF2.close() 
except KeyboardInterrupt:
    print('\n')



print(x, y)
BASE_PATH= '/Volumes/AlvaroJS/academlo/algoritmos/proyectoFinal/python_algorithms/buckets'

print(BASE_PATH)
onlyfiles = [f for f in listdir(BASE_PATH) 
if os.path.isfile(os.path.join(BASE_PATH, f))]

print(onlyfiles)

for i in onlyfiles:
    print(i, os.path.getsize(BASE_PATH+'/'+i))