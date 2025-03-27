#######################################################################################################################################################
# 
# Name: shraddha thakre
# SID: 740100657
# Exam Date:
# Module: BEMM458 programming in business analytics 
# Github link for this assignment:  
#
#######################################################################################################################################################
# Instruction 1. Read each question carefully and complete the scripts as instructed.

# Instruction 2. Only ethical and minimal use of AI is allowed. You may use AI to get advice on tool usage or language syntax, 
#                but not to generate code. Clearly indicate how and where you used AI.

# Instruction 3. Include comments explaining the logic of your code and the output as a comment below the code.

# Instruction 4. Commit to Git and upload to ELE once you finish.

#######################################################################################################################################################

# Question 1 - Loops and Lists
# You are given a list of numbers representing weekly sales in units.
weekly_sales = [120, 85, 100, 90, 110, 95, 130]

# Write a for loop that iterates through the list and prints whether each week's sales were above or below the average sales for the period.
# Calculate and print the average sales.

# Given sales data
weekly_sales = [120, 85, 100, 90, 110, 95, 130]

# Calculate the average sales
average_sales = sum(weekly_sales) / len(weekly_sales)
print("Average Sales: {average_sales}")

# Check the list and evaluate the sales performance for each week.
for sales in weekly_sales:
    if sales > average_sales:
        print(f"{sales} is above average")
    else:
        print(f"{sales} is below average")

#######################################################################################################################################################

# Question 2 - String Manipulation
# A customer feedback string is provided:
customer_feedback = """The product was good but could be improved. I especially appreciated the customer support and fast response times."""

# Find the first and last occurrence of the words 'good' and 'improved' in the feedback using string methods.
# Store each position in a list as a tuple (start, end) for both words and print the list.



# Finding positions of 'good'
start_1 = customer_feedback.find("good")
end_1 = start_1 + len("good") 

# Finding positions of 'improved'
start_2 = customer_feedback.find("improved")
end_2 =start_2 + len("improved") 

# Storing positions in a list of tuples
positions = [("good", (start_1, end_1)), ("improved", (start_2, end_2))]

print(positions)
#######################################################################################################################################################

# Question 3 - Functions for Business Metrics
# Define functions to calculate the following metrics, and call each function with sample values (use your student ID digits for customization).

# 1. Net Profit Margin: Calculate as (Net Profit / Revenue) * 100.
# 2. Customer Acquisition Cost (CAC): Calculate as (Total Marketing Cost / New Customers Acquired).
# 3. Net Promoter Score (NPS): Calculate as (Promoters - Detractors) / Total Respondents * 100.
# 4. Return on Investment (ROI): Calculate as (Net Gain from Investment / Investment Cost) * 100.

# 1-Function to calculate Net Profit Margin(NPM)
def net_profit_margin (net_profit, revenue):
    npm=(net_profit/revenue)*100
    if( npm != 0):
        return npm
    else:
        return 0

#2-Function to calculate Customer Acquisition Cost (CAC)
def Customer_Acquisition_Cost (total_marketing, new_customers):
    CAC= (total_marketing/ new_customers)
    if(CAC !=0):
        return CAC 
    else:
        return 0
    

#3-Function to calculate Net Promoter Score (NPS)
def net_promoter_score (promoters, detractors, total_respondents):
    NPS= (promoters - detractors) / total_respondents * 100
    if (NPS !=0):
        return NPS
    else:
        return 0
    
#4-Function to calculate Return on Investment (ROI)
def Return_on_Investment (net_gain, investment_cost):
    ROI=(net_gain / investment_cost)*100
    if (ROI !=0):
        return ROI 
    else:
        return 0

# Sample values
net_profit = 12000
revenue = 15000
total_marketing = 550
new_customers = 115
promoters = 89
detractors = 56 
total_respondents = 650
net_gain = 9000
investment_cost = 40000

print("Net profit margin: ", net_profit_margin(net_profit,revenue))
print("cost accuisiqtion cost:",Customer_Acquisition_Cost(total_marketing, new_customers)) 
print("net promoter score:",net_promoter_score (promoters, detractors, total_respondents))
print("return on investment:",Return_on_Investment (net_gain, investment_cost))

#######################################################################################################################################################

# Question 4 - Data Analysis with Pandas
# Using a dictionary sales_data, create a DataFrame from this dictionary, and display the DataFrame.
# Write code to calculate and print the cumulative monthly sales up to each month.
import pandas as pd

sales_data = {'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'], 'Sales': [200, 220, 210, 240, 250]}

import pandas as pd
sales_data = {'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'], 'Sales': [200, 220, 210, 240, 250]}
df=pd.DataFrame(sales_data)
df['Cumulative Sales'] = df['Sales'].cumsum()
print(df)
#######################################################################################################################################################

# Question 5 - Linear Regression for Forecasting
# Using the dataset below, create a linear regression model to predict the demand for given prices.
# Predict the demand if the company sets the price at £26. Show a scatter plot of the data points and plot the regression line.

# Price (£): 15, 18, 20, 22, 25, 27, 30
# Demand (Units): 200, 180, 170, 160, 150, 140, 130


 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Given data
price = np.array([15, 18, 20, 22, 25, 27, 30]).reshape(-1, 1)  
demand = np.array([200, 180, 170, 160, 150, 140, 130])

# Create and train the Linear Regression model
regression_model = LinearRegression()
regression_model.fit(price, demand)

# Predict demand for price £26
predicted_demand = regression_model.predict([[26]])[0]

# Display the predicted value
print(f"Predicted Demand at £26: {predicted_demand:.2f} units")

# Plot scatter points for actual data
plt.scatter(price, demand, color='blue', label="Actual Data")

# Plot the regression line
predicted_line = regression_model.predict(price)
plt.plot(price, predicted_line, color='red', label="Regression Line")

# Highlight predicted value at £26
plt.scatter(26, predicted_demand, color='green', marker='o', label=f"Prediction at £26")


plt.xlabel("Price (£)")
plt.ylabel("Demand (Units)")
plt.title("Price vs Demand - Linear Regression")
plt.legend()
plt.grid()
plt.show()


#######################################################################################################################################################

# Question 6 - Error Handling
# You are given a dictionary of prices for different products.
prices = {'A': 50, 'B': 75, 'C': 'unknown', 'D': 30}

# Write a function to calculate the total price of all items, handling any non-numeric values by skipping them.
# Include error handling in your function and explain where and why it’s needed.

prices = {'A': 50, 'B': 75, 'C': 'unknown', 'D': 30}

# Function to calculate total price
def calculate_total(prices):
    total = 0  
    for item, price in prices.items():
        try:
            # Try converting the price to a numeric value (float)
            total += float(price)
        except (ValueError, TypeError):  
            print(f"Skipping invalid price for item {item}: {price}")
    
    return total

# Calling the function
total_price = calculate_total(prices)
print(f"Total valid price: {total_price}")

#######################################################################################################################################################

# Question 7 - Plotting and Visualization
# Generate 50 random numbers between 1 and 500, then:
# Plot a histogram to visualize the distribution of these numbers.
# Add appropriate labels for the x-axis and y-axis, and include a title for the histogram.

import matplotlib.pyplot as plt
import random


# Generate 50 random numbers between 1 and 500
random_numbers = [random.randint(1, 500) for _ in range(50)]

# Plot histogram
plt.hist(random_numbers, bins=20, color='red', edgecolor='blue')

plt.xlabel("Value Range")
plt.ylabel("Frequency")
plt.title("Histogram of Random Numbers (1-500)")

# Show plot
plt.show()
#######################################################################################################################################################

# Question 8 - List Comprehensions
# Given a list of integers representing order quantities.
quantities = [5, 12, 9, 15, 7, 10]

# Use a list comprehension to create a new list that doubles each quantity that is 10 or more.
# Print the original and the new lists.
quantities = [5, 12, 9, 15, 7, 10]

# List comprehension to double quantities that are 10 or more
doubled_quantities = [quantity * 2 if quantity >= 10 else quantity for quantity in quantities]

# Print the original and the new lists
print("Original List:", quantities)
print("New List (Doubled quantities >= 10):", doubled_quantities)




#######################################################################################################################################################

# Question 9 - Dictionary Manipulation
# Using the dictionary below, filter out the products with a rating of less than 4 and create a new dictionary with the remaining products.
ratings = {'product_A': 4, 'product_B': 5, 'product_C': 3, 'product_D': 2, 'product_E': 5}


# Given dictionary of product ratings
ratings = {'product_A': 4, 'product_B': 5, 'product_C': 3, 'product_D': 2, 'product_E': 5}

# Create a new dictionary by filtering out products with a rating of less than 4
filtered_ratings = {product: rating for product, rating in ratings.items() if rating >= 4}

# Print the new dictionary
print("Filtered Products:", filtered_ratings)



#######################################################################################################################################################

# Question 10 - Debugging and Correcting Code
# The following code intends to calculate the average of a list of numbers, but it contains errors:
values = [10, 20, 30, 40, 50]
total = 0
#for i in values:
    #total = total + i
#average = total / len(values)
print("Total")

# Identify and correct the errors in the code.
# Comment on each error and explain your fixes.

values = [10, 20, 30, 40, 50]
total = 0

# Calculate the total of all numbers
for i in values:
    total = total + i  
# Calculate the average
average = total / len(values)  

print("Total:", total) 
print("Average:", average)  

#######################################################################################################################################################
