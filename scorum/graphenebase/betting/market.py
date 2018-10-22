from collections import OrderedDict

from scorum.graphenebase.graphene_types import Int16
from scorum.graphenebase.objects import GrapheneObject, StaticVariantObject

MARKETS = [
    "result_home_market",
    "result_draw_market",
    "result_away_market",
    "round_home_market",
    "handicap_market",
    "correct_score_home_market",
    "correct_score_draw_market",
    "correct_score_away_market",
    "correct_score_market",
    "goal_home_market",
    "goal_both_market",
    "goal_away_market",
    "total_market",
    "total_goals_home_market",
    "total_goals_away_market"
]


class Market(StaticVariantObject):
    def __init__(self, market_type):
        super().__init__(market_type, MARKETS)
        self.name = self.get_name(market_type) + "_market"
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
