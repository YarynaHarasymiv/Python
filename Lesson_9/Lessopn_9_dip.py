from enum import Enum
from abc import ABC, abstractmethod


class Teams(Enum):
    BLUE_TEAM = 1
    RED_TEAM = 2
    GREEN_TEAM = 3

class Students(Enum):
    OLEG = 1
    DIMA = 2
    SERGEY = 3


class TeamMembershipLookUp():
    @abstractmethod
    def find_all_students(self, team):
        pass

class StudentMembershipLookUp(ABC):
    @abstractmethod
    def find_all_teams(self, student):
        pass



class Student:
    def __init__(self, name):
        self.name = name

class Team:
    def __init__(self, name_team):
        self.name_team = name_team




class TeamMemberShips(TeamMembershipLookUp):
    def __init__(self):
        self.team_memberships = []

    def add_team_memberships(self, student, team):
        self.team_memberships.append((student, team))

    def find_all_students(self, team):
        for members in self.team_memberships:
            if members[1] == team:
                yield  members[0].name

        student_names = []
        for member in self.team_memberships:
            if member[1] == team:
                student_names.append(member[0].name)
        return student_names

class StudentMemberShips(StudentMembershipLookUp):
    def __init__(self):
        self.student_memberships = []

    def add_student_memberships(self, student, team):
        self.student_memberships.append((student, team))

    def find_all_teams(self, student):
        for teams in self.student_memberships:
            if teams[0] == student:
                yield teams[1].name_team



class Analysis_1():
    def __init__(self, team_member_ship_lookup):
        for student in team_member_ship_lookup.find_all_students(Teams.RED_TEAM):
            print(f"{student} is in Red team")

class Analysis_2:
    def __init__(self, student_member_ship_lookup):
        for team in student_member_ship_lookup.find_all_teams(Students.OLEG):
            print(f"Oleg is in a {team} ")



student_1 = Student("Oleg")
student_2 = Student("Dima")
student_3 = Student("Sergey")

team_memberships = TeamMemberShips()
team_memberships.add_team_memberships(student_1, Teams.RED_TEAM)
team_memberships.add_team_memberships(student_2, Teams.BLUE_TEAM)
team_memberships.add_team_memberships(student_3, Teams.GREEN_TEAM)


team_1 = Team("BLUE_TEAM")
team_2 = Team("RED_TEAM")
team_3 = Team("GREEN_TEAM")

student_membership = StudentMemberShips()
student_membership.add_student_memberships(Students.DIMA, team_1)
student_membership.add_student_memberships(Students.OLEG, team_2)
student_membership.add_student_memberships(Students.SERGEY, team_3)

Analysis_1(team_memberships)
print("-----")
Analysis_2(student_membership)