EXPECTED_BAKE_TIME = 40


def bake_time_remaining(number_of_time):
    """
    Calculate the bake time remaining.

    :return: int - remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - number_of_time


def preparation_time_in_minutes(preparation_time):
    """
    Calculate the preparation time.

    :param preparation_time:
    :return: int - remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    function that takes the actual minutes the lasagna has been in the oven as an argument
    and returns how many minutes the lasagna still needs to bake based on the EXPECTED_BAKE_TIME
    """

    return preparation_time * 2


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Return elapsed cooking time.

    This function takes two numbers representing the number of layers & the time already spent
    baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
