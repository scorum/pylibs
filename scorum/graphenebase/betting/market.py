from collections import OrderedDict

from scorum.graphenebase.graphene_types import Int16
from scorum.graphenebase.objects import GrapheneObject, StaticVariantObject

MARKETS = [
    "result_home",
    "result_draw",
    "result_away",
    "round_home",
    "handicap",
    "correct_score_home",
    "correct_score_draw",
    "correct_score_away",
    "correct_score",
    "goal_home",
    "goal_both",
    "goal_away",
    "total",
    "total_goals_home",
    "total_goals_away"
]


class Market(StaticVariantObject):
    def __init__(self, market_type):
        super().__init__(market_type, MARKETS)
        self.name = self.get_name(market_type)
        self.id = self.get_id(self.name)


class ResultHome(GrapheneObject):
    pass


class ResultDraw(GrapheneObject):
    pass


class ResultAway(GrapheneObject):
    pass


class RoundHome(GrapheneObject):
    pass


class Handicap(GrapheneObject):
    def __init__(self, threshold=0):
        self.data = OrderedDict([("threshold", Int16(threshold))])

        super(Handicap, self).__init__(self.data)


class CorrectScoreHome(GrapheneObject):
    pass


class CorrectScoreDraw(GrapheneObject):
    pass


class CorrectScoreAway(GrapheneObject):
    pass


class CorrectScore(GrapheneObject):
    def __init__(self, home=0, away=0):
        self.data = OrderedDict([("home", Int16(home)), ("away", Int16(away))])

        super(CorrectScore, self).__init__(self.data)


class GoalHome(GrapheneObject):
    pass


class GoalBoth(GrapheneObject):
    pass


class GoalAway(GrapheneObject):
    pass


class Total(GrapheneObject):
    def __init__(self, threshold=0):
        self.data = OrderedDict([("threshold", Int16(threshold))])

        super(Total, self).__init__(self.data)


class TotalGoalsHome(GrapheneObject):
    def __init__(self, threshold=0):
        self.data = OrderedDict([("threshold", Int16(threshold))])

        super(TotalGoalsHome, self).__init__(self.data)


class TotalGoalsAway(GrapheneObject):
    def __init__(self, threshold=0):
        self.data = OrderedDict([("threshold", Int16(threshold))])

        super(TotalGoalsAway, self).__init__(self.data)
