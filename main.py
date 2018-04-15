import configparser
import app
import os

config = configparser.RawConfigParser()

config.read('settings.cfg')


storePath = config.get('Postavke', 'SAVE_LOKACIJA')
threadLimit = config.get('Postavke', 'THREAD_LIMIT')

app = app.App(storePath, threadLimit)




