import pytest
import json

from binascii import hexlify

from scorum.graphenebase.betting import game, Game, market, Market, wincase, Wincase
from scorum.graphenebase import operations_fabric as ops
from scorum.graphenebase.signedtransactions import SignedTransaction


def to_hex(data):
    return hexlify(bytes(data))


@pytest.mark.parametrize('game_type,val', [
    (game.Hockey(), b'01'),
    (game.Soccer(), b'00')
])
def test_serialize_game_type_to_hex(game_type, val):
    assert to_hex(Game(game_type)) == val


@pytest.mark.parametrize('market_type, val', [
    (market.ResultHome(), b'00'),
    (market.ResultDraw(), b'01'),
    (market.ResultAway(), b'02'),
    (market.RoundHome(), b'03'),
    (market.Handicap(), b'040000'),
    (market.CorrectScoreHome(), b'05'),
    (market.CorrectScoreDraw(), b'06'),
    (market.CorrectScoreAway(), b'07'),
    (market.CorrectScore(), b'0800000000'),
    (market.CorrectScore(1, 2), b'0801000200'),
    (market.GoalHome(), b'09'),
    (market.GoalBoth(), b'0a'),
    (market.GoalAway(), b'0b'),
    (market.Total(), b'0c0000'),
    (market.TotalGoalsHome(), b'0d0000'),
    (market.TotalGoalsAway(), b'0e0000')
])
def test_serialize_markets_to_hex(market_type, val):
    assert to_hex(Market(market_type)) == val


@pytest.mark.parametrize('wincase_type, val', [
    (wincase.ResultHomeYes(), b'00'),
    (wincase.ResultHomeNo(), b'01'),
    (wincase.ResultDrawYes(), b'02'),
    (wincase.ResultDrawNo(), b'03'),
    (wincase.ResultAwayYes(), b'04'),
    (wincase.ResultAwayNo(), b'05'),
    (wincase.RoundHomeYes(), b'06'),
    (wincase.RoundHomeNo(), b'07'),
    (wincase.HandicapOver(), b'080000'),
    (wincase.HandicapUnder(), b'090000'),
    (wincase.CorrectScoreHomeYes(), b'0a'),
    (wincase.CorrectScoreHomeNo(), b'0b'),
    (wincase.CorrectScoreDrawYes(), b'0c'),
    (wincase.CorrectScoreDrawNo(), b'0d'),
    (wincase.CorrectScoreAwayYes(), b'0e'),
    (wincase.CorrectScoreAwayNo(), b'0f'),
    (wincase.CorrectScoreYes(), b'1000000000'),
    (wincase.CorrectScoreNo(), b'1100000000'),
    (wincase.GoalHomeYes(), b'12'),
    (wincase.GoalHomeNo(), b'13'),
    (wincase.GoalBothYes(), b'14'),
    (wincase.GoalBothNo(), b'15'),
    (wincase.GoalAwayYes(), b'16'),
    (wincase.GoalAwayNo(), b'17'),
    (wincase.TotalOver(), b'180000'),
    (wincase.TotalUnder(), b'190000'),
    (wincase.TotalGoalsHomeOver(), b'1a0000'),
    (wincase.TotalGoalsHomeUnder(), b'1b0000'),
    (wincase.TotalGoalsAwayOver(), b'1c0000'),
    (wincase.TotalGoalsAwayUnder(), b'1d0000')
])
def test_serialize_wincases_to_hex(wincase_type, val):
    assert to_hex(Wincase(wincase_type)) == val


@pytest.mark.parametrize('game_type,market_types,result_bin', [
    (
        game.Soccer(),
        [],
        b'23e629f9aa6b2c46aa8fa836770e7a7a5f0561646d696e027b7d9b2a645b210000000000'
    ),
    (
        game.Soccer(),
        [market.Total(1000)],
        b'23e629f9aa6b2c46aa8fa836770e7a7a5f0561646d696e027b7d9b2a645b2100000000010ce803'
    ),
    (
        game.Hockey(),
        [],
        b'23e629f9aa6b2c46aa8fa836770e7a7a5f0561646d696e027b7d9b2a645b210000000100'
    ),
    (
        game.Hockey(),
        [market.CorrectScore(home=1, away=2)],
        b'23e629f9aa6b2c46aa8fa836770e7a7a5f0561646d696e027b7d9b2a645b2100000001010801000200'
    )
])
def test_serialize_create_game_to_hex(game_type, market_types, result_bin):
    op = ops.create_game(
        'e629f9aa-6b2c-46aa-8fa8-36770e7a7a5f', "admin", "{}", "2018-08-03T10:12:43", 33,
        game_type, market_types
    )
    signed_ops = SignedTransaction.cast_operations_to_array_of_opklass([op])
    assert to_hex(signed_ops.data[0]) == result_bin


def test_serialize_cancel_game_to_hex():
    op = ops.cancel_game("e629f9aa-6b2c-46aa-8fa8-36770e7a7a5f", "admin")
    signed_ops = SignedTransaction.cast_operations_to_array_of_opklass([op])
    assert to_hex(signed_ops.data[0]) == b'24e629f9aa6b2c46aa8fa836770e7a7a5f0561646d696e'


def test_serialize_update_game_markets_to_hex():
    op = ops.update_game_markets("e629f9aa-6b2c-46aa-8fa8-36770e7a7a5f", "admin", [market.Total(1000)])
    signed_ops = SignedTransaction.cast_operations_to_array_of_opklass([op])
    assert to_hex(signed_ops.data[0]) == b'25e629f9aa6b2c46aa8fa836770e7a7a5f0561646d696e010ce803'


def test_serialize_update_game_start_time_to_hex():
    op = ops.update_game_start_time("e629f9aa-6b2c-46aa-8fa8-36770e7a7a5f", "admin", "2018-08-03T10:12:43")
    signed_ops = SignedTransaction.cast_operations_to_array_of_opklass([op])
    assert to_hex(signed_ops.data[0]) == b'26e629f9aa6b2c46aa8fa836770e7a7a5f0561646d696e9b2a645b'


def test_serialize_development_committee_empower_betting_moderator_to_hex():
    op = ops.development_committee_empower_betting_moderator("initdelegate", "alice", 86400)
    signed_ops = SignedTransaction.cast_operations_to_array_of_opklass([op])

    result_bin = b'1d0c696e697464656c6567617465805101000b05616c696365'
    assert hexlify(bytes(signed_ops.data[0])) == result_bin


def test_serialize_development_committee_change_betting_resolve_delay_to_hex():
    op = ops.development_committee_change_betting_resolve_delay("initdelegate", 10, 86400)
    signed_ops = SignedTransaction.cast_operations_to_array_of_opklass([op])

    result_bin = b'1d0c696e697464656c6567617465805101000c0a000000'
    assert hexlify(bytes(signed_ops.data[0])) == result_bin


@pytest.mark.parametrize('wincase_types,result_bin', [
    ([wincase.ResultHomeYes()], b'27e629f9aa6b2c46aa8fa836770e7a7a5f0561646d696e0100'),
    ([wincase.HandicapOver(1000)], b'27e629f9aa6b2c46aa8fa836770e7a7a5f0561646d696e0108e803'),
    ([wincase.TotalOver()], b'27e629f9aa6b2c46aa8fa836770e7a7a5f0561646d696e01180000'),
    ([wincase.CorrectScoreYes(home=1, away=2)], b'27e629f9aa6b2c46aa8fa836770e7a7a5f0561646d696e011001000200'),
])
def test_serialize_post_game_results_to_hex(wincase_types, result_bin):
    op = ops.post_game_results("e629f9aa-6b2c-46aa-8fa8-36770e7a7a5f", "admin", wincase_types)
    signed_ops = SignedTransaction.cast_operations_to_array_of_opklass([op])
    assert hexlify(bytes(signed_ops.data[0])) == result_bin


@pytest.mark.parametrize('wincase_type,odds,result_bin', [
    (
        wincase.CorrectScoreYes(17, 23),
        [1, 2],
        b'28e629f9aa6b2c46aa8fa836770e7a7a5f0561646d696ee629f9aa6b2c46aa8fa836770e7a7a5f1011001700010000000200000000e40'
        b'b5402000000095343520000000001'
    ),
    (
        wincase.HandicapOver(-500),
        [3, 2],
        b'28e629f9aa6b2c46aa8fa836770e7a7a5f0561646d696ee629f9aa6b2c46aa8fa836770e7a7a5f080cfe030000000200000000e40'
        b'b5402000000095343520000000001'
    ),
    (
        wincase.RoundHomeNo(),
        [4, 7],
        b'28e629f9aa6b2c46aa8fa836770e7a7a5f0561646d696ee629f9aa6b2c46aa8fa836770e7a7a5f07040000000700000000e40'
        b'b5402000000095343520000000001'
    )
])
def test_serialize_post_bet_to_hex(wincase_type, odds, result_bin):
    uuid = "e629f9aa-6b2c-46aa-8fa8-36770e7a7a5f"
    op = ops.post_bet(uuid, "admin", uuid, wincase_type, odds, "10.000000000 SCR", True)
    signed_ops = SignedTransaction.cast_operations_to_array_of_opklass([op])
    assert hexlify(bytes(signed_ops.data[0])) == result_bin


def test_serialize_cancel_pending_bets_to_hex():
    uuid = "e629f9aa-6b2c-46aa-8fa8-36770e7a7a5f"
    result_bin = b'2901e629f9aa6b2c46aa8fa836770e7a7a5f0561646d696e'
    op = ops.cancel_pending_bets([uuid], "admin")
    signed_ops = SignedTransaction.cast_operations_to_array_of_opklass([op])
    assert hexlify(bytes(signed_ops.data[0])) == result_bin


@pytest.mark.parametrize('wc', [
    wincase.HandicapOver(-1000),
    wincase.CorrectScoreNo(3, 4),
    wincase.ResultDrawYes(),
    wincase.TotalGoalsAwayOver(500)
])
def test_get_wincase_obj_from_json(wc):
    assert Wincase(wc) == wincase.create_obj_from_json(json.loads(str(Wincase(wc))))


@pytest.mark.parametrize('name, expected', [
    ("result_home::yes", "result_home::no"),
    ("total_goals_away::under", "total_goals_away::over"),
    ("correct_score_draw::no", "correct_score_draw::yes")
])
def test_get_wincase_opposite(name, expected):
    assert expected == wincase.opposite(name)
