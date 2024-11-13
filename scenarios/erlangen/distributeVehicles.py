import xml.etree.ElementTree as ET

def distribute_vehicle_types(input_file, output_file, vehicle_types):
    # Parse the input XML file
    tree = ET.parse(input_file)
    root = tree.getroot()

    # Extract all trip elements
    trips = root.findall('trip')

    # Distribute vehicle types equally
    for i, trip in enumerate(trips):
        trip.set('type', vehicle_types[i % len(vehicle_types)])

    # Write the updated trips to the output file
    tree.write(output_file, encoding='utf-8', xml_declaration=True)

if __name__ == "__main__":
    input_file = 'erlangen.trips.xml'
    output_file = 'distributed_junction.trips.xml'
    vehicle_types = ['krauss_0.5', 'krauss_0.75', 'cacc']
    distribute_vehicle_types(input_file, output_file, vehicle_types)
    print(f"Trips updated and saved to {output_file}")