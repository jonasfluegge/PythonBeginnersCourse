def get_student_data():
    name = input("Name?")
    nachname = input("Nachname?")
    studenten_id = input("Studenten-ID?")
    return name, nachname, studenten_id


print(get_student_data())
