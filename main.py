import pygame
import random

pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Babi's Birthday")

# Colors
WHITE = (255, 255, 255)
GREEN = (34, 177, 76)
BLACK = (0, 0, 0)

# FPS and clock
FPS = 60
clock = pygame.time.Clock()

# Load frog image
frog_img = pygame.image.load("assets/frog.png")  # You can use any frog image you like
frog_rect = frog_img.get_rect()
frog_rect.x = SCREEN_WIDTH // 2
frog_rect.y = SCREEN_HEIGHT - 100

# Load cake image
cake_img = pygame.image.load("assets/cake.png")  # You can use any cake image you like
cake_img = pygame.transform.scale(cake_img, (100, 100))
cake_rect = cake_img.get_rect()
cake_rect.x = SCREEN_WIDTH // 2 - 50
cake_rect.y = SCREEN_HEIGHT // 2 - 50

# Function to change frog image and maintain size
def change_frog_image(new_image_path):
    global frog_img, frog_rect
    new_frog_img = pygame.image.load(new_image_path)
    new_frog_img = pygame.transform.scale(new_frog_img, (frog_rect.width, frog_rect.height))
    frog_img = new_frog_img

# Load flower images
flower_images = [pygame.transform.scale(pygame.image.load(f"assets/{i}.png"), (60, 60)) for i in range(1, 4)]

# Frog attributes
frog_speed = 5
frog_jump = 30
is_jumping = False
jump_count = frog_jump

# Collectibles (flies, flowers)
items = []
item_size = 30
score = 0

# Create a font for score
font = pygame.font.SysFont(None, 30)

# Function to display score
def show_score():
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

# Function to display a message
def show_message(message):
    message_text = font.render(message, True, BLACK)
    text_rect = message_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(message_text, text_rect)

# Function to draw the frog
def draw_frog():
    screen.blit(frog_img, frog_rect)

# Function to create items (flowers)
def create_item():
    item = pygame.Rect(random.randint(50, SCREEN_WIDTH - 50), random.randint(50, SCREEN_HEIGHT - 200), item_size, item_size)
    flower_img = random.choice(flower_images)
    items.append((item, flower_img))

# Function to draw the cake and frog together
def draw_cake_and_frog():
    screen.blit(cake_img, cake_rect)
    frog_rect.x = cake_rect.x + cake_rect.width + 10
    frog_rect.y = cake_rect.y
    draw_frog()

# Confetti attributes
confetti = []
confetti_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

# Function to create confetti particles
def create_confetti():
    for _ in range(100):
        x = random.randint(0, SCREEN_WIDTH)
        y = random.randint(-SCREEN_HEIGHT, 0)
        size = random.randint(2, 5)
        color = random.choice(confetti_colors)
        speed = random.randint(1, 3)
        confetti.append([x, y, size, color, speed])

# Function to draw confetti particles
def draw_confetti():
    for particle in confetti:
        pygame.draw.rect(screen, particle[3], (particle[0], particle[1], particle[2], particle[2]))
        particle[1] += particle[4]
        if particle[1] > SCREEN_HEIGHT:
            particle[1] = random.randint(-SCREEN_HEIGHT, 0)
            particle[0] = random.randint(0, SCREEN_WIDTH)

# Main game loop
def game_loop():
    global score, frog_rect, is_jumping, jump_count, frog_img

    running = True
    create_confetti()
    while running:
        screen.fill(WHITE)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Key controls
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_e]:
            change_frog_image("assets/bb1.jpg")  # Change frog sprite and maintain size

        if keys[pygame.K_a]:
            frog_rect.x -= frog_speed
        if keys[pygame.K_d]:
            frog_rect.x += frog_speed
        if not is_jumping:
            if keys[pygame.K_SPACE]:
                is_jumping = True

        # Jumping logic
        if is_jumping:
            frog_rect.y -= jump_count
            jump_count -= 1
            if jump_count < -frog_jump:
                is_jumping = False
                jump_count = frog_jump

        # Spawn collectibles every 2 seconds
        if random.randint(1, 60) == 1:
            create_item()

        # Check for collision with items (collect them)
        for item, flower_img in items:
            if frog_rect.colliderect(item):
                items.remove((item, flower_img))
                score += 1

        # Draw items on screen
        for item, flower_img in items:
            screen.blit(flower_img, item.topleft)

        # Draw the frog or cake and frog together if score reaches 60
        if score < 60:
            draw_frog()
        else:
            draw_cake_and_frog()
            draw_confetti()

        # Display score
        show_score()

        # Display message when score reaches certain values
        if 10 <= score < 15:
            show_message("Happy Birthday babi!")
        
        if 15 <= score < 20:
            show_message("I love you bb.")

        if 20 <= score < 25:
            show_message("I reallay really love you babi.")

        if 25 <= score < 30:
            show_message("You are the best thing ever happened to me.")

        if 30 <= score < 35:
            show_message("You are my everything.")

        if 35 <= score < 40:            
            show_message("You are my favorite person in the world.")
        
        if 40 <= score < 45:
            show_message("I hope I can make you the happiest person in the world.")

        if 45 <= score < 50:
            show_message("I will try to give you your best birthday ever.")

        if 50 <= score < 55:
            show_message("I want you to look forward to your birthday every year.")

        # Update the screen
        pygame.display.update()

        # Set the frame rate
        clock.tick(FPS)

    pygame.quit()

# Run the game loop
game_loop()
