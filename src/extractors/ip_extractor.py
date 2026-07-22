import re

class IPExtractor:
    def __init__(self, email_data):
        self.email_data = email_data

    def extract_ips(self):
        ips = []
        body = self.email_data.get("body", "")
        
        pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
        ips.extend(re.findall(pattern, body))
        
        return list(set(ips))    