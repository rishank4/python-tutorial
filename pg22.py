def compound_interest(principal,rate,time):
    amount=principal*(1+rate/100)**time
    interest=amount-principal
    return interest,amount
P=float(input("enter principal amount:"))
R=float(input("enter annual interest rate(in %):"))
T=float(input("enter time period(in years):"))
compount_intrest,final_amount=compound_interest(P,R,T)
print(f"compound interest:{compount_intrest:.2f}")
print(f"final amount:{final_amount:.2f}")
