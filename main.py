from classes.hospital import Hospital
from classes.patient import Patient

new_hospital = Hospital("KN Hospital", 50)

patient1 = Patient("John Doe",["diabetes","fever"])
patient2 = Patient("Jane Doe",["broken leg"])
patient1.display_patient()
new_hospital.addPatient(patient1)
new_hospital.addPatient(patient2)

new_hospital.display_hospital();
new_hospital.admitPatient(patient1)

print("\n\n")
new_hospital.display_hospital();

