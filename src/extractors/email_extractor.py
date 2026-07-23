import re
class EmailExtractor:
    def __init__(self, email_data):
        self.email_data = email_data
        
    def extract_emails(self):
        body = self.email_data.get("body", "")
        if not body:
            return []
        
        email_pattenr = r'[a-zA-Z0-9._%+]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        
        email = re.findall(email_pattern,body)
        
        return list(set(emails))

    