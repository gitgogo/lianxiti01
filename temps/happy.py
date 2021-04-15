import os


class Plan:
    """test class methods"""
    def __init__(self, time):
        self._time = time

    def get_time(self):
        return self._time


print(os.path.abspath(__file__))
print(Plan.__getattribute__())
