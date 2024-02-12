class Logic:  # class that contains the logic of the program
    def __init__(self, grade1, grade2, grade3, absent):
        self.grade1 = float(grade1)
        self.grade2 = float(grade2)
        self.grade3 = float(grade3)

        self.absent = float(absent)

        self.total_of_lectures = 60

    def calculate_absence(self):  # calculate the percentage of absence
        return (self.absent / self.total_of_lectures) * 100

    def average_grade(self):  # calculate the average grade
        return (self.grade1 + self.grade2 + self.grade3) / 3

    def naf(self):  # calculate the grade that the student needs to get in the final exam
        return int(100 - self.average_grade())

    def approval(self):  # check if the student is approved or not
        average_grade = self.average_grade()
        percentage_absence = self.calculate_absence()

        if average_grade >= 70 and percentage_absence <= 25:  # if the student is approved
            return ["Aprovado", "0"]
        elif average_grade >= 50 and percentage_absence <= 25:  # if the student needs to do the final exam
            return ["Exame Final", f"{self.naf()}"]
        elif average_grade < 50:  # if the student is not approved because of the grade
            return ["Reprovado por Nota", "0"]
        elif percentage_absence > 25:  # if the student is not approved because of the absence
            return ["Reprovado por Falta", "0"]
