
import random

mylist = ["Everest", "Newton", "blueberry","library","continent"]
hidden_word = random.choice(mylist).lower()


def check_attempt(inputstr):
    if len(inputstr) > 1 and hidden_word == inputstr:
        print("Congratulations, you guessed the word!")
    elif len(inputstr) > 1:
        print("You failed!")
    else:
        ind = hidden_word.find(inputstr)



for i in range(1,len(hidden_word)):
    mask_word =+"*"

print("There is a hidden word:   "+mask_word)

nbr_att = int(input("Input your number of attempts:"))

for i in range(1,nbr_att):
    str_att = int(input("Input your letter or word:")).lower()
    if len(str_att) == 0:
        print("You need to enter a letter or word")
    check_attempt(str_att)



