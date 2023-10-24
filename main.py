
import random

mylist = ["Everest", "Newton", "blueberry", "library", "continent"]
hidden_word = random.choice(mylist).lower()
mask_word = ""
for i in range(0, len(hidden_word)):
    mask_word += "*"
print("There is a hidden word:   "+mask_word)
success = False

def check_attempt(inputstr):
    global success
    success = False
    mask2 = ""
    if len(inputstr) > 1 and hidden_word == inputstr:
        return hidden_word
    elif len(inputstr) > 1:
        print("You failed!")
        return mask_word
    else:
        for k in range(0, len(hidden_word)):
            if inputstr == hidden_word[k]:
                mask2 += inputstr
                success = True
            else:
                mask2 += mask_word[k]
        return mask2


nbr_att = int(input("Input your number of attempts:"))
i = 1
while i <= nbr_att:
    str_att = str(input(str(i)+ " Input your letter or word:")).lower()
    if len(str_att) == 0:
        print("You need to enter a letter or word")
    mask_word = check_attempt(str_att)
    if mask_word == hidden_word:
        print("Congratulations, you guessed the word!")
        break
    else:
        print("Check the word:  " + mask_word)
    if not success:
        i += 1

if mask_word != hidden_word:
    print("Game over")
