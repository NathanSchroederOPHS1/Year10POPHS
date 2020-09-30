age = int(input("enter an age"))

if age >=18:
    print("you can watch all films!")
elif age >=15:
    print("you can only watch films that are rated 15 and under")
elif age >=12:
    print("you can only watch 12 and under rated movies")
else:
    print("You can only watch U rated fims")
