bill = input("what is the bill tonight? ")

# I need to convert bill from a string to a float
bill = float(bill)
tip10 = bill + bill * .10
tip15 = bill + bill * .15
tip20 = bill + bill * .20
tip25 = bill + bill * .25

print("10% tip: " + str(tip10))
print("15% tip: " + str(tip15))
print("20% tip: " + str(tip20))
print("25% tip: " + str(tip25))

game1=13
game2=18
game3=25
game4=17
game5=31
print((game1+game2+game3+game4+game5)//5)