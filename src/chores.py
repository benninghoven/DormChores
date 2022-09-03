import json 
from timenow import TimeNow

class Chores:
    def __init__(self):
        with open ("../data/config.json") as f:
            config = json.load(f)
        self.users = config["users"]
        self.groupOne = self.users[:int(len(self.users)/2)]
        self.groupTwo = self.users[int(len(self.users)/2):]
        self.trashcleaner = config["trashcleaner"]
        self.bath1cleaner = config["bath1cleaner"]
        self.bath2cleaner = config["bath2cleaner"]
        print(f"Group one: {self.groupOne}")
        print(f"Group two: {self.groupTwo}")
        print(f"trashcleaner: {self.trashcleaner}")
        print(f"bath1cleaner: {self.bath1cleaner}")
        print(f"bath2cleaner: {self.bath2cleaner}")

    def UpdateChores(self):
        print(f"{TimeNow()} updating users")

    def Test(self):
        print(f"{TimeNow()} Trash Duty: {self.trashcleaner}")
        print(f"{TimeNow()} Bathroom One Duty: {self.bath1cleaner}")
        print(f"{TimeNow()} Bathroom Two Duty: {self.bath2cleaner}")
