import pygame


class Button:
    """
    abstract button class
    """
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.x = y
        self.WIDTH = width
        self.HEIGHT = height
        self.color = color


    def draw(self):
        raise Exception("Not implemented")
    

    def click(self, x, y):
        """
        if user clicked on button
        :param x: float
        :param y: float
        :return: bool
        """