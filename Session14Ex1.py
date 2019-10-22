#Write a function that takes the name of a text file as parameter. Print out the 3-letter words that start with "b"

def f1(file_name):
    fd = open(file_name)
    for line in fd:
        words = line.split()
        for word in words:
            if len(word) == 3 and word[0] == "b":
                print(word)
