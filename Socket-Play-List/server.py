"""
Created on Thu Feb 11 16:07:18 2021

@author: Oscar M Giraldo H
         
"""
"""
en python, el modulo de cola es util para la programacion de sub
procesos cuando la informacion debe intercambiarse de forma segura durante
varios procesos 
"""
import cv2, imutils, time
import queue, os
##
import threading

q = queue.Q

