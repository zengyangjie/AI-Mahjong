import time
import torch
import cv2
from PIL import Image

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(torch.cuda.is_available())  # 应该返回 True
print(torch.cuda.current_device())  # 显示当前使用的 GPU 索引
print(torch.cuda.get_device_name(0))  # 显示 GPU 名称


# 加载YOLOv5模型
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # yolov5s 模型
model.to(device)  # 将模型移动到 GPU

# 读取输入图片
img_path = '1.jpg'  # 输入图片路径
img = cv2.imread(img_path)  # 输入图片路径
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 转换为RGB格式

img = Image.open(img_path)

# 开始计时
start_time = time.time()

# 推理
results = model(img_rgb)  # 推理

# 计算检测时间（单位：毫秒）
inference_time = (time.time() - start_time) * 1000

# 显示推理结果
results.show()  # 显示处理后的图片

print(results.pandas().xywh)  # 打印预测结果，包括类别、置信度等

# 打印检测时间
print(f"Detection time: {inference_time:.2f} ms")