import sys
import re

inputs = [line.strip() for line in sys.stdin]

total = 0
cardCounts = {}

for card in inputs:
   
    gameId, first, second = re.search('Card (\d)\: ([\d\s]+) \| ([\d\s]+)', card).groups()
    gameId = int(gameId)
    winningNumbers = [int(x) for x in first.split() if len(x)]
    yourNumbers = [int(x) for x in second.split() if len(x)]
    cardCounts[gameId] = cardCounts.get(gameId, 0) + 1
    score = 0
    for w in winningNumbers:
        if w in yourNumbers:
            score += 1
    for i in range(score):
        cardCounts[gameId + i + 1] = cardCounts.get(gameId + i + 1, 0) + cardCounts[gameId]

for k in cardCounts:
    total += cardCounts[k]

print(cardCounts)
print(total)