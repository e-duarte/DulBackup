from json import loads, JSONDecodeError
from datetime import datetime
from pathlib import Path
import logging
import zipfile
import os

class BackupSetting:
    def __init__(self, setting_path):
        self.setting_path = setting_path
        self.source_folders = []
        self.destination_folders = Path()
        self.log_path = Path()
        self.schedule = ''
        self.allowed_extesions = []

    def load_setting(self):
        try:
            with open(self.setting_path) as setting_file:
                json_formated_text = setting_file.read().replace('\\', '\\\\')
                setting = loads(json_formated_text)

            self.source_folders = [Path(path) for path in setting['source_folders']]
            self.destination_folder = Path(setting['destination_folder'])
            # self.log_path = Path(setting['log_path'])
            self.scheduling = setting['scheduling']
            self.allowed_extesions = setting['allowed_extesions']

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

class ZipDocsBackup:
    def __init__(self, zip_src):
        filename_path = zip_src / 'backup_files' / f"backup_{datetime.today().strftime('%Y-%m-%d')}.zip"

        if not filename_path.parent.exists():
            os.mkdir(filename_path.parent)

        # mode = 'a' if filename_path.exists() else 'w'

        self.zip_obj = zipfile.ZipFile(
            filename_path,
            'a' if filename_path.exists() else 'w',
            zipfile.ZIP_DEFLATED
        )

    def add_dir(self, dir_path, allowed_files):
        try:
            for root, _, filenames in os.walk(dir_path):
                for filename in filenames:
                    filename = Path(filename)
                    if filename.suffix in allowed_files:
                        absolute_path_file = root / filename
                        
                        self.zip_obj.write(
                            absolute_path_file,
                            absolute_path_file.relative_to(dir_path.parent)
                        )
                        
        except FileNotFoundError:
            logging.error(f'{self.setting_path} wasnt found in add_dir from ZipDocsFile Object')
            logging.info('Ending script')

            print(f'[ERROR]:{self.setting_path} wasnt found')
            print('[INFO]:Ending script')

            exit()

    def close_zipfile(self):
        self.zip_obj.close()