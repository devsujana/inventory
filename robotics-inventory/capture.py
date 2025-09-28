#capture.py
#this file is used to capture images and give them tags for collection of data for training the model for robotics inventory .

#------------------imports----------------------------------------------------
import cv2
import os

#--------------- declares-------------------------------------------------------
# Ask for item name (e.g., motor, battery, board)
item_name = input("Enter item name (motor/battery/board): ").strip().lower()

# Create folder if not exists
save_path = f"data/{item_name}"
os.makedirs(save_path, exist_ok=True)

# Open webcam
cap = cv2.VideoCapture(0)
count = 0
#-----------------------main logic---------------------
while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Capture Item Images - Press 's' to save, 'q' to quit", frame)

    key = cv2.waitKey(1)
    if key == ord('s'):  # Save frame
        img_path = os.path.join(save_path, f"{item_name}_{count}.jpg")
        cv2.imwrite(img_path, frame)
        print(f"Saved: {img_path}")
        count += 1
    elif key == ord('q'):  # Quit
        break

cap.release()
cv2.destroyAllWindows()
