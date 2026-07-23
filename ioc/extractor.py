from src.extractors.url_extractor import URLExtractor
from src.extractors.ip_extractor import IPExtractor
from src.extractors.domain_extractor import DomainExtractor
from src.extractors.email_extractor import EmailExtractor
from src.extractors.hash_extractor import HashExtractor


class IOCExtractor:

    def __init__(self, email_data):
        self.email_data = email_data


    def extract_all(self):
        """
        Lance tous les extracteurs IOC
        et retourne les résultats.
        """

        results = {

            "urls": URLExtractor(
                self.email_data
            ).extract_urls(),


            "ips": IPExtractor(
                self.email_data
            ).extract_ips(),


            "domains": DomainExtractor(
                self.email_data
            ).extract_domains(),


            "emails": EmailExtractor(
                self.email_data
            ).extract_emails(),


            "hashes": HashExtractor(
                self.email_data.get("attachments", [])
            ).extract_hashes()

        }


        return results