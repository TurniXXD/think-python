import math
import random

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