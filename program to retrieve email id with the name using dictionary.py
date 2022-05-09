n=int(input())
d={}
for i in range (n):
    x=input().split()
    d[x[0]]=x[1]
while True:
    try:
        name=input()
        if name in d:
            print(name,'=',d[name])
        else:
            print('not found')
    except:
        break
        
output:
  3
jnaneswar jnaneswarkonathala@gmail.com
gopi gopin1432mokkina1432@gmail.com
abhinay abhinayr144555@gmail.com
pavan
not found
gopi
gopi = gopimokkina1432@gmail.com
abhinay
abhinay = abhinayr144555@gmail.com
jnaneswar
jnaneswar = jnaneswarkonathala@gmail.com
