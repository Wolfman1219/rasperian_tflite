import cv2
import time
import cvui
rtsp_username = "admin"
rtsp_password = "wolfman1556"
width = 2560
height = 1440
cam_no = 1
# rtsp://admin:Hikvision07!@192.169.0.100:554/h264/ch1/main/av_stream
rtsp = "rtsp://" + rtsp_username + ":" + rtsp_password + "@192.169.0.102:554/h264/ch1/main/av_stream" #change the IP to suit yours
# cap = cv2.VideoCapture()
# cap.open(rtsp)
def create_camera (channel):
    rtsp = "rtsp://" + rtsp_username + ":" + rtsp_password + "@192.169.0.102:554/h264/ch1/main/av_stream" #change the IP to suit yours
    cap = cv2.VideoCapture(rtsp)
    # cap.open(rtsp)
    # cap.set(3, 2560)  # ID number for width is 3
    # cap.set(4, 1440)  # ID number for height is 480
    # cap.set(10, 100)  # ID number for brightness is 10qq
    return cap

cam = create_camera(str(cam_no))

cam = create_camera(str(cam_no))
cvui.init('screen')
while True:
    success, current_cam = cam.read()

    cv2.imwrite("current_cam.jpg",current_cam)
    break
    dim = (width, height)
    Full_frame = cv2.resize(current_cam, dim, interpolation=cv2.INTER_AREA)
    cv2.namedWindow('screen', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('screen', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    if (cvui.button(Full_frame, width - 100, height - 40, "Next") and cvui.mouse(cvui.CLICK)):
        print("Next Button Pressed")
        cvui.init('screen')
        cam_no = cam_no+1
        if (cam_no>4):
            cam_no=1
        del cam
        cam = create_camera(str(cam_no))
    if (cvui.button(Full_frame, width - 200, height - 40, "Previous") and cvui.mouse(cvui.CLICK)):
        print("Previous Button Pressed")
        cvui.init('screen')
        cam_no = cam_no - 1
        if (cam_no<1):
            cam_no=4
