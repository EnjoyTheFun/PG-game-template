import json

with open("settings.json", "r") as f:
    json_dict = json.load(f)
    GAME_NAME = json_dict["game_name"]
    FPS = json_dict["fps"]
    WINDOW_WIDTH = json_dict["window_width"]
    WINDOW_HEIGHT = json_dict["window_height"]
    BASE_PATH = json_dict["base_path"]
