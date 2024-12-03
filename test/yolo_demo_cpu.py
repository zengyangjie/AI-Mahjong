import torch
import cv2
import time
from PIL import Image

# 加载预训练模型（YOLOv5s 是轻量化版本）
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # yolov5s 为轻量化版本

# 加载图片
img_path = '1.jpg'  # 替换成你自己的图片路径
img = cv2.imread(img_path)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 转换为RGB格式

# 开始计时
start_time = time.time()

# 推理
results = model(img)

# 计算检测时间（单位：毫秒）
inference_time = (time.time() - start_time) * 1000

results.show()
# 获取推理结果的图片（转换为 OpenCV 格式）
# img_cv = results.render()[0]  # 获取绘制了检测框的图像
# img_cv = cv2.cvtColor(img_cv, cv2.COLOR_RGB2BGR)  # 将 RGB 转换为 BGR 格式

# 显示图像
# cv2.imshow('YOLOv5 Detection', img_cv)  # 显示带检测框的图片
# cv2.waitKey(0)  # 等待键盘输入关闭窗口
# cv2.destroyAllWindows()  # 关闭所有OpenCV窗口

# 打印检测信息
print(results.pandas().xywh)  # 打印预测结果，包括类别、置信度等

# 打印检测时间
print(f"Detection time: {inference_time:.2f} ms")
