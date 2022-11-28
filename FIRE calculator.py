#more practice problems I don't want to run in the actual program
#print ('hello' == 'hello')
#print ('hello' == 'hEllo')
#print ('dog' != 'cat')
#print (True != False)

#print (51 == 000051.00000000)
#x = 3
#y = x + 9
#print ((y - 2)<4)
#y = y + 4
#print (y)
#y = y + 4
#print (y)
#y = y + 4
#print (y)
# will need to figure out some math on these values later, for now relying on the walletburst website linked below to get a monthly amount
#print ("How much do you have invested right now?")
#investedNow = input()
#print ("How much do you want to live off of when you retire?")
#liveOffamt = input()

#print ("That means you will need to invest " + y " per month to retire by 50")
print ("How much do you need to invest per month to retire when you want?")
print ("Go to this website which will help you answer the questions")
print ("https://walletburst.com/tools/coast-fire-calc/")
print ("How much did you need to end up contributing per month to reach FIRE?")
retAnswerperMonth = input ()
num = retAnswerperMonth
converted_num = int(num)

retAnswerinvestPeryear = converted_num * 12
print ( )
print ("That means you'll need to invest " + str(f"${retAnswerinvestPeryear:,.2f}") + " per year")
print ( )
print ("Now let's figure out what percentage of your income you'll need to invest.")
print("What percentage of your post tax income do you want to contribute to your retirement?")
print ("(e.g. if you only want to contribute 20% of your post tax income enter the number 20)")
incomePercent = input()
num = incomePercent
converted_num_2 = int(num)

x= retAnswerinvestPeryear
post_tax_income = x / (converted_num_2/100)
post_tax_income_in_dollars = (f"${post_tax_income:,.2f}")
print ( )
print ("The amount of post-tax income you will need to make per year while investing only " + incomePercent + " percent of  your income is " + post_tax_income_in_dollars)
living_money = post_tax_income - x
living_money_in_dollars = f"${living_money:,.2f}"
print ( "That will leave you with " + living_money_in_dollars + " to live on per year after investments and taxes.")
print ("What do you expect your overall tax rate to be?")
print ("If you think it'll be 35% then enter 35")
print ("(this is a good estimate number if you don't know)")
taxRate = input()
num = taxRate
converted_num_3 = int(num)
pretax_income = (int(post_tax_income) / (1 - (converted_num_3/100)))
pretax_income_in_dollars = f"${pretax_income:,.2f}"
print ("This means you'll need a pretax income of " + pretax_income_in_dollars + " per year if you only want to invest " + incomePercent  + " percent of your income per year")
print ("How much do you want to live off per year during retirement?")
print ("This will be the same number as you put in the website.")
retirementLive = input()
num = retirementLive
converted_num_4 = int(num)
print ("So to sum things up")
print ("The amount of pretax income you'll need in order to have " + str(f"${converted_num_4:,.2f}") + " per year paid to you in retirement is ")
print( pretax_income_in_dollars + " assuming a " + taxRate + " tax rate")

