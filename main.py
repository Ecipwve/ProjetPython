import sys ### INUTILE / POSSIBLE DE SUPPRIMER
sys.path.append(r"C:\Users\aresv\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages") ### INUTILE / POSSIBLE DE SUPPRIMER

from log_processor import LogProcessor
from system_diagnostics import SystemDiagnostics
from excel_exporter import ExcelExporter

def main():
    file_path = input("Veuillez entrer le chemin du fichier JSON : ")

    # Process logs
    processor = LogProcessor()
    data = processor.read_json(file_path)
    processor.extract_logs(data)
    logs = processor.get_logs()

    # Collect system diagnostics
    diagnostics = SystemDiagnostics()
    system_info = diagnostics.collect_all_info()

    # Export to Excel
    exporter = ExcelExporter(logs, system_info)
    exporter.export_to_excel('system_logs_and_diagnostics.xlsx')

    print("Les données ont été exportées avec succès dans 'system_logs_and_diagnostics.xlsx'.")

if __name__ == "__main__":
    main()
