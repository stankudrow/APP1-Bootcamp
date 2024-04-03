import purse


def split_booty(
    *purses: purse.PurseType,
) -> tuple[purse.PurseType, purse.PurseType, purse.PurseType]:
    """Returns the tuple of three purses with the booty split.

    The function returns three purses (dictionaries)
    such that in any two of the three purses
    the difference between the number of ingots is not greater than 1.

    Returns
    -------
    tuple[purse.PurseType, purse.PurseType, purse.PurseType]: the booty split
    """

    total_ingots: int = 0
    for purse_ in purses:
        total_ingots += purse_.get(purse.INGOTS, 0)

    purses_split = []
    for divisor in range(3, 0, -1):
        part = total_ingots // divisor
        purses_split.append({purse.INGOTS: part})
        total_ingots -= part

    return (
        purses_split[0],
        purses_split[1],
        purses_split[2],
    )
