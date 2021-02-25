#2-3 personal message
name = "jay"
message = f"Hello,{name.title()} would you like to learn some Python today?!\n"
print(message)

#2-4 naem case
F_name = "elgin malouw"
print(F_name.title())
print(F_name.upper())
print(f"{F_name.lower()}\n")

#2-5 famous quote
print(f'Albert Einstein once said, "A person never made a mistake never tried anything new"\n')

#2-6 famous quote 2
famous_person = "nick kroll"
quote = "everybody gets better looking on tv as shows go on, even the nerds on 'big bang theory' are getting better looking"
print(f'{famous_person} once said, "{quote}"')

#2-7 stipping names
M_name = " elgin malouw "
print(f"\t{M_name.lstrip()}")
print(f"\n{M_name.rstrip()}")
print(f"\t{M_name.strip()}\n")