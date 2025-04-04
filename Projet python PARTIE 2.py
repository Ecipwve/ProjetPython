import json

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
        print(f"{len(self.logs)} logs extraits.")

    def get_logs(self):
        return self.logs

# Exemple d'utilisation
if __name__ == "__main__":
    file_path = input("Veuillez entrer le chemin du fichier JSON : ")
    processor = LogProcessor()
    data = processor.read_json(file_path)
    processor.extract_logs(data)
    logs = processor.get_logs()

    # Afficher les logs extraits
    for log in logs:
        print(f"Log Level: {log['log_level']}, Message: {log['message']}, Station: {log['station_name']}")
