import re

def calculate_denms_pdr(file_path):
    total_sent_denms = 0
    total_received_denms = 0
    sum_pdr = 0
    count = 0

    with open(file_path, 'r') as file:
        sent_denms = 0
        received_denms = 0

        for line in file:
            if "DenService transmission:count" in line:
                sent_denms = int(re.search(r'\d+', line).group())
                total_sent_denms += sent_denms
            elif "DenService reception:count" in line:
                received_denms = int(re.search(r'\d+', line).group())
                total_received_denms += received_denms

            if sent_denms != 0 and received_denms != 0:
                sum_pdr += (received_denms / sent_denms)
                count += 1
                sent_denms = 0
                received_denms = 0

    # Calculate average PDR
    average_pdr = sum_pdr / count if count > 0 else 0
    return average_pdr

if __name__ == "__main__":
    file_path = '/home/haron/artery/scenarios/halmstad/results/veins-#25.sca'
    pdr = calculate_denms_pdr(file_path)
    print(f"PDR for DENMs: {pdr:.2f}")