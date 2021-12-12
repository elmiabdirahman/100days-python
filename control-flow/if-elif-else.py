print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height > 120:
    print("you can ride the rollercoaster!")
    age = int(input("what is your age? "))
    if age < 12:
        bill = 5
        print("child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("youth tickets are $7.")
    else:
        bill = 12
        print("adults tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        # add $3 to their bill
        bill += 3

    print(f"your final bill is ${bill}")

else:
    print("sorry, you have to be taller before you can ride")
