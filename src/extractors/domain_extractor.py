
import re
class DomainExtractor:

    def __init__(self, email_data):
        self.email_data = email_data


    def extract_domains(self):
        """
        Extrait les noms de domaine présents dans le mail.
        """

        domains = []

        body = self.email_data.get("body", "")

        if body:

            # Capture les domaines classiques :
            # exemple.com
            # secure-login.com
            # malware-test.net
            pattern = r"\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b"

            domains.extend(
                re.findall(pattern, body)
            )


        return list(set(domains))
