import cv2

def spinning_filter(input_pipe, output_pipe):
    angle = 0
    while True:
        frame = input_pipe.pull()
        if frame is None:
            output_pipe.push(None)
            break

        (h, w) = frame.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated_frame = cv2.warpAffine(frame, M, (w, h))
        angle += 1
        output_pipe.push(rotated_frame)
