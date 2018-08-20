# Imports
import serial, pygame, time
from pygame.locals import *
from enum import Enum

class CommandTypes(Enum):
    STOP = 0
    FORWARD = 1
    BACKWARD = 2
    LEFT = 3
    RIGHT = 4
    FORWARD_LEFT = 13
    FORWARD_RIGHT = 14
    BACKWARD_LEFT = 23
    BACKWARD_RIGHT = 24

class CommandStore:
    def __init__(self):
        self.should_continue = True
        self.previous_command = -1
        self.command = CommandTypes.STOP

def get_pygame_command(command_store):
    for event in pygame.event.get():
            # Press key on keyboard down
            if (event.type == KEYDOWN):
                keyinput = pygame.key.get_pressed()

                # 2D Commands
                if keyinput[pygame.K_UP] and keyinput[pygame.K_LEFT]:
                    command_store.command = CommandTypes.FORWARD_LEFT
                elif keyinput[pygame.K_UP] and keyinput[pygame.K_RIGHT]:
                    command_store.command = CommandTypes.FORWARD_RIGHT
                elif keyinput[pygame.K_DOWN] and keyinput[pygame.K_LEFT]:
                    command_store.command = CommandTypes.BACKWARD_LEFT
                elif keyinput[pygame.K_DOWN] and keyinput[pygame.K_RIGHT]:
                    command_store.command = CommandTypes.BACKWARD_RIGHT

                # 1D Commands
                elif keyinput[pygame.K_UP]:
                    command_store.command = CommandTypes.FORWARD
                elif keyinput[pygame.K_DOWN]:
                    command_store.command = CommandTypes.BACKWARD
                elif keyinput[pygame.K_LEFT]:
                    command_store.command = CommandTypes.LEFT
                elif keyinput[pygame.K_RIGHT]:
                    command_store.command = CommandTypes.RIGHT

                # Exit
                elif keyinput[pygame.K_q]:
                    command_store.should_continue = False
                    command_store.command = CommandTypes.STOP
            
            # Let go of keyboard key press
            elif event.type == pygame.KEYUP:

                # Single key
                if (command_store.command == CommandTypes.FORWARD
                or command_store.command == CommandTypes.BACKWARD
                or command_store.command == CommandTypes.LEFT
                or command_store.command == CommandTypes.RIGHT):
                    command_store.command = CommandTypes.STOP

                # `FORWARD_LEFT`
                elif command_store.command == CommandTypes.FORWARD_LEFT:
                    if event.key == pygame.K_LEFT:
                        command_store.command = CommandTypes.FORWARD
                    elif event.key == pygame.K_UP:
                        command_store.command = CommandTypes.LEFT

                # `FORWARD_RIGHT`
                elif command_store.command == CommandTypes.FORWARD_RIGHT:
                    if event.key == pygame.K_RIGHT:
                        command_store.command = CommandTypes.FORWARD
                    elif event.key == pygame.K_UP:
                        command_store.command = CommandTypes.RIGHT

                # `BACKWARD_LEFT`
                elif command_store.command == CommandTypes.BACKWARD_LEFT:
                    if event.key == pygame.K_LEFT:
                        command_store.command = CommandTypes.BACKWARD
                    elif event.key == pygame.K_DOWN:
                        command_store.command = CommandTypes.LEFT

                # `BACKWARD_RIGHT`
                elif command_store.command == CommandTypes.BACKWARD_RIGHT:
                    if event.key == pygame.K_RIGHT:
                        command_store.command = CommandTypes.BACKWARD
                    elif event.key == pygame.K_DOWN:
                        command_store.command = CommandTypes.RIGHT
                    
    return command_store.command

def setup_pygame():
    (width, height) = (300, 300)
    pygame.display.set_mode((width, height))
    pygame.init()

def send_command_arduino():
    setup_pygame()

    # Establish the connection
    arduino = serial.Serial('/dev/cu.usbmodem1461', 9600, timeout = 1)
    time.sleep(1)

    command_store = CommandStore()
    
    while command_store.should_continue:
        get_pygame_command(command_store)
        
        # Avoid sending an already existing command order
        if (command_store.command != command_store.previous_command):
            command_store.previous_command = command_store.command
            # TODO: See if I can remove the `+ 48` here and the `- 48` in the Arduino code
            byte_command = chr(command_store.command.value + 48).encode()
            arduino.write(byte_command)

    arduino.close()

if __name__ == "__main__":
    send_command_arduino()
