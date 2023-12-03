'''--- Day 2: Cube Conundrum ---
You're launched high into the atmosphere! The apex of your trajectory just barely reaches the surface of a large island floating in the sky. You gently land in a fluffy pile of leaves. It's quite cold, but you don't see much snow. An Elf runs over to greet you.

The Elf explains that you've arrived at Snow Island and apologizes for the lack of snow. He'll be happy to explain the situation, but it's a bit of a walk, so you have some time. They don't get many visitors up here; would you like to play a game in the meantime?

As you walk, the Elf shows you a small bag and some cubes which are either red, green, or blue. Each time you play this game, he will hide a secret number of cubes of each color in the bag, and your goal is to figure out information about the number of cubes.

To get information, once a bag has been loaded with cubes, the Elf will reach into the bag, grab a handful of random cubes, show them to you, and then put them back in the bag. He'll do this a few times per game.

You play several games and record the information from each game (your puzzle input). Each game is listed with its ID number (like the 11 in Game 11: ...) followed by a semicolon-separated list of subsets of cubes that were revealed from the bag (like 3 red, 5 green, 4 blue).

For example, the record of a few games might look like this:'''

from typing import TypedDict

class colorNums(TypedDict):
    red:int
    blue:int
    green:int


def inputs(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    colorsDict = {}
    for line in lines:
        gamenum, handfuls = line.split(":")
        #get the game number
        gamenum = int(gamenum.split(' ')[1])

        #split into each handful
        handfuls = handfuls.split(';')
        colorslist = []
        for handful in handfuls:
            colors:colorNums = {'red':0, 'blue':0, 'green':0}
            #colors.red, colors.blue, colors.green = 0,0,0 #set to default of 0
            handful = handful.split(',')
            for color in handful:
                if color.find('red') != -1:
                    colors['red'] = int(color.split()[0])
                if color.find('blue') != -1:
                    colors['blue'] = int(color.split()[0])
                if color.find('green') != -1:
                    colors['green'] = int(color.split()[0])
            colorslist.append(colors) 
        colorsDict[gamenum] = colorslist
    
    return colorsDict

def isPossible(colorsList):
    possible:colorNums = {'red':12, 'blue':14, 'green':13}
    for handful in colorsList:
        if handful['red'] > possible['red']:
            return False
        elif handful['blue'] > possible['blue']:
            return False
        elif handful['green'] > possible['green']:
            return False
    return True

def runFunction(filename):
    inputdict = inputs(filename)
    possiblegames = []
    for game, handfuls in inputdict.items():
        possiblegame = isPossible(handfuls)
        if possiblegame:
            possiblegames.append(game)
    return sum(possiblegames)

if __name__ == "__main__":
    print(runFunction('input.txt'))