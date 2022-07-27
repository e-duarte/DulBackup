from dulbackup.util import BackupSetting, ZipDocsBackup
from dulbackup.backup import Backup
from pathlib import Path
import logging
import os

def create_directory(path):
    if not path.exists():
        os.mkdir(path.parent)

def main():
    SETTING_PATH = Path('./backup_settings.json')
    LOG_PATH = Path('./output/log.txt')

    create_directory(LOG_PATH)
    logging.basicConfig(filename=LOG_PATH,format='[%(levelname)s]:%(message)s\t%(asctime)s',  level=logging.DEBUG)

    logging.info('Dulbackup started')
    print('[INFO] Dulbackup started')
    
    backup_pars = BackupSetting(SETTING_PATH)
    backup_pars.load_setting()

    zip_handler = ZipDocsBackup(Path(backup_pars.destination_folder))

    backup = Backup(backup_pars, zip_handler)
    backup.start_backup()
    
if __name__ == '__main__':
    main()