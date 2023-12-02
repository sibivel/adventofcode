import sys
inputs = [line.strip() for line in sys.stdin]
numbers = [
 ("one", 1),
 ("two", 2),
 ("three", 3),
 ("four", 4),
 ("five", 5),
 ("six", 6),
 ("seven", 7),
 ("eight", 8),
 ("nine", 9),
]

sum = 0
for input in inputs:
  i = 0
  digits = []
  while i < len(input):
    if (input[i].isnumeric()):
      digits.append(int(input[i]))
    else:
      for number in numbers:
        if input[:i+1].endswith(number[0]):
          digits.append(number[1])
          break
    i += 1
  sum += digits[0] * 10 + digits[-1]
print(sum)
