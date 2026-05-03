class Table:
    def __init__(self, name, die, columns):
        self.name = name
        self.die = die
        self.columns = columns

    def roll(self):
        import random
        roll = random.choice(self.columns)
        if isinstance(roll, Table):
            return roll.roll()
        else:
            return roll

    def __str__(self):
        header = f"{self.die} | {self.name}\n"

        columns_str = ""
        start_index = 0
        
        for i in range(len(self.columns)):
            column = self.columns[i]

            is_last_column = i+1 >= len(self.columns)
            if is_last_column or column != self.columns[i+1]:
                if start_index - i == 0:
                    columns_str += f"{i+1}: {column}"
                else:
                    columns_str += f"{start_index+1}-{i+1}: {column}"
                if not is_last_column:
                    columns_str += "\n"

                start_index = i+1
        
        return header + columns_str

if __name__ == "__main__":
    pass