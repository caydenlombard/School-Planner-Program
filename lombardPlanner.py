# /* School Planner
# lombardPlanner.py
# Cayden Lombard
# Lumbo
# ctlombar */

from graphics import *
from random import randrange

#########GLOBAL FUNCTIONS#########

# function that creates graphics window and returns the window
def setUpWindow():
    # GW
    win = GraphWin("School Planner", 1200,600)
    win.setBackground("white")
    win.setCoords(0,-4,7,10)
    return win

# function draws the frame of the planner, labels the days, and displays title and greeting
def drawFrame():
    # draw the vertical lines of the frame
    w=0
    for i in range(8):
        vertical = Line(Point(w, 0), Point(w, 8))
        vertical.setWidth(1)
        vertical.draw(win)
        w += 1

    # draw the top of the frame
    top = Line(Point(0, 8), Point(7, 8))
    top.draw(win)

    # draw the bottom of the frame
    bottom = Line(Point(0, 0), Point(7, 0))
    bottom.draw(win)

    # label the days
    week=['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
    w=.5
    for day in week:
        # OTXT
        dayText=Text(Point(w, 8.4), day)
        dayText.draw(win)
        w += 1

    # draw the title
    title = Text(Point(3.5, 9.6), "School Planner")
    title.setSize(24)
    title.setTextColor('red')
    title.draw(win)

    # draw the greeting in a random color each time
    greet = Text(Point(5.5, 9.4), "Welcome!")
    greet.setSize(16)
    randomColor=['blue','lightblue','red','green','lightgreen','yellow','pink','orange','purple']
    # RND
    random=randrange(0, len(randomColor))
    greet.setTextColor(randomColor[random])
    greet.draw(win)

# function draws the and labels all of the buttons
def drawButtons():
    # create close button
    button = Rectangle(Point(.2, 8.75), Point(1.8, 9.75))
    button.setFill("lightgray")
    buttonLabel = Text(button.getCenter(), "Click to close program")
    button.draw(win)
    buttonLabel.draw(win)

    # create new assignment buttons
    for i in range(8):
        button = Rectangle(Point(i, 7.2), Point(1+i, 8))
        button.setFill("lightgray")
        buttonLabel = Text(button.getCenter(), "Enter assignment")
        button.draw(win)
        buttonLabel.draw(win)

    # create submit button
    button = Rectangle(Point(6.3, -3.5), Point(6.8, -2.7))
    button.setFill("lightgray")
    buttonLabel = Text(button.getCenter(), "Submit")
    button.draw(win)
    buttonLabel.draw(win)

# checks location of click to see if user is clicking a button, parameters are location of click,
# location of lower left corner of button and location of upper right corner of button
def checkButtonClick(clickedPoint, leftLower, rightUpper):
    # if button is clicked function return in if white space is clicked button returns out
    if leftLower.getX() < clickedPoint.getX() < rightUpper.getX() and leftLower.getY() < clickedPoint.getY() < rightUpper.getY() :
        return 'in'
    else:
        return 'out'

# function creates entry boxes and uses submitted strings to return the course, assignment name, and time it's due
def getInfo():
    # create course entry box and get course once submit is pressed
    # if cancel is entered do not display assignment
    clickedPoint = Point(0,0)
    enterText=Text(Point(.3, -1), "Enter Class:")
    enterText.draw(win)
    cancel = Text(Point(3.5, -2), "Enter  'cancel' and submit entries to cancel.")
    cancel.draw(win)
    entry = Entry(Point(1.5, -1), 20)
    entry.draw(win)
    # IMS
    while not 'in' == (checkButtonClick(clickedPoint, Point(6.3, -3.5), Point(6.8, -2.7))):
        clickedPoint = win.getMouse()
    # IEB
    course = entry.getText()

    entry.undraw()
    enterText.undraw()
    cancel.undraw()

    # create assignment name entry box and get assignment name once submit is pressed
    enterText=Text(Point(.4, -1.5), "Enter Assignment:")
    enterText.draw(win)
    entry = Entry(Point(1.5, -1.5), 20)
    entry.draw(win)
    clickedPoint = Point(0,0)
    while not 'in' == (checkButtonClick(clickedPoint, Point(6.3, -3.5), Point(6.8, -2.7))):
        clickedPoint = win.getMouse()
    name = entry.getText()

    entry.undraw()
    enterText.undraw()

    # create time entry box and get time once submit is pressed
    enterText=Text(Point(.45, -2), "Enter Time(Military):")
    enterText.draw(win)
    entry = Entry(Point(1.5, -2), 20)
    entry.draw(win)
    time = '2500'
    clickedPoint = Point(0,0)

    # keep asking for time until valid time is entered
    wrong=Text(Point(3.5, -2), '')
    wrong.draw(win)
    wrong.setTextColor('red')
    while 'in' != (checkButtonClick(clickedPoint, Point(6.3, -3.5), Point(6.8, -2.7))) or len(time) == 0 or int(time) // 100 > 24 or len(time)==1 or len(time) != 4 or int(time[2]) > 5:
        clickedPoint=win.getMouse()
        time = entry.getText()
        if len(time) == 0 or int(time) // 100 > 24 or len(time)==1 or len(time) != 4 or int(time[2]) > 5:
            wrong.setText('Time entered is invalid, try again')

    entry.undraw()
    enterText.undraw()
    if wrong != '':
        wrong.setText('')

    return course, name, time

# function uses an x value, day of the week, and graphic window to create an instance of the assignment class
# and display the assignment on screen. returns the assignment
def makeAssignment(x,day,win):
    course, name, time = getInfo()
    # CLOD
    assign = Assignment(day, course, name, time, win)
    y = assign.calcY()
    assign.display(x, y, win)
    assign.displayName(win)
    return assign

# function accepts a list of assignments and calls makeAssignment to display and create an instance
# of the Assignment class. appends assignments to list and returns list
def getAssignment(officialWork):
    week=['Sun','Mon','Tue','Wed','Thu','Fri','Sat']

    # creates and appends Sunday assignment
    if 'in' == checkButtonClick(clickedPoint, Point(0, 7.2), Point(1, 8)):
        # FNC
        assign = makeAssignment(.5, week[0], win)
        assign.checkDel()
        officialWork.append(assign)

    # creates and appends Monday assignment
    elif 'in' == checkButtonClick(clickedPoint, Point(1, 7.2), Point(2, 8)):
        assign = makeAssignment(1.5, week[1], win)
        assign.checkDel()
        officialWork.append(assign)

    # creates and appends Tuesday assignment
    elif 'in' == checkButtonClick(clickedPoint, Point(2, 7.2), Point(3, 8)):
        assign = makeAssignment(2.5, week[2], win)
        assign.checkDel()
        officialWork.append(assign)

    # creates and appends Wednesday assignment
    elif 'in' == checkButtonClick(clickedPoint, Point(3, 7.2), Point(4, 8)):
        assign = makeAssignment(3.5, week[3], win)
        assign.checkDel()
        officialWork.append(assign)

    # creates and appends Thursday assignment
    elif 'in' == checkButtonClick(clickedPoint, Point(4, 7.2), Point(5, 8)):
        assign = makeAssignment(4.5, week[4], win)
        assign.checkDel()
        officialWork.append(assign)

    # creates and appends Friday assignment
    elif 'in' == checkButtonClick(clickedPoint, Point(5, 7.2), Point(6, 8)):
        assign = makeAssignment(5.5, week[5], win)
        assign.checkDel()
        officialWork.append(assign)

    # creates and appends Saturday assignment
    elif 'in' == checkButtonClick(clickedPoint, Point(6, 7.2), Point(7, 8)):
        assign = makeAssignment(6.5, week[6], win)
        assign.checkDel()
        officialWork.append(assign)

    return officialWork

# function creates instances of Assignment and displays them class using info from input file
# returns assignment
def infileAssignment(day,n):
    assign = Assignment(day[0], day[1], day[2], day[3], win)
    y = assign.calcY()
    assign.display(n+.5, y, win)
    assign.displayName(win)

    return assign

# function creates a list of instances of the Assignment class using infileAssignment and an info from input file
# returns list
def checkAssignment():
    # IFL
    # open file and skip first line
    infile = open("inputPlanner.txt", "r")
    infile.readline()

    # create list and append instances of assignments to that list using info from the text file
    assignmentList=[]
    for line in infile:
        line=line.split()
        assignmentList.append(line)

    # close input file and create new list
    infile.close()
    officialWork=[]

    # creates and appends Sunday assignment
    if len(assignmentList[0]) > 1:
        sun = assignmentList[0]
        assign = infileAssignment(sun, 0)
        officialWork.append(assign)

    # creates and appends Monday assignment
    if len(assignmentList[1]) > 1:
        mon = assignmentList[1]
        assign=infileAssignment(mon,1)
        officialWork.append(assign)

    # creates and appends Tuesday assignment
    if len(assignmentList[2]) > 1:
        tue = assignmentList[2]
        assign=infileAssignment(tue,2)
        officialWork.append(assign)

    # creates and appends Wednesday assignment
    if len(assignmentList[3]) > 1:
        wed = assignmentList[3]
        assign=infileAssignment(wed,3)
        officialWork.append(assign)

    # creates and appends Thursday assignment
    if len(assignmentList[4]) > 1:
        thu = assignmentList[4]
        assign=infileAssignment(thu, 4)
        officialWork.append(assign)

    # creates and appends Friday assignment
    if len(assignmentList[5]) > 1:
        fri = assignmentList[5]
        assign=infileAssignment(fri,5)
        officialWork.append(assign)

    # creates and appends Saturday assignment
    if len(assignmentList[6]) > 1:
        sat = assignmentList[6]
        assign=infileAssignment(sat,6)
        officialWork.append(assign)

    return officialWork

#########CLASS FUNCTIONS#########

# CLOD
# create class Assignment that assigns a day, course, name, and time to an instance and creates the instance
class Assignment:
    def __init__(self,day,course,name,time,win):
        self.day = day
        self.course = course
        self.name = name
        self.time = time
        self.hidden = True

    # method uses due time of the assignment to determine y value
    # returns y value
    def calcY(self):
        if 0 <= int(self.time) <= 359:
            y = (6*(7/6))-.1
        elif 400 <= int(self.time) <= 759:
            y = (5*(7/6))-.1
        elif 800 <= int(self.time) <= 1159:
            y = (4*(7/6))-.1
        elif 1200 <= int(self.time) <= 1559:
            y = (3*(7/6))-.1
        elif 1600 <= int(self.time) <= 1959:
            y = (2*(7/6))-.1
        elif 2000 <= int(self.time) <= 2400:
            y = (7/6)-.1
        return y

    # method sets text of assignment using x value, y value, and graphic window
    def display(self,x,y,win):
        self.text1 = Text(Point(x, y), self.course + ' ' + self.name)
        self.text2 = Text(Point(x, y - .4), 'Due: ' + self.time)

    # method displays an assignment's text in graphic window
    def displayName(self,win):
        if self.hidden:
            self.text1.draw(win)
            self.text2.draw(win)
            self.hidden = False

    # method stops an assignment from being draw if cancel is entered into course entry box
    def checkDel(self):
        if self.course.upper() == 'CANCEL':
            if self.hidden == False:
                self.text1.undraw()
                self.text2.undraw()
                self.hidden = True

    # method prints assignment data to output file
    def outPrint(self):
        print("{0:<10}{1:>10}{2:>20}{3:>20}".format(self.day, self.course, self.name, self.time), file=outfile)

if __name__=='__main__':
    # set up graphics window
    win = setUpWindow()

    # draw frame, buttons, and display labels
    drawFrame()
    drawButtons()

    # create and display list of assignments from input file
    # return assignment list
    officialWork=checkAssignment()

    # initialize clickedPoint and run getAssignment until close program is clicked
    # return assignment list
    clickedPoint = Point(0,0)
    while not 'in' == checkButtonClick(clickedPoint, Point(.2, 8.75), Point(1.8, 9.75)):
        clickedPoint = win.getMouse()
        officialWork=getAssignment(officialWork)

    # OFL
    # open output file
    outfile = open("outputPlanner.txt", 'w')

    # LOOD
    # print list of assignments to output file
    print("{0:<10}{1:>10}{2:>20}{3:>20}".format('Day:', 'Class:', 'Assignment:', 'Due time:'), file=outfile)
    for work in officialWork:
        work.outPrint()
    outfile.close()

    # close window
    win.close()