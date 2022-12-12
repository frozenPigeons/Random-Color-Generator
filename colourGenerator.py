import random
import cv2
import numpy as np

type_of_generation = random.randint(1, 6)

#dimensions of the canvas
height = 500
width = 500

#generates a random rgb colour
def rgb():
    #OPENCV USES RBG
    red = random.randint(0, 255)
    blue = random.randint(0, 255)
    green = random.randint(0, 255)
    colour_made = [red, blue, green]
    return colour_made

def avgColour(colour_1, colour_2):
    red = (colour_1[0] + colour_2[0]) // 2
    blue = (colour_1[1] + colour_2[1]) // 2
    green = (colour_1[2] + colour_2[2]) // 2
    newColour = [red, blue, green]
    return newColour

img = np.zeros((height,width,3), np.uint8)
type_of_generation = 2


#complete random!!
if type_of_generation == 1:
    for i in range(5):
        colour_1 = rgb()
        for j in range(500-i*100):
            for k in range(img.shape[1]):
                img[j][k] = colour_1
    cv2.imshow('Image', img)

#gradient of two random colours!!
if type_of_generation == 2:
    colour_1 = rgb()
    colour_2 = rgb()
    middle = avgColour(colour_1, colour_2)
    midtone_1 = avgColour(colour_1, middle)
    midtone_2 = avgColour(middle, colour_2)
    for i in range(5):
        for j in range(500-i*100):
            for k in range(img.shape[1]):
                if i == 0:
                    img[j][k] = colour_1
                if i == 1:
                    img[j][k] = midtone_1
                if i == 2:
                    img[j][k] = middle
                if i == 3:
                    img[j][k] = midtone_2
                if i == 4:
                    img[j][k] = colour_2
    cv2.imshow('Image', img)



cv2.waitKey(0)