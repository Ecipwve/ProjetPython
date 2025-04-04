import psutil
import platform
from datetime import datetime

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

    def collect_all_info(self):
        self.get_os_info()
        self.get_cpu_info()
        self.get_ram_info()
        self.get_top_processes()
        self.get_env_variables()
        self.get_disk_partitions()
        self.get_disk_usage()
        self.get_network_interfaces()
        self.get_boot_time()
        return self.system_info