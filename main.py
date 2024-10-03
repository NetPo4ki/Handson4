import cv2
import threading
from pipe import Pipe
from filters.black_white import black_white_filter
from filters.mirror import mirror_filter
from filters.spinning import spinning_filter
from filters.blur import blur_filter

def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        return

    pipe1 = Pipe()
    pipe2 = Pipe()
    pipe3 = Pipe()
    pipe4 = Pipe()

    threading.Thread(target=black_white_filter, args=(pipe1, pipe2)).start()
    threading.Thread(target=mirror_filter, args=(pipe2, pipe3)).start()
    threading.Thread(target=blur_filter, args=(pipe3, pipe4)).start()
    threading.Thread(target=spinning_filter, args=(pipe4, pipe1)).start()

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        pipe1.push(frame)

        processed_frame = pipe4.pull()

        if processed_frame is None:
            break

        cv2.imshow('Processed video', processed_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            pipe1.push(None)
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
