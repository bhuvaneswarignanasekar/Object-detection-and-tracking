import turtle

wn=turtle.Screen() # create screen
wn.bgcolor("black") # set background color of the screen
wn.title("ball")
#wn.tracer(0)

ball=turtle.Turtle() #create turtle object
ball.shape("circle")       # set the object as ball
ball.color("yellow")        #set ball color
ball.penup()  # removes the tracing line
ball.speed(0)  # set speed of the ball
ball.goto(0,300)        # dropping ball from position 300
gravity=0.1  
ball.dy=0
ball.dx=2
while True:
    try:
        ball.dy -= gravity
        ball.sety(ball.ycor()+ball.dy)
        ball.setx(ball.xcor()+ball.dx)
        
        #Y axis limit
        
        if ball.ycor()>310:
            ball.dx*=-1
        if ball.ycor()<-310:
            ball.dy*=-1
        #x axis limit   
        if ball.xcor()>310:
            ball.dx*=-1
        
        if ball.xcor()<-300:
            ball.dx*=-1
    except KeyboardInterrupt:
        print("program stopped")
        break