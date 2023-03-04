from settings import GAME_NAME, WINDOW_WIDTH, WINDOW_HEIGHT, BASE_PATH, FPS
from Source.asset_library import AssetLibrary
from Source.game_manager import GameManager
from Source.ui_manager import UIManager
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

    # Init UI manager
    ui_manager = UIManager(window)

    # Get size.
    # Assuming that the asset size is also equivalent to the unit's hitbox
    size = assets.TEST_ASSET.get_width()

    # Create controllable Unit object
    game_manager.spawn_player_unit(position=(WINDOW_WIDTH / 2 - size / 2,
                                             WINDOW_HEIGHT / 2 - size / 2),
                                   size=size, speed=2)

    # Create first goal unit
    game_manager.spawn_goal_unit()

    # Game loop
    while True:
        # Limit fps
        clock.tick(FPS)

        # Handle movement
        game_manager.handle_movement()

        # Check for collisoin
        game_manager.unit_collide()

        # Handle events
        game_manager.handle_events()

        # Draw all objects
        game_manager.draw_objects()

        # Display score
        ui_manager.display_score(game_manager.player.score)

        # Update on each 'tick'
        pygame.display.update()


if __name__ == "__main__":
    # Initialize pygame
    pygame.init()

    # Run main function
    main()
