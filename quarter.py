User_input = int(input("Please enter a month: "))


if User_input >=1 and User_input <= 3:
    print('first quarter')
elif User_input >=4 and User_input <= 6:
    print('second quarter')
elif User_input >=7 and User_input <= 9:
    print('third quarter')
elif User_input >=10 and User_input <= 12:
    print('fourth quarter')
else:
    print('error')