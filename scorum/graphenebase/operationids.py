from enum import Enum


class AutoNumber(Enum):
    def __new__(cls):
        value = len(cls.__members__) if len(cls.__members__) else 0
        obj = object.__new__(cls)
        obj._value_ = value
        return obj


class OperationsBase(AutoNumber):
    def __str__(self):
        return self.name

    def __int__(self):
        return self.value


class Operations(OperationsBase):
    vote = ()
    comment = ()

    transfer = ()
    transfer_to_scorumpower = ()
    withdraw_scorumpower = ()

    account_create_by_committee = ()
    account_create = ()
    account_create_with_delegation = ()
    account_update = ()

    witness_update = ()
    account_witness_vote = ()
    account_witness_proxy = ()

    delete_comment = ()
    comment_options = ()
    set_withdraw_scorumpower_route_to_account = ()
    set_withdraw_scorumpower_route_to_dev_pool = ()

    prove_authority = ()

    request_account_recovery = ()
    recover_account = ()
    change_recovery_account = ()
    escrow_approve = ()
    escrow_dispute = ()
    escrow_release = ()
    escrow_transfer = ()

    decline_voting_rights = ()
    delegate_scorumpower_shares = ()

    create_budget = ()
    close_budget = ()

    proposal_vote = ()
    proposal_create = ()

    atomicswap_initiate = ()
    atomicswap_redeem = ()
    atomicswap_refund = ()

    close_budget_by_advertising_moderator = ()
    update_budget = ()

    # betting
    create_game = ()
    cancel_game = ()
    update_game_markets = ()
    update_game_start_time = ()
    post_game_results = ()

    post_bet = ()
    cancel_pending_bets = ()

    # virtual operations
    author_reward = ()
    comment_benefactor_reward = ()
    comment_payout_update = ()
    comment_reward = ()
    curation_reward = ()
    hardfork = ()
    producer_reward = ()
    active_sp_holders_reward = ()
    return_scorumpower_delegation = ()
    shutdown_witness = ()
    witness_miss_block = ()
    expired_contract_refund = ()
    acc_finished_vesting_withdraw = ()
    devpool_finished_vesting_withdraw = ()
    acc_to_acc_vesting_withdraw = ()
    devpool_to_acc_vesting_withdraw = ()
    acc_to_devpool_vesting_withdraw = ()
    devpool_to_devpool_vesting_withdraw = ()
    proposal_virtual = ()

    budget_outgo = ()
    budget_owner_income = ()
    active_sp_holders_reward_legacy = ()
    budget_closing = ()

    bets_matched = ()
    game_status_changed = ()
    bet_resolved = ()
    bet_cancelled = ()


class ProposalOperations(OperationsBase):
    registration_committee_add_member = ()
    registration_committee_exclude_member = ()
    registration_committee_change_quorum = ()
    development_committee_add_member = ()
    development_committee_exclude_member = ()
    development_committee_change_quorum = ()
    development_committee_withdraw_vesting = ()
    development_committee_transfer = ()
    development_committee_empower_advertising_moderator = ()
    development_committee_change_post_budgets_auction_properties = ()
    development_committee_change_banner_budgets_auction_properties = ()


operations = {k: v for Ops in [Operations, ProposalOperations] for k, v in Ops.__members__.items()}
