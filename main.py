'''
2/08/21 Notes
Boolean Operators
- Used as conjunctions to combine or exclude keywords in a search

A = True
B = False
C = 5 > 3 # True
D = 6 == 4 # False

if (A and B): # True and False >> False
  print ("Hello")

elif (C or D): # True or False >> True
  print ("Hi")

Truth Table:
   
    A       B          A and B       A or B     not a
  True     True         True          True      False
  True     False        False         True      False
  False    True         False         True      True
  False    False        False         False     True
---------------------------------------------------------------------
print (5 > 1 and not 0 != 0 or False and not 6 >= 6) and 10 <= 11)
print (5 > 1 and not 0 != 0 or False and not 6 >= 6) and 10 <= 11)
print (False or not(True and True) or False and not True and True)
print (False or not(True and True) or False and not True and True)
print (False or False or False and False and True)
print (False or False or False and False and True)
print (False or False or False)
print (False or False)
print (False)
''' 
# Review of Leap Year Mini-Test:

year=int(input('Please enter a random year:'))
if (year % 4 == 0 and year % 100 != 0):
    print(year, "is a Leap Year")
elif (year % 100 == 0):
    print(year, "is not a Leap Year")
elif (year % 400 ==0):
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")

