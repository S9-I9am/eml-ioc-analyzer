from parser.eml_parser import EMLParser

parser = EMLParser("test_attachment.eml")

resultat = parser.parse()

print(resultat)