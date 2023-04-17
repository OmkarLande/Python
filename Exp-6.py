#...........Map.........
def square(x):
    return x*x

l=[1,2,3,4,5]

print("Square of a given list is: ")
new_l=list(map(square, l))
print(new_l)

#..........Filter...........
def filter_fun(a):
    return a>2
print("List after filter:")
new_newl=list(filter(filter_fun,l))
print(new_newl)

#.......Lambda Function.......
l=[1,2,3,4,5]

print("Square of a given list is: ")
new_l=list(map(lambda x:x*x, l))
print(new_l)

#.........Reduce.........
from functools import reduce

nums=[3,2,1]
sum_num=reduce(lambda x,y: x+y, nums)
print("Sum of nums are:\n",sum_num)