import cv2
import argparse
import mediapipe as mp
from utils import *
from body_part_angle import BodyPartAngle
from types_of_exercise import TypeOfExercise

# Argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-t", "--exercise_type", type=str, help='Type of activity to do', required=True)
ap.add_argument("-vs", "--video_source", type=str, help='Path to video file (optional)', required=False)
args = vars(ap.parse_args())

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# Open video source
if args["video_source"]:
    video_path = "Exercise Videos/" + args["video_source"]
    cap = cv2.VideoCapture(video_path)
    print(f"Loading video: {video_path}")
else:
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Use CAP_DSHOW for better webcam compatibility

cap.set(3, 800)  # Width
cap.set(4, 480)  # Height

# Setup MediaPipe Pose
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    counter = 0  # Exercise counter
    status = True  # Movement status

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Error: Video source not available")
            break

        frame = cv2.resize(frame, (800, 480), interpolation=cv2.INTER_AREA)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame.flags.writeable = False
        results = pose.process(frame)
        frame.flags.writeable = True
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        if results.pose_landmarks:
            landmarks = results.pose_landmarks.landmark
            counter, status = TypeOfExercise(landmarks).calculate_exercise(
                args["exercise_type"], counter, status)

        frame = score_table(args["exercise_type"], frame, counter, status)

        # Draw pose landmarks
        mp_drawing.draw_landmarks(
            frame,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=2, circle_radius=2),
            mp_drawing.DrawingSpec(color=(174, 139, 45), thickness=2, circle_radius=2),
        )

        cv2.imshow('AI Fitness Trainer', frame)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
