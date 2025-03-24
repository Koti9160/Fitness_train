# Fitness_train


AI Fitness Trainer using TensorFlow and OpenCV
The AI Fitness Trainer is a real-time exercise tracking application that uses TensorFlow and OpenCV to monitor, analyze, and provide feedback on five specific exercises. By leveraging advanced computer vision models, it accurately tracks body movements using the MediaPipe Pose Detection model. The trainer provides personalized feedback to ensure proper form, enhancing workout efficiency and reducing the risk of injury.

✅ Key Features:
Real-Time Pose Estimation: Uses TensorFlow Lite and MediaPipe Pose to detect key body landmarks.

Exercise Recognition: Supports recognition and analysis of five popular exercises:

Push-ups

Pull-ups

Sit-ups

Squats

Walk


Repetition Counting: Automatically counts repetitions using motion tracking algorithms.

Form Correction: Provides visual and audible feedback for improper form.

Real-Time Visualization: Displays skeleton tracking with landmark overlays using OpenCV.

Custom Training Modes: Users can select exercises based on their fitness goals.

✅ How It Works:
Camera Input: The application captures live video using OpenCV (cv2.VideoCapture).

Pose Detection: TensorFlow's MediaPipe model detects 33 key body landmarks from the video frames.

Angle Calculation: Joint angles are calculated to ensure correct posture for each exercise.

Repetition Counter: Motion detection algorithms track joint movements to count repetitions.

Feedback Mechanism: Provides instant feedback using visual alerts on the screen and optional voice output.

✅ Exercise Detection Details:
Push-ups: Detects chest lowering and proper arm extension using elbow and shoulder angles.

Sit-ups: Tracks core movement and head-to-knee proximity using hip and shoulder landmarks.

Squats: Monitors knee bend angle to ensure proper form and prevent injury.


✅ Technologies Used:
Python for application logic and control flow.

TensorFlow with MediaPipe Pose for real-time pose estimation.

OpenCV for video capture, processing, and visualization.

NumPy for efficient numerical computations.


✅ Future Enhancements:
Personalized workout plans based on user performance.

Detailed analytics and exercise reports.

Integration with voice assistants for hands-free control.

AI-powered virtual coach for advanced form correction.

