from parser.eml_parser import EMLParser
from ioc.extractor import IOCExtractor

parser = EMLParser("test_attachment.eml")

resultat = parser.parse()

extractor = IOCExtractor(resultat)

urls = extractor.extract_urls()

print(resultat)
print(urls)