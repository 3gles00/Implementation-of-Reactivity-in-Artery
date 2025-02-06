import csv

def calculate_averages(csv_file_path):
    total_speed = 0.0
    total_waiting_time = 0.0
    total_speed_factor = 0.0
    count = 0

    with open(csv_file_path, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the header row

        for row in csv_reader:
            average_speed = float(row[1])
            waiting_time = float(row[2])
            speed_factor = float(row[3])

            total_speed += average_speed
            total_waiting_time += waiting_time
            total_speed_factor += speed_factor
            count += 1

    average_speed = total_speed / count if count > 0 else 0
    average_waiting_time = total_waiting_time / count if count > 0 else 0
    average_speed_factor = total_speed_factor / count if count > 0 else 0

    return average_speed, average_waiting_time, average_speed_factor, count

if __name__ == "__main__":
    csv_file_path = '/home/haron/artery/scenarios/halmstad/extraxted0.csv'
    avg_speed, avg_waiting_time, avg_speed_factor, num_ids = calculate_averages(csv_file_path)
    print(f"Average Speed: {avg_speed:.2f} km/h")
    print(f"Average Waiting Time: {avg_waiting_time:.2f} s")
    print(f"Average Speed Factor: {avg_speed_factor:.2f}")
    print(f"Number of IDs: {num_ids}")