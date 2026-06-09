user_name = input("Ener Username :")
password = input("Enter Password :")

if user_name =="admin" and password == "123456" :
  print("Login Successful....!")
elif user_name =="admin" and password !="123456":
  print("Invalid password")
elif user_name != "admin" and password == "123456" :
  print("invalid username")
else:
  print("Invalid username & password")