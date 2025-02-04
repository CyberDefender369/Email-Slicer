#get user's email address
email = input("What is your email address?: ").strip()

#slice out user name
username = email[:email.index("@")]

#slice out domain name
domain = email[email.index("@") + 1:]

#format message
output = f"Your username is {username.lower()} and your domain is {domain.lower()}"

#display output
print(output)