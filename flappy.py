import arcade

from models import World, Bird
import pyglet.gl as gl

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 500

class ModelSprite(arcade.Sprite):
	def __init__(self, *args, **kwargs):
		self.model = kwargs.pop('model', None)
		
		super().__init__(*args, **kwargs)

	def sync_with_model(self):
		if self.model:
			self.set_position(self.model.x, self.model.y)

	def draw(self):
		self.sync_with_model()
		super().draw()

class FlappyBirdWindow(arcade.Window):
	def __init__(self, width, height):
		super().__init__(width, height)

		arcade.set_background_color(arcade.color.BRICK_RED)

		self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT)

		self.bird_sprite = ModelSprite('images/MomBird.png', model=self.world.bird)

	def animate(self, delta):
		self.world.animate(delta)

	def draw_walls(self):
		walls = self.world.walls
		for w in walls:
			arcade.draw_rectangle_filled(w.x + w.width/2 , w.y - w.height/2,
							             w.width, w.height,
										 arcade.color.SPANISH_GRAY)

	def on_draw(self):
		arcade.set_viewport(self.world.bird.x - SCREEN_WIDTH/2,
						    self.world.bird.x + SCREEN_WIDTH/2,
							0,SCREEN_HEIGHT)

		arcade.start_render()
		self.draw_walls()

		self.bird_sprite.draw()

		if not self.world.bird.is_touch:
			arcade.draw_text("Score:"+str(self.world.score), self.world.bird.x + (SCREEN_WIDTH // 2) - 890, self.height -30, arcade.color.BLACK, 20)

		else:
			arcade.draw_text("YOUR TOTAL Score : "+str(self.world.score), self.world.bird.x + (SCREEN_WIDTH // 2) - 680, self.height -100, arcade.color.BLACK, 30)
			arcade.draw_text(">>GameOver<<", self.world.bird.x + (SCREEN_WIDTH // 2) - 800, self.height -300, arcade.color.BLACK, 60)


		gl.glDisable(gl.GL_TEXTURE_2D)
	
	def on_key_press(self, key, key_modifiers):
		self.world.on_key_press(key, key_modifiers)



if __name__ == '__main__':
	window = FlappyBirdWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
	arcade.set_window(window)
	arcade.run()
