import cv2
from tqdm import tqdm
import numpy as np
from datetime import timedelta

OPTIONS = {
    "format": "bestvideo",
    "extractaudio": False,
}


class SZException(Exception):
    pass


def get_properties(cap):
    props = dict()
    props["is_stream"] = False
    try:
        cap = cap.stream
        props["is_stream"] = True
    except AttributeError:
        pass

    props["width"] = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    props["height"] = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    props["frames"] = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    props["fps"] = cap.get(cv2.CAP_PROP_FPS)

    print(f"Capture properties:")
    print(f"Width: {props['width']}")
    print(f"Height: {props['height']}")
    print(f"FPS: {props['fps']}")
    print(f"Total Frames: {props['frames']}")
    print(f"Length: {timedelta(seconds=props['frames']/props['fps'])}")
    print()

    return props