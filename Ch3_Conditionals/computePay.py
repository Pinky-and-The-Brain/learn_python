# compute pay with conditionals
hours_prompt = 'Enter hours:'
hours = input(hours_prompt)
pay_prompt = 'Enter pay:'
pay = input(pay_prompt)
if int(hours) <= 40:
    rate = int(hours)*int(pay)
else:
    overtime = int(hours) - 40
    rate = 40*int(pay) + overtime*(1.5*int(pay))
print('Rate for the hours is : ' + str(rate))