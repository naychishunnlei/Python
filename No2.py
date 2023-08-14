import turtle

year = 2023
first_day = 1  # 0 for Sunday, 1 for Monday, etc.

turtle.speed(0)
turtle.penup()
turtle.goto(-250, 250)

def draw_grid_box(content):
    turtle.pendown()
    for _ in range(4):
        turtle.forward(40)
        turtle.right(90)
    turtle.penup()
    turtle.goto(turtle.xcor() - 20, turtle.ycor() - 20)
    turtle.write(content, align='center', font=('Arial', 12, 'normal'))
    turtle.goto(turtle.xcor() + 20, turtle.ycor() + 20)

month = 1
month_lengths = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while month <= 12:
    daysOfMonth = month_lengths[month]
    month_name = f"Month #{month}"
    
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)

    turtle.goto(-250, turtle.ycor() - 40)
    turtle.write(month_name, align='center', font=('Arial', 16, 'normal'))
    turtle.goto(-250, turtle.ycor() - 20)
    turtle.write("  Sun Mon Tue Wed Thu Fri Sat", align='center', font=('Arial', 12, 'normal'))

    i = 0
    while i < first_day:
        draw_grid_box('')
        turtle.goto(turtle.xcor() + 40, turtle.ycor())
        i += 1

    day = 1
    while day <= daysOfMonth:
        if (day + first_day - 1) % 7 == 0:
            turtle.goto(-250, turtle.ycor() - 20)
        draw_grid_box(str(day))
        turtle.goto(turtle.xcor() + 40, turtle.ycor())
        day += 1

    turtle.goto(-250, turtle.ycor() - 40)
    turtle.goto(-250, turtle.ycor() - 20)

    first_day = (first_day + daysOfMonth) % 7
    month += 1

# Keep the Turtle graphics window open until it's clicked
turtle.done()
