import random
import psycopg2

# Establish connection to PostgreSQL
conn = psycopg2.connect(database="Customer",
                        host="localhost",
                        user="postgres",
                        password="shagun1296",
                        port="5432")

cursor = conn.cursor()

# Create the 'users' table if it doesn't exist
create_table_sql = """CREATE TABLE IF NOT EXISTS users(
                        Account_number SERIAL PRIMARY KEY,
                        FIRST_NAME VARCHAR(20) NOT NULL,
                        LAST_NAME VARCHAR(20),
                        Amount FLOAT)"""

cursor.execute(create_table_sql)
print("Table created successfully........")

def deposit_amount(acc_no, amount):
    dep_amount = float(input("Enter the amount you want to deposit: "))
    current_balance = Balance_enquiry(acc_no)
    if isinstance(current_balance, float):
        amount = current_balance + dep_amount
        sql = "UPDATE users SET Amount=%s WHERE Account_number=%s"
        cursor.execute(sql, (amount, acc_no))
        print("Amount deposited successfully........")
        conn.commit()
    else:
        print("Account not found or error retrieving balance.")

    return amount

def withdrawal_amount(acc_no, amount):
    withdrawal_amount = float(input("Enter the amount you want to withdraw: "))
    if amount < 3000:
        print("Insufficient Balance to Withdraw")
    elif amount < withdrawal_amount:
        print("Withdrawal amount exceeds the current balance")
    else:
        amount -= withdrawal_amount
        sql = "UPDATE users SET Amount=%s WHERE Account_number=%s"
        cursor.execute(sql, (amount, acc_no))
        print("Amount withdrawal successful........")

        conn.commit()
    return amount

def Balance_enquiry(acc_no):
    sql = "SELECT Amount FROM users WHERE Account_number=%s"
    cursor.execute(sql, (acc_no,))
    result = cursor.fetchone()
    if result:
        return result[0]  # Return the amount if the account is found
    else:
        return "Account not found"

def Create_account(account_number, firstname, lastname, amount):
    sql = "INSERT INTO users(Account_number, FIRST_NAME, LAST_NAME, Amount) VALUES(%s, %s, %s, %s)"
    cursor.execute(sql, (account_number, firstname, lastname, amount))
    print(f"Account created successfully with Account_number ={account_number}")

    conn.commit()
x='y'

while x=='y':

    user_choice = input("""Enter the function you want to choose :
                        1- Create Account
                        2- Withdrawal
                        3- Deposit
                        4- Balance Enquiry
                        5- Exit\n""")

    if user_choice == '1':
        account_number = random.randint(10000, 99999)
        firstname = input("Enter your firstname: ")
        lastname = input("Enter your lastname: ")
        amount = float(input("Enter the amount you want to deposit: "))
        if amount < 3000:
            print("Amount is too less to open account. Please deposit minimum 3000 to open your new account")
        else:
            Create_account(account_number, firstname, lastname, amount)

    elif user_choice == '2':
        acc_no = input("Enter the Account number you want to access: ")
        print(f"Total amount present in your {acc_no} is {withdrawal_amount(acc_no, Balance_enquiry(acc_no))}")

    elif user_choice == '3':
        acc_no = input("Enter the Account number you want to access: ")
        print(f"Total amount present in your {acc_no} is {deposit_amount(acc_no, Balance_enquiry(acc_no))}")


    elif user_choice == '4':
        acc_no = input("Enter the Account number you want to access: ")
        balance = Balance_enquiry(acc_no)
        if isinstance(balance, float):
            print(f"Total amount present in your {acc_no} is {balance}")
        else:
            print(balance)

    elif user_choice == '5':
        print("Exiting the program...")
        break

    else:
        print("Invalid choice !! Please enter valid option")

    x=input("press y to choose again and n to exit:")
    print("\n")
cursor.close()
conn.close()
