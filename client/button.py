import pygame


class Button:
    """
    abstract button class
    """
    def __init__(self, x, y, width, height, color, bordercolor=(0, 0, 0)):
        self.x = x
        self.x = y
        self.WIDTH = width
        self.HEIGHT = height
        self.color = color
        self.bordercolor = bordercolor
        self.BORDERWIDTH = 2


    def draw(self):
        raise Exception("Not implemented")
    

    def click(self, x, y):
        """
        if user clicked on button
        :param x: float
        :param y: float
        :return: bool
        """

        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True # user clicked button

        return False
    

class TectButton():
    def __init__(self, x, y, width, height, color, text, bordercolor=(0, 0, 0))
        super().__init__(x, y, width, height, color, bordercolor)
        self.text = text


    def draw(self, win):
        pygame.rect.draw(win, self.color, (self.x + self.BORDERWIDTH, self.y + self.BORDERWIDTH,self.width - self.BORDERWIDTH*2, self.height - self.BORDERWIDTH* 2), 0)
        pygame.rect.draw(win, self.color, (self.x, self.y, self.width, self.height), 0)


class TextButton(Button):
    def draw(self, win):
        pass
