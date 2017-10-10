answer = input("do you want to here a joke ")

Yes = ["yes", "YES", "Y", "y"]
No = ["no", "NO", "N", "n"]

if answer in Yes:
	print("Im so funny")
elif answer in No:
	print("No joke for you")
else:
	print("I dont understand")