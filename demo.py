r"""OpenCV 安装验证 / 简单绘图示例。

运行：
    .\.venv\Scripts\python.exe demo.py

会在当前目录生成 demo_output.png，不需要摄像头或联网。
"""

import cv2
import numpy as np

W, H = 720, 420
img = np.zeros((H, W, 3), dtype=np.uint8)

# 渐变背景（深蓝 -> 青绿）
for y in range(H):
    t = y / (H - 1)
    img[y, :] = (
        int(40 * (1 - t) + 10 * t),      # B
        int(25 * (1 - t) + 110 * t),     # G
        int(20 * (1 - t) + 90 * t),      # R
    )

# 半透明装饰圆
overlay = img.copy()
cv2.circle(overlay, (620, 70), 120, (0, 200, 255), -1)
cv2.circle(overlay, (80, 370), 90, (255, 120, 0), -1)
img = cv2.addWeighted(overlay, 0.35, img, 0.65, 0)

# 卡片
cv2.rectangle(img, (60, 80), (660, 340), (245, 245, 245), -1)
cv2.rectangle(img, (60, 80), (660, 340), (0, 180, 160), 4)

# 标题与文字
cv2.putText(img, "OpenCV 5.0", (95, 160),
            cv2.FONT_HERSHEY_DUPLEX, 1.7, (30, 40, 50), 3, cv2.LINE_AA)
cv2.putText(img, "Python 3.14  |  NumPy 2.5.4", (98, 205),
            cv2.FONT_HERSHEY_SIMPLEX, 0.65, (60, 70, 80), 2, cv2.LINE_AA)
cv2.line(img, (98, 230), (620, 230), (200, 200, 200), 2)

# 简单图形：圆、矩形、多边形
cv2.circle(img, (140, 285), 32, (0, 170, 255), -1, cv2.LINE_AA)
cv2.rectangle(img, (205, 258), (280, 312), (80, 200, 80), -1)
pts = np.array([[330, 312], [365, 255], [400, 312]], np.int32)
cv2.fillPoly(img, [pts], (200, 90, 200), cv2.LINE_AA)
cv2.putText(img, "image I/O + drawing OK", (440, 295),
            cv2.FONT_HERSHEY_SIMPLEX, 0.55, (90, 90, 90), 1, cv2.LINE_AA)

ok, buf = cv2.imencode(".png", img)
if not ok:
    raise RuntimeError("PNG 编码失败")
decoded = cv2.imdecode(buf, cv2.IMREAD_COLOR)
cv2.imwrite("demo_output.png", decoded)

print(f"OpenCV {cv2.__version__} / NumPy {np.__version__}")
print(f"Image: {decoded.shape[1]}x{decoded.shape[0]}, PNG: {len(buf)} bytes")
print("Saved demo_output.png")
