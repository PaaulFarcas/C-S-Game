import socket
import pygame
import os
import pickle

pygame.font.init()

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432  # The port used by the server
WIDTH, HEIGHT = 750, 750
Client_Window = pygame.display.set_mode((WIDTH, HEIGHT))
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))


def main():
    # main code
    main_font = pygame.font.SysFont("comicsans", 50)
    clock = pygame.time.Clock()
    level_label = main_font.render(f"", 1, (255, 255, 255))
    running = True
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    while running:
        #clock.tick(240)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]: # left
            level_label = main_font.render(f"left", 1, (255, 255, 255))
        if keys[pygame.K_d]: # right
            level_label = main_font.render(f"right", 1, (255, 255, 255))
        if keys[pygame.K_w]: # up
            level_label = main_font.render(f"up", 1, (255, 255, 255))
        if keys[pygame.K_s]: # down
            level_label = main_font.render(f"down", 1, (255, 255, 255))
        if keys[pygame.K_SPACE]:
            level_label = main_font.render(f"space", 1, (255, 255, 255))

        message_to_sent = pickle.dumps(keys)
        client_socket.send(message_to_sent)

        Client_Window.blit(BG, (0, 0))
        Client_Window.blit(level_label, (WIDTH/2, 10))
        pygame.display.update()

    client_socket.close()

main()

