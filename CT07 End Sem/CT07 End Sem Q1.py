"""
============================================================
Q1. August Sales Analysis
============================================================
You are analysing the daily sales of an e-commerce store for August.
The sales for the 31 days are provided in a list.

Program Requirements:
- Use the list:
  daily_sales = [1205, 986, 1354, 10535, 15741, 11200, 800, 
                 13056, 952, 1100, 1025, 8574, 14014, 9987, 
                 1238, 1458, 7803, 900, 13674, 14539, 13241, 
                 10886, 7541, 8743, 1482, 11523, 977, 12181, 
                 8903, 1008, 1530]

- Find the day with the highest sales
- Find the day with the lowest sales
- Calculate the average daily sales

Print the result exactly in this format:
    5 August has highest sales of $15741
    7 August has lowest sales of $800
    Average daily sales for August is $6714.71

Note:
- The first item in the list represents 1 August
- The average must be rounded to 2 decimal places

============================================================
"""

# ============================================================
# Step 1: Create the list
# ============================================================
daily_sales = [1205, 986, 1354, 10535, 15741, 11200, 800, 
                13056, 952, 1100, 1025, 8574, 14014, 9987, 
                1238, 1458, 7803, 900, 13674, 14539, 13241, 
                10886, 7541, 8743, 1482, 11523, 977, 12181, 
                8903, 1008, 1530]


# ============================================================
# Step 2: Find highest sales
# ============================================================

high = max(daily_sales)
indexhigh = daily_sales.index(high) + 1

# ============================================================
# Step 3: Find lowest sales
# ============================================================

low = min(daily_sales)
indexlow = daily_sales.index(low) +1 

# ============================================================
# Step 4: Calculate average sales (round to 2 decimal places)
# ============================================================
i = 0
total = 0
while i != len(daily_sales):
    total = total + daily_sales[i]
    i = i + 1
average = total / len(daily_sales)
roundaverage = round(average,2)
# ============================================================
# Step 5: Print results in correct format
# ============================================================

print(f"{indexhigh} August has highest sales of ${high}")
print(f"{indexlow} August has lowest sales of ${low}")
print(f"Average daily sales for August is ${roundaverage}")
