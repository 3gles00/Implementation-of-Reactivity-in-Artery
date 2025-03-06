import xml.etree.ElementTree as ET

def change_flow_vehicle_count(xml_file_path, output_file_path, new_vehicle_count):
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # Iterate through each flow element and update the number attribute
    for flow in root.findall('flow'):
        flow.set('number', str(new_vehicle_count))

    # Write the modified XML to the output file
    tree.write(output_file_path, encoding='utf-8', xml_declaration=True)

if __name__ == "__main__":
    xml_file_path = '/home/haron/artery/scenarios/halmstad/flow.trips.xml'
    output_file_path = '/home/haron/artery/scenarios/halmstad/flow.trips.xml'
    new_vehicle_count = 6  # Set the desired number of vehicles per flow

    change_flow_vehicle_count(xml_file_path, output_file_path, new_vehicle_count)
    print(f"Updated vehicle count in flows and saved to {output_file_path}")