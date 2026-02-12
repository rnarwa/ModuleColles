from planche_handler import PlancheSemaine
from datetime import date

class Rapport:
    def __init__(self):
        self.student = None
        self.commentary = None
        self.exercices = None
        self.exercices_note = []
        self.note = ''
        self.date = None
        self.question_cours = None

    def get_exercises(self, exe_list):
        self.exercices = exe_list

    def set_note(self, exercise, note):
        idx = self.exercices.index(exercise)
        self.exercices_note.insert(idx, note)

    def get_date(self, classe_date):

        td = date.today()
        if classe_date > td: 
            self.date = date.fromisocalendar(classe_date.year, classe_date.isocalendar().week -1, classe_date.isocalendar().weekday)
        else: 
            self.date = classe_date

