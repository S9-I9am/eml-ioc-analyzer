
import unittest

from src.extractors.domain_extractor import DomainExtractor


class TestDomainExtractor(unittest.TestCase):

    def test_extract_domains(self):
        email_data = {
            "body": """
            Visitez https://secure-login.com/account
            Le serveur utilisé est malware-test.net
            """
        }

        extractor = DomainExtractor(email_data)

        result = extractor.extract_domains()

        self.assertIn("secure-login.com", result)
        self.assertIn("malware-test.net", result)


if __name__ == "__main__":
    unittest.main()