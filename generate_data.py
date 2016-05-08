# Imports for Comma Separated Values and Math!
import csv
import math

# Define the number of rows in the CSV
ROWS = 6000

# Main Function
def run():
    fileHandle = open("sine.csv", "w")
    writer = csv.writer(fileHandle)
    writer.writerow(["angle", "sine"])
    writer.writerow(["float", "float"])
    writer.writerow(["", ""])

    for i in range(ROWS):
        angle = (i * math.pi) / 50
        sine_value = math.sin(angle)
        writer.writerow([angle, sine_value])

    fileHandle.close()

if __name__ == "__main__":
    run()
