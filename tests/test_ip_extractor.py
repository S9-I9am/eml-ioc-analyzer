import unittest

from src.extractors.ip_extractor import IPExtractor
class TestIPExtractor(unittest.TestCase):
    def test_extract_ips(self):
        email_data = {
            "body": """
            Ce mail contient une IP suspecte :
            192.168.1.50
            et une autre : 
            8.8.8.8
            """
        }
        extractor = IPExtractor(email_data)
        
        result = extractor.extract_ips()
        
        self.assertIn("192.168.1.50", result)
        self.assertIn("8.8.8.8", result)
        
if __name__ == "__main__":unittest.main()      