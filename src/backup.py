from json import loads, JSONDecodeError

class BackupSetting:
    def __init__(self, setting_path):
        self.setting_path = setting_path
        self.source_folders = []
        self.destination_folders = ''
        self.log_path = ''
        self.schedule = ''
    
    def load_setting(self):
        try:
            with open(self.setting_path) as setting_file:
                json_formated_text = setting_file.read().replace('\\', '\\\\')
                print(json_formated_text)
                setting = loads(json_formated_text)

            self.source_folders = setting['source_folders']
            self.destination_folder = setting['destination_folder']
            self.log_path = setting['log_path']
            self.schedule = setting['scheduling']

        except JSONDecodeError:
            print("[ERROR]\tBackup setting file is not valid Json")
            print("[INFO]\tEnding script")

            exit()

        except FileNotFoundError:
            print("[ERROR]\tSetting file not found")
            print("[INFO]\tEnding script")

            exit()