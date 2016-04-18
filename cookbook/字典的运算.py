prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

min_price = min(zip(prices.values(), prices.keys()))
# min_price is (10.75, 'FB')
print(min_price)
max_price = max(zip(prices.values(), prices.keys()))
# max_price is (612.78, 'AAPL')
print(max_price)

prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)

print(max(prices))
# out IBM
print(min(prices))
#out AAPL