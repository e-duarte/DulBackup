import schedule
import logging
import time

class SchelingMethod:
    def start_scheduling():
        pass

class SchedulingByTime(SchelingMethod):
    pass

class SchedulginByFileEvent(SchelingMethod):
    pass

class Backup:
    def __init__(self, backup_settings, zip_handler):
        self.backup_settings = backup_settings
        self.zip_handler= zip_handler

    def copy_files(self):
        logging.info('Routine started. The files are being copyed')
        print('[INFO]Routine started. The files are being copyed')

        for src in self.backup_settings.source_folders:
            if src.exists():
                self.zip_handler.add_dir(src, self.backup_settings.allowed_extesions)
                logging.info(f'The Files in {src} were copied')
                print(f'[INFO]The Files in {src} were copied')
            else:
                logging.error(f'The Files in {src} were not found')
                print(f'[ERROR]The Files in {src} were not found')
        
        self.zip_handler.close_zipfile()
    
    def start_backup(self):
        schedule.every().day.at(self.backup_settings.scheduling).do(self.copy_files)
        
        logging.info('Looping started')
        print('[INFO] Looping Started')

        while True:
            schedule.run_pending()
            time.sleep(1)
