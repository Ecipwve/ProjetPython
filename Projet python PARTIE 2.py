import sys # 
sys.path.append(r"C:\Users\aresv\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages")
import json
import platform
import psutil

class LogProcessor:
    def __init__(self):
        self.logs = []

    def read_json(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
            print("Fichier JSON lu avec succès.")
            return data
        except Exception as e:
            print(f"Erreur lors de la lecture du fichier JSON : {e}")
            return None

    def extract_logs(self, data):
        if data is None:
            print("Aucune donnée à traiter.")
            return

        for hit in data.get('hits', {}).get('hits', []):
            source = hit.get('_source', {})
            log_level = source.get('log', {}).get('level', '').lower()
            if log_level in ['warning', 'error']:
                log_entry = {
                    "log_level": log_level,
                    "message": source.get('message', 'No message'),
                    "station_name": source.get('agent', {}).get('name', 'Unknown station')
                }
                self.logs.append(log_entry)

    def get_logs(self):
        return self.logs

class SystemDiagnostics:
    def __init__(self):
        self.system_info = {}

    def get_os_info(self):
        os_info = platform.system()
        os_version = platform.version()
        self.system_info['os'] = f"{os_info} {os_version}"
    
    def get_cpu_info(self):
        cpu_info = platform.processor()
        cpu_count = psutil.cpu_count(logical=False)
        cpu_freq = psutil.cpu_freq().max
        self.system_info['cpu'] = f"{cpu_info}, Cores: {cpu_count}, Max Frequency: {cpu_freq}MHz"

diag = SystemDiagnostics()
diag.get_os_info()
diag.get_cpu_info()
for key, value in diag.system_info.items():
    print(f"{key}: {value}")
