#Sam Smedinghoff
#1/30/18
#compoundDemo.py - how to use and/or

num = int(input('Enter a number: '))

if num > 0 and num%7 == 0:
    print(num, 'is positive and divisible by 7')
elif num > 0 and num%7 != 0:
    print(num, 'is positive and not divisible by 7 :(')
