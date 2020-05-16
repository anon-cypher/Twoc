score1,score2,score3 = int(input("Score1:")),int(input("Score2:")),int(input("Score3:"))
strike1,strike2,strike3 = (score1/60)*100, (score2/60)*100,(score3/60)*100

print("Strike Rate of Players:\n",strike1,strike2,strike3,sep=" ")

# If players get 60 more balls
print('Run scored by player 1 after 60 more balls:',score1*2)
print('Run scored by player 2 after 60 more balls:',score2*2)
print('Run scored by player 3 after 60 more balls:',score3*2)

# Max number of sixes each player could hit
print("Maximum number of sixes by player 1:", score1//6)
print("Maximum number of sixes by player 2:", score2//6)
print("Maximum number of sixes by player 3:", score3//6)
