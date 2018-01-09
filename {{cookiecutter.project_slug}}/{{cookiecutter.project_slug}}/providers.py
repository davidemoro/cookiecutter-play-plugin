class NewProvider(object):
    """ Print provider """

    def __init__(self, engine):
        self.engine = engine

    def command_print(self, command, **kwargs):
        print(command['message'])

    def command_yetAnotherCommand(self, command, **kwargs):
        pass
