import sys

inputs = [line.strip() for line in sys.stdin]

sum = 0
for input in inputs:
    parts = input.split(':')
    gameId = int(parts[0].split(" ")[1])
    gameDict = {"red": 0, "green": 0, "blue": 0}
    pulls = parts[1].split(";")
    for pull in pulls:
        colors = pull.split(",")
        for colorCount in colors:
            [_, count, color] = colorCount.split(" ")
            gameDict[color] = max(gameDict[color], int(count))
    # print(gameId)
    # print(gameDict)
    sum += gameDict["red"] * gameDict["blue"] * gameDict["green"]
print(sum)