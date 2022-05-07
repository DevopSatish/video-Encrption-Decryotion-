import cv2

FILENAME_RAW = "raw/{}.mp4"
FILENAME_ENC = "enc/{}_enc.mp4"
FILENAME_DEC = "dec/{}_dec.mp4"
FILENAME_SHUF_ORDER = "shuf/{}_shuf_order"


def get_properties(cap):
    is_stream = False
    try:
        cap = cap.stream
        is_stream = True
    except AttributeError:
        pass

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    return is_stream, width, height, fps, frames