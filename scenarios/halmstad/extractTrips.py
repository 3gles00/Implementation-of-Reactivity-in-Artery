import xml.etree.ElementTree as ET

def extract_trips_from_flows(xml_file_path, output_file_path):
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    trips = []

    # Iterate through each flow element and generate trips
    for flow in root.findall('flow'):
        flow_id = flow.get('id')
        begin = float(flow.get('begin'))
        end = float(flow.get('end'))
        number = int(flow.get('number'))
        from_edge = flow.get('from')
        to_edge = flow.get('to')
        vtype = flow.get('type')

        # Calculate the interval between trips
        interval = (end - begin) / number if number > 1 else 0

        # Generate trips based on the flow definition
        for i in range(number):
            trip_id = f"{flow_id}_trip_{i}"
            depart = begin + i * interval
            trips.append({
                'id': trip_id,
                'depart': depart,
                'from': from_edge,
                'to': to_edge,
                'type': vtype
            })

    # Create the root element for the trips file
    trips_root = ET.Element('routes')

    # Add each trip to the trips_root element
    for trip in trips:
        trip_element = ET.SubElement(trips_root, 'trip')
        trip_element.set('id', trip['id'])
        trip_element.set('depart', f"{trip['depart']:.2f}")
        trip_element.set('from', trip['from'])
        trip_element.set('to', trip['to'])
        trip_element.set('type', trip['type'])

    # Write the trips to the output file
    tree = ET.ElementTree(trips_root)
    tree.write(output_file_path, encoding='utf-8', xml_declaration=True)

if __name__ == "__main__":
    xml_file_path = '/home/haron/artery/scenarios/halmstad/flow.trips.xml'
    output_file_path = '/home/haron/artery/scenarios/halmstad/extractedtrips.xml'
    extract_trips_from_flows(xml_file_path, output_file_path)
    print(f"Extracted trips saved to {output_file_path}")