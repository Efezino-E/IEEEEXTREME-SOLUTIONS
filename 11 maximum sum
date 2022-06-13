def sumy(listu,n):
  ans= 0
  for i in range(0,n-1):
    ans += listu[i]*listu[i+1]
  return ans

def maxim2(listy,n):
  listy.sort()
  rl = []
  ll = []
  for i in range(n):
    if listy[-1] ==0:
      ll.append(0)
    elif ll == [] or ll[-1] == 0:
      ll.append(listy[i])
    elif rl == []:
      rl.append(listy[i])
    elif ll[-1] >rl[-1]:
      rl.append(listy[i])
    elif rl[-1] >ll[-1]:
      ll.append(listy[i])
    elif rl[-1] == ll[-1]:
      ll.append(listy[i])
  out = ""
  for i in range(len(ll)):
    out += str(ll[i])+" "
  for i in range(-1,-1-len(rl),-1):
    out+= str(rl[i])+" "
  #print(rl,"**",ll)
  rl.reverse()
  
  return out, ll+rl

for i in range(int(input())):
  n = int(input())
  listy = list(map(int,input().split(' ')))
  ans1,ans2 = maxim2(listy,n)
  print(sumy(ans2,n))
  print(ans1)
#maxim2([1, 2, 1, 5 ,4, 2, 1 ,1 ,8 ,9],10)
