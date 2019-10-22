# Write a function that forces the user to enter a multiple of 6 number. Use try, except to catch invalid inputs.
# Return that number

def f4():
    while True:
        try:
            n = input("give me a multiple of 6")
            n = int(n)
        except ValueError:
            print("That was not a number")
            continue

        if n % 6 == 0:
            #bingo
            return n
