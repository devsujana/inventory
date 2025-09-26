# data_collect.py
import cv2, os, argparse
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument("--label", required=True, help="Label name to collect (e.g. motor)")
parser.add_argument("--out", default="dataset", help="Output dataset folder")
parser.add_argument("--auto", action="store_true", help="Auto-capture every N frames")
parser.add_argument("--interval", type=float, default=0.5, help="Auto-capture interval (seconds)")
args = parser.parse_args()

label = args.label
outdir = os.path.join(args.out, label)
os.makedirs(outdir, exist_ok=True)
print(f"Saving to {outdir}")

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise RuntimeError("Cannot open camera")

count = len(os.listdir(outdir))
last_time = 0
print("Press SPACE to capture, q to quit. Or run with --auto to auto capture.")
while True:
    ret, frame = cap.read()
    if not ret:
        break
    # show instructions
    overlay = frame.copy()
    cv2.putText(overlay, f"Label: {label}  Count: {count}", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)
    cv2.putText(overlay, "SPACE: capture | q: quit | a: toggle auto", (10,60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (200,200,200), 1)
    cv2.imshow("Collect - press SPACE", overlay)

    key = cv2.waitKey(1) & 0xFF
    if args.auto:
        import time
        now = time.time()
        if now - last_time > args.interval:
            last_time = now
            fname = os.path.join(outdir, f"{label}_{count:04d}.jpg")
            cv2.imwrite(fname, frame)
            print("Saved", fname)
            count += 1

    if key == ord(' '):  # space
        fname = os.path.join(outdir, f"{label}_{count:04d}.jpg")
        cv2.imwrite(fname, frame)
        print("Saved", fname)
        count += 1
    elif key == ord('q'):
        break
    elif key == ord('a'):
        args.auto = not args.auto
        print("Auto mode ->", args.auto)

cap.release()
cv2.destroyAllWindows()
