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
print ("How much do you need to invest per month to retire at 50 assuming you are currently 36 (hey.. my exact age..)")
print ("per this website? https://walletburst.com/tools/coast-fire-calc/")
retAnswerperMonth = input ()
num = retAnswerperMonth
converted_num = int(num)

retAnswerinvestPeryear = converted_num * 12
print ( )
print ("That means you'll need to invest " + str(f"${retAnswerinvestPeryear:,.2f}") + " per year assuming you are currently 36")
print ( )
x= retAnswerinvestPeryear
post_tax_income = x / .3
post_tax_income_in_dollars = (f"${post_tax_income:,.2f}")
print ("The amount of post tax income you will need to make in order to retire by 50 while investing only 30 percent of  your income is " + post_tax_income_in_dollars)
living_money = post_tax_income - x
living_money_in_dollars = f"${living_money:,.2f}"
print (' ')
print ( "That will leave you with " + living_money_in_dollars + " to live on per year")
print ( )
pretax_income = (int(post_tax_income) / .65)
pretax_income_in_dollars = f"${pretax_income:,.2f}"
retirementLive = 40000
print ("Assuming a 35% overall tax rate")
print ("The amount of pretax income you will need in order to live off of is " + str(f"${retirementLive:,.2f}") + " a year is " + pretax_income_in_dollars)

