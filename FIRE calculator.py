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
print ("The amount of post-tax income you will need to make per year while investing only " + incomePercent + "percent of  your income is " + post_tax_income_in_dollars)
living_money = post_tax_income - x
living_money_in_dollars = f"${living_money:,.2f}"
print ( "That will leave you with " + living_money_in_dollars + " to live on per year after investments and taxes.")
print ("Or " + str(f"${(living_money / 12):,.2f}") + " per month to live on")
print ( )
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
print ( )
print ("So to sum things up")
print ("The amount of pretax income you'll need in order to have " + str(f"${converted_num_4:,.2f}") + " per year paid to you in retirement is ")
print( pretax_income_in_dollars + " assuming a " + taxRate + "% tax rate")

print ("Now we can figure out how this translates to what you currently make.")
print ("Write a rough estimate of your after tax salary")
userSalary = input()
converted_num_5 = int(userSalary)
print ("So if you make " + str(f"${converted_num_5:,.2f}") + " per year and you invest " + str(f"${retAnswerinvestPeryear:,.2f}") + " per year")
print ("You'll end up with " + str(f"${(converted_num_5 - retAnswerinvestPeryear):,.2f}") + " left over at the end of the year")
print ("Per month you'll have " + str(f"${(converted_num_5 / 12):,.2f}") + " of take home pay")
print ("And will need to invest " + str(f"${(retAnswerinvestPeryear / 12):,.2f}") + " per month")
print ("Which leaves you with " + str(f"${((converted_num_5 / 12) - (retAnswerinvestPeryear / 12)):,.2f}") + " left over to spend on everything else per month")
