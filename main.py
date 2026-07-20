from parser.eml_parser import EMLParser

parser = EMLParser("test_mail.eml")

resultat = parser.parse()

print(resultat)