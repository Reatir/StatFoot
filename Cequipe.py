class Cequipe(object):

    name = ""
    match = []
    def __init__(self,name_):
        self.name = name_


    def add_match(self,match_):
        self.match.append(match_)