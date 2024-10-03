import cv2

def blur_filter(input_pipe, output_pipe):
    while True:
        frame = input_pipe.pull()
        if frame is None:
            output_pipe.push(None)
            break

        blurred_frame = cv2.GaussianBlur(frame, (15, 15), 0)
        output_pipe.push(blurred_frame)
