import json
import pandas as pd
import numpy as np


class Patient:
    def __init__(self, patient_id, p_name, p_age, p_gender, p_ward):
        self.patient_id = patient_id
        self.p_name = p_name
        self.p_age = p_age
        self.p_gender = p_gender
        self.p_ward = p_ward
        self.days = 0
        self.status = "Admitted"

    def bill(self):
        cost = 2000 if self.p_ward == "General" else 5000
        return self.days * cost

    def to_dict(self):
        return {
            "patient_id": self.patient_id,
            "p_name": self.p_name,
            "p_age": self.p_age,
            "p_gender": self.p_gender,
            "p_ward": self.p_ward,
            "days": self.days,
            "status": self.status
        }


class Hospital:
    def __init__(self):
        self.data = {}
        self.load()

    def save(self):
        d = {i: p.to_dict() for i, p in self.data.items()}
        with open("patients.json", "w") as f:
            json.dump(d, f, indent=4)

    def load(self):
        try:
            with open("patients.json", "r") as f:
                d = json.load(f)
                for i, x in d.items():
                    p = Patient(
                        x["patient_id"],
                        x["p_name"],
                        x["p_age"],
                        x["p_gender"],
                        x["p_ward"]
                    )
                    p.days = x["days"]
                    p.status = x["status"]
                    self.data[i] = p
        except FileNotFoundError:
            print("No previous data found")

    def add(self):
        i = input("Enter ID: ")
        if i in self.data:
            print("Already exists\n")
            return

        n = input("Enter name: ")
        try:
            a = int(input("Enter age: "))
        except ValueError:
            print("Invalid age\n")
            return

        g = input("Enter gender: ")
        w = input("Ward (General/ICU): ")

        if w not in ["General", "ICU"]:
            print("Invalid ward\n")
            return

        self.data[i] = Patient(i, n, a, g, w)
        self.save()
        print("Added\n")

    def view(self):
        if not self.data:
            print("No records\n")
            return
        for p in self.data.values():
            print(p.patient_id, p.p_name, p.p_age, p.p_gender, p.p_ward, p.days, p.status)

    def stay(self):
        i = input("Enter ID: ")
        if i not in self.data:
            print("Not found\n")
            return

        try:
            self.data[i].days = int(input("Enter days: "))
        except ValueError:
            print("Invalid\n")
            return

        print("Bill:", self.data[i].bill())
        self.save()

    def status(self):
        i = input("Enter ID: ")
        if i not in self.data:
            print("Not found\n")
            return

        print("1 Treatment  2 Discharged")
        c = input("Enter: ")

        if c == "1":
            self.data[i].status = "Under Treatment"
        elif c == "2":
            self.data[i].status = "Discharged"
        else:
            print("Wrong\n")
            return

        self.save()
        print("Updated\n")

    def search(self):
        i = input("Enter ID: ")
        p = self.data.get(i)

        if not p:
            print("Not found\n")
            return

        print(p.p_name, p.p_ward, p.days, p.bill(), p.status)

    def delete(self):
        i = input("Enter ID: ")
        if i in self.data:
            del self.data[i]
            self.save()
            print("Deleted\n")
        else:
            print("Not found\n")

    def sort(self):
        for p in sorted(self.data.values(), key=lambda x: x.bill()):
            print(p.patient_id, "-", p.bill())

    def report(self):
        if not self.data:
            print("No data\n")
            return

        d = [[p.patient_id, p.p_name, p.p_ward, p.days, p.bill(), p.status]
             for p in self.data.values()]

        df = pd.DataFrame(d, columns=["ID", "Name", "Ward", "Days", "Bill", "Status"])
        print(df)

        arr = df["Bill"].to_numpy()
        print("Total:", arr.sum())
        print("Avg:", arr.mean())
        print("Max:", arr.max())
        print("Min:", arr.min())

    def filter(self):
        w = input("Enter ward: ").lower()
        found = False
        for p in self.data.values():
            if p.p_ward.lower() == w:
                print(p.patient_id, p.p_name, p.p_ward)
                found = True
        if not found:
            print("No record")


def main():
    h = Hospital()
    while True:
        print("\n1 Add\n2 View\n3 Stay/Bill\n4 Status\n5 Search\n6 Delete\n7 Sort\n8 Report\n9 Filter\n10 Exit")
        c = input("Enter: ")

        if c == "1": h.add()
        elif c == "2": h.view()
        elif c == "3": h.stay()
        elif c == "4": h.status()
        elif c == "5": h.search()
        elif c == "6": h.delete()
        elif c == "7": h.sort()
        elif c == "8": h.report()
        elif c == "9": h.filter()
        elif c == "10": break
        else: print("Wrong choice")


if __name__ == "__main__":
    main()
