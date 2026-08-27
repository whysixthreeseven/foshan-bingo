# Canvas script:
from canvas import create_canvas
from card import create_card
from populate import generate_options


def run():
    bingo_options: tuple[str, ...] = generate_options(
        permanent_option_limit = 0,
        ignore_assertion = False,
        )
    bing_card_list: list = [create_card(bingo_text = option) for option in bingo_options]
    create_canvas(bingo_card_list = bing_card_list)


if __name__ == "__main__":
    run()
    
    