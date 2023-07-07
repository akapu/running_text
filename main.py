import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

def main():
    WIDTH = 100
    HEIGHT = 100
    LAYERS = 3

    FPS = 60
    DURATION = 3
    TOTAL_FRAMES = DURATION * FPS

    FILENAME = "running_text.mp4"
    CODECNAME = "vp09"

    TEXT = "Р"
    H_PAD = 5
    V_PAD = 5
    FONT = ImageFont.truetype("Jura.ttf", HEIGHT - 2*V_PAD)
    TEXT_WIDTH = int(FONT.getlength(TEXT))

    video = cv2.VideoWriter(
        FILENAME,
        cv2.VideoWriter_fourcc(*CODECNAME),
        FPS,
        (WIDTH, HEIGHT)
    )

    total_shift = 0

    if TEXT_WIDTH > (WIDTH - 2*H_PAD):
        total_shift = WIDTH - TEXT_WIDTH - 2*H_PAD

    for i in range(TOTAL_FRAMES):
        img_pil = Image.new("RGB", (WIDTH, HEIGHT))
        img_drw = ImageDraw.Draw(img_pil)

        shift = int((i / (TOTAL_FRAMES - 1)) * total_shift)
        
        img_drw.text(
                (H_PAD + shift, V_PAD), 
                TEXT,
                font=FONT,
                fill=(255, 255, 255)
        )

        img = np.array(img_pil)

        video.write(img)

    video.release()


if __name__ == "__main__":
    main()
