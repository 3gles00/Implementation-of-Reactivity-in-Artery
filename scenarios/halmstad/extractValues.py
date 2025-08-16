import xml.etree.ElementTree as ET
import csv

# File paths
input_file = "/home/haron/artery/scenarios/halmstad/results/v100/value3.xml"
output_file = "/home/haron/artery/scenarios/halmstad/results/v100/value3.csv"

# Parse the XML file
tree = ET.parse(input_file)
root = tree.getroot()

# Open CSV file for writing
with open(output_file, mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    # Write the header
    writer.writerow(["id", "speed_kmh", "timeloss", "routelength", "duration"])

    # Iterate through each tripinfo element
    for tripinfo in root.findall("tripinfo"):
        trip_id = tripinfo.get("id")
        timeloss = tripinfo.get("timeLoss", "0")
        routelength = tripinfo.get("routeLength", "0")
        duration = tripinfo.get("duration", "0")
        speed_mps = float(routelength/duration)
        speed_kmh = speed_mps * 3.6  # Convert m/s to km/h

        # Write the row to the CSV
        writer.writerow([trip_id, round(speed_kmh, 2), timeloss, routelength, duration])

print(f"Data extracted and saved to {output_file}")