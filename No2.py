import turtle

year = 2023
first_day = 1  # 0 for Sunday, 1 for Monday, etc.

turtle.speed(0)
turtle.penup()
turtle.goto(-250, 250)

def draw_grid_box(content, width=40, height=40):
    turtle.pendown()
    for _ in range(4):
        turtle.forward(width)
        turtle.right(90)
    turtle.penup()
    turtle.goto(turtle.xcor() - width / 2, turtle.ycor() - height / 2)
    turtle.write(content)
    turtle.goto(turtle.xcor() + width, turtle.ycor() + height)

month = 1
month_lengths = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_labels = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

while month <= 12:
    daysOfMonth = month_lengths[month]
    month_name = f"Month #{month}"
    
    for _ in range(7):  # Adjust for alignment
        draw_grid_box('')
    
    turtle.goto(-250, turtle.ycor() - 40)
    draw_grid_box(month_name, width=280, height=40)
    
    for day_label in days_labels:
        draw_grid_box(day_label)
    
    i = 0
    while i < first_day:
        draw_grid_box('')
        i += 1

    day = 1
    while day <= daysOfMonth:
        if (day + first_day - 1) % 7 == 0:
            turtle.goto(-250, turtle.ycor() - 40)
        draw_grid_box(str(day))
        day += 1

    turtle.goto(-250, turtle.ycor() - 40)
    turtle.goto(-250, turtle.ycor() - 20)

    first_day = (first_day + daysOfMonth) % 7
    month += 1

# Keep the Turtle graphics window open until it's clicked
turtle.done()
