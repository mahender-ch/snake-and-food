import pygame as p
import time
import random
p.init()
width=500
height=500
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
snake=10
dis=p.display.set_mode((width,height))
p.display.set_caption('eat more to score more')
def snake_length(snake_list):
	for x in snake_list:
		p.draw.rect(dis,black,[x[0],x[1],snake,snake])

def game():	
	game_over=False
	game_close=False
	x_move=y_move=0
	x=y=width//2 #snake starting point
	foodx=round(random.randrange(0,width-snake)/10.0)*10.0
	foody=round(random.randrange(0,height-snake)/10.0)*10.0
	score=0
	snake_list=[]
	while not game_over:
		while game_close:
			dis.fill(white)
			font=p.font.SysFont(None,30)
			score_str='you lost ---SCORE: '+str(score)
			msg_s=font.render(score_str,True,red)
			dis.blit(msg_s,[width/3,height/3])	
			msg_s=font.render("press c to continue",True,red)
			dis.blit(msg_s,[width/3,height/3+40])	
			msg_s=font.render("press q to continue",True,red)
			dis.blit(msg_s,[width/3,height/3+80])			
			p.display.update()

			for event in p.event.get():
				if event.type ==p.KEYDOWN:
					if event.key==p.K_q:
						game_over=True
						game_close=False
					if event.key== p.K_c:
						game()
					if event.type==p.QUIT:
						game_over=True	

		for event in p.event.get():
			if event.type==p.QUIT:
				game_over=True
			if event.type==p.KEYDOWN:
				if event.key == p.K_LEFT:
					x_move=-snake
					y_move=0
				if event.key == p.K_RIGHT:
					x_move=snake
					y_move=0
				if event.key == p.K_UP:
					x_move=0
					y_move=-snake
				if event.key == p.K_DOWN:
					x_move=0
					y_move=snake
			#print(x,y)

		x=(x+x_move)%width
		y=(y+y_move)%height
		
		dis.fill(white)
		p.draw.rect(dis,black,[x,y,snake,snake])
		p.draw.rect(dis,red,[foodx,foody,snake,snake])
		
		snake_head=[]
		snake_head.append(x)
		snake_head.append(y)
		snake_list.append(snake_head)
		if len(snake_list) >score+1:
			del snake_list[0]
		for t in snake_list[:-1]:
			if t==snake_head:
				game_close=True
		snake_length(snake_list)

		font=p.font.SysFont(None,30)
		score_str='SCORE: '+str(score)
		msg_s=font.render(score_str,True,red)
		dis.blit(msg_s,[0,0])
		p.display.update()
		
		if x==foodx and y==foody:
			print("ate")
			score=score+1
			foodx=round(random.randrange(0,width-snake)/10.0)*10.0
			foody=round(random.randrange(0,height-snake)/10.0)*10.0
		time.sleep(0.05)
	p.quit()
	quit()
game()