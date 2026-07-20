import re
class IOCExtractor:
    def __init__(self, email_data):
        self.email_data = email_data
        
    def extract_urls(self):
        urls = []
        body = self.email_data.get("body")
        if body:
            pattern = r"https?://[^\s]+"
            urls = re.findall(pattern, body)
        return urls        
        