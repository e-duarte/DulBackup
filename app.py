from dulbackup.util import BackupSetting, ZipDocsBackup
import logging
from pathlib import Path

def main():
    SETTING_PATH = Path('./backup_settings.json')
    LOG_PATH = Path('./output/log.txt')
    
    allowed_files = [
        '',
        'pdf', 
        'txt',
        'odt',
        'doc',
        'docx',
        'csv',
        'xls',
        'xlsx',
        'pot',
        'potx',
        'png',
        'jpg',
        'jpeg'
    ]

    logging.basicConfig(filename=LOG_PATH,format='[%(levelname)s]:%(message)s\t%(asctime)s',  level=logging.DEBUG)

    logging.info('*** Dulbackup started***')
    print('[INFO]*** Dulbackup started***')
    
    backup_pars = BackupSetting(SETTING_PATH)
    backup_pars.load_setting()


    zip_backup = ZipDocsBackup(Path(backup_pars.destination_folder))

    zip_backup.add_dir(backup_pars.source_folders[0], allowed_files)

    zip_backup.close_zipfile()
    
if __name__ == '__main__':
    main()