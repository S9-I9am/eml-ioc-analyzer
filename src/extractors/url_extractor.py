import re
class URLExtractor:
    def __init__(self, email_data):
        self.email_data = email_data

    def extract_urls(self):
        urls = []
        
        body = self.email_data.get("body", "")
        
        pattern = r"(?:https?|ftp)://[^\s<>\"']+"
        
        urls.extend(re.findall(pattern, body))
        
        return list(set(urls))