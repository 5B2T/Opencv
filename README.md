# OpenCV 工具包

已在本目录安装好 OpenCV，使用独立虚拟环境，**不会影响系统 Python**。

| 组件 | 版本 |
| --- | --- |
| OpenCV (`opencv-python`) | **5.0.0** |
| NumPy | **2.5.4** |
| Python | 3.14.0 |
| pip | 26.3 |

安装位置：`.venv\Lib\site-packages`（整个 `.venv` 约 165 MB）  
离线安装包：`downloads\`（约 58 MB，已校验 SHA-256）

## 快速开始

在 PowerShell 中进入本目录，直接运行示例：

```powershell
cd "C:\Users\Admin\Desktop\Opencv"
.\.venv\Scripts\python.exe demo.py
```

运行后会输出 OpenCV / NumPy 版本，并生成 `demo_output.png`。

### 激活虚拟环境（可选）

```powershell
.\.venv\Scripts\Activate.ps1
python demo.py
```

如果提示“禁止运行脚本”，先执行：

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

> 注意：本机系统里的 `python` 命令是 Microsoft Store 的占位程序，不一定可用。
> 请使用本目录虚拟环境中的 `.\.venv\Scripts\python.exe`，或先激活虚拟环境。

## 在代码中使用

```python
import cv2
import numpy as np

img = np.zeros((200, 300, 3), dtype=np.uint8)
cv2.putText(img, "Hello OpenCV", (20, 100),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
cv2.imwrite("hello.png", img)

print(cv2.__version__)   # 5.0.0
```

## 安装更多包

```powershell
.\.venv\Scripts\python.exe -m pip install 包名 -i https://pypi.tuna.tsinghua.edu.cn/simple
```

如果只是需要 SIFT、SURF 等 contrib 扩展模块，可改装 `opencv-contrib-python`（先卸载 `opencv-python`，两者不要同时安装）。

## 离线重装

```powershell
.\.venv\Scripts\python.exe -m pip install `
  .\downloads\opencv_python-5.0.0.93-cp37-abi3-win_amd64.whl `
  .\downloads\numpy-2.5.4-cp314-cp314-win_amd64.whl `
  .\downloads\pip-26.3-py3-none-any.whl
```

## 目录说明

```text
Opencv\
├─ .venv\              # Python 虚拟环境（OpenCV + NumPy）
├─ downloads\          # 离线 wheel 安装包
├─ demo.py             # 功能验证 / 绘图示例
├─ demo_output.png     # 示例生成的图片
└─ README.md
```

不需要时，直接删除整个 `Opencv` 文件夹即可完成卸载。
