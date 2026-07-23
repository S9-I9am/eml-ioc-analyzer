#Importation des resultats des scripts crée auparavant 
from .url_extractor import extracts_urls 
from .domain_extrator import extract_domain
from .email_extractor import extract_emails 
from .ip_extractor import extract_ips
from .hash_extractor import calculates_hashes
def extract_all
 #Rassemble tt les iocs extraits 
   return{
    "urls": extract_urls
    "domain": extract_domain
    "email":extract_emails
    "ip": extract_ips
    "hashes":calculates_hashes
   }
