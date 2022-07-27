from getpass import getuser
from os import path
from pathlib import Path
from sys import argv


def startup():
        file_path="app.pyw"
        USER = getuser()
        dir_file_path = path.dirname(path.realpath(file_path))

        bat_path = fr'C:\Users\{USER}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'
        bat_path = Path(bat_path)

        with open(bat_path / "dulbackup.bat", "w+") as bat_file:
            bat_file.write(f'cd {dir_file_path}\n')
            bat_file.write(fr'start "" {Path(dir_file_path) / file_path}')
            
startup()