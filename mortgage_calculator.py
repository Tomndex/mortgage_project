print("Mortgage Calculator 2.0 - calculate your monthly mortgage payments, your total mortgage repayment and your total interest paid")
print("""
Please have the following information available when you start - 1) Price of House
                                                                 2) Fixed Annual Interest Rate
                                                                 3) Deposit Required
                                                                 4) Length of Mortgage""")

price_of_house = float(input("How much does the house cost?: $"))
# have decided to let user know not to include the % symbol as im not sure how i would be able to only use the number without the symbol if it is not seperated by space
deposit = float(input("How much is the required deposit? (dont include percentage symbol) "))
fixed_annual_interest_rate = float(input("What is the fixed annual interest rate? (dont include percentage symbol) "))
length_of_mortgage = int(input("How long is the mortgage supposed to run for? "))

principal = price_of_house - (deposit/100*price_of_house)
interest_rate = (fixed_annual_interest_rate/100)/12
number_of_payments = length_of_mortgage * 12

def monthly_mortgage_payment(principal, interest_rate, number_of_payments):
    single_payment = principal * interest_rate *(1 + interest_rate)**number_of_payments / (1 + interest_rate)**number_of_payments -1
    print(single_payment)
monthly_mortgage_payment(principal,interest_rate,number_of_payments)