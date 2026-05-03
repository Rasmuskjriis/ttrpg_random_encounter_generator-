import unittest
import table_reader

class TestTable(unittest.TestCase):
    def setUp(self):
        self.table = table_reader.Table("Test Table", "d3", ["Zombie", "Zombie", "Skeleton"])
    
    def test_string_method(self):
        result = str(self.table)
        correct = f"d3 | Test Table\n1-2: Zombie\n3: Skeleton"
        assert result == correct

    def test_read_table(self):
        table = table_reader.read_table_file("table")
        assert table.die == "d3"
        assert table.name == "Test Table"
        assert table.rows == ['Zombie', 'Zombie', 'Skeleton']

if __name__ == '__main__':
    unittest.main()