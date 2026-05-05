from table_reader import Table, read_table_file

if __name__ == "__main__":
    table = read_table_file("default_table")

    for _ in range(5):
        enc = table.roll()
        print(enc)