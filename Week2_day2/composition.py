class Id_card:
    def __init__(self, id_no, blood_group):
        self.id_no = id_no
        self.blood_group = blood_group

    def display(self):
        print("id_no is:", self.id_no)
        print("blood_group is:", self.blood_group)


class Staff:
    def __init__(self, job_designation, Id_card):
        self.job_designation = job_designation
        self.id_card = Id_card

    def display_name(self):
        print(object_i.display())
        print("job_designation is:", self.job_designation)


object_i = Id_card(23, 'o-ve')
s = Staff('web_developer', object_i)
s.display_name()
