import time

def release_displays():
    import displayio
    # release any currently configured displays
    displayio.release_displays()

def get_matrix():
    import board
    import rgbmatrix
    matrix = rgbmatrix.RGBMatrix(
        width=64, bit_depth=4,
        rgb_pins=[
            board.MTX_R1,
            board.MTX_G1,
            board.MTX_B1,
            board.MTX_R2,
            board.MTX_G2,
            board.MTX_B2
        ],
        addr_pins=[
            board.MTX_ADDRA,
            board.MTX_ADDRB,
            board.MTX_ADDRC,
            board.MTX_ADDRD
        ],
        clock_pin=board.MTX_CLK,
        latch_pin=board.MTX_LAT,
        output_enable_pin=board.MTX_OE
    )
    return matrix

def get_display(matrix):
    import framebufferio
    display = framebufferio.FramebufferDisplay(matrix)
    return display

def get_font():
    import terminalio
    return terminalio.FONT

def get_label(font, text):
    from adafruit_display_text.scrolling_label import ScrollingLabel
    label = ScrollingLabel(
        font, 
        text=text,
        color=0xFF0000,
        scale=1,
        max_characters=len(text),
        animate_time=0.2
    )
    label.x = 0
    label.y = 16
    return label

def get_main_font():
    from adafruit_bitmap_font import bitmap_font
    font = bitmap_font.load_font("fonts/font_league_spartan_vf_30_latin1.pcf")
    return font

def load_font(font_name):
    from adafruit_bitmap_font import bitmap_font
    font = bitmap_font.load_font(f"fonts/{font_name}/font.pcf")
    return font

def find_fonts():
    import os
    font_files = [f for f in os.listdir("fonts") if not f.startswith(".")]
    return font_files

release_displays()

matrix = get_matrix()
display = get_display(matrix)
font = get_font()
label = get_label(font, "Test")
display.root_group = label

fonts = find_fonts()

font_index = 0
last_update = time.monotonic()
while(True):
    label.update()
    if time.monotonic() - last_update > 8:
        if font_index == len(fonts):
            font_index = 0
        font_name = fonts[font_index]
        font = load_font(font_name)
        label = get_label(font, font_name)
        display.root_group = label
        font_index = font_index + 1
        last_update = time.monotonic()

