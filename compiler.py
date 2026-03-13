import csv
import os

# -----------------------------------------------
# Research Data Compiler
# Built by Keshav Suresh
# Filters and exports rows from a CSV by topic
# -----------------------------------------------

print("Research Data Compiler")
print("----------------------")

# Keep asking for a filename until a valid one is entered
filename = input("Enter the name of your CSV file: ")

while not os.path.exists(filename):
    print("Error: File '" + filename + "' not found. Try again.")
    filename = input("Enter the name of your CSV file: ")

search = input("Filter by topic (or press Enter to show all): ")

# Open and read the CSV file
file = open(filename, "r")
reader = csv.DictReader(file)

results = []

# Loop through every row and filter by topic
for row in reader:
    if search == "" or search.lower() in row["topic"].lower():
        results.append(row)

file.close()

# Check if any results were found before asking for output
if len(results) == 0:
    print("No rows matched your filter. Nothing was exported.")
else:
    output = input("Enter output filename (e.g. results.csv): ")

    # Write filtered results to a new CSV file
    outfile = open(output, "w", newline="")
    writer = csv.DictWriter(outfile, fieldnames=["title", "author", "year", "topic"])
    writer.writeheader()
    writer.writerows(results)
    outfile.close()

    # Summary
    print("----------------------")
    print("Filter applied: " + (search if search != "" else "none"))
    print("Rows saved: " + str(len(results)))
    print("Output file: " + output)
    print("Done.")