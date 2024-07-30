from enum import Enum


PurseType = dict[str, int]


class PurseFields(str, Enum):
    GI = "gold_ingots"


def empty() -> PurseType:
    """Returns the empty purse (dict).

    Notes
    -----
    The task suggests the `empty(purse)` signature.
    However, passing the parametre is pointless,
    because the function must return an empty purse.
    So the incoming parametre does not take part in
    returning a new instance of the Purse type.
    Also, it might be better to return a `{PurseFields.GI: 0}`.
    However, technically it will not be an empty purse/dict.
    Returning an empty purse as an empty dictionary has benefits:
    the functions `add/get_ingots` should not make any assumptions
    on the structure of an empty purse, so it can be either `{}`
    or `{PurseFields.GI: 0}` and both are good to be processed correctly.

    Returns
    -------
    PurseType: an empty purse
    """

    return {}


def add_ingot(purse: PurseType) -> PurseType:
    """Returns a new purse with the incremented number of ingots.

    A new instance of the PurseType is returned.
    Such behaviour ensures the functional purity.

    Returns
    -------
    PurseType: a new instance of PurseType
    """

    ingots = purse.get(PurseFields.GI, 0)
    return {PurseFields.GI.value: ingots + 1}


def get_ingot(purse: PurseType) -> PurseType:
    """Returns a new purse with the decremented number of ingots.

    A new instance of the PurseType is returned.
    Such behaviour ensures the functional purity.

    Raises
    ------
    ValueError: getting an ingot from an empty purse

    Returns
    -------
    PurseType: a new instance of PurseType
    """

    ingots = purse.get(PurseFields.GI, 0)
    if not ingots:
        raise ValueError("cannot get more from an already empty purse")
    return {PurseFields.GI.value: ingots - 1}
