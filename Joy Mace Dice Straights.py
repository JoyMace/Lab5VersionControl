import random

# Create an empty list
dice = []

# Roll five dice (random numbers 1-6) and store each one in the list
for i in range(0,5):
    dice.append(random.randint(1,6))

# Print the dice that were rolled
print(dice)

# Create list to count the number of each die that showed up
# Initially, each value is zero
count = [0,0,0,0,0,0]

# Look at teach die in the list
for die in dice:
    # This lets us count how many of each value were rolled
    # For example, if we rolled a 1, increment the value at count[0] by 1
    count[die-1] += 1 
    # You can uncomment this for debugging
    #print(die)
    #print(count)
# Need a way to add up the value of each die. If the total is 15 or 20 and
# max count is 1, it is a straight
value = sum(dice)
print(value)
# Finding the biggest number in the count list
# to determine if we rolled 2 of a kind, 3 of a kind, etc.
if max(count) > 1:
    print('You had', max(count),'of a kind.')    
else:
    print('You had no pairs or better.')
#straights
if max(count) == 1 and (value == 15 or value == 20):
    print('You rolled a straight.')
