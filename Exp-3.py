#...........Loops.............

print("Following output is by for loop ")
for x in range(10):
    print(x*10, end=" ")

print(" \nFollowing output is by while  ")
n=5
while n>=0:
    print(n, end=" ")
    n-=1

print(" \nFollowing output is by nested loop  ")
i=[1,2]
j=[3,4]

for y in i:
    for q in j:
        print(y,q)