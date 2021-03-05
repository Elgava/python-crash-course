known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "George", "Harry"]

while True:
    print("hi my name is Travis")
    name = input("what is you name: ").strip().capitalize()
    
    if name in known_users:
        print("Hello {}".format(name))
        remove = input("would you like to be removed from th system(y/n)?:").lower()
        
        if remove == "y":
            known_users.remove(name)
        elif remove == "n":
            print("no problem, i didnt want you to leave anyways")
            
    else:
        print("hmm i dont think ive met you {}".format(name))
        add_me = input("would you like to be added on the system(y/n)?: ").strip().lower()
        if add_me == "y":
            known_users.append(name)
        elif add_me == "n":
            print("no worries, see you around")

        


