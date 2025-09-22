#Write a simpel program that will calculate how much money a party of people would pay if they shared the bill
bill = float(input("How much is the total bill?: "))
print("Dont' write the % signe!!!")
tip = int(input("How much do you want to tip? 10%, 15% or 20%: "))
people = float(input("How many people are splitting the bill?: "))

#Always go step by step instead of trying to put all on a singed line. You still new to this, you are remembering how math works. You are doing good.
tip_calculation = float(bill* (tip / 100))
total_bill_amount = bill + tip_calculation
pay = round(total_bill_amount / people, 2)
print(f" Your share of the bill is: {pay}")