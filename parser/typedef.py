from abc import ABC, abstractmethod

from random import random

class Rollable(ABC):
    @abstractmethod
    def roll(self):
        pass


class Table(Rollable):
    def __init__(self, die, name, rows):
        self.die = die
        self.name = name
        self.rows = rows

    def roll(self):
        row = random.choice(self.rows)
        return row

    def __str__(self):
        header = f"{self.die} | {self.name}\n"

        rows_str = ""
        start_index = 0
        
        for i in range(len(self.rows)):
            rows = self.rows[i]

            is_last_column = i+1 >= len(self.rows)
            if is_last_column or rows != self.rows[i+1]:
                if start_index - i == 0:
                    rows_str += f"{i+1}: {rows}"
                else:
                    rows_str += f"{start_index+1}-{i+1}: {rows}"
                if not is_last_column:
                    rows_str += "\n"

                start_index = i+1
        
        return header + rows_str