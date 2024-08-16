"""
Cam = CameraNode()
Cam.run()
frame = Cam.process_frame()
"""
import cv2

class CameraNode:
    def __init__(self, camera_index=0):
        self.cap = cv2.VideoCapture(camera_index)
        if not self.cap.isOpened():
            raise ValueError("Camera not accessible.")

    def get_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            raise ValueError("Failed to capture image.")
        return frame

    def release(self):
        self.cap.release()

    def run(self):
        while True:
            frame = self.get_frame()

            # 将帧传递给 rm_vision 处理
            self.process_frame(frame)

            # 显示视频
            cv2.imshow('Camera Feed', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.release()
        cv2.destroyAllWindows()

    def process_frame(self, frame):       
        return frame

if __name__ == "__main__":
    node = CameraNode()
    node.run()