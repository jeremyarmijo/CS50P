from classes import Apple, Snake
import pygame
import macro
import sys

pygame.init()
FONT = pygame.font.Font("font.ttf", macro.BLOCK_SIZE * 2)

def drawGrid(screen):
    for x in range(0, macro.WIDTH, macro.BLOCK_SIZE):
        for y in range(0, macro.HEIGHT, macro.BLOCK_SIZE):
            rect = pygame.Rect(x, y, macro.BLOCK_SIZE, macro.BLOCK_SIZE)
            pygame.draw.rect(screen, "#3c3c3b", rect, 1)

def check_moves(event, snake):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN and snake.dir != macro.UP:
            snake.dir = macro.DOWN
        elif event.key == pygame.K_UP and snake.dir != macro.DOWN:
            snake.dir = macro.UP
        elif event.key == pygame.K_RIGHT and snake.dir != macro.LEFT:
            snake.dir = macro.RIGHT
        elif event.key == pygame.K_LEFT and snake.dir != macro.RIGHT:
            snake.dir = macro.LEFT

def exit_window(snake):
    for event in pygame.event.get():
        check_moves(event, snake)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def display_on_window(screen, apple, snake):
    pygame.draw.rect(screen, "red", apple.rectangle)
    pygame.draw.rect(screen, "green", snake.head)
    for square in snake.body:
        pygame.draw.rect(screen, "green", square)
    pygame.display.update()

def main():
    screen = pygame.display.set_mode((800, 800))
    clock = pygame.time.Clock()
    score = FONT.render("1", True, "white")
    snake = Snake()
    apple = Apple(snake.body)
    pygame.display.set_caption("Snake!")
    while True:
        exit_window(snake)
        screen.fill('black')
        drawGrid(screen)
        score = FONT.render(f"{len(snake.body) + 1}", True, "white")
        screen.blit(score, score.get_rect(center=(macro.WIDTH / 2, macro.HEIGHT / 20)))
        snake = snake.snake_dead()
        apple = snake.update_snake(apple)
        display_on_window(screen, apple, snake)
        clock.tick(5)

if __name__ == "__main__":
    main()