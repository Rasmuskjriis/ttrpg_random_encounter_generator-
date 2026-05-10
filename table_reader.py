from abc import abstractmethod, ABC
import random

import argparse
    
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
    
    file.close()
        
    return Table(name, die, rows)


if __name__ == "__main__":
    paser = argparse.ArgumentParser()
    paser.add_argument("--filename", type=str)

    args = paser.parse_args()

    table = read_table_file(args.filename)
    print(table)