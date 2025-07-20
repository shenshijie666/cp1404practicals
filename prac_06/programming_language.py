class ProgrammingLanguage:
    all_objects = []
    def __init__(self, name, Typing, Reflection, Year):
        self.name = name
        self.Typing = Typing
        self.Reflection = Reflection
        self.Year = Year
        ProgrammingLanguage.all_objects.append(self)


    def __str__(self):
        return f'{self.name}, {self.Typing} Typing, Reflection = {self.Reflection}, First appeared in {self.Year}\n'

    def is_dynamic(self):
        if self.Typing == "Dynamic":return True
        else:return False



