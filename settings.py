class __SETTINGS:
    
    # Options
    BINGO_OPTIONS_PERMANENT: int = 2
    BINGO_OPTIONS_COUNT: int = 9
    
    # Image settings:
    CARD_SIDE_LEN: int = 300
    CARD_MARGIN_MODIFIER: float = 0.02
    CARD_MARGIN_LEN: int = int(CARD_SIDE_LEN * CARD_MARGIN_MODIFIER)
    CARD_COUNT_PER_ROW: int = 3
    CARD_COUNT_PER_COLUMN: int = 3
    CARD_BACKGROUND_COLOR: str = "white"
    CARD_TEXT_COLOR: str = "black"
    CARD_FONT_NAME: str = "arial.ttf"
    CARD_FONT_SIZE: int = 24
    
    # Canvas settings:
    CAVNAS_BACKGROUND_COLOR: str = "black"
    CANVAS_BINGO_SIDE_LEN: int = int(
        CARD_SIDE_LEN * CARD_COUNT_PER_ROW +
        CARD_MARGIN_LEN * (CARD_COUNT_PER_ROW + 1)
        )
    CANVAS_WIDHT: int = CANVAS_BINGO_SIDE_LEN
    CANVAS_HEIGHT: int = CANVAS_BINGO_SIDE_LEN
    CANVAS_SAVE_FILENAME: str = "fonshan_bingo"
    CANVAS_SAVE_EXTENSION: str = "png"
    
    # Render settings:
    RENDER_MODE: str = "RGB"
    

# Initializing settings class instance:
SETTINGS = __SETTINGS()

