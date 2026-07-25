import pandas as pd
from ucimlrepo import fetch_ucirepo 

online_retail = fetch_ucirepo(id=352) 
df = online_retail.data.features # get the data


total_salary = df['UnitPrice'] * df['Quantity'] #multiply the unit price by the quantity to get the total salary for each row

def calculate_total_revenue(number_of_rows): #calculate the total revenue by summing up the total salary for each row
    count_number = 0 #set a counter to keep track of the number of rows we have iterated through
    total_revenue = 0 #initialize the total revenue to 0
    while count_number < number_of_rows: #by using a while loop, we can iterate through each row and add the total salary to the total revenue
        

        total_revenue = total_revenue + total_salary[count_number] #add the total salary for the current row to the total revenue

        count_number += 1 #increment the counter by 1 to move to the next row

    return total_revenue

def find_the_most_expensive_item(): #find the most expensive item in the dataset
    max_price = df['UnitPrice'].max() #get the maximum unit price from the dataset
    most_expensive_item = df[df['UnitPrice'] == max_price] #filter the dataframe to get the row with the maximum unit price

    return most_expensive_item

def the_most_expensive_item(): #find the most expensive item in the dataset
    max_price = df['UnitPrice'].max() #get the maximum unit price from the dataset
    most_expensive_item = df[df['UnitPrice'] == max_price] #filter the dataframe to get the row with the maximum unit price

    if not most_expensive_item.empty: #check if the dataframe is not empty
        most_expensive_item = most_expensive_item.iloc[0] #get the first row of the dataframe
        
    else:
        most_expensive_item = None #if the dataframe is empty, set the most expensive item to None
    return most_expensive_item

def the_most_shipped_country(): #find the country with the most shipped items
    most_shipped_country = df['Country'].value_counts().idxmax() #get the country with the most shipped items

    return most_shipped_country



print(calculate_total_revenue(len(total_salary))) #print the total revenue for the dataset
print(find_the_most_expensive_item()) #print the most expensive item in the dataset
print(the_most_expensive_item()) #print the most expensive item in the dataset
print(the_most_shipped_country()) #print the country with the most shipped items
