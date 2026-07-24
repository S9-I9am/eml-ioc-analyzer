from src.reports.json_report import  JSONReport
donnes_test= {
    "mail":"test_pishing.eml",
    "verdict": "SUSPECT",
    "iocs": {
       "emails": ["pirate@phishing.com"],
       "urls": ["http://site-piege.com"],
       "hashes":[]
    }
}
print("[*]Lancement du test de géneration JSON...")
rapporteur = JSONReport(donnes_test)
chemin_fichier =rapporteur.generate_json()
print(f"[+] Test terminé. Veuillez vérifier si le fichier existe.")