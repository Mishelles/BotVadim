#Console to debug application
class Console:
    def __init__(self, bot):
        self.bot = bot

    def eventListener(self):
        print("Welcome to debug mode!")
        while True:
            request = input()
            if request == "addNewUser":
                print("Input user's fields")
                user_id, user_first_name, user_last_name, user_sex = input().split(" ")
                self.bot.addNewUser(user_id, user_first_name, user_last_name, user_sex)
                print ("New user successfully added")
                continue
            response = self.bot.giveAnswer(request = request)
            print(response)
