# You work in a company where salespeople receive 13%
# commissions on their total sales, and your boss wants you to help the salespeople
# calculate their commissions by creating a program that asks them their name and
# how much they've sold this month.

name = input("Please, tell me your name:\n")
sales = int(input("please, input your total month sales:\n"))

commission = round(sales * 13/100, 2)

print(f'Hello {name}, your commissions this month is ${commission}')
