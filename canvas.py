# Pillow library annotations:
from PIL import Image

# Settings instance:
from settings import SETTINGS

# Timestamp function:
from timestamp import timestamp


def create_canvas(bingo_card_list: list[Image.Image]) -> Image.Image:

    # Creating canvas
    canvas_image = Image.new(
        mode = SETTINGS.RENDER_MODE,
        size = (SETTINGS.CANVAS_WIDHT, SETTINGS.CANVAS_HEIGHT),
        color = SETTINGS.CAVNAS_BACKGROUND_COLOR
        )

    # Placing cards
    for index, card in enumerate(bingo_card_list):
        
        # Calculating positions:
        row = index // SETTINGS.CARD_COUNT_PER_ROW
        column = index % SETTINGS.CARD_COUNT_PER_ROW

        coordinate_x = (
            SETTINGS.CARD_MARGIN_LEN + 
            column * (SETTINGS.CARD_SIDE_LEN + SETTINGS.CARD_MARGIN_LEN)
            )
        coordinate_y = (
            SETTINGS.CARD_MARGIN_LEN + 
            row * (SETTINGS.CARD_SIDE_LEN + SETTINGS.CARD_MARGIN_LEN)
            )

        # Adding card to canvas image:
        canvas_image.paste(card, (coordinate_x, coordinate_y))

    # Saving canvas image:
    canvas_filename: str = "{filename}_{timestamp}.{extension}".format(
        filename = SETTINGS.CANVAS_SAVE_FILENAME,
        timestamp = timestamp(),
        extension = SETTINGS.CANVAS_SAVE_EXTENSION
        )
    canvas_image.save(canvas_filename)

    # Returning:
    return canvas_image

