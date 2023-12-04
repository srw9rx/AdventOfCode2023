def readInput(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    answersList = []
    inputsList = []
    for line in lines:
        ignoregame = line.split(':')[1]
        win = ignoregame.split('|')[0]
        card = ignoregame.split('|')[1]
        print(win)
        winlist = [int(x) for x in win.split()]
        cardlist = [int(x) for x in card.split()]
        answersList.append(winlist)
        inputsList.append(cardlist)
    return answersList, inputsList

def checkwins(winvals, inputvals):
    scores = []
    for i in range(len(winvals)):
        winlist = winvals[i]
        inputs = inputvals[i]
        scores.append(winscore(winlist, inputs))
    return scores
        

def winscore(winlist, inputs):
    wins = 0
    for input in inputs:
        if input in winlist:
            wins = wins+1
    if wins>0:
        return 2**(wins-1)
    else:
        return 0

if __name__ == '__main__':
    winvals, inputvals = readInput('day4/input.txt')
    scores = checkwins(winvals, inputvals)
    print(scores)
    print(sum(scores))