films = {
    "Finding Dory":[3,5],
    "Bourne":[18,5],
    "Tarzan":[15,5],
    "Ghost Busters":[12,5]

    }
while True:
    print("your choices are: Finding Dory, Bourne, Tarzan and Ghost Busters")
    choice = input("which movie do you want to watch?: ").strip().title()
    if choice in films:
        age = int(input("How old are you?: ").strip())

        #check user age
        if age >=films[choice][0]:

            number_seats = films[choice][1]
           
            #check enough seats
            if number_seats > 0:
                print("enjoy the film...")
                films[choice][1] = films[choice][1]-1
                
            else:
                print("sorry we dont have enough seats")
                
        else:
            print("you are too young to watch that film")
            
    else:
        print("we dont have that film...")
