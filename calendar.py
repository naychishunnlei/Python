import turtle
import calendar as cal

year = 2023
first_day = 1  # 0 for Sunday, 1 for Monday, etc.

turtle.speed(0)
turtle.penup()
turtle.goto(-250, 250)

def draw_grid_box(content):
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(40)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(turtle.xcor() - 20, turtle.ycor() - 20)
    turtle.write(content, align='center', font=('Arial', 12, 'normal'))
    turtle.goto(turtle.xcor() + 20, turtle.ycor() + 20)

for month in range(1, 13):
    daysOfMonth = cal.monthrange(year, month)[1]
    month_name = f"Month #{month}"
    
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)

    turtle.goto(-250, turtle.ycor() - 40)
    turtle.write(month_name, align='center', font=('Arial', 16, 'normal'))
    turtle.goto(-250, turtle.ycor() - 20)
    turtle.write("  Sun Mon Tue Wed Thu Fri Sat", align='center', font=('Arial', 12, 'normal'))

    for i in range(0, first_day):
        draw_grid_box('')
        turtle.goto(turtle.xcor() + 40, turtle.ycor())

    for i in range(1, daysOfMonth + 1):
        if (i + first_day - 1) % 7 == 0:
            turtle.goto(-250, turtle.ycor() - 20)
        draw_grid_box(str(i))
        turtle.goto(turtle.xcor() + 40, turtle.ycor())

    turtle.goto(-250, turtle.ycor() - 40)
    turtle.goto(-250, turtle.ycor() - 20)

    first_day = (first_day + daysOfMonth) % 7

# Keep the Turtle graphics window open until it's clicked
turtle.done()
