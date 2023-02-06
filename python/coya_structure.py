choice1 = input('a or b?').lower()
if choice1 == "a":
  choice2 = input('a or b?').lower()
  if choice2 == "a":
    choice3 = input("a or b?").lower()
    if choice3 == "a":
      print("a")
    elif choice3 == "b":
      print("b")
    elif choice2 == "b":
      print("b")
  elif choice1 == "b":
    print("b")
else:
  print("c")