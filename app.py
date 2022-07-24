from dulbackup.util import BackupSetting
import logging

def main():
    SETTING_PATH = 'backup_settings.json'

    logging.basicConfig(filename='log.txt',format='[%(levelname)s]:%(message)s\t%(asctime)s',  level=logging.DEBUG)
    logging.info('*** Dulbackup started***')
    print('[INFO]*** Dulbackup started***')

    
    backup_pars = BackupSetting(SETTING_PATH)
    backup_pars.load_setting()
    
if __name__ == '__main__':
    main()