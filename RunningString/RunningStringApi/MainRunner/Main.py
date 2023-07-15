import cv2
import numpy as np

from cache.get_path import path

frameSize = (100, 100)


def cut_frame(s: str, start_pos: int = 0, frame_size: int = None) -> str:
    frame_size = frame_size or len(s)
    left_space = ' ' * min(start_pos, frame_size)
    if start_pos < 0:
        s = s[-start_pos:]
    return f'{(left_space + s)[:frame_size]:{frame_size}}'


def parse(s: str):
    s = s.split('#')
    s[1] = s[1].split(',')
    s[2] = s[2].split(',')
    for i in range(0, 3):
        s[1][i] = int(s[1][i])
        s[2][i] = int(s[2][i])
    return s


frameSize = (100, 100)


def run(s: str):
    s = parse(s)
    out = cv2.VideoWriter(r''+ path + '\output_video.mp4',
                          cv2.VideoWriter_fourcc(*'mp4v'), len(s[0]) / 2, frameSize)
    lenth = len(s[0])

    for i in range(-lenth + 1, lenth)[::-1]:
        img = np.full((100, 100, 3), s[2], dtype=np.uint8)
        substring = str.format(cut_frame(s[0], i, lenth))
        img = cv2.putText(img, substring, (0, 60), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=2, color=s[1],
                          thickness=2)
        out.write(img)

    out.release()

# run("раз два три четыре пять#255,255,255#0, 0, 0")
