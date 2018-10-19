import pytest

from binascii import hexlify

from scorum.graphenebase.betting import market, Game, Market
from scorum.graphenebase import operations_fabric as ops
from scorum.graphenebase.signedtransactions import SignedTransaction


def to_hex(data):
    return hexlify(bytes(data))


@pytest.mark.parametrize('game,val', [
    (Game.hockey, b'01'),
    (Game.soccer, b'00')
])
def test_serialize_game_type(game, val):
    assert to_hex(game) == val


@pytest.mark.parametrize('market_type, val', [
    (market.ResultHome, b'00'),
    (market.ResultDraw, b'01'),
    (market.ResultAway, b'02'),
    (market.RoundHome, b'03'),
    (market.Handicap, b'040000'),
    (market.CorrectScoreHome, b'05'),
    (market.CorrectScoreDraw, b'06'),
    (market.CorrectScoreAway, b'07'),
    (market.CorrectScore, b'0800000000'),
    (market.GoalHome, b'09'),
    (market.GoalBoth, b'0a'),
    (market.GoalAway, b'0b'),
    (market.Total, b'0c0000'),
    (market.TotalGoalsHome, b'0d0000'),
    (market.TotalGoalsAway, b'0e0000')
])
def test_serialize_markets(market_type, val):
    assert to_hex(Market(market_type())) == val


@pytest.mark.parametrize('game,markets,result_bin', [
    (
        Game.soccer,
        [],
        b'23e629f9aa6b2c46aa8fa836770e7a7a5f0561646d696e0967616d65206e616d659b2a645b210000000000'
    ),
    (
        Game.soccer,
        [market.Total(1000)],
        b'23e629f9aa6b2c46aa8fa836770e7a7a5f0561646d696e0967616d65206e616d659b2a645b2100000000010ce803'
    ),
    (
        Game.hockey,
        [],
        b'23e629f9aa6b2c46aa8fa836770e7a7a5f0561646d696e0967616d65206e616d659b2a645b210000000100'
    )
])
def test_serialize_create_game(game, markets, result_bin):
    op = ops.create_game(
        'e629f9aa-6b2c-46aa-8fa8-36770e7a7a5f', "admin", "game name", "2018-08-03T10:12:43", 33, game, markets
    )
    signed_ops = SignedTransaction.cast_operations_to_array_of_opklass([op])
    assert to_hex(signed_ops.data[0]) == result_bin


def test_serialize_cancel_game():
    op = ops.cancel_game("e629f9aa-6b2c-46aa-8fa8-36770e7a7a5f", "admin")
    signed_ops = SignedTransaction.cast_operations_to_array_of_opklass([op])
    assert to_hex(signed_ops.data[0]) == b'24e629f9aa6b2c46aa8fa836770e7a7a5f0561646d696e'


def test_serialize_development_committee_empower_betting_moderator_to_byte():
    op = ops.development_committee_empower_betting_moderator("initdelegate", "alice", 86400)
    signed_ops = SignedTransaction.cast_operations_to_array_of_opklass([op])

    result_bin = b'1d0c696e697464656c6567617465805101000b05616c696365'
    assert hexlify(bytes(signed_ops.data[0])) == result_bin


def test_serialize_development_committee_change_betting_resolve_delay_to_byte():
    op = ops.development_committee_change_betting_resolve_delay("initdelegate", 10, 86400)
    signed_ops = SignedTransaction.cast_operations_to_array_of_opklass([op])

    result_bin = b'1d0c696e697464656c6567617465805101000c0a000000'
    assert hexlify(bytes(signed_ops.data[0])) == result_bin
