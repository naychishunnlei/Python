import turtle

year = 2023
day = 0  # Assuming 0 for Sunday

days_of_month = 0
for month in range(1, 13):
    days_of_week = ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"]
    days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Draw month and year header
    turtle.penup()
    turtle.goto(-300, 200)
    turtle.pendown()
    turtle.write(f"{month}/{year}")
    
    # Draw days of the week header
    turtle.penup()
    turtle.goto(-300, 150)
    turtle.pendown()
    for day_of_week in days_of_week:
        turtle.forward(60)
        turtle.write(day_of_week)

    # Position for drawing dates
    turtle.penup()
    turtle.goto(-300, 120)
    turtle.pendown()

    # Offset for the starting day of the month
    for _ in range(day):
        turtle.forward(60)

    # Draw dates in grid boxes
    for date in range(1, days_of_month[month - 1] + 1):
        if date < 10:
            turtle.write(f"  {date}")
        else:
            turtle.write(f" {date}")
        
        if (day + date) % 7 == 0:
            turtle.penup()
            turtle.goto(-300, turtle.ycor() - 40)
            turtle.pendown()

    day = (day + days_of_month[month - 1]) % 7

turtle.done()
