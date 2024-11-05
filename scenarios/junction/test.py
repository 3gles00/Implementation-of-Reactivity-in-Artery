import xml.etree.ElementTree as ET

def update_trips(input_file, output_file, interval=3, max_time=1000):
    # Parse the input XML file
    tree = ET.parse(input_file)
    root = tree.getroot()

    # Extract all trip elements
    trips = root.findall('trip')

    # Update departure times and limit the number of trips
    updated_trips = []
    for i, trip in enumerate(trips):
        depart_time = i * interval
        if depart_time >= max_time:
            break
        trip.set('id', str(i))
        trip.set('depart', f"{depart_time}.00")
        updated_trips.append(trip)

    # Clear the root element and append updated trips
    root.clear()
    for trip in updated_trips:
        root.append(trip)

    # Write the updated trips to the output file
    tree.write(output_file, encoding='utf-8', xml_declaration=True)

if __name__ == "__main__":
    input_file = 'junction.trips.xml'
    output_file = 'updated_junction.trips.xml'
    update_trips(input_file, output_file)
    print(f"Trips updated and saved to {output_file}")