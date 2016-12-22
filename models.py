import arcade.key

from random import randint

GRAVITY = -2
MAX_VX = 3
ACCX = 1
JUMP_VY = 13
class Model:
	def __init__(self, world, x, y, angle):
		self.world = world
		self.x = x
		self.y = y
		self.angle = 0

class Bird(Model):
	def __init__(self, world, x, y, base_y):
		super().__init__(world, x, y, 0)
		self.vx = 0
		self.vy = 0

		self.is_jump = False
		self.is_touch =False

		self.base_y = base_y

	def jump(self):
		if not self.is_jump:
			self.is_jump = True
			self.vy = JUMP_VY
			self.count = 0

	def touch(self):
		walls = self.world.walls
		for w in walls:
			if self.x >=  w.x and self.x <= w.x+w.width:
				if self.y >= w.y-w.height and self.y <= w.y:
					self.is_touch = True
					
		
		

	def animate(self, delta):

		if self.vx < MAX_VX:
			self.vx += ACCX
			

#	if self.x >= self.world.width:
#			self.x = 0
		self.touch()
		if self.is_touch == True:
			self.y -= 10

		self.x += self.vx
		self.y += -1

		if self.is_jump:
			self.y += self.vy
			self.vy = self.vy + GRAVITY
			self.count += 1

			if self.count == 10:
				self.vy =0
				self.is_jump = False

class Walls:
	def __init__(self, world, x, y, width, height):
		self.world = world
		self.x = x
		self.y = y
		self.width = width
		self.height = height
        

class World:
	def __init__(self, width, height):
		self.width = width
		self.height = height

		self.bird = Bird(self, -100 ,300, 0)

		self.walls =[]
		init = 100
			
		for i in range(1,100):
			self.walls.append(Walls(self, init, 900, 50, randint(500,600)))
			self.walls.append(Walls(self, init, randint(180,280), 50,600))
			init += 130
		

#self.walls.append(Walls(self, 0, 150, 50, 400))

#
#		self.walls.append(Walls(self, 100, 900, 50, 500))
#		self.walls.append(Walls(self, 100, 150, 50, 600))
#
#self.walls.append(Walls(self, 250, 900, 50, 600))
#		self.walls.append(Walls(self, 250, 150, 50, 400))
#
#		self.walls.append(Walls(self, 400, 900, 50, 600))
#		self.walls.append(Walls(self, 400, 150, 50, 400))

		
	def animate(self, delta):
		self.bird.animate(delta)
	
	def on_key_press(self, key, key_modifiers):
		if key == arcade.key.SPACE:
			self.bird.jump()

