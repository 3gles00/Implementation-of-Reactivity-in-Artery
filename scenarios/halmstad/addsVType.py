import xml.etree.ElementTree as ET

def add_vtype_to_trips(trips_file, vtype_id, output_file):
    # Parse the trips file
    tree = ET.parse(trips_file)
    root = tree.getroot()

    # Iterate over each trip and add the vType attribute
    for trip in root.findall('trip'):
        trip.set('type', vtype_id)

    # Write the modified XML to the output file
    tree.write(output_file, encoding='utf-8', xml_declaration=True)

if __name__ == "__main__":
    trips_file = '/home/haron/artery/scenarios/halmstad/OneTripPerSec.trips.xml'
    vtype_id = 'krauss'
    output_file = '/home/haron/artery/scenarios/halmstad/krauss.trips.xml'

    add_vtype_to_trips(trips_file, vtype_id, output_file)
    print(f'Added vType "{vtype_id}" to all trips in {trips_file} and saved to {output_file}')