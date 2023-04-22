from random import randint
from Macros.DetectorsMacros import *


def detect_serie(image):
    rand = randint(0, 1000)
    return SPOILER if rand > 700 else NOT_SPOILER
