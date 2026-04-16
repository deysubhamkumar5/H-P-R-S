# module3_storage.py
import csv

class Patient:
    def __init__(self, pid, name):
        self.pid = pid
        self.name = name

    def save(self):
        with open("patients.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([self.pid, self.name])


def load_patients():
    try:
        with open("patients.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                print("ID:", row[0], "Name:", row[1])
    except:
        print("File not found")


def main():
    while True:
        print("\n1. Add Patient\n2. View Records\n3. Exit")
        ch = input("Choice: ")

        if ch == "1":
            pid = input("ID: ")
            name = input("Name: ")
            p = Patient(pid, name)
            p.save()
            print("Saved")

        elif ch == "2":
            load_patients()

        elif ch == "3":
            break


if __name__ == "__main__":
    main()