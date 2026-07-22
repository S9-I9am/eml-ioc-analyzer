import unittest

from src.extractors.domain_extractor import DomainExtractor


class TestDomainExtractor(unittest.TestCase):

    def test_extract_domains(self):
        email_data = {
            "body": """
            Visitez https://securelogin.com
            Le serveur utilisé est malwaretest.net
            """
        }

        extractor = DomainExtractor(email_data)

        result = extractor.extract_domains()

        self.assertIn("securelogin.com", result)
        self.assertIn("malwaretest.net", result)


if __name__ == "__main__":
    unittest.main()