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

print(total_salary)
print(len(total_salary))
print(calculate_total_revenue(len(total_salary)))
