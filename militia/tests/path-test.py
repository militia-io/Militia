import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__)) # This is your Project Root
CONFIG_PATH = os.path.join(BASE_DIR, 'tools/config.json')
print CONFIG_PATH