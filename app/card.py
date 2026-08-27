# Pillow library:
from PIL import Image, ImageDraw, ImageFont

# Settings import:
from app.settings import SETTINGS


def create_card(bingo_text: str) -> Image:
    
    # Creating card image object:
    card_size: tuple[int, int] = (SETTINGS.CARD_SIDE_LEN, SETTINGS.CARD_SIDE_LEN)
    card_image: Image = Image.new(
        mode = SETTINGS.RENDER_MODE,
        size = card_size,
        color = SETTINGS.CARD_BACKGROUND_COLOR
        )
    
    # Drawing card:
    card_draw = ImageDraw.Draw(card_image)
    card_draw.rectangle(
        (0, 0, SETTINGS.CARD_SIDE_LEN - 1, SETTINGS.CARD_SIDE_LEN - 1),
        outline = None,
        width = 0
        )
    
    # Creating text font:
    text_font = ImageFont.truetype(
        SETTINGS.CARD_FONT_NAME, 
        SETTINGS.CARD_FONT_SIZE
        )
    
    # Drawing bingo text:
    card_bbox = card_draw.textbbox((0, 0), bingo_text, text_font)
    text_width = card_bbox[2] - card_bbox[0]
    text_height = card_bbox[3] - card_bbox[1]
    text_coordinate_x = (SETTINGS.CARD_SIDE_LEN - text_width) / 2
    text_coordinate_y = (SETTINGS.CARD_SIDE_LEN - text_height) / 2
    
    # Adding text to card image:
    card_draw.text(
        (text_coordinate_x, text_coordinate_y),
        bingo_text,
        fill = SETTINGS.CARD_TEXT_COLOR,
        font = text_font,
        align = "center"
        )
    
    # Returning:
    return card_image

