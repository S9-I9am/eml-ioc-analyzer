import re
class DomainExtractor:
    def __init__(self, email_data):
        self.email_data = email_data
        
    
    def extract_domains(self):
        domains = []
        body = self.email_data.get("body", "")
        pattern =  r"\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b"
        domains.extend(re.findall(pattern, body))
        
        return list(set(domains))
            