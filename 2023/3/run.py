import sys

inputs = [line.strip() for line in sys.stdin]

width = len(inputs[0])
height = len(inputs)
sum = 0
h = 0
gearNums = {}
while h < height:
  w = 0
  while w < width:
    gears = []
    if inputs[h][w].isnumeric():
      if h > 0 and w > 0 and inputs[h-1][w-1] == '*':
        gears.append((h-1, w-1))
      if w > 0 and inputs[h][w-1] =='*':
        gears.append((h, w-1))
      if h < height-1 and w > 0 and inputs[h+1][w-1] =='*':
        gears.append((h+1, w-1))
      pn = 0
      while w < width and inputs[h][w].isnumeric():
        if (h > 0 and inputs[h-1][w] =='*'):
          gears.append((h-1, w))
        if (h < height-1 and inputs[h+1][w] =='*'):
          gears.append((h+1, w))
        pn = pn * 10 + int(inputs[h][w])
        w += 1
      if w < width and h > 0 and inputs[h-1][w] =='*':
        gears.append((h-1, w))
      if w < width and inputs[h][w] =='*':
        gears.append((h, w))
      if w < width and h < height-1 and inputs[h+1][w] =='*':
        gears.append((h+1, w))
      
      for gear in gears:
        if not gear in gearNums:
          gearNums[gear] = []
        gearNums[gear].append(pn)
    w += 1
  h += 1
for gear in gearNums:
  pns = gearNums[gear]
  if len(pns) == 2:
    sum += pns[0] * pns[1]
    
  
print(sum)

      
        