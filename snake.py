from turtle import *
import random

def generate_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"

def playing_area():
    pen = Turtle()
    pen.ht()
    pen.speed(0)
    pen.color('green')
    pen.begin_fill()
    pen.goto(-240,240)
    pen.goto(240,240)
    pen.goto(240,-240)
    pen.goto(-240,-240)
    pen.goto(-240,240)
    pen.end_fill()
    
class Head(Turtle):
  def __init__(self, screen):
    super().__init__()
    self.ht()
    self.speed(2)
    self.color(generate_color())
    self.player_color = color
    self.penup()
    self.setheading(90)
    self.shape("square")
    self.direction = "up"
    self.alive = True
    self.speed(2)
    self.st()
    screen.onkeypress(self.left, "Left")
    screen.onkeypress(self.right, "Right")
    screen.onkeypress(self.up, "Up")
    screen.onkeypress(self.down, "Down")

  def up(self):
    if self.direction != "down":
      self.speed(0)
      self.setheading(90)
      self.direction = "up"
      self.speed(0)

  def down(self):
    if self.direction != "up":
      self.speed(0)
      self.setheading(-90)  
      self.direction = "down"
      self.speed(0)

  def left(self):
    if self.direction != "right":
      self.speed(0)
      self.setheading(180)
      self.direction = "left"
      self.speed(0)

  def right(self):
    if self.direction != "left":
      self.speed(0)
      self.setheading(0)
      self.direction = "right"
      self.speed(0)

  def move(self):
    self.forward(20)
    if self.xcor() < -240:
      self.die()
    elif self.xcor() > 240:
      self.die()
    elif self.ycor() > 240:
      self.die()
    elif self.ycor() < -240:
      self.die() 

    
  def die(self):
    self.alive = False
    self.ht()


class Segment(Turtle):
  def __init__(self, other):
    super().__init__()
    self.ht()
    self.speed(0)
    self.shape("square")
    self.color(generate_color())
    self.pu()
    self.st()
  def move (self,seg):
    self.goto(seg.pos())
class Apple(Turtle):
  def __init__(self):
    super().__init__()
    self.ht()
    self.color("red")
    self.shape("circle")
    self.pu()
    self.goto(random.randint(-230,230),random.randint(-230,230))
    self.st()

  def relocate(self):
    self.ht()
    self.goto(random.randint(-230,230),random.randint(-230,230))
    self.st()

def update():
  if head.alive == True:
    head.move()

    for i in range(len(body)-1,0,-1):
        body[i].move(body[i-1])

    if head.distance(apple) < 20:
      apple.relocate()
      new = Segment(body[-1])
      body.append(new)
  screen.ontimer(update, 100)

screen = Screen()
screen.bgcolor("black")
screen.setup(520,520)
playing_area()
screen.listen()

head = Head(screen)
body = [head]
apple = Apple()

update()


screen.exitonclick()
