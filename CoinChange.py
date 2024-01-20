# Problem Description: 
# Given a list of coin denominations (e.g., 1-cent, 5-cent, 10-cent) and a specific target
# amount (e.g., 27 cents), find the minimum number of coins needed to reach the exact amount, considering
# all possible combinations.

# Input the denominations
denominations = list( map(int, input("Enter the denominations space separated : ").split()))

# Input the amount
amount = int(input("Ebter the amount : "))

# Sort the denominations into descending order using selection sort
# denominations.sort(reverse=True)
def sort1(data):
    for i in range(len(data) - 1):
        max_index= i
        for j in range( i+1, len(data)):
            if data[j] > data[max_index]:
                max_index = j

        data[i], data[max_index] = data[max_index], data[i]
            
    return data

denominations = sort1(denominations)

# Number of coins
coins = 0
ncoins = {}

# Find most number of largest coin (by value) we can use smaller than the Amount given.
# Repeat the same with next smaller coin value, until all amount is depleated.
while amount > 0:
    for coin in denominations:
        if amount >= coin:
            coins += amount // coin
            amount %= coin
            ncoins[coin] = coins
            
# Print the answer
print("The minimum number of coins required : ", coins)

# Required Coins
print("The coins required are : ", ncoins)