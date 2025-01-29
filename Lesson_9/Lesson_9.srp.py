


class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def  add_entry(self, text):
        self.count += 1
        self.text = text
        self.entries.append(f"{self.count}: {text}")


    def remove_entry(self, pos):
        del self.entries[pos]
        print(f"We are remove : {self.count}: {self.text}")

    def __str__(self):
        return "\n".join(self.entries)



class SaveFiles:

    @staticmethod
    def save_to_file(journal, filename):
        with open(file=filename, mode="w") as file:
            file.write(journal)


class LoadFromWeb:

    @staticmethod
    def load(journal, filename):
        pass



j = Journal()
j.add_entry("I ate today")
j.add_entry("I slept yesterday")

print(f"Count of entries:\n{j}")

j.remove_entry(0)
print(f"Count of entries \n{j}")


