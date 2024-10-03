import cv2

def mirror_filter(input_pipe, output_pipe):
    while True:
        frame = input_pipe.pull()
        if frame is None:
            output_pipe.push(None)
            break

        mirror_frame = cv2.flip(frame, 1)
        output_pipe.push(mirror_frame)
