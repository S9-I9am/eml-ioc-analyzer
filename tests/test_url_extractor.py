import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.extractors.url_extractor import URLExtractor


email_data = {
    "body": """
    Bonjour,

    Consultez :
    https://google.com
    http://test.com/page
    ftp://files.example.org
    """
}

extractor = URLExtractor(email_data)

print(extractor.extract_urls())