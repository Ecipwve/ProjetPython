import sys ### INUTILE / POSSIBLE DE SUPPRIMER
sys.path.append(r"C:\Users\aresv\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages") ### INUTILE / POSSIBLE DE SUPPRIMER

import time
from log_processor import LogProcessor
from system_diagnostics import SystemDiagnostics
from excel_exporter import ExcelExporter
from population_utils import recuperer_population  # Module pour l'API population

def display_progress(step, total_steps):
    """Affiche une barre de progression simple"""
    progress = int((step / total_steps) * 100)
    bar = f"[{'#' * (progress // 10)}{'.' * (10 - (progress // 10))}] {progress}%"
    print(bar)

def export_logs_and_diagnostics():
    """Gère l'exportation des logs et diagnostics système vers un fichier Excel"""
    print("Lecture du fichier JSON...")
    file_path = input("Veuillez entrer le chemin du fichier JSON : ")
    processor = LogProcessor()
    data = processor.read_json(file_path)
    display_progress(1, 4)

    print("Extraction des logs...")
    processor.extract_logs(data)
    logs = processor.get_logs()
    display_progress(2, 4)

    print("Collecte des informations système...")
    diagnostics = SystemDiagnostics()
    system_info = diagnostics.collect_all_info()
    display_progress(3, 4)

    base_filename = input("Veuillez entrer le nom du fichier de sortie : ")
    output_filename = f"{base_filename}.xlsx"
    print(f"Exportation des données vers '{output_filename}'...")
    exporter = ExcelExporter(logs, system_info)
    exporter.export_to_excel(output_filename)
    display_progress(4, 4)

    print("\n✅ Les données ont été exportées avec succès")
    print(f"📂 Fichier généré : '{output_filename}'\n")

def get_population_info():
    code = input("Entrez un code de département (ex: 75) ou un code postal (ex: 75001) : ")
    nom, population = recuperer_population(code)

    if nom:
        print(f"🌍 {nom} : {population}\n")
    else:
        print(f"⚠️ {population}\n")

def main():
    """Menu principal interactif."""
    while True:
        print("\n📌 MENU PRINCIPAL")
        print("1️⃣  Exporter les logs et informations système")
        print("2️⃣  Consulter la population d'une ville ou d'un département")
        print("0️⃣  Quitter")

        choix = input("\n👉 Veuillez choisir une option : ")

        if choix == "1":
            export_logs_and_diagnostics()
        elif choix == "2":
            get_population_info()
        elif choix == "0":
            print("👋 Merci d'avoir utilisé le programme. À bientôt !")
            break
        else:
            print("❌ Option invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()
