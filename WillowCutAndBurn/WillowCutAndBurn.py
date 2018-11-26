import math
import sys
import time

from random import randint, uniform
import cv2
import numpy as np
import pyautogui as pag



class WillowCutAndBurn(obj):
    """
    Cuts the willow trees at Draynor and burns them for both
    woodcutting and firemaking experience

    TODO: - Add the banking feature
          - Add a login/log off function
          - 
    """

    def __init__(self):
        pass

    def cut_trees(self, )



    def random_spot(x_low, y_low, x_range, y_range):
        """ Move to a random spot on the object """
        x = randint(x_low, x_low + x_range)
        y = randint(y_low, y_low + y_range)
        dur = random.uniform(0.5, 3.0)

        return pyautogui.moveTo(x, y, dur)
