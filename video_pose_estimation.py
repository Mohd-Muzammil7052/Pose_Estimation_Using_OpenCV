import cv2
import mediapipe as mp

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils  # For drawing Landmarks

# Capture Video
video_source = 0
# cap = cv2.VideoCapture(video_source)
cap = cv2.VideoCapture("run.mov")

# Set video resolution for webcam
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Initialize MediaPipe Pose
with mp_pose.Pose(
    static_image_mode=False,  # For real-time video processing
    model_complexity=1,       # Adjust complexity (0, 1, or 2)
    enable_segmentation=False,  # Disable segmentation for performance
    min_detection_confidence=0.5,  # Minimum confidence for detection
    min_tracking_confidence=0.5    # Minimum confidence for tracking
) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Video Capture Ended")
            break

        # Flip frame horizontally for a mirror-like effect
        frame = cv2.flip(frame, 1)

        # Convert the BGR image to RGB image for MediaPipe
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame with MediaPipe Pose
        results = pose.process(frame_rgb)

        # Draw Landmarks
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(
                frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),  # Landmarks
                mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2)   # Connections
            )

        # Resize frame to fit the screen
        display_frame = cv2.resize(frame, (960, 540))

        # Display the processed frame
        cv2.imshow('Pose Estimation', display_frame)

        # Break loop if "q" is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
