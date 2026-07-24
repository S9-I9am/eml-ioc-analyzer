import os
import unittest

from src.reports.csv_report import CSVReport


class TestCSVReport(unittest.TestCase):

    def test_generate_csv(self):

        results = [
            {
                "filename": "test.eml",
                "urls": ["https://google.com"],
                "ips": ["8.8.8.8"],
                "domains": ["google.com"]
            }
        ]

        report = CSVReport("test_report.csv")

        report.generate(results)

        self.assertTrue(
            os.path.exists("test_report.csv")
        )

        self.assertGreater(
            os.path.getsize("test_report.csv"),
            0
        )

        os.remove("test_report.csv")


if __name__ == "__main__":
    unittest.main()