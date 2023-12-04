'''
--- Part Two ---
Just as you're about to report your findings to the Elf, one of you realizes that the rules have actually been printed on the back of every card this whole time.

There's no such thing as "points". Instead, scratchcards only cause you to win more scratchcards equal to the number of winning numbers you have.

Specifically, you win copies of the scratchcards below the winning card equal to the number of matches. So, if card 10 were to have 5 matching numbers, you would win one copy each of cards 11, 12, 13, 14, and 15.

Copies of scratchcards are scored like normal scratchcards and have the same card number as the card they copied. So, if you win a copy of card 10 and it has 5 matching numbers, it would then win a copy of the same cards that the original card 10 won: cards 11, 12, 13, 14, and 15. This process repeats until none of the copies cause you to win any more cards. (Cards will never make you copy a card past the end of the table.)

This time, the above example goes differently:
'''

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
    #check what we need to multiply each row by
    multipliers = [1 for i in range(len(winvals))]
    for i in range(len(winvals)):
        winlist = winvals[i]
        inputs = inputvals[i]
        score, wins = winscore(winlist, inputs)
        #add one to each eligible card
        for cardbonus in range(i+1, i+wins+1):
            multipliers[cardbonus] = multipliers[i]+multipliers[cardbonus]
        scores.append(score)

    return multipliers
        

def winscore(winlist, inputs):
    wins = 0
    for input in inputs:
        if input in winlist:
            wins = wins+1
    if wins>0:
        return 2**(wins-1), wins
    else:
        return 0, 0

if __name__ == '__main__':
    winvals, inputvals = readInput('day4/input.txt')
    scores = checkwins(winvals, inputvals)
    print(scores)
    print(sum(scores))