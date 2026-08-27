# Random library:
import random

# Pillow library annotations:
from PIL import Image, ImageColor

# Settings instance:
from app.settings import SETTINGS

# Timestamp function:
from app.scripts.timestamp import timestamp


def create_canvas(bingo_card_list: list[Image.Image], random_bg: bool = True) -> Image.Image:
    
    # Selecting canvas color:
    if random_bg:
        canvas_color_list: tuple[str, ...] = tuple(color for color, _ in ImageColor.colormap.items())
        canvas_color: str = random.choice(canvas_color_list)
    else:
        canvas_color: str = SETTINGS.CANVAS_BACKGROUND_COLOR

    # Creating canvas
    canvas_image = Image.new(
        mode = SETTINGS.RENDER_MODE,
        size = (SETTINGS.CANVAS_WIDHT, SETTINGS.CANVAS_HEIGHT),
        color = canvas_color
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

