import pygame
from settings import WINDOW_WIDTH

class UIManager():
    """Class that manages all UI elements and interactions"""
    
    def __init__(self, surface):
        self.surface = surface
        self.font = pygame.font.SysFont("Arial", 20)
        
    def display_score(self, score):
        "Blit text on the main surface repesenting the current score."
        text = self.font.render(str(score), True, pygame.Color("white"))
        # center the text_rect so text remains centered no matter the length
        text_rect = text.get_rect(center=(WINDOW_WIDTH/2, 10))
        # draw text inside text_rect over the main surface
        self.surface.blit(text, text_rect)