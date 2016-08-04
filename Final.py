title = "\033[1m\033[35m\nFinal Project by Devin Rosenthal\n\033[0m"
instructions = "\ntemp - fill in later"
temp=""
while("start" not in temp.lower()):
	temp = input("Type \"Info\" for Tutorial\nType \"Start\" to Start\nType \"Credits\" for Credits\n")
	if("info" in temp.lower()):
		print(instructions)
	if ("credits" in temp.lower()):
		print(title)
