#atm machine system
menu = """
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit
"""
balance = 0
while True:
  print(menu)
  user = input("Enter your choice sir: ")
  if user == "1":
  	print(f"Your current balance is {balance} rs")
  elif user == "2":
  	deposit = int(input("Enter your deposit amount: "))
  	balance += deposit
  	print("Your current balance is: ",balance)
  elif user == "3":
  	withdraw = int(input("Enter withdraw Amount: "))
  	if balance >= withdraw:
  		balance -= withdraw
  		print(f"Your Amount {withdraw} Successfully withdrawn\nyour current balance",balance)
  	else:
  		print("insufficient balance")
  elif user == "4":
  	print("Thank you for using atm")
  	break
  else:
  	print("invalid choice")
