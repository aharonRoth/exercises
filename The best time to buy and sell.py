def the_best_time_to_buy_and_sell(prices):
    buy = prices[0]
    sale = 0
    the_difference = 0
    for i in range(len(prices)):
        if  prices[i] < buy:
            buy = prices[i]
        elif prices[i] > buy:
            sale = prices[i]
            if sale - buy > the_difference:
                the_difference = sale - buy
    return the_difference
   
    

prices = [3,3,5,0,0,3,1,4]
print(the_best_time_to_buy_and_sell(prices))