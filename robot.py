name = ""
cmdinput = ""
y = 0
x = 0
coordinate = 0
sprint = 0

def robot_name():
    """
        This function asks the user for their user name and stores it.
    """
    name = input("What do you want to name your robot? ")
    while len(name) == 0:
        name = input("What do you want to name your robot? ")
    print(name +": " "Hello kiddo!")
    return name
    
    
    
def user_input():
    """
        This function asks the user what they would want the robot to do next.
        It takes the user input and carries on the the command. 
    """
    name = robot_name()
    
    while 1:
        usercmd = input(name +": "+"What must I do next? ")
        command_list = split_input(usercmd)
        cmdinput = command_list
        command = ["off","help", "forward", "back", "right", "left", "sprint"]
        if cmdinput[0].lower() == command[0]:
            print(name + ": " + "Shutting down..")
            off_command()
            break
        elif cmdinput[0].lower() == command[1]:
            print("I can understand these commands:\n\
OFF  - Shut down robot\n\
HELP - provide information about commands\n\
Forward - Move forward a certain amount of steps\n\
Back - Move back a certain amount of steps\n\
Right - Turn right\n\
Left - Turn left\n\
Sprint - Move forward by a short burst of speed")
        elif cmdinput[0].lower() == command[2]:
            forward_command(name,cmdinput)
        elif cmdinput[0].lower() == command[3]:
            back_command(name,cmdinput)
        elif cmdinput[0].lower() == command[4] or cmdinput[0].lower() == command[5]:
            get_coordinate(name,cmdinput)
            if cmdinput[0].lower() == command[4] and len(cmdinput) == 1:
                print (' > ' + name + ' turned right.')
                print (' > ' + name + ' now at position ' + '('+ str(x) + ',' + str(y) + ')' + '.')
            if cmdinput[0].lower() == command[5] and len(cmdinput) == 1:
                print (' > ' + name + ' turned left.')
                print (' > ' + name + ' now at position ' + '('+ str(x) + ',' + str(y) + ')' + '.')
        elif cmdinput[0].lower()== command[6]:
            n = int(cmdinput[1])
            sprint_command(name,n)
        else:
            print(name + ": " + "Sorry, I did not understand", '\''+ usercmd + '\'' +".")

def off_command():
    """
        This function shuts down the game.
    """
    global x
    global y
    global coordinate
    global sprint
    sprint = 0
    x = 0
    y = 0
    coordinate = 0
        

def split_input(command_input):
    """
        This function splits the user input.
    """
    return command_input.split()

def forward_command(name,cmdinput):
    """
        This function tells the robot what to do if the user inputs forward. 
        It prints out the position of the robot.
        It includes the range.
    """
    global x
    global y
    global coordinate
   
    if(len(cmdinput) == 2):
        if coordinate == 0:
            y_old = y
            y = y + int(cmdinput[1])
            if y <= -200 or y >= 200:
                y = y_old
                print(name +  ": Sorry, I cannot go outside my safe zone.")
            elif x <= -100 or x >= 100:
                x = x_old
                print(name +  ": Sorry, I cannot go outside my safe zone.")
            elif int(cmdinput[1]) < -200 or int(cmdinput[1]) > 200:
                y = y_old
                print(name +  ": Sorry, I cannot go outside my safe zone.")
            else:
                print(' > ' + name + ' moved forward by ' + cmdinput[1] + ' steps.')
        if coordinate == 1:
            x_old = x
            x = x + int(cmdinput[1])
            if y <= -200 or y>= 200:
                y = y_old
                print(name +  ": Sorry, I cannot go outside my safe zone.")
            elif x <= -100 or x >= 100:
                x = x_old
                print(name +  ": Sorry, I cannot go outside my safe zone.")
            elif int(cmdinput[1]) < -100 or int(cmdinput[1]) > 100:
                x = x_old
                print(name +  ": Sorry, I cannot go outside my safe zone.")
            else:
                print(' > ' + name + ' moved forward by ' + cmdinput[1] + ' steps.')
        if coordinate == 2:
            y_old = y
            y = y - int(cmdinput[1])
            if y <= -200 or y >= 200:
                y = y_old
                print(name +  ": Sorry, I cannot go outside my safe zone.")
            elif x <= -100 or x >= 100:
                x = x_old
                print(name +  ": Sorry, I cannot go outside my safe zone.")
            elif int(cmdinput[1]) < -200 or int(cmdinput[1]) > 200:
                y = y_old
                print(name +  ": Sorry, I cannot go outside my safe zone.")
            else:
                print(' > ' + name + ' moved forward by ' + cmdinput[1] + ' steps.')
        if coordinate == 3:
            x_old = x
            x = x - int(cmdinput[1])
            if y <= -200 or y >= 200:
                y = y_old
                print(name +  ": Sorry, I cannot go outside my safe zone.")
            elif x <= -100 or y >= 100:
                x = x_old
                print(name +  ": Sorry, I cannot go outside my safe zone.")
            elif int(cmdinput[1]) < -100 or int(cmdinput[1]) > 100:
                x = x_old
                print(name +  ": Sorry, I cannot go outside my safe zone.")
            else:
                print(' > ' + name + ' moved forward by ' + cmdinput[1] + ' steps.')
    
    print(' > ' + name + ' now at position ' + '('+ str(x) + ',' + str(y) + ')' + '.')

def back_command(name, cmdinput):
    """
        This function tells the robot what to do if the user inputs back.
        It pronts out the position of the robot.
        It includes the range.
    """
    global x
    global y
    global coordinate

    if (len(cmdinput) == 2):
        if coordinate == 0:
            y_old = y
            y = y - int(cmdinput[1])
            if y <= -200 or y >= 200:
                y = y_old
                print(name +  ": Sorry, I cannot go outside my safe zone.")
            elif x <= -100 or x >= 100:
                x = x_old
                print(name +  ": Sorry, I cannot go outside my safe zone.")
            elif int(cmdinput[1]) < -200 or int(cmdinput[1]) > 200:
                y = y_old
                print(name +  ": Sorry, I cannot go outside my safe zone.")
            else:
                print (' > ' + name + ' moved back by ' + cmdinput[1] + ' steps.')
        if coordinate == 1:
            x_old = x
            x = x - int(cmdinput[1])
            if y<= -200 or y >= 200:
                y = y_old
                print(name +  ": Sorry, I cannot go outside my safe zone.")
            elif x <= -100 or x >= 100:
                x = x_old
                print(name +  ": Sorry, I cannot go outside my safe zone.")
            elif int(cmdinput[1]) < -100 or int(cmdinput[1]) > 100:
                x = x_old
                print(name +  ": Sorry, I cannot go outside my safe zone.")
            else:
                print (' > ' + name + ' moved back by ' + cmdinput[1] + ' steps.')
        if coordinate == 2:
            y_old = y
            y = y + int(cmdinput[1])
            if y <= -200 or y >= 200:
                y = y_old
                print(name +  ": Sorry, I cannot go outside my safe zone.")
            elif x <= -100 or x >= 100:
                x = x_old
                print(name +  ": Sorry, I cannot go outside my safe zone.")
            elif int(cmdinput[1]) < -200 or int(cmdinput[1]) > 200:
                y = y_old
                print(name +  ": Sorry, I cannot go outside my safe zone.")
            else: 
                print (' > ' + name + ' moved back by ' + cmdinput[1] + ' steps.')
        if coordinate == 3:
            x_old = x
            x = x + int(cmdinput[1])
            if y<= -200 or y >= 200:
                y = y_old
                print(name +  ": Sorry, I cannot go outside my safe zone.")
            elif x <= -100 or x >= 100:
                x = x_old
                print(name +  ": Sorry, I cannot go outside my safe zone.")
            elif int(cmdinput[1]) < -100 or int(cmdinput[1]) > 100:
                x = x_old
                print(name +  ": Sorry, I cannot go outside my safe zone.")
            else:
                print (' > ' + name + ' moved back by ' + cmdinput[1] + ' steps.') 

    print (' > ' + name + ' now at position ' + '('+ str(x) + ',' + str(y) + ')' + '.')
   
def sprint_command(name,n):
    """
        This function tell the robot what to do if the user inputs sprint. 
        It prints out the steps everytime it moves as well as the position.
        It includes the range for sprint.
    """
    global x
    global y
    global coordinate
    global step_temp
    global sprint

    if n == 0:
        print (' > ' + name + ' now at position ' + '('+ str(x) + ',' + str(y) + ')' + '.')
    else:
        if coordinate == 0:
            if y + int(n) > 200 :
                print(name +  ": Sorry, I cannot go outside my safe zone.")
                print (' > ' + name + ' now at position ' + '('+ str(x) + ',' + str(y) + ')' + '.')
            else:
                y += int(n)
                print(' > ' + name +" moved forward by " +str(n) + " steps.") 
                sprint_command(name, n - 1)
           
        elif coordinate == 1:
            if x + int(n) > 100:
                print(name +  ": Sorry, I cannot go outside my safe zone.")
                print (' > ' + name + ' now at position ' + '('+ str(x) + ',' + str(y) + ')' + '.')
            else:
                x += int(n)
                print(' > ' + name +" moved forward by " +str(n) + " steps.") 
                sprint_command(name, n - 1)
        elif coordinate == 2:
            if y - int(n) < -200:
                print(name +  ": Sorry, I cannot go outside my safe zone.")
                print (' > ' + name + ' now at position ' + '('+ str(x) + ',' + str(y) + ')' + '.')
            else:
                y -= int(n)
                print(' > ' + name +" moved forward by " +str(n) + " steps.") 
                sprint_command(name, n - 1)
        elif coordinate == 3:
            if x - int(n) < -100:
                print(name +  ": Sorry, I cannot go outside my safe zone.")
                print (' > ' + name + ' now at position ' + '('+ str(x) + ',' + str(y) + ')' + '.')
            else:
                x -= int(n)
                print(' > ' + name +" moved forward by " +str(n) + " steps.") 
                sprint_command(name, n - 1)
        else:
            print(' > ' + name +" moved forward by " +str(n) + " steps.") 
            return n + sprint_command(name, n - 1)

def get_coordinate(name, cmdinput):
    """
        This function controls the co-ordinates of the robot.
    """
    global coordinate
    if len(cmdinput) == 1:
        if coordinate == 0:
            if cmdinput[0] == "right":
                coordinate = 1
            if cmdinput[0] == "left":
                coordinate = 3
        elif coordinate == 1:
            if cmdinput[0] == "right":
                coordinate = 2
            if cmdinput[0] == "left":
                coordinate = 0
        elif coordinate == 2:
            if cmdinput[0] == "right":
                coordinate = 3
            if cmdinput[0] == "left":
                coordinate = 1
        elif coordinate == 3:
            if cmdinput[0] == "right":
                coordinate = 0
            if cmdinput[0] == "left":
                coordinate = 2



def robot_start():
    """This is the entry function, do not change"""
    global x
    global y
    global coordinate
    global sprint
    sprint = 0
    x = 0
    y = 0
    coordinate = 0 
    user_input()


if __name__ == "__main__":
    robot_start()
    