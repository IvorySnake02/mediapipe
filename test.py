import mediapipe as mp
import cv2

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
    image = cv2.imread("image.jpg")

    # BGR 2 RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        

    # Set flag
    image.flags.writeable = False
    
    # Detections
    results = hands.process(image)
    
    # Set flag to true
    image.flags.writeable = True
    
    # RGB 2 BGR
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    
    # Detections
    print(results)
    
    # Rendering results
    if results.multi_hand_landmarks:
        for num, hand in enumerate(results.multi_hand_landmarks):
            mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS, 
                                    mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                                    mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2),
                                        )
        
    
cv2.imshow('Hand Tracking', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

