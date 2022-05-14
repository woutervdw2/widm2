"""Hier komen alle classes te staan die we nodig gaan hebben"""
import time

class Spelers:
    def __init__(self, naam : str, mol : bool, in_game):
        self.naam = naam
        self.in_game = in_game
        self.laatste_test = 0
        self.vragen_goed = 0
        self.mol = mol
        self.antwoorden = ""
        self.bool_antwoorden = ""
        
    def __str__(self):
        if self.in_game  == True:
            return "%s is nog in het spel" % (self.name)
        else:
            return "%s is uit het spel" % (self.name)
    
    def add_antwoord(self, antwoord):
        self.antwoorden += "}" + antwoord
    def vraag_goed(self):
        self.vragen_goed += 1
    def add_bool_antwoord(self, bool_antwoord):
        self.bool_antwoorden += "}" + str(bool_antwoord)
    def tussen_tijd_berekenen(self):
        self.tussen_tijd = time.time() - self.test_tijd_begin
        return self.tussen_tijd
    def begin_quiz(self):
        self.test_tijd_begin = time.time()
        
    def eind_quiz(self):
        self.test_tijd_eind = time.time()
        
    def total_tijd(self):
        self.test_tijd = self.test_tijd_eind - self.test_tijd_begin
        self.laatste_test += 1

    def nieuwe_ronde(self):
        self.vragen_goed = 0

    #def einde_quiz(self):
        
        
class Buttons():

    def __init__(self, text, correct):
        self.text = text
        self.correct = correct
    
    def __str__(self):
        return self.text

class Quiz():

    def __init__(self, deelnemers_lijst, quiz_file):
        self.deelnemers_lijst = deelnemers_lijst
        self.quiz_file = quiz_file