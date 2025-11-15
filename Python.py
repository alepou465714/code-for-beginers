password = input("Enter password: ")
if password == "1234":
    print("Welcome")
    import turtle
    turtle.pencolor("brown")
    turtle.pensize(20)
    turtle.bgcolor("white")
    for i in range(1):
        turtle.left(90)
        turtle.forward(50)
        turtle.back(100)
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(50)
        turtle.back(100)
else:
    print("Try again")
