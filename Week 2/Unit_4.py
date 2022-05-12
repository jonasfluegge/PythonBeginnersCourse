stocks = [["SAP", 106, -3.0], ["AAPL", 165, 1.25], ["TSLA", 860, 54.2], ["ORCL", 76, -0.25], ["ZM", 114, 6.2]]

i = len(stocks)
x = 0
sell_list = []

for i in stocks:
    if stocks[x][2] > 5:
        sell_list.append(stocks[x][0])
    x += 1

print(sell_list)
