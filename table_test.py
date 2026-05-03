import unittest
import table_reader

class TestTable(unittest.TestCase):
    def test_string_method(self):
        table = table_reader.Table("Test Table", "d3", ["Zombie", "Zombie", "Skeleton"])
        result = str(table)
        correct = f"d3 | Test Table\n1-2: Zombie\n3: Skeleton"
        print(result)
        print(correct)
        assert result == correct

if __name__ == '__main__':
    unittest.main()