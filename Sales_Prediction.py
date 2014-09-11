__author__ = 'dwight'

# A company has determined that its annual profit is typically 23 percent of total sales. Write a program that asks
# the user to enter the projected amount of total sales, and then displays the profit that will be made from that
# amount.

ANNUAL_PERCENTAGE_PROFIT = 0.23

projectedTotalSales = (float(input("Enter projected total sales: $")))
annualProfit = projectedTotalSales * ANNUAL_PERCENTAGE_PROFIT
print("Annual Profit: $", format(annualProfit, ',.2f'), sep='')