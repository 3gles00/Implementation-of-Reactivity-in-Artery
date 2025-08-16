import xml.etree.ElementTree as ET
import csv
import os

# File paths
input_file = "/home/haron/artery/scenarios/halmstad/results/v100/statistics3.xml"
output_file = "/home/haron/artery/scenarios/halmstad/statistics.csv"

# Parse the XML file
tree = ET.parse(input_file)
root = tree.getroot()

# Check if the CSV file already exists
file_exists = os.path.isfile(output_file)

# Open CSV file for appending
with open(output_file, mode='a', newline='') as csv_file:
    writer = csv.writer(csv_file)
    
    # Write the header only if the file is being created
    if not file_exists:
        writer.writerow(["speed", "timeLoss", "routeLength", "duration"])

    # Find the <vehicleTripStatistics> element
    vehicle_stats = root.find("vehicleTripStatistics")
    if vehicle_stats is not None:
        # Extract the required attributes
        speed = vehicle_stats.get("speed", "0")
        time_loss = vehicle_stats.get("timeLoss", "0")
        route_length = vehicle_stats.get("routeLength", "0")
        duration = vehicle_stats.get("duration", "0")

        # Append the data to the CSV
        writer.writerow([speed, time_loss, route_length, duration])

print(f"Data extracted and appended to {output_file}")