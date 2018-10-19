try:
    from . import operations
    from . import PublicKey
    from .amount import Amount
except (ImportError, SystemError):
    import operations
    import PublicKey
    from amount import Amount


def transfer_operation(_from, to, amount: Amount, memo):
    return operations.Transfer(
        **{"from": _from,
           "to": to,
           "amount": str(amount),
           "memo": memo
           })


def transfer_to_scorumpower_operation(_from, to, amount: Amount):
    return operations.TransferToScorumpower(
        **{'from': _from,
           'to': to,
           'amount': str(amount)
           })


def withdraw(account: str, scorumpower: Amount):
    return operations.WithdrawScorumpower(**{"account": account, "scorumpower": str(scorumpower)})


def devpool_withdraw_vesting(account: str, amount: Amount, lifetime: int):
    return operations.ProposalCreate(**{
        "creator": account, "lifetime_sec": lifetime,
        "operation": operations.DevelopmentCommitteeWithdrawVesting(**{"amount": str(amount)})
    })


def proposal_vote_operation(account: str, proposal_id: int):
    return operations.ProposalVote(**{
        "voting_account": account, "proposal_id": proposal_id
    })


def account_create_operation(
    creator: str,
    fee: Amount,
    name: str,
    owner: str,
    active: str,
    posting: str,
    memo,
    json_meta,
    additional_owner_accounts,
    additional_active_accounts,
    additional_posting_accounts,
    additional_owner_keys,
    additional_active_keys,
    additional_posting_keys
):
    creation_fee = str(fee)

    owner_pubkey = owner if type(owner) is PublicKey else PublicKey(owner)
    active_pubkey = active if type(active) is PublicKey else PublicKey(active)
    posting_pubkey = posting if type(posting) is PublicKey else PublicKey(posting)
    memo_pubkey = memo if type(memo) is PublicKey else PublicKey(memo)

    owner_key_authority = [[str(owner_pubkey), 1]]
    active_key_authority = [[str(active_pubkey), 1]]
    posting_key_authority = [[str(posting_pubkey), 1]]
    owner_accounts_authority = []
    active_accounts_authority = []
    posting_accounts_authority = []

    for k in additional_owner_keys:
        owner_key_authority.append([k, 1])
    for k in additional_active_keys:
        active_key_authority.append([k, 1])
    for k in additional_posting_keys:
        posting_key_authority.append([k, 1])

    for k in additional_owner_accounts:
        owner_accounts_authority.append([k, 1])
    for k in additional_active_accounts:
        active_accounts_authority.append([k, 1])
    for k in additional_posting_accounts:
        posting_accounts_authority.append([k, 1])
    return operations.AccountCreate(
        **{'fee': creation_fee,
           'creator': creator,
           'new_account_name': name,
           'owner': {'account_auths': owner_accounts_authority,
                     'key_auths': owner_key_authority,
                     'weight_threshold': 1},
           'active': {'account_auths': active_accounts_authority,
                      'key_auths': active_key_authority,
                      'weight_threshold': 1},
           'posting': {'account_auths': posting_accounts_authority,
                       'key_auths': posting_key_authority,
                       'weight_threshold': 1},
           'memo_key': str(memo_pubkey),
           'json_metadata': json_meta}
    )


def account_create_by_committee_operation(
    creator: str,
    name: str,
    owner: str,
    active: str,
    posting: str,
    memo,
    json_meta,
    additional_owner_accounts,
    additional_active_accounts,
    additional_posting_accounts,
    additional_owner_keys,
    additional_active_keys,
    additional_posting_keys
):

    owner_pubkey = owner if type(owner) is PublicKey else PublicKey(owner)
    active_pubkey = active if type(active) is PublicKey else PublicKey(active)
    posting_pubkey = posting if type(posting) is PublicKey else PublicKey(posting)
    memo_pubkey = memo if type(memo) is PublicKey else PublicKey(memo)

    owner_key_authority = [[str(owner_pubkey), 1]]
    active_key_authority = [[str(active_pubkey), 1]]
    posting_key_authority = [[str(posting_pubkey), 1]]
    owner_accounts_authority = []
    active_accounts_authority = []
    posting_accounts_authority = []

    for k in additional_owner_keys:
        owner_key_authority.append([k, 1])
    for k in additional_active_keys:
        active_key_authority.append([k, 1])
    for k in additional_posting_keys:
        posting_key_authority.append([k, 1])

    for k in additional_owner_accounts:
        owner_accounts_authority.append([k, 1])
    for k in additional_active_accounts:
        active_accounts_authority.append([k, 1])
    for k in additional_posting_accounts:
        posting_accounts_authority.append([k, 1])
    return operations.AccountCreateByCommittee(
        **{'creator': creator,
           'new_account_name': name,
           'owner': {'account_auths': owner_accounts_authority,
                     'key_auths': owner_key_authority,
                     'weight_threshold': 1},
           'active': {'account_auths': active_accounts_authority,
                      'key_auths': active_key_authority,
                      'weight_threshold': 1},
           'posting': {'account_auths': posting_accounts_authority,
                       'key_auths': posting_key_authority,
                       'weight_threshold': 1},
           'memo_key': str(memo_pubkey),
           'json_metadata': json_meta}
    )


def account_witness_vote_operation(account, witness, approve):
    return operations.AccountWitnessVote(
        **{'account': account,
           'witness': witness,
           'approve': approve}
    )


def create_budget_operation(uuid, owner, json_metadata, balance: Amount, start, deadline, type):
    return operations.CreateBudget(
        **{'uuid': uuid,
           'owner': owner,
           'json_metadata': json_metadata,
           'balance': str(balance),
           'start': start,
           'deadline': deadline,
           'type': type}
    )


def close_budget_operation(uuid, owner, type):
    return operations.CloseBudget(
        **{'owner': owner,
           'uuid': uuid,
           'type': type}
    )


def update_budget_operation(uuid, owner, json_metadata, type):
    return operations.UpdateBudget(
        **{'type': type,
           'uuid': uuid,
           'owner': owner,
           'json_metadata': json_metadata}
    )


def invite_new_committee_member(inviter, invitee, lifetime_sec):
    return operations.ProposalCreate(
        **{'creator': inviter,
           'data': invitee,
           'action': 'invite',
           'lifetime_sec': lifetime_sec
           }
    )


def witness_update_operation(owner, url, block_signing_key, props: dict):
    return operations.WitnessUpdate(
        **{'owner': owner,
           'url': url,
           'block_signing_key': block_signing_key,
           'props': props}
    )


def vote_operation(voter, author, permlink, weight):
    return operations.Vote(
        **{'voter': voter,
           'author': author,
           'permlink': permlink,
           'weight': weight}
    )


def post_comment_operation(author, permlink, parent_author, parent_permlink, title, body, json_metadata):
    return operations.Comment(
        **{'parent_author': parent_author,
           'parent_permlink': parent_permlink,
           'author': author,
           'permlink': permlink,
           'title': title,
           'body': body,
           'json_metadata': json_metadata}
    )


def delegate_scorumpower(delegator, delegatee, scorumpower):
    return operations.DelegateScorumPower(
        **{'delegator': delegator,
           'delegatee': delegatee,
           'scorumpower': str(scorumpower)}
    )


def create_game(uuid, moderator, name, start_time, auto_resolve_delay_sec, game, markets):
    return operations.CreateGame(**{
        'uuid': uuid,
        'moderator': moderator,
        'name': name,
        'start_time': start_time,
        'auto_resolve_delay_sec': auto_resolve_delay_sec,
        'game': game,
        'markets': markets
    })


def cancel_game(uuid, moderator):
    return operations.CancelGame(**{
        'uuid': uuid,
        'moderator': moderator
    })


def update_game_start_time(uuid, moderator, start_time):
    return operations.UpdateGameStartTime(**{
        'uuid': uuid,
        'moderator': moderator,
        'start_time': start_time
    })


def development_committee_empower_advertising_moderator(initiator, moderator, lifetime_sec):
    return operations.ProposalCreate(
        **{
            "creator": initiator,
            "lifetime_sec": lifetime_sec,
            "operation": operations.DevelopmentCommitteeEmpowerAdvertisingModerator(**{"account": moderator})
        }
    )


def development_committee_change_budgets_auction_properties(initiator, lifetime, coeffs, type):
    change_budget_op = operations.DevelopmentCommitteeChangePostBudgetsAuctionProperties
    if type == "banner":
        change_budget_op = operations.DevelopmentCommitteeChangeBannerBudgetsAuctionProperties

    return operations.ProposalCreate(
        **{
            "creator": initiator,
            "lifetime_sec": lifetime,
            "operation": change_budget_op(**{"coeffs": coeffs})
        }
    )


def close_budget_by_advertising_moderator(uuid, moderator, type):
    return operations.CloseBudgetByAdvertisingModerator(
        **{
            "moderator": moderator,
            "uuid": uuid,
            "type": type
        }
    )


def development_committee_empower_betting_moderator(initiator, moderator, lifetime_sec):
    return operations.ProposalCreate(
        **{
            "creator": initiator,
            "lifetime_sec": lifetime_sec,
            "operation": operations.DevelopmentCommitteeEmpowerBettingModerator(**{"account": moderator})
        }
    )


def development_committee_change_betting_resolve_delay(initiator, delay_sec, lifetime_sec):
    return operations.ProposalCreate(
        **{
            "creator": initiator,
            "lifetime_sec": lifetime_sec,
            "operation": operations.DevelopmentCommitteeChangeBettingResolveDelay(**{"delay_sec": delay_sec})
        }
    )
