import argparse

class Table:
    def __init__(self, name, die, rows):
        self.name = name
        self.die = die
        self.rows = rows

    def roll(self):
        import random
        roll = random.choice(self.rows)
        if isinstance(roll, Table):
            return roll.roll()
        else:
            return roll

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
    
def read_table_file(filename):
    file = open(file=filename)

    header = file.readline()

    # parse header
    die, _, name = header.partition("|")
    die = die.strip()
    name = name.strip()

    # parse rows
    rows = []
    for line in file:
        interval, _, result = line.partition(":")

        begin, _, end = interval.strip().partition("-")
        if end == "":
            rows.append(result.strip())
        else:
            for _ in range(int(begin), int(end)+1):
                rows.append(result.strip())
        
    return Table(name, die, rows)


if __name__ == "__main__":
    paser = argparse.ArgumentParser()
    paser.add_argument("--filename", type=str)

    args = paser.parse_args()

    table = read_table_file(args.filename)
    print(table)