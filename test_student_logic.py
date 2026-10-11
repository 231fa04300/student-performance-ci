import csv
import unittest

from student_logic import predict_performance


class TestStudentLogic(unittest.TestCase):

    def test_high_case(self):
        self.assertEqual(predict_performance(85), "High")

    def test_medium_case(self):
        self.assertEqual(predict_performance(60), "Medium")

    def test_low_case(self):
        self.assertEqual(predict_performance(40), "Low")

    def test_logic_matches_dataset(self):
        with open("student_performance_classification.xls") as f:
            rows = list(csv.DictReader(f))
        self.assertEqual(len(rows), 300)
        for row in rows:
            self.assertEqual(
                predict_performance(float(row["Final_Score"])),
                row["Performance_Class"],
            )


if __name__ == "__main__":
    unittest.main()
