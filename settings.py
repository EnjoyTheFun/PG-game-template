import json
import pygame

# open file for reading
with open("settings.json", "r") as file:
    # attempt to load json data in a python dictionary
    json_dict = json.load(file)

    # define data as constants
    # (technically you can call them directly from a dict but i believe this is cleaner)
    GAME_NAME = json_dict["game_name"]
    FPS = json_dict["fps"]
    WINDOW_WIDTH = json_dict["window_width"]
    WINDOW_HEIGHT = json_dict["window_height"]
    BASE_PATH = json_dict["base_path"]

CUSTOM_EVENT = pygame.USEREVENT + 1
