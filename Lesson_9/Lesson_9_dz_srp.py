
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def update_name(self, update_name):
        self.name = update_name

    def update_email(self, update_email):
        self.email =update_email

    def update_user(self, update_name, update_email):
        self.name = update_name
        self.email = update_email

    def __repr__(self):
        return f"name = {self.name}, email = {self.email}"


class ManagerUser:
    def __init__(self):
        self.list_of_users = []


    def create_user(self, name, email):
        user = User(name, email)
        self.list_of_users.append(user)
        return user


    def delete_user(self, user):
        if user in self.list_of_users:
            self.list_of_users.remove(user)
        else:
            print(f"User {user} not found.")

        print(f"User: {user} is delete\n")

    def __str__(self):
        result = "Users:\n"
        count = 1
        for user in self.list_of_users:
            result += f"{count}. {user}\n"
            count += 1
        return result


manageruser = ManagerUser()
user_1 = manageruser.create_user("Olya", "Olya@gmail.com")
user_2 = manageruser.create_user("Katya", "Katya@gmail.com")
print(manageruser)

user_1.update_name("Sonya")
user_1.update_email("Sonya@gmail.com")
user_2.update_user("Viktor", "Victor@gmail.com")
print(manageruser)

user_3 = manageruser.create_user("Olya", "Olya@gmail.com")
print(manageruser)

manageruser.delete_user(user_3)
print(manageruser)





