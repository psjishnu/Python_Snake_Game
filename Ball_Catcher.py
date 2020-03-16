import turtle
import time
import random
import pygame
import itertools
import threading
import sys
done=0
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done==1 :
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
done=1
t = threading.Thread(target=animate)
t.start()

time.sleep(3)
pygame.mixer.init()

delay = 0.1  

score = 0
high_score = 0
wn = turtle.Screen()
wn.title("Snake Game By psjishnu")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0) 
def ready(basketx,a,b):
	basketx.speed(0)
	basketx.shape("square")
	basketx.color("orange")
	basketx.penup()
	basketx.goto(a,b)
	basketx.direction = "stop"
basket= turtle.Turtle()
basket2 = turtle.Turtle()
basket3 = turtle.Turtle()
basket4 = turtle.Turtle()
def reset():
	ready(basket,0,-260)
	ready(basket2,-20,-260)
	ready(basket3,20,-260)
reset()



ball = turtle.Turtle()
ball.speed()
ball.shape("circle")
ball.color("green")
ball.penup()
ball.goto(0,100)
bomb = turtle.Turtle()
bomb.speed(0)
bomb.shape("circle")
bomb.color("red")
bomb.penup()
bomb.goto(100,100)

segments = []
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))

def go_right():
	basket2.direction = "right"
	basket.direction="right"
	basket3.direction="right"

def go_left():
	basket.direction = "left"
	basket2.direction="left"
	basket3.direction="left"

def move():
	f11=ball.ycor()
	f12=bomb.ycor()
	ball.sety(f11-20)
	bomb.sety(f12-20)
	if basket.direction == "left":
		x = basket.xcor()
		x11=basket2.xcor()
		x21=basket3.xcor()
		basket.setx(x - 20)
		basket2.setx(x11 - 20)
		basket3.setx(x21-20)

	if basket.direction == "right":
		x = basket.xcor()
		x12=basket2.xcor()
		x22=basket3.xcor()
		basket.setx(x + 20)
		basket2.setx(x12+20)
		basket3.setx(x22+20)


wn.listen()
#wn.onkeypress(go_up, "Up")
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_left, "Left")

start=1
def music():
	pygame.mixer.music.load("Music.mp3")
	pygame.mixer.music.play()
def hit():
	pygame.mixer.music.load("hit.mp3")
	pygame.mixer.music.play()
def bombped():
	pygame.mixer.music.load("red.mp3")
	pygame.mixer.music.play()

while True:
	wn.update()
	if(start==1):
		music()
		start=0
	def gameover():
		time.sleep(1)
		basket.direction = "stop"
		score =0
		delay = 0.01
		pen.clear()
		pen.write("Score: {} High Score: {}".format(score,high_score), align="center", font= ("Courier", 24, "normal"))

	if basket2.xcor()>290 or basket2.xcor()<-290 or basket3.xcor()>290 or basket3.xcor()<-290:
		arr=[]
		hit()
		reset()
		gameover()
		music()
	if (basket.distance(ball) < 20 or basket2.distance(ball) < 20 or basket3.distance(ball) < 20 or ball.ycor()<-290):
		x = random.randint(-270, 270)
		y = random.randint(-270, 270)
		x1 = random.randint(-270, 270)
		y1 = random.randint(-270, 270)
		ball.goto(x,270)
		bomb.goto(x1,270)
		delay -= 0.001
		score += 10
		if score > high_score:
			high_score = score
		pen.clear()
		pen.write("Score: {} High Score: {}".format(score,high_score), align="center", font= ("Courier", 24, "normal"))
	
	if (basket.distance(bomb) < 20 or basket2.distance(bomb) < 20 or basket3.distance(bomb) < 20 ):
		arr=[]
		reset()
		bombped()
		gameover()
		music()

	move()
	time.sleep(delay)
wn.mainloop()
