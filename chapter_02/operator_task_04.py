balance = 1000
withdraw_amount = int(input("Enter amount to withdraw :"))

if withdraw_amount > 0 and withdraw_amount <=balance :
  balance -= withdraw_amount
  print("Remaining Balance :", balance)
else :
  print("insufficent Balance ......")