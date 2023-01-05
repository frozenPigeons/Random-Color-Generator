import random
import time
import cv2
import numpy as np
import os

file_header = random.randint(1, 200000)
type_of_generation = random.randint(1, 5)
# type_of_generation = 3

#dimensions of the canvas
height = 500
width = 500

white = [random.randint(205, 255), random.randint(205, 255), random.randint(205, 255)]
black = [random.randint(0, 50), random.randint(0, 50), random.randint(0, 50)]

#generates a random rgb colour
def rgb():
    #OpenCV uses RBG
    red = random.randint(0, 255)
    blue = random.randint(0, 255)
    green = random.randint(0, 255)
    colour_made = [red, blue, green]
    return colour_made

#Finds the average colour between two colours
def avgColour(colour_1, colour_2):
    red = (colour_1[0] + colour_2[0]) // 2
    blue = (colour_1[1] + colour_2[1]) // 2
    green = (colour_1[2] + colour_2[2]) // 2
    newColour = [red, blue, green]
    return newColour

#Converts an RBG colours to an RGB colour
def conversion(colourVal):
    colourVal = [colourVal[2], colourVal[1], colourVal[0]]
    newColour = colourVal
    return newColour

def darkRandom():
    dark = random.randint(0, 2)
    if dark == 0:
        red = random.randint(10, 100)
    if dark == 1:
        green = random.randint(10, 100)
    if dark == 2:
        blue = random.randint(10, 100)
    colour_1 = [red, blue, green]
    return colour_1

def invert(colour):
    invertedColour = [256 - colour[0], 256 - colour[1], 256 - colour[2]]
    return invertedColour

img = np.zeros((height,width,3), np.uint8)

#complete random!!
if type_of_generation == 1:
    print("The colours are:")
    rgbColour = []
    for i in range(5):
        colour_1 = rgb()
        rgbColour.append(conversion(colour_1))
        for j in range(height-i*100):
            for k in range(img.shape[1]):
                img[j][k] = colour_1
    rgbColour = rgbColour[4], rgbColour[3], rgbColour[2], rgbColour[1], rgbColour[0]
    for i in range(len(rgbColour)):
        print(rgbColour[i])
cv2.imshow('Image', img)

#gradient of two random colours!!
if type_of_generation == 2:
    print("The colours are:")
    colour_1 = rgb()
    colour_2 = rgb()
    middle = avgColour(colour_1, colour_2)
    midtone_1 = avgColour(colour_1, middle)
    midtone_2 = avgColour(middle, colour_2)
    rgbColour = [colour_2, midtone_2, middle, midtone_1, colour_1]
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
    for i in range(len(rgbColour)):
        print(rgbColour[i])
    cv2.imshow('Image', img)

#monochromatic
#consider chaning the lightest and darkest colours to more midtones
if type_of_generation == 3:
    print("The colours are:")
    colour_1 = rgb()
    midLight = avgColour(white, colour_1)
    midDark = avgColour(colour_1, black)
    lightest = avgColour(midLight, white)
    darkest = avgColour(midDark, black)
    rgbColour = [
        conversion(darkest), 
        conversion(midDark), 
        conversion(colour_1), 
        conversion(midLight), 
        conversion(lightest)
        ]
    for i in range(5):
        for j in range(500-i*100):
            for k in range(img.shape[1]):
                if i == 0:
                    img[j][k] = lightest
                if i == 1:
                    img[j][k] = midLight
                if i == 2:
                    img[j][k] = colour_1
                if i == 3:
                    img[j][k] = midDark
                if i == 4:
                    img[j][k] = darkest
    for i in range(len(rgbColour)):
        print(rgbColour[i])
    cv2.imshow('Image', img)

#monochromatic with three mid tones with black and white
#maybe try getting dark dark, dark white, white dark, white white, or try splitting the colours throught the top and bottom (similar to a gradient)
if type_of_generation == 4:
    print("The colours are:")
    colour_1 = rgb()
    midLight = avgColour(white, colour_1)
    midDark = avgColour(colour_1, black)
    lightest = avgColour(midLight, white)
    darkest = avgColour(midDark, black)
    rgbColour = [
        conversion(midLight), 
        conversion(colour_1), 
        conversion(midDark), 
        conversion(white), 
        conversion(black)
        ]
    for i in range(5):
        for j in range(500-i*100):
            for k in range(img.shape[1]):
                if i == 0:
                    img[j][k] = black
                if i == 1:
                    img[j][k] = white
                if i == 2:
                    img[j][k] = midDark
                if i == 3:
                    img[j][k] = colour_1
                if i == 4:
                    img[j][k] = midLight
    for i in range(len(rgbColour)):
        print(rgbColour[i])
    cv2.imshow('Image', img)

#Inverted colours just a funky one basically random 2 
if type_of_generation == 5:
    print("The colours are:")
    colours = []
    inverteds = []
    for i in range(5):
        colour_1 = rgb()
        colourInverted = invert(colour_1)
        colours.append(conversion(colour_1))
        inverteds.append(conversion(colourInverted))
        for j in range(500 - i * 100):
            for k in range(img.shape[1]):
                img[j][k] = colourInverted
    for i in range(len(inverteds)):
        print(colours[4-i], "-->", inverteds[4-i])
    cv2.imshow("Image", img)

cv2.waitKey(0)

#instead of using random to make sure there are no dupe image names use the colour generator file
a = input("Would you like to save the image? [Y/N]")
if a == "Y":
    name = random.randint(1, 2)
    if name == 1:
        cv2.imwrite("Gradient{}.png".format(file_header), img)
    else:
        cv2.imwrite("Gradient_{}.png".format(file_header), img)

cv2.destroyAllWindows()
