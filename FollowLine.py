NO_LINE = 0
ON_LINE = 1
IN_CORNER = 2
currentState = 0
while True:
    if currentState == NO_LINE:
        if linesensors == [0,0,0]:
            # Searching for line , keep turning left.
        elif linesensors == [1,0,0] or linesensors == [1,1,0]:
            currentState = ON_LINE
    elif currentState == ON_LINE:
            if linesensors == [1,0,0] or linesensors == [1,1,0]:
                # Stay on line GO straight.
            elif  linesensors == [1,1,1]:
                currentState = IN_CORNER
            elif linsensors == [0,0,0]:
                currentState == NO_LINE

    elif currentState == IN_CORNER:
        if linesensors = [0,0,0]:
            currentState == NO_LINE

def Execute(currentState):
    if currentState == NO_LINE:
        antimattter.turnwheels(left)
    if currentState == ON_LINE:
        antimatter.turnwheels(straight)
    if currentState == IN_CORNER:
        antimatter.turnwheels(right)

