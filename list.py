user_names = ['Falz', 'Peter', 'Johnson','Admin', 'John']
if user_names == 'Admin':
   print("Hello admin, would you like to lsee a status report?")
else:
   print(f"Adding {user_names}.")
print("\nHello, thanks for logging in again.")
user_names = []
if user_names:
    for user_names in user_names:
        print(f"Adding {user_names}.")
print("\nwe need to find some users!")
current_users = ['Peter', 'Fawaz', 'Admin']
new_users = ['John', 'Johnson', 'Google']
for new_users in new_users:
    if new_users in current_users:
        print(f"Adding {new_users}.")
    else:
       print(f"The username is available{user_names}.")
ordinal_numbers = list(range(1, 10))
print (ordinal_numbers)
for i in ordinal_numbers:
    if i == 1:
        print(f"{i}st")
    if i == 2:
        print(f"{i}nd")
    if i == 3:
        print(f"{i}rd")
    if i >= 4:
        print(f"{i}th")
