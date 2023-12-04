class Human:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    def does_work(self):
        if self.occupation == "athlete":
            print(self.name, "Plays sport")
        elif self.occupation == "actor":
            print(self.name, "Shoots a movie")

    def talks(self):
        user = input("What is your name ?\n")
        print(self.name, " Says hello there - ", user)


tom = Human("tom", "actor")
tom.does_work()
tom.talks()
maria = Human("Maria","athlete")
maria.talks()
maria.does_work()
