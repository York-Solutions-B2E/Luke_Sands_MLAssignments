# Create a function that gets a list of numbers, and returns the sum of all positive ones.
def num_list(a):
    total = 0
    for i in a:
        if i >= 0:
            total += i
    print("The total of all positive numbers is", total)
    return total


num_list([1, -2, 3, 4, -5])


# Create a function that takes a boolean value and returns a "Yes" for true and "No" for false
def bool_func(b):
    if b:
        print("Yes")
        return "Yes"
    # else:   #apparently the else is redundant,  when would we need it?
    print("No")
    return "No"
    # else:
    #     print("Invalid Input")
    #     return "Invalid Input"


#bool_func()


# Create a function that when given a list of numbers returns the smallest number in the list.
# def get_min(c):
#     smallest = min(c)
#     print("The smallest number in the list is", smallest)
#     return smallest


# get_min([1, 2, 3, 4, 5])
def get_min(c):
    smallest = c[0]
    for i in c:
        if i < smallest:
            smallest = i
    print("The smallest number in the list is", smallest)
    return smallest


get_min([2, 3, -2, 3, 4, 5])


# Create a function that calculates the average of the values in a list
def get_avg(d):
    mySUM = 0
    for i in d:
        mySum += i
    print("The average of the list is", counter / len(d))
    return mySum / len(d)


get_avg([2, 4, 6, 8])


# For every number from 1 to 20 do the following:
# if the number is a multiple of 3, print "Fizz"
# if the number is a multiple of 5, print "Buzz"
# if the number is a multiple of both 3 and 5 print "FizzBuzz"
# Otherwise, just print the number

#My Solution
def fizz_buzz_1():
    for i in range(1, 21):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


#Jenny's Solution:
def fizz_buzz_2():
    for i in range(1, 21):
        if i % 3 == 0:
            if i % 5 == 0:
                print("FizzBuzz")
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


fizz_buzz_1()
fizz_buzz_2()
