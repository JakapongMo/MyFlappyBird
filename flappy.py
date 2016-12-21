import arcade

from models import World, Bird

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

	def on_draw(self):
		arcade.start_render()

		self.bird_sprite.draw()
	
	def on_key_press(self, key, key_modifiers):
		self.world.on_key_press(key, key_modifiers)

if __name__ == '__main__':
	window = FlappyBirdWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
	arcade.run()
