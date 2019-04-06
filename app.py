x = ""
while x.upper() != "QUIT":
    x = input('>')
    if x.upper() == "HELP":
        print("Kindly type \nSTART to start the car\nSTOP to stop the car\nQuit to end")
    elif x.upper() == "START":
        print("Car is moving .................")
    elif x.upper() == "STOP":
        print("Car is Stopped .................")
    elif x.upper() == "QUIT":
        break
    else:
        print("I dont Understand That")
    