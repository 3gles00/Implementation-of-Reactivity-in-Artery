import xml.etree.ElementTree as ET

def update_trips(input_file, output_file):
    # Parse the input XML file
    tree = ET.parse(input_file)
    root = tree.getroot()

    # Extract all trip elements
    trips = root.findall('trip')

    # Update trip IDs and departure times
    for i, trip in enumerate(trips):
        trip.set('id', str(i))
        trip.set('depart', f"{i}.00")

    # Clear the root element and append updated trips
    root.clear()
    for trip in trips:
        root.append(trip)

    # Write the updated trips to the output file
    tree.write(output_file, encoding='utf-8', xml_declaration=True)

if __name__ == "__main__":
    input_file = 'junction.trips.xml'
    output_file = 'updated_junction.trips.xml'
    update_trips(input_file, output_file)
    print(f"Trips updated and saved to {output_file}")