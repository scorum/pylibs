from scorum.graphenebase.objects import GrapheneObject, StaticVariantObject

GAMES = [
    'soccer_game',
    'hockey_game'
]


class Game(StaticVariantObject):
    def __init__(self, game_type):
        super().__init__(game_type, GAMES)
        self.name = self.get_name(game_type) + "_game"
        self.id = self.get_id(self.name)


class Soccer(GrapheneObject):
    pass


class Hockey(GrapheneObject):
    pass
