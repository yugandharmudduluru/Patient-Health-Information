import sqlite3

conn = sqlite3.connect("hospital.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS patient (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    disease TEXT NOT NULL,
    doctor TEXT NOT NULL,
    treatment TEXT
)
""")
conn.commit()

class Patient:

   def add_patient(self):
        patient_id = int(input("Enter Patient ID: "))
        name = input("Enter Patient Name: ")
        age = int(input("Enter Age: "))
        disease = input("Enter Disease: ")
        doctor = input("Enter Doctor Assigned: ")
        Treatement=input("Enter Treatment Name:")

        try:
            cursor.execute("""
            INSERT INTO patient (id, name, age, disease, doctor, treatment) 
            VALUES (?, ?, ?, ?, ?, ?)""",
            (patient_id, name, age, disease, doctor, Treatement))
            conn.commit()
            print(" Patient added successfully!\n")
        except sqlite3.IntegrityError:
            print(" Patient ID already exists.\n")

    def view_all_patients(self):
        cursor.execute("SELECT * FROM patient")
        rows = cursor.fetchall()
        if not rows:
            print(" No patient records found.\n")
            return

        print("\n Patient Records:")
        print("ID\tName\tAge\tDisease\tDoctor\tTreatment")
        print("-" * 60)

        for row in rows:
            print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5] if row[5] else 'N/A'}")
        print()

    def search_patient(self):
        patient_id = int(input("Enter Patient ID to Search: "))
        cursor.execute("SELECT * FROM patient WHERE id=?", (patient_id,))
        row = cursor.fetchone()
        if row:
            print("\nID\tName\tAge\tDisease\tDoctor\tTreatment")
            print("-" * 60)
            print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5] if row[5] else 'N/A'}\n")
        else:
            print(" Patient not found.\n")

    def update_treatment(self):
        patient_id = int(input("Enter Patient ID to Update: "))
        treatment = input("Enter New Treatment/Diagnosis: ")
        cursor.execute("UPDATE patient SET treatment=? WHERE id=?", (treatment, patient_id))
        conn.commit()
        if cursor.rowcount:
            print(" Treatment updated successfully.\n")
        else:
            print(" Patient not found.\n")

    def delete_patient(self):
        patient_id = int(input("Enter Patient ID to Delete: "))
        cursor.execute("DELETE FROM patient WHERE id=?", (patient_id,))
        conn.commit()
        if cursor.rowcount:
            print(" Patient deleted successfully.\n")
        else:
            print(" Patient not found.\n")

    def count_by_disease(self):
        cursor.execute("SELECT disease, COUNT(*) FROM patient GROUP BY disease")
        rows = cursor.fetchall()
        print("\n Patient Count by Disease:")
        for row in rows:
            print(f"{row[0]}: {row[1]} patients")
        print()

    def count_by_doctor(self):
        cursor.execute("SELECT doctor, COUNT(*) FROM patient GROUP BY doctor")
        rows = cursor.fetchall()
        print(f"\n Patient Count by Doctor: if ")
        for row in rows:
            print(f"{row[0]}: {row[1]} patients")
        print()


p = Patient()

while True:
    print("=====  Hospital Patient Management System =====")
    print("1. Add Patient")
    print("2. View All Patients")
    print("3. Search Patient by ID")
    print("4. Update Treatment/Diagnosis")
    print("5. Delete Patient Record")
    print("6. Show Patient Count by Disease")
    print("7. Show Patient Count by Doctor")
    print("8. Exit")

    choice = input("Enter choice (1-8): ")

    if choice == "1":
        p.add_patient()
    elif choice == "2":
        p.view_all_patients()
    elif choice == "3":
        p.search_patient()
    elif choice == "4":
        p.update_treatment()
    elif choice == "5":
        p.delete_patient()
    elif choice == "6":
        p.count_by_disease()
    elif choice == "7":
        p.count_by_doctor()
    elif choice == "8":
        print(" Exiting... Goodbye!")
        break
    else:
        print(" Invalid choice, please try again.\n")


conn.close()


