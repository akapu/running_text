import cv2
import numpy as np

def main():
    WIDTH = 100
    HEIGHT = 100
    LAYERS = 3

    FPS = 60
    DURATION = 3
    TOTAL_FRAMES = DURATION * FPS

    FILENAME = "running_text.mp4"
    CODECNAME = "vp09"

    FONTSCALE = 3
    FONT = cv2.FONT_HERSHEY_DUPLEX
    THICKNESS = 1
    TEXT = "it-solution.ru akapu"
    TEXT_SIZE, _ = cv2.getTextSize(
        TEXT,
        FONT,
        FONTSCALE,
        THICKNESS
    )
    H_PAD = 5
    BOTTOM_PAD = 5

    video = cv2.VideoWriter(
        FILENAME,
        cv2.VideoWriter_fourcc(*CODECNAME),
        FPS,
        (WIDTH, HEIGHT)
    )

    for i in range(TOTAL_FRAMES):
        img = np.zeros((WIDTH, HEIGHT, LAYERS), dtype=np.uint8)

        shift = int((i / (TOTAL_FRAMES - 1)) * (WIDTH - TEXT_SIZE[0] - 2*H_PAD))

        cv2.putText(
            img,
            TEXT,
            (H_PAD + shift, HEIGHT - BOTTOM_PAD),
            FONT,
            FONTSCALE,
            (255, 255, 255),
            THICKNESS,
            cv2.FILLED
        )

        video.write(img)

    video.release()


if __name__ == "__main__":
    main()
