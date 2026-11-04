import numpy as np
prices = np.array([100, 102, 101, 105, 107, 106, 110, 108, 112, 115])
length = len(prices)

#finding the maximum, minimum and average price 
min_price = np.min(prices)
max_price = np.max(prices)
average_price = np.average(prices)

#finding the last three abd last ones operations 
first_three = np.arange(start = 0, stop = 3, step = 1)
last_three = np.arange(start = -3, stop =0 , step = 1)

#profitability of each day 
returns = (prices[1:] - prices[:-1]) / prices[:-1]

#fiding positive days 
positive_days = np.sum(returns > 0 )

#counting the volatility of each day 
volatility = np.std(returns)

#finding wining and losing days 
win = np.argmax(returns)
lose = np.argmin(returns)

print(f"length - {length}\nminimum price - {min_price}\nmaximum price - {max_price}\naverage price {average_price}\n"
f"first three prices - {prices[first_three]}\nlast three prices {prices[last_three]}\n"
f"profitability - {returns}\npositive days - {positive_days}\nvolatility dats - {volatility}profit days - {win}")
