#Email Slicer Program

#Get the user's email address
email = input("Please enter your email address: ")

#Slice the email address
username = email[:email.index("@")]
domain = email[email.index("@") + 1:]

#Display the results
print(f"Username: {username}")
print(f"Domain: {domain}")