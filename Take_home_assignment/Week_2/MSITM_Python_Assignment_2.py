# Write a function that reads and sort the incoming CSV file and outputs the result into another CSV files.
import csv

# Creating a dataset
data = [
    {'ID': 1, 'Name': 'Rajesh', 'Age': 40},
    {'ID': 17, 'Name': 'Suresh', 'Age': 30},
    {'ID': 29, 'Name': 'Chandu', 'Age': 22},
    {'ID': 51, 'Name': 'Rajat', 'Age': 27},
    {'ID': 41, 'Name': 'Rajeev', 'Age': 19},
    {'ID': 39, 'Name': 'Nikhil', 'Age': 34},
    {'ID': 21, 'Name': 'Nithin', 'Age': 38},
    {'ID': 48, 'Name': 'Vivek', 'Age': 75},
    {'ID': 68, 'Name': 'Rahul', 'Age': 49},
    {'ID': 28, 'Name': 'Mohan', 'Age': 37}
]

# Writing Data to input.csv
file = open('input.csv', 'w', newline='')
writer = csv.DictWriter(file, fieldnames=['ID', 'Name', 'Age'])
writer.writeheader()
writer.writerows(data)
file.close()

# Reading Data from input.csv
file = open('input.csv', 'r')
reader = csv.DictReader(file)
data_list = list(reader)
file.close()

# Bubble Sort Function
def bubble_sort(data, key):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if int(data[j][key]) > int(data[j+1][key]):
                data[j], data[j+1] = data[j+1], data[j]

# Sorting the data by ID using Bubble sort function
bubble_sort(data_list, 'ID')

# Writing sorted data to output.csv
file = open('output.csv', 'w', newline='')
writer = csv.DictWriter(file, fieldnames=['ID', 'Name', 'Age'])
writer.writeheader()
writer.writerows(data_list)
file.close()
