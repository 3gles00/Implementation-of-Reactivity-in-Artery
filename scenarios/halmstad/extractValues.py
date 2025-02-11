import xml.etree.ElementTree as ET
import csv

def extract_tripinfo_to_csv(xml_file_path, csv_file_path):
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # Open the CSV file for writing
    with open(csv_file_path, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        # Write the header row
        csv_writer.writerow(['ID', 'Average Speed (km/h)', 'Waiting Time', 'Speed Factor'])

        # Iterate through each tripinfo element and extract the required data
        for tripinfo in root.findall('tripinfo'):
            trip_id = tripinfo.get('id')
            duration = float(tripinfo.get('duration'))
            route_length = float(tripinfo.get('routeLength'))
            average_speed_m_s = route_length / duration if duration > 0 else 0
            average_speed_km_h = average_speed_m_s * 3.6  # Convert m/s to km/h
            waiting_time = float(tripinfo.get('waitingTime'))
            speed_factor = float(tripinfo.get('speedFactor'))

            # Write the extracted data to the CSV file
            csv_writer.writerow([trip_id, average_speed_km_h, waiting_time, speed_factor])

if __name__ == "__main__":
    xml_file_path = '/home/haron/artery/scenarios/halmstad/value.xml'
    csv_file_path = '/home/haron/artery/scenarios/halmstad/extracted0.csv'
    extract_tripinfo_to_csv(xml_file_path, csv_file_path)
    print(f"Extracted tripinfo data to {csv_file_path}")