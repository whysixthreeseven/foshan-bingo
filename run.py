# Modules and scripts:
from app.canvas import create_canvas
from app.card import create_card
from app.scripts.populate import generate_options


# Main entry function:
def run():
    bingo_options: tuple[str, ...] = generate_options(
        permanent_option_limit = 0,
        ignore_assertion = True,
        )
    bing_card_list: list = [create_card(bingo_text = option) for option in bingo_options]
    create_canvas(
        bingo_card_list = bing_card_list,
        random_bg = False
        )


# Running application:
if __name__ == "__main__":
    run()
    
    