import pytest

from scorum.graphenebase.operationids import Operations, ProposalOperations, operations


@pytest.mark.parametrize('name, op', [
    ('transfer', Operations.transfer),
    ('hardfork', Operations.hardfork),
    ('bets_matched', Operations.bets_matched),
    ('registration_committee_add_member', ProposalOperations.registration_committee_add_member)
])
def test_string_to_operation(name, op):
    assert operations[name] == op


@pytest.mark.parametrize('name, value', [
    ('transfer', 2),
    ('bets_matched', 65),
    ('registration_committee_add_member', 0)
])
def test_serialize(name, value):
    x = operations[name]

    assert x.value == value
    assert x.name == name

    assert int(x) == value
    assert str(x) == name
