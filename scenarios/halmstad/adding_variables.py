import xml.etree.ElementTree as ET

def update_flows(xml_file_path, output_file_path, new_vehicle_count, new_vehicle_type):
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # Iterate through each flow element and update the number and type attributes
    for flow in root.findall('flow'):
        flow.set('number', str(new_vehicle_count))
        flow.set('type', new_vehicle_type)

    # Write the modified XML to the output file
    tree.write(output_file_path, encoding='utf-8', xml_declaration=True)

if __name__ == "__main__":
    xml_file_path = '/home/haron/artery/scenarios/halmstad/flow.trips.xml'
    output_file_path = '/home/haron/artery/scenarios/halmstad/flow_updated.trips.xml'
    new_vehicle_count = 20  # Set the desired number of vehicles per flow
    new_vehicle_type = 'krauss'  # Set the desired vehicle type

    update_flows(xml_file_path, output_file_path, new_vehicle_count, new_vehicle_type)
    print(f"Updated flows saved to {output_file_path}")