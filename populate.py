# Random library:
import random

# Importing bingo option lists and settings:
from list import RANDOM_OPTIONS, PERMANENT_OPTIONS
from settings import SETTINGS


def __validate_param(validate_value: int) -> None:
    
    # Assertion control:
    assert isinstance(validate_value, int), "Parameter must be integer."
    assert validate_value >= 0, "Parameter must be positive."
    assert validate_value <= SETTINGS.BINGO_OPTIONS_PERMANENT, f"Parameter must be less or equal to {SETTINGS.BINGO_OPTIONS_PERMANENT}"


def generate_options(permanent_option_limit: int = 0, ignore_assertion: bool = False) -> tuple[str, ...]:
    
    # Validating value:
    if not ignore_assertion:
        __validate_param(validate_value = permanent_option_limit)
    
    # Preparing variables:
    options: list[str] = []
            
    # Adding permanent options:
    if permanent_option_limit == 0:
        options: list[str] = [entry for entry in PERMANENT_OPTIONS]
    else:
        while len(options) < permanent_option_limit:
            for entry in PERMANENT_OPTIONS:
                options.append(entry)
    
    # Selecting random options and adding:
    while len(options) < SETTINGS.BINGO_OPTIONS_COUNT:
        entry_random: str = random.choice(RANDOM_OPTIONS)
        if entry_random not in options:
            options.append(entry_random)
            
    # Shuffling and converting options:
    random.shuffle(options)
    options_converted: tuple[str, ...] = tuple(options)
            
    # Returning:
    return options_converted

