import pygame 
from settings import *
from tile import Tile
from player import Player
from debug import debug
from support import *
from random import choice
from weapon import Weapon

class Level:
	# Initialize level 
	def __init__(self):

		# get the display surface 
		self.display_surface = pygame.display.get_surface()

		# sprite group setup
		self.visible_sprites = YSortCameraGroup()
		self.obstacle_sprites = pygame.sprite.Group()

		# attack sprites
		self.current_weapon = None

		# sprite setup
		self.create_map()

	# import map and sprite data
	def create_map(self):
		layouts = {
			'boundary': import_csv_layout('../mapdata/map_Boundary.csv'),
			'grass': import_csv_layout('../mapdata/map_Grass.csv'),
			'object': import_csv_layout('../mapdata/map_Objects.csv')
		}
		graphics = {
			'grass': import_folder('../graphics/grass'),
			'object': import_folder('../graphics/objects')
		}
		for style,layout in layouts.items():
			for row_index,row in enumerate(layout):
				for col_index, col in enumerate(row):
					if col != '-1':
						x = col_index * TILESIZE
						y = row_index * TILESIZE
						if style == 'boundary':
							Tile((x,y),[self.obstacle_sprites],'invisible')
						if style == 'grass':
							random_grass_image = choice(graphics['grass'])
							Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'grass',random_grass_image)
						if style == 'object':
							object_image = graphics['object'][int(col)]
							Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'object',object_image)
		self.player = Player((2000,1430),[self.visible_sprites],self.obstacle_sprites,self.create_weapon,self.destroy_weapon)

	# Creating weapon on the surface
	def create_weapon(self):
		self.current_weapon = Weapon(self.player,[self.visible_sprites])

	# Removing weapon from the surface
	def destroy_weapon(self):
		if self.current_weapon:
			self.current_weapon.kill()
		self.current_weapon = None

	# Updating class information given by custom_draw
	def run(self):
		# update and draw the game
		self.visible_sprites.custom_draw(self.player)
		self.visible_sprites.update()
		# debug(len(list(weapon_data.keys())))


class YSortCameraGroup(pygame.sprite.Group):
	# Initialize YSortCameraGroup
	def __init__(self):

		# general setup 
		super().__init__()
		self.display_surface = pygame.display.get_surface()
		self.half_width = self.display_surface.get_size()[0] // 2
		self.half_height = self.display_surface.get_size()[1] // 2
		self.offset = pygame.math.Vector2()

		# creating the floor
		self.floor_ground = pygame.image.load('../graphics/tilemap/ground.png').convert()
		self.floor_rect = self.floor_ground.get_rect(topleft = (0,0))

	# getting offset for images
	def custom_draw(self,player):

		# getting the offset 
		self.offset.x = player.rect.centerx - self.half_width
		self.offset.y = player.rect.centery - self.half_height

		# drawing the floor
		floor_offset_pos = self.floor_rect.topleft - self.offset
		self.display_surface.blit(self.floor_ground,floor_offset_pos)

		# sorting sprites by lambda function to get a overlap in the y-dimension
		for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
			offset_pos = sprite.rect.topleft - self.offset
			self.display_surface.blit(sprite.image,offset_pos)
