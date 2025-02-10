import xml.etree.ElementTree as ET

def remove_departures_over_700(xml_file_path, output_file_path):
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # Iterate through all person elements and remove those with depart > 700
    for persons in root.findall('persons1') + root.findall('persons2') + root.findall('persons3'):
        for person in list(persons):
            depart_time = float(person.get('depart'))
            if depart_time > 700:
                persons.remove(person)

    # Write the modified XML to the output file
    tree.write(output_file_path, encoding='utf-8', xml_declaration=True)

if __name__ == "__main__":
    xml_file_path = '/home/haron/artery/scenarios/halmstad/pedestrian.rou.xml'
    output_file_path = '/home/haron/artery/scenarios/halmstad/pedestrian_filtered.rou.xml'
    remove_departures_over_700(xml_file_path, output_file_path)
    print(f"Filtered XML saved to {output_file_path}")