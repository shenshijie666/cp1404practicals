from programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)
print("The dynamically typed languages are:")
for obj in ProgrammingLanguage.all_objects:
    if obj.is_dynamic(): print(obj.name)


