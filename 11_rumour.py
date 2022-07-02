def rum(a,b):
  steps = 0
  if a == b: 
    return 0
  while True:
    if a>b:
      a = a//2
      steps += 1
      if a == b:
        return steps
    elif b>a:
      b = b//2
      steps += 1
      if a == b:
        return steps

N = input()
for i in range(int(N)):
  a,b = list(map(int,input().split(" ")))
  print(rum(a,b))
