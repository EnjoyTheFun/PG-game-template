import pygame

class Player:
    def __init__(self):
        self.score = 0
        
    def score_exceeds(self, amount, event):
        if self.score >= amount:
            pygame.event.post(event)
            amount += 1
        return amount
