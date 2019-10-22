#Write a function that takes an integer as parameter and returns a list of all the divisors of that number

def f3(a):
    my_list = []
    for i in range (1, a+1):
        if a % i ==0:
            my_list.append(i)
    return my_list