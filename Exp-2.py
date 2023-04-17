#........Conditional statement........

roll_num =int(input('Enter roll number from 400 to 480 '))
print(" your roll number is ",roll_num)

if roll_num>400 and roll_num<=420:
    print("You are in s1 batch")
elif roll_num>420 and roll_num<=440:
    print("You are in s2 batch")
elif roll_num>440 and roll_num<=460:
    print("You are in s3 batch")
else :
    print("You are in s4 batch")