from librouteros import connect
from librouteros.query import Key

# MikroTik bağlantı bilgileri
mikrotik_ip = '192.168.88.1'
username = 'admin'
password = 'password'

# MikroTik cihazına bağlanma
api = connect(username=username, password=password, host=mikrotik_ip)

# Yedek alma komutu
api(cmd='/system/backup/save', file_name='backup_name.backup')

# Yedek dosyasını indirme
backup_file = api(cmd='/file/print', where=Key('name')=='backup_name.backup')
with open('backup_name.backup', 'wb') as file:
    file.write(backup_file[0]['contents'])
