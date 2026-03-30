import turtle

# Screen setup
screen = turtle.Screen()
screen.setup(width=700, height=600)
screen.title("Victory Day of Bangladesh - 16th December")
screen.bgcolor("#181717")

t = turtle.Turtle()
t.speed(3)

# 1. Green rectangle (flag background)
t.penup()
t.goto(-200, 100)
t.pendown()
t.color("#006a4e")
t.begin_fill()
for _ in range(2):
    t.forward(400)
    t.right(90)
    t.forward(240)
    t.right(90)
t.end_fill()

# ২. Red circle (red sun in the flag)
t.penup()
t.goto(45, -85) #
t.pendown()
t.color("#f42a41")
t.begin_fill()
t.circle(80)
t.end_fill()

# 3. Text Design (Victory Day Greetings)
t.penup()
t.goto(0, -200)
t.color("#006a4e")
t.write("𝓿𝓲𝓬𝓽𝓸𝓻𝔂 𝓭𝓪𝔂 𝓸𝓯 𝓫𝓪𝓷𝓰𝓵𝓪𝓭𝓮𝓼𝓱", align="center", font=("Arial", 30, "bold"))

t.goto(0, -250)
t.color("#f42a41")
t.write("16𝓽𝓱 𝓓𝓮𝓬𝓮𝓶𝓫𝓮𝓻", align="center", font=("Verdana", 20, "italic"))

#finishing touches
t.hideturtle()
screen.mainloop()