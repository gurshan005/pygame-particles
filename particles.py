"""A small procedural Pygame particle animation."""

import math
import random

import pygame

WIDTH, HEIGHT = 800, 600


class FallingHeart:
    def __init__(self):
        self.reset()

    def reset(self):
        self.x = random.uniform(0, WIDTH)
        self.y = random.uniform(-HEIGHT, 0)
        self.speed = random.uniform(1.2, 3.2)
        self.size = random.randint(8, 14)
        self.phase = random.uniform(0, math.pi * 2)
        self.drift = random.uniform(0.6, 1.4)

    def update(self):
        self.y += self.speed
        self.phase += 0.05 * self.drift
        self.x += math.sin(self.phase) * 0.9
        if self.y > HEIGHT + 30:
            self.reset()

    def draw(self, surf):
        s = self.size
        x, y = int(self.x), int(self.y)
        color = (255, 105, 180)
        pygame.draw.circle(surf, color, (x - s // 2, y - s // 3), s // 2)
        pygame.draw.circle(surf, color, (x + s // 2, y - s // 3), s // 2)
        pygame.draw.polygon(surf, color, [(x - s, y - s // 4), (x + s, y - s // 4), (x, y + s)])


def draw_rose(surf, center):
    x, y = center

    # stem
    pygame.draw.line(surf, (34, 139, 34), (x, y + 70), (x, y + 200), 7)

    # leaves
    pygame.draw.ellipse(surf, (60, 170, 60), (x - 55, y + 120, 70, 28))
    pygame.draw.ellipse(surf, (60, 170, 60), (x - 15, y + 150, 70, 28))

    # petals (layered circles for a cute rose)
    pygame.draw.circle(surf, (180, 0, 60), (x, y), 30)
    pygame.draw.circle(surf, (210, 10, 80), (x - 12, y - 10), 24)
    pygame.draw.circle(surf, (160, 0, 50), (x + 10, y - 8), 22)
    pygame.draw.circle(surf, (230, 40, 110), (x - 2, y - 2), 16)


def main():
    pygame.init()
    try:
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Falling hearts")
        clock = pygame.time.Clock()
        hearts = [FallingHeart() for _ in range(45)]
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (
                    event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
                ):
                    return
            screen.fill((28, 18, 34))
            for heart in hearts:
                heart.update()
                heart.draw(screen)
            draw_rose(screen, (WIDTH // 2, HEIGHT // 2 - 70))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
