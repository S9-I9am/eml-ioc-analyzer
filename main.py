from parser.eml_parser import EMLParser
from ioc.extractor import IOCExtractor

parser = EMLParser("test_attachment.eml")

resultat = parser.parse()

extractor = IOCExtractor(resultat)

urls = extractor.extract_urls()
ips = extractor.extract_ips()
fichiers_suspects = extractor.extract_suspicious_files()

print(resultat)
print("URLs détectées :", urls)
print("IPs détectées :", ips)
print("Fichiers suspects :", fichiers_suspects)