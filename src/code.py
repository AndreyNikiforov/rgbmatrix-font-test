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
    from adafruit_display_text.label import Label
    label = Label(
        font, 
        text=text,
        color=0xFF0000,
        scale=1,
    )
    label.x = 0
    label.y = 16
    return label

def get_main_font():
    from adafruit_bitmap_font import bitmap_font
    font = bitmap_font.load_font("fonts/font_league_spartan_vf_30_latin1.pcf")
    return font

release_displays()

matrix = get_matrix()
display = get_display(matrix)
font = get_font()
label = get_label(font, "Test")
display.root_group = label

while(True):
    pass
