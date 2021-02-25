#3-4 guest list
guests = ['sudhir', 'tiffany', 'ashlyn', 'carti', 'mishka']
print (f"yo {guests[0]}, its ya boi, im making my specialty, and your favourite, im having a dinner party on saturday, pull through broshizzle")
print (f"hey {guests[1]}, im having a dinner party on saturday and woud like ot know if oyu can make it, im cooking the same thing i made the first time i cooked for you")
print (f"broooo, {guests[2]} tune your stekkie you busy saturday, you coming to my house for a dinner party")
print (f"yo {guests[3]}, its been too long bro, pul up to my hosue for a dinner party on saturday")
print (f"hey {guests[4]}, its boyfie, im having a dinner party on saturday, would you like to come?")

#3-5 guest list changer
guests.append("andrea")

print (f"yo {guests[0]} im still having a dinner party, someone just canceled ")
print (f"{guests[1]}")
print (f"{guests[2]}")
print (f"{guests[3]}")
print (f"{guests[4]}")

#3-6 more guests
guests.insert(1, 'logan')
guests.insert(2, 'dylan')
guests.append('keenan')
print (f"yo {guests[0]} im still having a dinner party, someone just canceled ")
print (f"{guests[1]}")
print (f"{guests[2]}")
print (f"{guests[3]}")
print (f"{guests[4]}")
print("i copped a bigger table that we can use for the dinner party")

#3-7 shrinking guest list
cnt_come = guests.pop(0)
cnt_come = guests.pop(3)
cnt_come = guests.pop(4)

print (f"yo {guests[0]} ")
print (f"{guests[1]}")
print (f"{guests[2]}")
print (f"{guests[3]}")
print (f"{guests[4]}")

print(f"im sorry {guests[0]} but theres not enough space anymore")
print(f"im sorry {guests[3]} but theres not enough space anymore")
print(f"im sorry {guests[4]} but theres not enough space anymore")