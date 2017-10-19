import bot
import controller
import console


class Application:

    def __init__(self, dict, config, users):
        self.config = config
        self.bot = bot.Bot(dict = dict, users = users, config = config)
        # print (self.config['debug'])
        # if self.config['debug'] == 0:
        self.controller = controller.Controller(bot = self.bot)
        # else:
        # self.controller = console.Console(bot = self.bot)
    def start(self):
        # self.controller.eventListener()
        # self.controller.killGroup()
        self.controller.birthdayBot()
