from turtle import color, back, left, forward, right, exitonclick

color("white") #Sets the cursor to the beginning of the "line".
back(450)

########## I ##########
color("red")
left(90)
forward(100)
back(100)
right(90)

########## I ##########
color("white")
forward(100)

########## L ##########
color("red")
left(90)
forward(100)
back(100)
right(90)
forward(50)

########## L ##########
color("white") 
forward(50)

########## O ##########
def O_U(u=0):
 forward(50) 
 back(50) 
 left(90) 
 forward(100) 
 right(90) 
 forward(50) 
 right(90) 
 forward(100) 
 left(90) 
 if u == 1:
  color("white") 
  forward(50)
  right(90)
 if u == 1:
  color("red")
  forward(100)
  left(90)

########## O ##########
color("white")
forward(100)


########## V ##########
color("red")
left(120)
forward(110)
back(110)
right(60)
forward(110)
back(110)
right(60)

########## V ##########
color("white")
forward(100)

########## E ##########
color("red")
for x in range(1):
 forward(50)
 back(50)
 left(90)
 forward(50)
 right(90)
 forward(50)
 back(50)
 right(90) 
 forward(100)
 left(90)
 forward(50)

########## E ##########
color("white")
forward(100)


########## Y ##########
color("red")
left(90)
forward(50)
left(45)
forward(75)
back(75)
right(90)
forward(75)
back(75)
left(45)
back(50)
right(90)

########## Y ##########
color("white")
forward(100)

########## O ##########
O_U(u=0) 

########## O ##########
color("white")
forward(100)


########## U ##########
O_U(u=1) 

exitonclick() #Exit