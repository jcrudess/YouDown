import app
import configparser

config = configparser.RawConfigParser()

#TODO konverzija u MP3

config.read('settings.cfg')


storePath = config.get('Postavke', 'SAVE_LOKACIJA')

app = app.App(storePath)






