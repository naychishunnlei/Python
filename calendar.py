import turtle
import calendar

year = int(input("Enter a year: "))
day = int(input("Enter the first day of the year (0 for Sunday, 1 for Monday, etc.): "))

daysOfMonth = 0

# Set up the Turtle
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.goto(-250, 250)

def draw_grid_box(content):
    pen.pendown()
    pen.begin_fill()
    for _ in range(4):
        pen.forward(40)
        pen.right(90)
    pen.end_fill()
    pen.penup()
    pen.goto(pen.xcor() - 20, pen.ycor() - 20)
    pen.write(content, align='center', font=('Arial', 12, 'normal'))
    pen.goto(pen.xcor() + 20, pen.ycor() + 20)

for month in range(1, 13):
    daysOfMonth = calendar.monthrange(year, month)[1]
    month_name = calendar.month_name[month]
    
    for _ in range(4):
        pen.forward(100)
        pen.right(90)

    pen.goto(-250, pen.ycor() - 40)
    pen.write(month_name, align='center', font=('Arial', 16, 'normal'))
    pen.goto(-250, pen.ycor() - 20)
    pen.write("  Sun Mon Tue Wed Thu Fri Sat", align='center', font=('Arial', 12, 'normal'))

    for i in range(0, day):
        draw_grid_box('')
        pen.goto(pen.xcor() + 40, pen.ycor())

    for i in range(1, daysOfMonth + 1):
        if (i + day - 1) % 7 == 0:
            pen.goto(-250, pen.ycor() - 20)
        draw_grid_box(str(i))
        pen.goto(pen.xcor() + 40, pen.ycor())

    pen.goto(-250, pen.ycor() - 40)
    pen.goto(-250, pen.ycor() - 20)

    day = (day + daysOfMonth) % 7

# Keep the Turtle graphics window open until it's clicked
turtle.done()
