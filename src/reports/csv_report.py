import csv

class CSVReport:
    def __init__(self, output_file="rpport.csv"):
        self.output_file = output_file
        
    def generate(self, results):
        with open(
            self.output_file,
            mode="w",
            newline="",
            encoding="utf-8"
        ) as csvfile:
            
            
            writer = csv.writer(csvfile) 
            # En-tête
            writer.writerow(
                ["Fichier", "Type", "Valeur"]
            )
            
             # Parcours des résultats
            for result in results:

                filename = result["filename"]
                
                # URLs
                for url in result.get("urls", []):
                    writer.writerow(
                        [filename, "URL", url]
                    )

                # IPs
                for ip in result.get("ips", []):
                    writer.writerow(
                        [filename, "IP", ip]
                    )

                # Domaines
                for domain in result.get("domains", []):
                    writer.writerow(
                        [filename, "DOMAIN", domain]
                    )