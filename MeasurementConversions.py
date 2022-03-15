print("This converts between grams and ounces.")
choice = input("Enter 1 to convert from oz to g. Enter 2 to convert from g to oz")
if choice == "1":
  oz = float(input("Please input the number of ounces."))
  print("You have " + str(oz * 28.3495) + " grams.")
elif choice == "2":
  g = float(input("Please input the number of grams."))
  print("You have " + str(g / 28.3495) + " grams.")
else:
  print("Error: Invalid Choice")
