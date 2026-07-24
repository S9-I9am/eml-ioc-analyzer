import json
import os
from datetime import datetime

class JSONReport:
  def __init__(self, analysis_data, output_dir="reports"):
     self.analysis_data = analysis_data
     self.output_dir = output_dir
  def generate_json(self):
     if not os.path.exists(self.output_dir):
        os.makedirs(self.output_dir)
     timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
     report_filename = f"report_{timestamp}.json"
     filepath = os.path.join(self.output_dir, report_filename)
     with open(filepath, "w", encoding="utf-8") as f:
        json.dump(self.analysis_data, f, indent=4, ensure_ascii=False)
        print(f"[+] Rapport json a été généré avec succès:{filepath}")
     return filepath