costP = float(input("Enter the cost price:"))
sellP = float(input("Enter the Selling Price:"))
profit = sellP-costP
print("Profit:",profit)
new_profit = profit + (profit*0.05)
new_sellP = costP + new_profit
print("New selling Price:",new_sellP) 
