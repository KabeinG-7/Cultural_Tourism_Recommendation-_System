import csv

# Open the CSV file
with open(r"C:\Users\kavin\Desktop\MP-Recommendation System\recdata.csv") as csv_file:
    # Read the CSV file into a list of lists
    dataset = []
    for row in csv.reader(csv_file):
        dataset.append(row)

# Define the code scheme
type_codes = ["Religious Sites", "Festivals", "Traditional Arts", "Other"]
subtype_codes = ["Hindu Temples", "Buddhist Temples", "Cultural Festivals", "Jain Festivals", "Religious Festivals", "Handicrafts"]

# Create empty dictionaries to store the coded data
type_counts = {}
subtype_counts = {}

# Iterate over the dataset and code the data
for row in dataset:
    # Get the type and subtype of the destination
    type = row[0]
    subtype = row[1]

    # Increment the counts for the type and subtype
    if type in type_counts:
        type_counts[type] += 1
    else:
        type_counts[type] = 1

    if subtype in subtype_counts:
        subtype_counts[subtype] += 1
    else:
        subtype_counts[subtype] = 1

# Print the results
print("Type counts:")
for type in type_codes:
    count = type_counts.get(type, 0)
    print("{}: {}".format(type, count))

print("\nSubtype counts:")
for subtype in subtype_codes:
    count = subtype_counts.get(subtype, 0)
    print("{}: {}".format(subtype, count))
