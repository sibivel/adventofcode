import sys

inputs = [line.strip() for line in sys.stdin]

total = 0
for card in inputs:
    [firstPart, secondPart] = card.split('|')
    yourNumbers = [int(x) for x in secondPart.split(' ') if len(x) > 0]
    winningNumbers = [int(x) for x in firstPart.split(':')[1].split(' ') if len(x) > 0]
    score = 0
    for w in winningNumbers:
        if w in yourNumbers:
            if score == 0:
                score = 1
            else:
                score = score * 2
    total += score
print(total)