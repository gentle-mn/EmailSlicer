# get user Email Address

email = input("What is your email address?: ").strip()

# slice out Username

user = email[:email.index("@")]

# slice Domain Name

domain = email[email.index("@") + 1 :]

# format Message

output = "Your username is {} and your domain name is {}".format(user, domain)

# display Output Message

print(output)
