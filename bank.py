import os
#retrieved from: https://github.com/python/cpython/blob/3.11/Lib/os.py
import csv 
#retrieved from: https://github.com/python/cpython/blob/3.11/Lib/csv.py
import random 
#retrieved from: https://github.com/python/cpython/blob/3.11/Lib/random.py
rows=[]
e=False #to exit or continue while loop

fieldnames=["account_number", " account_holder", " balance"]


#title: Writing CSV Files in Python
#retrieved from: https://www.youtube.com/watch?v=s1XiCh-mGCA&t=67s&ab_channel=PrettyPrinted
def create_file():
  with open('accounts.csv', 'w', newline='') as f:
    f.close()

def create_account():
  with open('accounts.csv', 'a', newline='') as f:
    thewriter = csv.DictWriter(f, fieldnames=fieldnames)
    account_number = ''.join(str(random.randint(0, 9)) for i in range(8))
    account_holder = input("Enter account holder name: ")
    global balance
    balance = float(input("Enter opening balance: "))
    rows.append([account_number, account_holder, balance])
    thewriter.writerow({'account_number': (account_number), ' account_holder':  (account_holder), ' balance': (balance)})
    print("your account number is: " + str(account_number))
    f.close()
    return account_number

#title: Searching Data in CSV File using Python
#retreived from: https://www.youtube.com/watch?v=7TOfPrOt2HE&ab_channel=RaiyadRaa
def read_file():
  with open('accounts.csv', 'r') as file:
    reader=csv.reader(file)
    for row in reader:
      rows.append(row)
    file.close()

def login():
  read_file()
  print("please enter your account number in order to proceed")
  current_account_number=input()
  if current_account_number in (item for sublist in rows for item in sublist):
    print("you've successfully logged in!")
    for i in range(len(rows)):
      if rows[i][0]==current_account_number:
        return i
    
  else:
    print("account not found, let's create a new account instead")
    create_account()
    return False
    
      
def information():
  print(rows[id])

def clear():
  with open("accounts.csv",'r+') as file:
    file.truncate(0)
  

def withdrawal(amount_withdrawing, id):
  print(id)
  global rows
  rows=[]
  read_file()
  if float(amount_withdrawing)<=float(rows[id][2]):
    rows[id][2]=float(rows[id][2])-float(amount_withdrawing)
    clear()
    with open('accounts.csv', 'w', newline='') as f:
      csv_writer=csv.writer(f)
      for row in rows:
        csv_writer.writerow(row)
    print("You've successfully withdrawn " + str(amount_withdrawing))
    return rows[id][2]

  else:
    print("you do not have enough money, the transaction could not be completed.")

def depositing(amount_depositing, id):
  global rows
  rows=[]
  read_file()
  rows[id][2]=float(rows[id][2])+float(amount_depositing)
  clear()
  with open('accounts.csv', 'w', newline='') as f:
    csv_writer=csv.writer(f)
    for row in rows:
      csv_writer.writerow(row)
    print("You've successfully deposited "+ str(amount_depositing))
    return rows[id][2]




#Beginning of code:
print("Welcome to the bank")

exist=False

if os.path.isfile('accounts.csv'):
  exist=True
else:
  exist=False

if exist!=True:
  print("it seems like you dont have an account, let's fix that")
  create_file()
  create_account()
  id=login()
else:
  start=input("-- login (l), create account (ca) ")
  if start=='l':
    #read_file()
    id=login()
  elif start=='ca':
    create_account()
    login()
    


#Loop of code


while e!=True:
  commands= input("-- account info (i), withrdaw (w), deposit (d), exit (e) ")
    
  if commands=="i":
    information()
 
  elif commands=="w":
    amount_withdrawing=float(input("How much do you want to withdraw? "))
    withdraw= withdrawal(amount_withdrawing, id)


  elif commands=="d":
    amount_depositing=float(input("How much do you want to deposit? "))
    deposit= depositing(amount_depositing, id)
    



  elif commands=="e":
    print("Thanks for visiting, see you next time.")
    e=True
    
  else:
    print("It seems like the your input is invalid, try again?")