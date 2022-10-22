# encoding: utf-8
data = ['ACME', 50, 91.1, (2012, 12, 21)]

name, shares, price, date = data

print(name, date)

name, shares, price, (year, month, day) = data

print(name, year, month, day)

_, shares, price, _ = data
print(shares, price)
