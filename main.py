import app
import configparser

config = configparser.RawConfigParser()

#TODO dodati config file i postavke slati u konstruktor
#TODO konverzija u MP3

config.read('settings.cfg')


storePath = config.get('Postavke', 'SAVE_LOKACIJA')

app = app.App(storePath)






