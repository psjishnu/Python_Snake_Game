import turtle
import time
import random
import pygame
import itertools
import threading
import sys

done = False
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)

t = threading.Thread(target=animate)
t.start()

time.sleep(3)
done = True
pygame.mixer.init()

delay = 0.1  

score = 0
high_score = 0
wn = turtle.Screen()
wn.title("Snake Game By psjishnu")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0) 
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("orange")
head.penup()
head.goto(0,0)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("green")
food.penup()
food.goto(0,100)
trap = turtle.Turtle()
trap.speed(0)
trap.shape("circle")
trap.color("red")
trap.penup()
trap.goto(100,100)

segments = []
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))


def go_up():
	if head.direction != "down":
		head.direction = "up"

def go_down():
	if head.direction != "up":
		head.direction = "down"

def go_right():
	if head.direction != "left":
		head.direction = "right"

def go_left():
	if head.direction != "right":
		head.direction = "left"

def move():
	if head.direction == "up":
		y = head.ycor()
		head.sety(y + 20)

	if head.direction == "down":
		y = head.ycor()
		head.sety(y - 20)

	if head.direction == "left":
		x = head.xcor()
		head.setx(x - 20)

	if head.direction == "right":
		x = head.xcor()
		head.setx(x + 20)

wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_left, "Left")

arr=[]
start=1
snakelen=0
def music():
	pygame.mixer.music.load("Music.mp3")
	pygame.mixer.music.play()
def hit():
	pygame.mixer.music.load("hit.mp3")
	pygame.mixer.music.play()
def trapped():
	pygame.mixer.music.load("red.mp3")
	pygame.mixer.music.play()

while True:
	wn.update()
	if(start==1):
		music()
		start=0
	def gameover():
		time.sleep(1)
		head.goto(0,0)
		head.direction = "stop"
		for segment in segments:
			segment.goto(1000,1000)
		segments.clear()
		score =0
		delay = 0.01
		pen.clear()
		pen.write("Score: {} High Score: {}".format(score,high_score), align="center", font= ("Courier", 24, "normal"))

	if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
		arr=[]
		snakelen=0
		hit()
		gameover()
		music()
	if head.distance(food) < 20:
		snakelen=snakelen+1
		print(snakelen)
		x = random.randint(-270, 270)
		y = random.randint(-270, 270)
		x1 = random.randint(-270, 270)
		y1 = random.randint(-270, 270)
		food.goto(x,y)
		trap.goto(x1,y1)
		new_segment = turtle.Turtle()
		new_segment.speed(0) 
		new_segment.shape("square")
		new_segment.color("yellow")
		new_segment.penup()
		arr.append(new_segment)
		segments.append(new_segment)
		delay -= 0.001

		score += 10

		if score > high_score:
			high_score = score
		pen.clear()
		pen.write("Score: {} High Score: {}".format(score,high_score), align="center", font= ("Courier", 24, "normal"))
	
	if (head.distance(trap) < 20):
		if (snakelen>0):
			x = random.randint(-270, 270)
			y = random.randint(-270, 270)
			trap.goto(x,y)
			pops=arr.pop(snakelen-1)
			segments.remove(pops)
			pops.goto(1000,1000)
			snakelen=snakelen-1
		else:
			arr=[]
			snakelen=0
			trapped()
			gameover()
			music()

		
	for index in range(len(segments)-1, 0, -1):
		x = segments[index-1].xcor()
		y = segments[index-1].ycor()
		segments[index].goto(x,y)

	if len(segments) > 0:
		x = head.xcor()
		y = head.ycor()
		segments[0].goto(x,y)


	move()

	for segment in segments:
		if segment.distance(head) < 20:			
			arr=[]
			snakelen=0
			trapped()
			gameover()
			music()			

	time.sleep(delay)
wn.mainloop()
