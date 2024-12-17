
import cv2
import random
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import time

# 画面のサイズ
width, height = 640, 480
font = ImageFont.load_default()  # デフォルトフォントを使用

# ビデオ設定
fps = 30
duration = 5  # ビデオの長さ（秒）
video_filename = 'lottery_draw.avi'

# ビデオ出力の準備
fourcc = cv2.VideoWriter_fourcc(*'XVID')
video_writer = cv2.VideoWriter(video_filename, fourcc, fps, (width, height))

# ランダム抽選プロセスの表示
def draw_text(image, text, position, font, color=(255, 255, 255)):
    draw = ImageDraw.Draw(image)
    draw.text(position, text, font=font, fill=color)

# 数字リスト（1から150まで）
numbers = list(range(1, 151))

# ビデオ作成
for frame_num in range(fps * duration):
    # ランダムに数字を選ぶ過程を表示
    img = np.zeros((height, width, 3), dtype=np.uint8)
    pil_image = Image.fromarray(img)
    
    # 途中でランダムに数字が表示される
    random_numbers = random.sample(numbers, 10)  # 10個のランダムな数字
    for i, number in enumerate(random_numbers):
        draw_text(pil_image, str(number), (50, 50 + i * 40), font, color=(random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)))
    
    # 最終的に選ばれた数字（ランダムに1つ選ぶ）
    if frame_num == fps * (duration - 1):  # 最後のフレームで
        final_number = random.choice(numbers)
        draw_text(pil_image, f'Winner: {final_number}', (200, height // 2), font, color=(255, 0, 0))  # 赤で表示

    # OpenCVの形式に変換してビデオに追加
    img = np.array(pil_image)
    video_writer.write(img)
    time.sleep(1 / fps)

# ビデオ保存を終了
video_writer.release()
cv2.destroyAllWindows()

print("ビデオが作成されました:", video_filename)
