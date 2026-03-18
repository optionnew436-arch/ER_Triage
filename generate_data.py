import csv
import random
from datetime import datetime, timedelta

def generate_dataset(filename="patients.csv", num_patients=1000):
    start_time = datetime(2025, 3, 18, 0, 0, 0)

    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["patient_id", "priority", "arrival_time"])

        for i in range(1, num_patients + 1):
            patient_id = f"P{str(i).zfill(4)}"
            priority = random.randint(1, 10)
            random_second = random.randint(0, 24*3600 - 1)
            arrival = start_time + timedelta(seconds=random_second)
            writer.writerow([patient_id, priority, arrival.strftime("%Y-%m-%d %H:%M:%S")])

    print(f"✅ Generated {num_patients} patients and saved to {filename}")

if __name__ == "__main__":
    generate_dataset(r"C:\Users\Hp\Desktop\patients.csv")