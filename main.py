import math
import random
import time
import turtle

kek="s"

num=2

def logger(section, *stuff):
  print(f"\n\n{section}:\n", *stuff)

logger("Prints", "hello world mf %f" * 2, kek, num * 2, { "m": "kek", "pi": math.pi})

logger("Randoms", random.random(), random.randint(1, 10), random.uniform(7.5, 10))

degrees=45
radians=degrees / 180.0 * math.pi

logger("Math", degrees, radians, math.sin(radians), math.sqrt(2) / 2.0)

def grid_gen(index):
  if (index < 5):
    print("Index must be greater than 5")

  if (index %2 == 0):
    print("Index must be an odd number")

  row = 0
  halfIndex = math.floor(index / 2)

  def resolve_print_x_axis_char(col):
    if col == 0:
      return "+"
    if col == halfIndex:
      return "+"
    if col == index - 1:
      return "+"
    return "-"

  def resolve_print_y_axis_char(col):
    if col == 0 or col == halfIndex or col == index - 1:
      return "|"
    return " "

  while row < index:
      printout=""
      col = 0

      while col < index:
        if row == 0 or row == halfIndex or row == index - 1:
          printout += resolve_print_x_axis_char(col)
        else:
          printout += resolve_print_y_axis_char(col)
        col += 1

      print(printout)
      row += 1

logger("Grid")
grid_gen(19)

# tkinter._test()
# bob = turtle.Turtle()


# bob.fd(100)
# bob.lt(90)

# print(bob)

# turtle.mainloop()

def draw_fibonacci_spiral(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])

    turtle.pensize(2)
    turtle.speed(0.2)  # slow speed (1 = slowest visible)

    # Draw Fibonacci squares
    for i in range(n):
        turtle.forward(fib[i] * 5)
        turtle.left(90)
        time.sleep(0.1)

    # Reset position for spiral
    turtle.penup()
    turtle.setposition(0, 0)
    turtle.setheading(0)
    turtle.pendown()

    # Draw Fibonacci spiral (quarter circles)
    for i in range(n):
        radius = fib[i] * 2
        turtle.circle(radius, 90)
        time.sleep(0.1)

    turtle.done()

draw_fibonacci_spiral(10)