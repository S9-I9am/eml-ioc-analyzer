import re
from urllib.parse import urlparse
class DomainExtractor:
    def __init__(self, email_data):
        self.email_data = email_data
        
    
    def extract_domains(self):
        domains = []
        body = self.email_data.get("body", "")
        
        url_pattern = r"(?:https?|ftp)://[^\s<>\"']+"
        urls = re.findall(url_pattern, body)

        for url in urls:
            domain = urlparse(url).netloc
            if domain:
                domains.append(domain)
        
        
        domain_pattern =  r"\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b"
        domains.extend(re.findall(domain_pattern, body))
        
        return list(set(domains))
            