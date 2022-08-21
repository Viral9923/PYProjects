#Program to accept username and password to reveal information

username = input("Enter username:");

print("The username is:", username);

password = input("Enter password:");

if password=='jsk23':
  print("Access granted !");
  print("Details....");
  print(" Hotel Name: Boston Marriott");
  print(" Room No: 502");
  print("Person Name: Jack Steven");
  print("Type: Economy");
else:
  print("Sorry..Wrong Password..");