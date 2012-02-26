"""
Resulting paper model schema:
                                    Head
            Right arm             +-------+             Left arm
          +-----------+           |       |           +-----------+
          | inward    |           | back  |           | inward    |
          +-----------+           |       |           +-----------+
          | back      |   +-------+-------+-------+   | back      |
      +---+-----------+---+       |       |       +---+-----------+---+
 hand |   | otwrad    |   | right | top   | left  |   | outside   |   | hand
      +---+-----------+---+       |       |       +---+-----------+---+
          | front     |   +-------+-------+-------+   | front     |
          +-----------+ ^shoulder |       | shoulder^ +-----------+
                                  | front |                    
                                  |       |                    
                    bottom font > +-------+   +-------+ < bottom back
                              +---+-------+---+-------+
                              | r |       | l |       |
                              | i |       | e |       |
                    Body >    | g | front | f | back  |
                              | h |       | t |       |
                              | t |       |   |       |
                              +---+---+---+---+---+---+
                              | o | f | f | o | f | f |
                              | u | r | r | u | r | r |
                              | t | o | o | t | o | o |
                              | w | n | n | w | n | n |
                              | . | t | t | . | t | t |
                              +---+---+---+---+---+---+
                           foot > |   |   | < foot
                                  +---+---+

"""

try:
    from PIL import Image
except ImportError:
    import Image

import sys

parts = {
    "head_top":    ( 8, 0, 16,  8),
    "head_bottom": (16, 0, 24,  8),
    "head_right":  ( 0, 8,  8, 16),
    "head_front":  ( 8, 8, 16, 16),
    "head_left":   (16, 8, 24, 16),
    "head_back":   (24, 8, 32, 16),

    "accessory_top":    (40, 0, 48,  8),
    "accessory_bottom": (48, 0, 64,  8),
    "accessory_right":  (32, 8, 40, 16),
    "accessory_front":  (40, 8, 48, 16),
    "accessory_left":   (48, 8, 56, 16),
    "accessory_back":   (56, 8, 64, 16),

    "leg_top":    ( 4, 16,  8, 20),
    "leg_bottom": ( 8, 16, 12, 20),
    "leg_out":    ( 0, 20,  4, 32),
    "leg_front":  ( 4, 20,  8, 32),
    "leg_in":     ( 8, 20, 12, 32),
    "leg_back":   (12, 20, 16, 32),

    "body_top":    (20, 16, 28, 20),
    "body_bottom": (28, 16, 36, 20),
    "body_right":  (16, 20, 20, 32),
    "body_front":  (20, 20, 28, 32),
    "body_left":   (28, 20, 32, 32),
    "body_back":   (32, 20, 40, 32),

    "arm_top":    (44, 16, 48, 20),
    "arm_bottom": (48, 16, 52, 20),
    "arm_out":    (40, 20, 44, 32),
    "arm_front":  (44, 20, 48, 32),
    "arm_in":     (48, 20, 52, 32),
    "arm_back":   (52, 20, 56, 32),
}

def main(argv):
    infile = argv[0]
    image = Image.open(infile)
    tpl = Image.new(image.mode,(64,64))
    # HEAD
    tpl.paste(image.crop(parts["head_top"]), (8,8))
    tpl.paste(image.crop(parts["head_right"]), (0,16))
    tpl.paste(image.crop(parts["head_front"]), (8,16))
    tpl.paste(image.crop(parts["head_left"]), (16,16))
    tpl.paste(image.crop(parts["head_bottom"]), (8,24))
    head_back=image.crop(parts["head_back"]).transpose(Image.ROTATE_180)
    tpl.paste(head_back, (8,0))
    tpl.save("template.png")

if __name__ == "__main__":
    main(sys.argv[1:])
