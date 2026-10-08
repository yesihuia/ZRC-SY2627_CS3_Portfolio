# Activity 1 Answers
# 1. GameCharacter.username -> public
# 2. BankAccount.__balance -> private
# 3. Vehicle._engineCode -> protected
# 4. Student.schoolName -> public
# 5. VotingSystem.__voterID -> private

class GameCharacter:
    def __init__(self, username):
        self.username = username


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance


class Vehicle:
    def __init__(self, engineCode):
        self._engineCode = engineCode


class Student:
    def __init__(self, schoolName):
        self.schoolName = schoolName


class VotingSystem:
    def __init__(self, voterID):
        self.__voterID = voterID