import cv2
import numpy as np

def main():
    WIDTH = 100
    HEIGHT = 100
    LAYERS = 3

    FPS = 60
    DURATION = 3

    FILENAME = "running_text.mp4"
    CODECNAME = "vp09"

    background = np.zeros((WIDTH, HEIGHT, LAYERS), dtype=np.uint8)

    fourcc = cv2.VideoWriter_fourcc(*CODECNAME)

    video = cv2.VideoWriter(
        FILENAME,
        fourcc,
        FPS,
        (WIDTH, HEIGHT))

    for i in range(DURATION * FPS):
        video.write(background)

    video.release()


if __name__ == "__main__":
    main()
