import schedule
import logging
import time

class Backup:
    def __init__(self, backup_settings, zip_handler):
        self.backup_settings = backup_settings
        self.zip_handler= zip_handler

    def copy_files(self):
        logging.info('Routine started. The files are being copyed')
        print('[INFO]Routine started. The files are being copyed')
        for src in self.backup_settings.source_folders:
            self.zip_handler.add_dir(src, self.backup_settings.allowed_extesions)
        
        self.zip_handler.close_zipfile()
        logging.info('The Files were copied')
        print('[INFO]The Files were copied')

    def start_backup(self):
        schedule.every().day.at(self.backup_settings.scheduling).do(self.copy_files)
        
        logging.info('Looping started')
        print('[INFO] Looping Started')

        while True:
            schedule.run_pending()
            time.sleep(1)
