from enum import Enum
from abc import  abstractmethod


class Teams(Enum):
    BLUE_TEAM = 1
    RED_TEAM = 2
    GREEN_TEAM = 3


class TeamMembershipLookUp():
    @abstractmethod
    def find_all_students(self, team):
        pass

class Student:
    def __init__(self, name):
        self.name = name

class TeamMemberShips:
    def __init__(self):
        self.team_memberships = []

    def add_team_memberships(self, student, team):
        self.team_memberships.append((student, team))

    def find_all_students(self, team):
        for members in self.team_memberships:
            if members[1] == team:
                yield  members[0].name

        # student_names = []
        # for member in self.team_memberships:
        #     if member[1] == team:
        #         student_names.append(member[0].name)
        # return student_names


class Analysis:
    def __init__(self, team_member_ship_lookup):
        for student in team_member_ship_lookup.find_all_students(Teams.RED_TEAM):
            print(f"{student} is in Red team")



student_1 = Student("Oleg")
student_2 = Student("Dima")
student_3 = Student("Sergey")

team_memberships = TeamMemberShips()
team_memberships.add_team_memberships(student_1, Teams.RED_TEAM)
team_memberships.add_team_memberships(student_2, Teams.RED_TEAM)
team_memberships.add_team_memberships(student_3, Teams.RED_TEAM)

Analysis(team_memberships)