# module1_basic.py

patients = {}
wards = {
    "General": [],
    "ICU": []
}

def add_patient():
    pid = input("Enter Patient ID: ")
    if pid in patients:
        print("Patient already exists")
        return

    name = input("Enter Name: ")
    age = input("Enter Age: ")
    gender = input("Enter Gender: ")

    patients[pid] = {
        "name": name,
        "age": age,
        "gender": gender
    }

    print("Patient added successfully")


def show_patients():
    if not patients:
        print("No patients found")
        return

    for pid, data in patients.items():
        print(pid, data)


def main():
    while True:
        print("\n1. Add Patient\n2. Show Patients\n3. Exit")
        ch = input("Choice: ")

        if ch == "1":
            add_patient()
        elif ch == "2":
            show_patients()
        elif ch == "3":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()