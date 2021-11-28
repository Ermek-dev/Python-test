num = 18
name = "John Smith"
patient = True
while patient:
    age_man = int(input('Enter the age: '))
    if age_man == num:
        print("Sush a patient exists his name is",'-', name)
        patient = False
    elif age_man>num:
        print("Such a patient has'nt been admitted")
    else:
        print("Patient in another department")
