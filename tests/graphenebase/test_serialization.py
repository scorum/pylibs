import pytest

from binascii import hexlify

from scorum.graphenebase.graphene_types import BudgetType
from scorum.graphenebase.amount import Amount
from scorum.graphenebase.signedtransactions import SignedTransaction
from scorum.graphenebase.operations_fabric import (
    devpool_withdraw_vesting, create_budget_operation, development_committee_empower_advertising_moderator,
    close_budget_by_advertising_moderator, development_committee_change_budgets_auction_properties,
    update_budget_operation, close_budget_operation, development_committee_empower_betting_moderator
)


def test_serialize_banner_to_string():
    x = BudgetType("banner")
    assert str(x) == "banner"


def test_serialize_post_to_string():
    x = BudgetType("post")
    assert str(x) == "post"


def test_serialize_banner_to_byte():
    x = BudgetType("banner")
    assert hexlify(bytes(x)) == b'0100000000000000'


def test_serialize_post_to_byte():
    x = BudgetType("post")
    assert hexlify(bytes(x)) == b'0000000000000000'


@pytest.mark.parametrize(
    'budget_type,result_bin',
    [
        ("post", b'1a00000000000000006dcd3132e5df480a89a891984bca0a090c696e697464656c6567617465027b7d00e40b5402000000'
                 b'09534352000000009b2a645bb92a645b'),
        ("banner", b'1a01000000000000006dcd3132e5df480a89a891984bca0a090c696e697464656c6567617465027b7d00e40b5402000000'
                   b'09534352000000009b2a645bb92a645b'),
    ]
)
def test_serialize_create_budget_to_byte(budget_type, result_bin):
    op = create_budget_operation(
        "6DCD3132-E5DF-480A-89A8-91984BCA0A09", "initdelegate", "{}", Amount("10.000000000 SCR"),
        "2018-08-03T10:12:43", "2018-08-03T10:13:13", budget_type
    )
    signed_ops = SignedTransaction.cast_operations_to_array_of_opklass([op])
    assert hexlify(bytes(signed_ops.data[0])) == result_bin


def test_serialize_devpool_withdraw_vesting_proposal_create_to_byte():
    op = devpool_withdraw_vesting("initdelegate", Amount("10.000000000 SP"), 86400)
    signed_ops = SignedTransaction.cast_operations_to_array_of_opklass([op])

    result_bin = b'1d0c696e697464656c6567617465805101000600e40b54020000000953500000000000'
    assert hexlify(bytes(signed_ops.data[0])) == result_bin


def test_serialize_development_committee_empower_advertising_moderator_to_byte():
    op = development_committee_empower_advertising_moderator("initdelegate", "alice", 86400)
    signed_ops = SignedTransaction.cast_operations_to_array_of_opklass([op])

    result_bin = b'1d0c696e697464656c6567617465805101000805616c696365'
    assert hexlify(bytes(signed_ops.data[0])) == result_bin


@pytest.mark.parametrize(
    'budget_type,result_bin',
    [
        ("post", b'2100000000000000006dcd3132e5df480a89a891984bca0a090c696e697464656c6567617465'),
        ("banner", b'2101000000000000006dcd3132e5df480a89a891984bca0a090c696e697464656c6567617465'),
    ]
)
def test_serialize_close_budget_by_advertising_moderator_to_byte(budget_type, result_bin):
    op = close_budget_by_advertising_moderator("6DCD3132-E5DF-480A-89A8-91984BCA0A09", "initdelegate", budget_type)
    signed_ops = SignedTransaction.cast_operations_to_array_of_opklass([op])
    assert hexlify(bytes(signed_ops.data[0])) == result_bin


@pytest.mark.parametrize(
    'budget_type,result_bin',
    [
        ("post", b'1d0c696e697464656c65676174658051010009025a003200'),
        ("banner", b'1d0c696e697464656c6567617465805101000a025a003200'),
    ]
)
def test_serialize_development_committee_change_budgets_auction_properties_to_byte(budget_type, result_bin):
    op = development_committee_change_budgets_auction_properties("initdelegate", 86400, [90, 50], budget_type)
    signed_ops = SignedTransaction.cast_operations_to_array_of_opklass([op])
    assert hexlify(bytes(signed_ops.data[0])) == result_bin


@pytest.mark.parametrize(
    'budget_type,result_bin',
    [
        ("post", b'2200000000000000006dcd3132e5df480a89a891984bca0a090c696e697464656c6567617465157b226d657461223a'
                 b'2022736f6d655f6d657461227d'),
        ("banner", b'2201000000000000006dcd3132e5df480a89a891984bca0a090c696e697464656c6567617465157b226d657461223a'
                   b'2022736f6d655f6d657461227d'),
    ]
)
def test_serialize_update_budget_to_byte(budget_type, result_bin):
    op = update_budget_operation(
        "6DCD3132-E5DF-480A-89A8-91984BCA0A09", "initdelegate", "{\"meta\": \"some_meta\"}", budget_type
    )
    signed_ops = SignedTransaction.cast_operations_to_array_of_opklass([op])
    assert hexlify(bytes(signed_ops.data[0])) == result_bin


@pytest.mark.parametrize(
    'budget_type,result_bin',
    [
        ("post", b'1b00000000000000006dcd3132e5df480a89a891984bca0a090c696e697464656c6567617465'),
        ("banner", b'1b01000000000000006dcd3132e5df480a89a891984bca0a090c696e697464656c6567617465'),
    ]
)
def test_serialize_close_budget_to_byte(budget_type, result_bin):
    op = close_budget_operation("6DCD3132-E5DF-480A-89A8-91984BCA0A09", "initdelegate", budget_type)
    signed_ops = SignedTransaction.cast_operations_to_array_of_opklass([op])
    assert hexlify(bytes(signed_ops.data[0])) == result_bin


def test_serialize_development_committee_empower_betting_moderator_to_byte():
    op = development_committee_empower_betting_moderator("initdelegate", "alice", 86400)
    signed_ops = SignedTransaction.cast_operations_to_array_of_opklass([op])

    result_bin = b'1d0c696e697464656c6567617465805101000b05616c696365'
    assert hexlify(bytes(signed_ops.data[0])) == result_bin
