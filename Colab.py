import csv

# Open the CSV file
with open(r"C:\Users\kavin\Downloads\self made 1.csv") as csv_file:
    # Read the CSV file into a list of lists
    dataset = []
    for row in csv.reader(csv_file):
        dataset.append(row)

# Get the user's preferred word
desired_word = input("Enter a word that is in the type or subtype: ")

# Get the user's desired approximate rating
desired_rating = float(input("Enter your desired approximate rating: "))

# Filter the dataset to only include destinations that contain the desired word in the type or subtype and have a rating close to the desired rating
filtered_dataset = [row for row in dataset if (desired_word in row[0] or desired_word in row[1]) and abs(float(row[3]) - desired_rating) <= 0.5]

# Sort the filtered dataset by rating in descending order
filtered_dataset.sort(key=lambda row: float(row[3]), reverse=True)

# Recommend the top 5 destinations to the user
print("Here are my top 5 recommendations for cultural tourism destinations that contain the word {} in the type or subtype and have a rating close to {} with cultural type, subtype, place, rating & visitor's frequency :".format(desired_word, desired_rating))
for i in range(5):
    print("{}, {}, {}, {}, {}".format(filtered_dataset[i][0], filtered_dataset[i][1], filtered_dataset[i][2], filtered_dataset[i][3], filtered_dataset[i][4]))
