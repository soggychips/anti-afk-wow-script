from pyautogui import keyDown, keyUp
from time import sleep
from random import random, seed, choice

moves = ['w', 'a', 's', 'd']


def rand_sleep(a=5, b=60):
    seed()
    sleep_time = a + (random() * (b - a))
    sleep(sleep_time)


def rand_move():
    seed()
    move = choice(moves)
    keyDown(move)
    rand_sleep(0, 2)
    keyUp(move)


if __name__ == '__main__':
    while True:
        rand_move()
        rand_sleep(1, 5)
        rand_move()
        rand_sleep()
