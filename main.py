from settings import GAME_NAME, WINDOW_WIDTH, WINDOW_HEIGHT, BASE_PATH, FPS
from Data.asset_library import AssetLibrary
from Data.game_manager import GameManager
import pygame


def main():
    # Define window title
    pygame.display.set_caption(GAME_NAME)

    # Create clock object
    clock = pygame.time.Clock()

    # Create main window object
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), vsync=True)

    # Hold all assets in one object
    assets = AssetLibrary(BASE_PATH)

    # Set window icon
    pygame.display.set_icon(assets.TEST_ASSET)

    # Convert all assets so they are optimized for redrawing with blit
    assets.optimize_all_assets()

    # Init game manager
    game_manager = GameManager(window, assets)

    # Assuming that the asset size is also equivalent to the unit's hitbox
    size = assets.TEST_ASSET.get_width()
    # Create Unit object
    game_manager.spawn_unit(position=(WINDOW_WIDTH / 2 - size / 2,
                                      WINDOW_HEIGHT / 2 - size / 2),
                            size=size, speed=2)

    # Game loop
    while True:
        # Limit fps
        clock.tick(FPS)

        # Handle movement
        game_manager.handle_movement()

        # Handle events
        game_manager.handle_events()

        # Update objects
        game_manager.update_objects()

        # Update on each 'tick'
        pygame.display.update()


if __name__ == "__main__":
    # Initialize pygame
    pygame.init()

    # Run main function
    main()
