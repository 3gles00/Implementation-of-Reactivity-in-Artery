import xml.etree.ElementTree as ET

def set_fixed_interval_departure_times(file_path, interval):
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Initialize the base departure time
    base_depart_time = None

    # Iterate through each trip element and set the departure time
    for trip in root.findall('trip'):
        if base_depart_time is None:
            # Set the base departure time to the first trip's departure time
            base_depart_time = float(trip.get('depart'))
        else:
            # Increment the base departure time by the interval
            base_depart_time += interval

        # Set the new departure time for the trip
        trip.set('depart', f"{base_depart_time:.2f}")

    # Write the modified XML back to the file
    tree.write(file_path, encoding='utf-8', xml_declaration=True)

if __name__ == "__main__":
    file_path = '/home/haron/artery/scenarios/halmstad/halmstad.trips.xml'
    interval = 1.0  # Set 2 seconds between each departure
    set_fixed_interval_departure_times(file_path, interval)
    print(f"Set 2 seconds between each departure in {file_path}")