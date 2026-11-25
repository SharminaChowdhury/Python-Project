import turtle
import math
import random

# ==============================
# SCREEN SETUP
# ==============================

screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("#050316")
#screen.title("COSMIC ODYSSEY - OUR SOLAR SYSTEM")
screen.tracer(0)

# ==============================
# BACKGROUND STARS
# ==============================

stars = turtle.Turtle()
stars.hideturtle()
stars.speed(0)
stars.penup()

for i in range(220):
    x = random.randint(-380, 380)
    y = random.randint(-380, 380)

    stars.goto(x, y)
    stars.dot(
        random.randint(1, 3),
        random.choice(["white", "#A78BFA", "#70E1FF"])
    )

# ==============================
# PROJECT TITLE
# ==============================

title = turtle.Turtle()
title.hideturtle()
title.penup()

title.goto(-130, 380)
title.color("#70E1FF")
title.write("COSMIC ODYSSEY",
            font=("Arial", 20, "bold"))

title.goto(-100, 360)
title.color("white")
title.write("OUR SOLAR SYSTEM",
            font=("Arial", 15, "normal"))

title.goto(-65, -375)
title.color("#A78BFA")
title.write("A JOURNEY THROUGH SPACE",
            font=("Arial", 9, "normal"))

# ==============================
# ORBIT DESIGN
# ==============================

orbit = turtle.Turtle()
orbit.hideturtle()
orbit.speed(0)
orbit.pensize(1)

radii = [55, 90, 125, 165, 210, 255, 300, 345]

for r in radii:
    orbit.penup()
    orbit.goto(0, -r)
    orbit.setheading(0)
    orbit.pencolor("#51428F")
    orbit.pendown()
    orbit.circle(r)
    orbit.penup()

# ==============================
# SUN
# ==============================

sun = turtle.Turtle()
sun.hideturtle()
sun.penup()

sun.goto(0, 0)
sun.dot(100, "#512B20")

sun.goto(0, 0)
sun.dot(85, "#B94E16")

sun.goto(0, 0)
sun.dot(70, "#FF8C00")

sun.goto(0, 0)
sun.dot(52, "#FFD700")

sun.goto(0, 0)
sun.dot(35, "#FFF1A8")

sun.goto(-18, -8)
sun.color("#713D20")
sun.write("SUN", font=("Arial", 9, "bold"))

# ==============================
# PLANET INFORMATION
# radius, size, color, speed, name
# ==============================

planets = [
    [55, 8, "#A9A9A9", 4.0, "Mercury"],
    [90, 11, "#D9B38C", 3.0, "Venus"],
    [125, 14, "#168BFF", 2.5, "Earth"],
    [165, 11, "#C14432", 2.0, "Mars"],
    [210, 24, "#D69A62", 1.5, "Jupiter"],
    [255, 21, "#DCC69A", 1.2, "Saturn"],
    [300, 17, "#83D8D5", 1.0, "Uranus"],
    [345, 17, "#4169E1", 0.8, "Neptune"]
]

# ==============================
# PLANET DRAWING TURTLE
# ==============================

planet_draw = turtle.Turtle()
planet_draw.hideturtle()
planet_draw.speed(0)
planet_draw.penup()

angles = [0] * 8

# ==============================
# ELLIPTICAL SATURN RING
# ==============================

def draw_saturn_ring(x, y):

    planet_draw.penup()
    planet_draw.pencolor("#EAD7A1")
    planet_draw.pensize(4)

    for a in range(361):

        angle = math.radians(a)

        rx = 34 * math.cos(angle)
        ry = 13 * math.sin(angle)

        px = x + rx
        py = y + ry

        if a == 0:
            planet_draw.goto(px, py)
            planet_draw.pendown()
        else:
            planet_draw.goto(px, py)

    planet_draw.penup()

# ==============================
# JUPITER SURFACE BANDS
# ==============================

def draw_jupiter(x, y, size):

    radius = size / 2

    bands = [
        (-7, "#A76B43"),
        (-3, "#F1D0A0"),
        (3, "#B77A50"),
        (7, "#F1D0A0")
    ]

    for offset, color in bands:

        half_width = math.sqrt(
            max(0, radius * radius - offset * offset)
        )

        planet_draw.penup()
        planet_draw.goto(x - half_width, y + offset)
        planet_draw.pencolor(color)
        planet_draw.pensize(2)
        planet_draw.pendown()
        planet_draw.goto(x + half_width, y + offset)
        planet_draw.penup()

# ==============================
# EARTH DETAILS
# ==============================

def draw_earth(x, y, size):

    planet_draw.goto(x - 3, y + 2)
    planet_draw.dot(5, "#36C66A")

    planet_draw.goto(x + 3, y - 3)
    planet_draw.dot(4, "#36C66A")

    planet_draw.goto(x + 2, y + 4)
    planet_draw.dot(3, "#36C66A")

# ==============================
# ANIMATION
# ==============================

def animate():

    planet_draw.clear()

    for i in range(len(planets)):

        radius = planets[i][0]
        size = planets[i][1]
        color = planets[i][2]
        speed = planets[i][3]
        name = planets[i][4]

        angle = math.radians(angles[i])

        x = radius * math.cos(angle)
        y = radius * math.sin(angle)

        # Saturn ring behind planet
        if name == "Saturn":
            draw_saturn_ring(x, y)

        # Planet glow
        planet_draw.penup()
        planet_draw.goto(x, y)
        planet_draw.dot(size + 8, "#242044")

        # Planet body
        planet_draw.goto(x, y)
        planet_draw.dot(size, color)

        # Earth surface
        if name == "Earth":
            draw_earth(x, y, size)

            # Moving Moon
            moon_angle = math.radians(angles[i] * 4)

            moon_x = x + 21 * math.cos(moon_angle)
            moon_y = y + 21 * math.sin(moon_angle)

            planet_draw.goto(moon_x, moon_y)
            planet_draw.dot(5, "#DADADA")

        # Jupiter bands
        if name == "Jupiter":
            draw_jupiter(x, y, size)

        # Mars polar cap
        if name == "Mars":
            planet_draw.goto(x, y + 3)
            planet_draw.dot(3, "#F2C9B8")

        # Venus atmosphere detail
        if name == "Venus":
            planet_draw.goto(x - 2, y + 2)
            planet_draw.dot(3, "#F7D9A1")

        # Planet highlight
        planet_draw.goto(x - size / 5, y + size / 5)
        planet_draw.dot(3, "#FFFFFF")

        # Planet name
        planet_draw.goto(x + size / 2 + 5,
                         y + size / 2 + 5)

        planet_draw.color("white")
        planet_draw.write(
            name,
            font=("Arial", 7, "normal")
        )

        # Update orbital angle
        angles[i] = (angles[i] + speed) % 360

    screen.update()
    screen.ontimer(animate, 50)

# ==============================
# START ANIMATION
# ==============================

animate()

screen.mainloop()