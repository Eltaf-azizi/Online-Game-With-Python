class Person:
    """
    Pepresents a person, holds name, socket client and IP address
    """
    def __init__(self, addr, client):
        self.addr = addr
        self.client = client
        self.name = None


def set_name(self, name):
    """
    set the person's name
    :param name: str
    :return: None
    """
    self.name = name


    def __repr__(self):
        return f"Person ({self.addr}, {self.name})"