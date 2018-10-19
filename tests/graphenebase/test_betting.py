import pytest

from binascii import hexlify

from scorum.graphenebase.betting import market, Game, Market
from scorum.graphenebase.operations import CreateGame
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
    op = CreateGame(
        **{'uuid': 'e629f9aa-6b2c-46aa-8fa8-36770e7a7a5f',
           'moderator': "admin",
           'name': "game name",
           'start_time': "2018-08-03T10:12:43",
           'auto_resolve_delay_sec': 33,
           'game': game,
           'markets': markets}
    )

    signed_ops = SignedTransaction.cast_operations_to_array_of_opklass([op])
    assert to_hex(signed_ops.data[0]) == result_bin
