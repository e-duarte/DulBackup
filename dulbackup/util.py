from json import loads, JSONDecodeError
import logging

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
                setting = loads(json_formated_text)

            self.source_folders = setting['source_folders']
            self.destination_folder = setting['destination_folder']
            self.log_path = setting['log_path']
            self.schedule = setting['scheduling']

        except JSONDecodeError:
            logging.error(f'{self.setting_path} file is not valid Json')
            logging.info('Ending script')

            print(f'{self.setting_path} file is not valid Json')
            print('[INFO]Ending script')

            exit()

        except FileNotFoundError:
            logging.error(f'{self.setting_path} wasnt found')
            logging.info('Ending script')

            print(f'[ERROR]:{self.setting_path} wasnt found')
            print('[INFO]:Ending script')

            exit()

class ZipBackup:
    pass