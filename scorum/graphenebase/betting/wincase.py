from collections import OrderedDict

from scorum.graphenebase.graphene_types import Int16
from scorum.graphenebase.objects import GrapheneObject, StaticVariantObject

WINCASES = [
    "result_home::yes",
    "result_home::no",
    "result_draw::yes",
    "result_draw::no",
    "result_away::yes",
    "result_away::no",
    "round_home::yes",
    "round_home::no",
    "handicap::over",
    "handicap::under",
    "correct_score_home::yes",
    "correct_score_home::no",
    "correct_score_draw::yes",
    "correct_score_draw::no",
    "correct_score_away::yes",
    "correct_score_away::no",
    "correct_score::yes",
    "correct_score::no",
    "goal_home::yes",
    "goal_home::no",
    "goal_both::yes",
    "goal_both::no",
    "goal_away::yes",
    "goal_away::no",
    "total::over",
    "total::under",
    "total_goals_home::over",
    "total_goals_home::under",
    "total_goals_away::over",
    "total_goals_away::under"
]


class Wincase(StaticVariantObject):
    def __init__(self, wincase_type):
        super().__init__(wincase_type, WINCASES)
        self.wincase_type = wincase_type
        self.name = "::".join(self.get_name(wincase_type).rsplit('_', 1))
        self.id = self.get_id(self.name)


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
        self.data = OrderedDict([("threshold", Int16(threshold))])

        super(HandicapOver, self).__init__(self.data)


class HandicapUnder(GrapheneObject):
    def __init__(self, threshold=0):
        self.data = OrderedDict([("threshold", Int16(threshold))])

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
    def __init__(self, home=0, away=0):
        self.data = OrderedDict([("home", Int16(home)), ("away", Int16(away))])

        super(CorrectScoreYes, self).__init__(self.data)


class CorrectScoreNo(GrapheneObject):
    def __init__(self, home=0, away=0):
        self.data = OrderedDict([("home", Int16(home)), ("away", Int16(away))])

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
        self.data = OrderedDict([("threshold", Int16(threshold))])

        super(TotalOver, self).__init__(self.data)


class TotalUnder(GrapheneObject):
    def __init__(self, threshold=0):
        self.data = OrderedDict([("threshold", Int16(threshold))])

        super(TotalUnder, self).__init__(self.data)


class TotalGoalsHomeOver(GrapheneObject):
    def __init__(self, threshold=0):
        self.data = OrderedDict([("threshold", Int16(threshold))])

        super(TotalGoalsHomeOver, self).__init__(self.data)


class TotalGoalsHomeUnder(GrapheneObject):
    def __init__(self, threshold=0):
        self.data = OrderedDict([("threshold", Int16(threshold))])

        super(TotalGoalsHomeUnder, self).__init__(self.data)


class TotalGoalsAwayOver(GrapheneObject):
    def __init__(self, threshold=0):
        self.data = OrderedDict([("threshold", Int16(threshold))])

        super(TotalGoalsAwayOver, self).__init__(self.data)


class TotalGoalsAwayUnder(GrapheneObject):
    def __init__(self, threshold=0):
        self.data = OrderedDict([("threshold", Int16(threshold))])

        super(TotalGoalsAwayUnder, self).__init__(self.data)
