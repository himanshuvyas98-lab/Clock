import time
import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.title("Clock")
wn.tracer(0)

#creat our drawing
pen = turtle.Turtle() 
pen.speed(0)
pen.pensize(5)


def draw_clock(h, m, s, pen):

    # draw clock face
    pen.up()
    pen.goto(0,210)
    pen.setheading(180)
    pen.color("green")
    pen.pendown()
    pen.circle(210)

    # draw the line for hours
    pen.penup()
    pen.goto(0,0)
    pen.setheading(90)

    for _ in range(12):
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0,0)
        pen.rt(30)
    # draw the hour hand
    pen.penup()
    pen.goto(0,0)
    pen.color("gold")
    pen.setheading(90)
    angle = (h / 12) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(110)

    # draw the munite hand
    pen.penup()
    pen.goto(0,0)
    pen.color("gold")
    pen.setheading(90) 
    angle = (m / 60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(170)

    # draw the second hand
    pen.penup()
    pen.goto(0,0)
    pen.color("red")
    pen.setheading(90)
    angle = (s / 60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(80)

while True:    
    h = int(time.strftime("%H"))
    m = int(time.strftime("%M"))
    s = int(time.strftime("%S"))


    draw_clock(h, m, s, pen) 
    wn.update()

    time.sleep(1)


    pen.clear()


wn.mainloop()