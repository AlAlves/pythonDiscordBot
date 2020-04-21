import random
import numpy as np
from PIL import Image, ImageDraw, ImageFont

WORDLIST_FILENAME = "WORDLIST.txt"
random.seed(69)

def makeWordList():
    with open(WORDLIST_FILENAME,'r') as f:
        data = f.read()
        datas = f.readlines()
    return set([word for word in data.splitlines()])

# 0 -> noir
# 1 -> neutre
# 2 -> couleur1
# 3 -> couleur2
def createWordGrid(nbWords = 25, listColors = [1, 8, 8, 8]):
    grid = []
    wordList = makeWordList()
    tmpColorList = listColors.copy()
    np.set_printoptions(precision=15)
    for i in range(nbWords):
        p = [v/(nbWords-i) for v in tmpColorList]
        p = np.array(p)
        p /= p.sum() # normalize
        color = np.random.choice(np.arange(0, 4), p=p)
        tmpColorList[color] -= 1
        grid.append((wordList.pop(),color))
    return grid

def imageGridNeutral(wordSetWithValues):
    word_width = 200
    word_height = 100
    width = word_width*5+4*10
    height = word_height*5+4*10
    black = (0,0,0)
    white = (245,245,245)

    img = Image.new('RGB', (width, height), color = white)
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype("FreeSans.ttf", 20)

    # DRAWING VERTICAL LINES
    for i in range(4):
        shape = [(width/5*(i+1), 0), (width/5*(i+1), height)]
        d.line(shape, fill="black", width=5)

    # DRAWING HORIZONTAL LINES
    for i in range(4):
        shape = [(0, height/5*(i+1)), (width, height/5*(i+1))]
        d.line(shape, fill="black", width=5)

    # WRITING TEXTS
    i = 0
    j = 0
    for e,v in wordSetWithValues:
        d.text((20+(210*i),20+(110*j)), e, fill=black, font=font)
        i = (i+1)
        if(i >= 5):
            j += 1
            i = 0

    img.save('tmp/codenames/neutralCodeNames.png')
    return 'tmp/codenames/neutralCodeNames.png'

def imageGridColored(wordSetWithValues):
    word_width = 200
    word_height = 100
    width = word_width*5+4*10
    height = word_height*5+4*10
    black = (0,0,0)
    blue = (50,50,255)
    red = (255,50,50)
    white = (245,245,245)

    img = Image.new('RGB', (width, height), color = white)
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype("FreeSans.ttf", 20)

    # WRITING TEXTS
    i = 0
    j = 0
    for e,v in wordSetWithValues:
        bg=black
        text=white
        if(v==1):
            bg=white
            text=black
        elif(v==2):
            bg=blue
            text=black
        elif(v==3):
            bg=red
            text=black
        d.rectangle((width/5*i, height/5*j, width/5*i+width/5, height/5*j+height/5), fill=bg, outline=black)
        d.text((20+(210*i),20+(110*j)), e, fill=text, font=font)
        i = (i+1)
        if(i >= 5):
            j += 1
            i = 0

    # DRAWING VERTICAL LINES
    for i in range(4):
        shape = [(width/5*(i+1), 0), (width/5*(i+1), height)]
        d.line(shape, fill="black", width=5)

    # DRAWING HORIZONTAL LINES
    for i in range(4):
        shape = [(0, height/5*(i+1)), (width, height/5*(i+1))]
        d.line(shape, fill="black", width=5)

    img.save('tmp/codenames/SPOILER_teamCodeNames.png')
    return 'tmp/codenames/SPOILER_teamCodeNames.png'

# imageGridNeutral(createWordGrid())
# imageGridColored(createWordGrid())
