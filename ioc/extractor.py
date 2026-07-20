import re

class IOCExtractor:
    def __init__(self, email_data):
       self.email_data = email_data
    def extract_urls(self):
        urls = []
        body = self.email_data.get("body")
        if body:
            pattern = r"https://[^\s]+"
            urls = re.findall(pattern, body)
        return urls 
    def extract_ips(self):
        ips = []
        body = self.email_data.get("body")
        if body:
            pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
            ips = re.findall(pattern, body)
        return ips
    def extract_suspicious_files(self):

        suspicious = []

        dangerous_extensions = [
            ".exe",
            ".dll",
            ".scr",
            ".bat",
            ".cmd",
            ".vbs",
            ".js"
        ]

        attachments = self.email_data.get("attachments", [])

        for file in attachments:

            if file["extension"].lower() in dangerous_extensions:
                suspicious.append(file["filename"])

        return suspicious