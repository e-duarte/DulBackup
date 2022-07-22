from backup import BackupSetting
if __name__ == '__main__':
    backup_pars = BackupSetting('backup_settings.json')
    backup_pars.load_setting()

