import requests
import os

url = "http://clients.flux4test.ru/api/amo/leads/add?token=vupxqa59lxrmtccklzfz6ivh2hqt7gfv"

file = open("123", 'w')
file.write("{\"tag\": \"бот\",\"name\": \"Vsevolod\",\"phone\": \"123\",\"message\": \"test\",\"email\": \"@\"}")
file.close()

file = open("123")
text = file.read()
file.close()

os.remove("123")

text = eval(text)
r = requests.post(url, text)
