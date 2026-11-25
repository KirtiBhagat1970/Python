try:
    balance=int(input("Enter a balance:"))
    withdrawal_amt=int(input("Enter a withdrawal amount:"))
    
    if withdrawal_amt > balance:
        raise ValueError("insufficient balance to withdrawal")
    print("withdrawal successfully")
    balance=balance-withdrawal_amt
    print("balance:",balance)
    
except ValueError as e:
    print("Error:",e)
    
finally:
    print("Transaction completed")