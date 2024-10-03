import cv2

def black_white_filter(input_pipe, output_pipe):
    while True:
        frame = input_pipe.pull()
        if frame is None:
            output_pipe.push(None)
            break

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_frame = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2BGR)
        output_pipe.push(gray_frame)
