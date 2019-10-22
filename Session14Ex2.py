#Write a recursive function that computes a to the power b (a and b are parameters given to the function)

def f2(a,b):
    if b == 0:
        return 1
    return a* f2(a,b-1)
