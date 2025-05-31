import random
def main():
  score = float(input("Enter score: "))
  print(outcome(score))
  print("random grades")
  random_grades = random.randint(0, 100)
  print(random_grades)
  print(outcome(random_grades))

def outcome(s):
  if s<0 or s>100:
    return "Invalid score"
  elif s>=90 :
    return"Excellent"
  elif s>=50 :
    return"Passable"
  else:
    return"Bad"

main()

