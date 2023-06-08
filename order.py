"""Wrote a program to show the remaining days, weeks, months and years for any age lived for 
a perticular person for a maximum age of 90 years.
"""
age=input('enter your age:')
maximum_age=90*365
age= int(age) *365
remaining_days=maximum_age-age
remaining_weeks=round(remaining_days/7)
remaining_months=round(remaining_days/30)
remaining_years=remaining_days/365
print('remaining days to live:',  remaining_days)
print('remaining weeks to live:', remaining_weeks)
print('remaining months to live:',remaining_months )
print('Remaining years to live:', remaining_years)