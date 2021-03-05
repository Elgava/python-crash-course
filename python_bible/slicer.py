#get user email address
email = input("what is you email address: ").strip()

#slice out username
user = email[:email.index("@")]

#slice out domain name
domain = email[email.index("@")+1:]

#format message
output="your username is {} and your domain name is {}".format(user, domain)

#display output message
print(output)
