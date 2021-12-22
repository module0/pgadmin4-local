import os


print('Activate config_local.py.')

current_dir = os.getcwd()
pgadmin4_data_dir = 'pgadmin4_data'

SQLITE_PATH = current_dir + '/' + pgadmin4_data_dir + '/pgadmin4.db'
LOG_FILE = current_dir + '/' + pgadmin4_data_dir + '/pgadmin4.log'
SESSION_DB_PATH = current_dir + '/' + pgadmin4_data_dir + '/sessions'
STORAGE_DIR  = current_dir + '/' + pgadmin4_data_dir + '/storage'

MASTER_PASSWORD_REQUIRED=False
