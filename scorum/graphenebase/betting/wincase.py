import json
from collections import OrderedDict

from scorum.graphenebase.graphene_types import Id, Uint16, Uint32
from scorum.graphenebase.objects import GrapheneObject, to_method_name

WINCASES = [
    "result_home_yes",
    "result_home_no",
    "result_draw_yes",
    "result_draw_no",
    "result_away_yes",
    "result_away_no",
    "round_home_yes",
    "round_home_no",
    "handicap_over",
    "handicap_under",
    "correct_score_home_yes",
    "correct_score_home_no",
    "correct_score_draw_yes",
    "correct_score_draw_no",
    "correct_score_away_yes",
    "correct_score_away_no",
    "correct_score_yes",
    "correct_score_no",
    "goal_home_yes",
    "goal_home_no",
    "goal_both_yes",
    "goal_both_no",
    "goal_away_yes",
    "goal_away_no",
    "total_over",
    "total_under",
    "total_goals_home_over",
    "total_goals_home_under",
    "total_goals_away_over",
    "total_goals_away_under"
]


class Wincase:
    def __init__(self, wincase_type):
        self.wincase_type = wincase_type
        self.name = self.get_wincase_name(wincase_type)
        self.id = self.get_wincase_id(self.name)

    @staticmethod
    def get_wincase_id(name: str):
        try:
            return WINCASES.index(name)
        except ValueError:
            raise Exception("no such wincase %s" % name)

    @staticmethod
    def get_wincase_name(wincase_type):
        """ Take a name of a class, like ResultHomeYes and turn it into method name like result_home_yes. """
        class_name = type(wincase_type).__name__  # also store name
        return to_method_name(class_name)

    def __bytes__(self):
        return bytes(Id(self.id)) + bytes(self.wincase_type)

    def __str__(self):
        return json.dumps([self.name, self.wincase_type.toJson()])


class ResultHomeYes(GrapheneObject):
    pass


class ResultHomeNo(GrapheneObject):
    pass


class ResultDrawYes(GrapheneObject):
    pass


class ResultDrawNo(GrapheneObject):
    pass


class ResultAwayYes(GrapheneObject):
    pass


class ResultAwayNo(GrapheneObject):
    pass


class RoundHomeYes(GrapheneObject):
    pass


class RoundHomeNo(GrapheneObject):
    pass


class HandicapOver(GrapheneObject):
    def __init__(self, threshold=0):
        self.data = OrderedDict({"threshold": Uint16(threshold)})

        super(HandicapOver, self).__init__(self.data)


class HandicapUnder(GrapheneObject):
    def __init__(self, threshold=0):
        self.data = OrderedDict({"threshold": Uint16(threshold)})

        super(HandicapUnder, self).__init__(self.data)


class CorrectScoreHomeYes(GrapheneObject):
    pass


class CorrectScoreHomeNo(GrapheneObject):
    pass


class CorrectScoreDrawYes(GrapheneObject):
    pass


class CorrectScoreDrawNo(GrapheneObject):
    pass


class CorrectScoreAwayYes(GrapheneObject):
    pass


class CorrectScoreAwayNo(GrapheneObject):
    pass


class CorrectScoreYes(GrapheneObject):
    def __init__(self, threshold=0):
        self.data = OrderedDict({"threshold": Uint32(threshold)})

        super(CorrectScoreYes, self).__init__(self.data)


class CorrectScoreNo(GrapheneObject):
    def __init__(self, threshold=0):
        self.data = OrderedDict({"threshold": Uint32(threshold)})

        super(CorrectScoreNo, self).__init__(self.data)


class GoalHomeYes(GrapheneObject):
    pass


class GoalHomeNo(GrapheneObject):
    pass


class GoalBothYes(GrapheneObject):
    pass


class GoalBothNo(GrapheneObject):
    pass


class GoalAwayYes(GrapheneObject):
    pass


class GoalAwayNo(GrapheneObject):
    pass


class TotalOver(GrapheneObject):
    def __init__(self, threshold=0):
        self.data = OrderedDict({"threshold": Uint16(threshold)})

        super(TotalOver, self).__init__(self.data)


class TotalUnder(GrapheneObject):
    def __init__(self, threshold=0):
        self.data = OrderedDict({"threshold": Uint16(threshold)})

        super(TotalUnder, self).__init__(self.data)


class TotalGoalsHomeOver(GrapheneObject):
    def __init__(self, threshold=0):
        self.data = OrderedDict({"threshold": Uint16(threshold)})

        super(TotalGoalsHomeOver, self).__init__(self.data)


class TotalGoalsHomeUnder(GrapheneObject):
    def __init__(self, threshold=0):
        self.data = OrderedDict({"threshold": Uint16(threshold)})

        super(TotalGoalsHomeUnder, self).__init__(self.data)


class TotalGoalsAwayOver(GrapheneObject):
    def __init__(self, threshold=0):
        self.data = OrderedDict({"threshold": Uint16(threshold)})

        super(TotalGoalsAwayOver, self).__init__(self.data)


class TotalGoalsAwayUnder(GrapheneObject):
    def __init__(self, threshold=0):
        self.data = OrderedDict({"threshold": Uint16(threshold)})

        super(TotalGoalsAwayUnder, self).__init__(self.data)
