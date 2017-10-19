import random
import re
import json

class Bot:
    def __init__(self, dict, users, config):
        self.dict = dict
        self.users = users
        self.config = config

    def giveAnswer(self, request):
        # section = self.__getSection__(request = request)
        answer = random.choice(self.dict['sections']['hate']['answers'])
        # answer = random.choice(self.dict['sections'][section]['answers'])
        return answer

    def addNewUser(self, user_id, user_first_name, user_last_name, user_sex):
        new_user_fields = self.__userPack__(user_first_name, user_last_name, user_sex)
        self.users[user_id] = new_user_fields
        self.__usersDump__()


    def __getSection__(self, request):
        request = request.lower()
        section_found = 'default'
        for section in self.dict['sections'].keys():
            for question in self.dict['sections'][section]['questions']:
                if re.findall(r'{}'.format(question), request):
                    section_found = section
                    break
        return section_found

    #Packs user's fields to dictionary
    def __userPack__(self, user_first_name, user_last_name, user_sex):
        new_user = dict.fromkeys(['first_name', 'last_name', 'sex'])
        new_user['sex'] = user_sex
        new_user['last_name'] = user_last_name
        new_user['first_name'] = user_first_name
        return new_user

    #Adds updated user's dictionary to database
    def __usersDump__(self):
        dump = json.dumps(self.users)
        users_file = open(self.config['users_path'], "w")
        users_file.write(dump)
        users_file.close()
