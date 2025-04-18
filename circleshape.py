import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
    
    def collision(self, circle):
        return self.position.distance_to(circle.position) <= self.radius + circle.radius
        #distance = pygame.math.Vector2.distance_to(self.position, circle.position)
        #if distance <= self.radius + circle.radius:
            #return True

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
