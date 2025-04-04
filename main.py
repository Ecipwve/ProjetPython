import sys ### INUTILE / POSSIBLE DE SUPPRIMER
sys.path.append(r"C:\Users\aresv\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages") ### INUTILE / POSSIBLE DE SUPPRIMER

from log_processor import LogProcessor
from system_diagnostics import SystemDiagnostics
from excel_exporter import ExcelExporter
import time 

def display_progress(step, total_steps):
    """Affiche une barre de progression simple."""
    progress = int((step / total_steps) * 100)
    bar = f"[{'#' * (progress // 10)}{'.' * (10 - (progress // 10))}] {progress}%"
    print(bar)

def main():
    print("Bienvenue dans le script de diagnostic système et de traitement des logs !")
    time.sleep(1)  # Petite pause pour l'effet

    # Lecture du fichier JSON
    file_path = input("Veuillez entrer le chemin du fichier JSON : ")
    print("Lecture du fichier JSON...")
    processor = LogProcessor()
    data = processor.read_json(file_path)
    display_progress(1, 4)

    # Extraction des logs
    print("Extraction des logs...")
    processor.extract_logs(data)
    logs = processor.get_logs()
    display_progress(2, 4)

    # Collection des informations systeme
    print("Collecte des informations système...")
    diagnostics = SystemDiagnostics()
    system_info = diagnostics.collect_all_info()
    display_progress(3, 4)

    # Export vers Excel
    base_filename = input("Veuillez entrer le pour le fichier de sortie : ")
    output_filename = f"{base_filename}.xlsx"
    print(f"Exportation des données vers '{output_filename}'...")
    exporter = ExcelExporter(logs, system_info)
    exporter.export_to_excel(output_filename)
    display_progress(4, 4)

    print("\nLes données ont été exportées avec succès")
    print(f"Le fichier Excel a été généré sous le nom : '{output_filename}'.")
    print("Merci d'avoir utilisé notre script")

if __name__ == "__main__":
    main()