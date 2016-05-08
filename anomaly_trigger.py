import csv, sys

def parse():
    with open('sine_out.csv', 'rb') as f:
        reader = csv.reader(f)

        #Skip to Anomaly Data
        reader.next()
        reader.next()
        reader.next()

        # Anomaly Data
        for row in reader:
            anomaly_score = float(row[3])
            if anomaly_score >= 0.5:
                print "Significant Anomaly: " + str(anomaly_score)

    f.close()

if __name__ == "__main__":
    parse()
