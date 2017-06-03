from random import randint

while True:
    raw = raw_input("Roll the Dice? Yes or no: ")

    if raw == "yes":
        print (randint(1,6))

    if raw == "no":
        print "Finished"
        break
