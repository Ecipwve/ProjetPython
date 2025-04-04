import sys # 
sys.path.append(r"C:\Users\aresv\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages")
import json
import platform
import psutil
import os
from datetime import datetime

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

    def get_ram_info(self):
        ram = psutil.virtual_memory()
        total_ram = ram.total / (1024 ** 3) # Conversion en GB
        self.system_info['ram'] = f"{total_ram:.2f} GB"

    def get_top_processes(self):
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            processes.append(proc.info)
        processes.sort(key=lambda p: p['cpu_percent'], reverse=True)
        top_processes = processes[:5]
        self.system_info['top_processes'] = top_processes
    
    def get_env_variables(self):
        env_vars = dict(os.environ)
        self.system_info['env_variables'] = env_vars

    def get_disk_partitions(self):
        partitions = psutil.disk_partitions()
        self.system_info['disk_partitions'] = partitions
    
    def get_disk_usage(self):
        usage = []
        for partition in psutil.disk_partitions():
            try:
                usage_info = psutil.disk_usage(partition.mountpoint)
                usage.append({
                    'device': partition.device,
                    'total': usage_info.total,
                    'used': usage_info.used,
                    'free': usage_info.free,
                    'percent':usage_info.percent
                })
            except PermissionError:
                continue
        self.system_info['disk_usage'] = usage

    def get_network_interfaces(self):
        interfaces = list(psutil.net_if_addrs().keys())
        self.system_info['network_interfaces'] = interfaces
    
    def get_boot_time(self):
        boot_time = datetime.fromtimestamp(psutil.boot_time()).strftime("%H:%M:%S")
        self.system_info['boot_time'] = boot_time

diag = SystemDiagnostics()
diag.get_os_info()
diag.get_cpu_info()
diag.get_ram_info()
diag.get_top_processes()
diag.get_env_variables()
diag.get_disk_partitions()
diag.get_disk_usage()
diag.get_network_interfaces()
diag.get_boot_time()
for key, value in diag.system_info.items():
    print(f"{key}: {value}")
