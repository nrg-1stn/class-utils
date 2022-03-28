from pygame.font import Font, SysFont


def get_dynamic_font(
    max_width: int, max_height: int, text: str, font_type: str, max_font_size: int
) -> Font:
    low = 1
    high = max_font_size

    while low < high:
        font_size = (low + high) // 2
        font = SysFont(font_type, font_size)

        text_surf = font.render(text, True, (0, 0, 0))

        if text_surf.get_width() > max_width or text_surf.get_height() > max_height:
            high = font_size - 1
        else:
            low = font_size + 1

    return font
