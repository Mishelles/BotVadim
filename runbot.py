#!/usr/bin/python3
#Start application script
import application
import json

#Pathes to config files
CONFIG_PATH = "config.json"

#Reading all configs
config_file = open(CONFIG_PATH, "r")
config = json.loads(config_file.read())
config_file.close()

dict_file = open(config['dict_path'], "r")
dictionary = json.loads(dict_file.read())
dict_file.close()

users_file = open(config['users_path'], "r")
users = json.loads(users_file.read())
users_file.close()


#Starting application
app = application.Application(dict = dictionary, config = config, users = users)
app.start()
