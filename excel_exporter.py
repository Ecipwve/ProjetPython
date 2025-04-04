import pandas as pd

class ExcelExporter:
    def __init__(self, logs, system_info):
        self.logs = logs
        self.system_info = system_info

    def export_to_excel(self, file_name):
        with pd.ExcelWriter(file_name, engine='xlsxwriter') as writer:
            # Export logs
            logs_df = pd.DataFrame(self.logs)
            logs_df.to_excel(writer, sheet_name='logs', index=False)

            # Export system info
            system_info_df = pd.DataFrame(list(self.system_info.items()), columns=['Metric', 'Value'])
            system_info_df.to_excel(writer, sheet_name='System Status', index=False)
