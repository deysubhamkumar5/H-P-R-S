# module2_admission.py

patients = {}
wards = {
    "General": [],
    "ICU": []
}

def add_patient(pid, name):
    patients[pid] = {"name": name, "admitted": False}


def admit_patient(pid, ward):
    if pid not in patients:
        print("Patient not found")
        return

    if patients[pid]["admitted"]:
        print("Already admitted")
        return

    wards[ward].append(pid)
    patients[pid]["admitted"] = True
    print("Patient admitted")


def discharge_patient(pid):
    for ward in wards:
        if pid in wards[ward]:
            wards[ward].remove(pid)
            patients[pid]["admitted"] = False
            print("Patient discharged")
            return

    print("Patient not found in wards")


def show_wards():
    print("Ward Status:")
    for w, p in wards.items():
        print(w, ":", p)


# Demo Run
add_patient("101", "Rahul")
admit_patient("101", "General")
show_wards()
discharge_patient("101")
show_wards()