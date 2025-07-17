from moviepy.editor import VideoFileClip
import os


def extract_all_frames(video_path, output_folder, prefix="frame", ext="jpg"):
    """提取视频的每一帧"""
    # 创建输出目录
    os.makedirs(output_folder, exist_ok=True)

    # 加载视频
    clip = VideoFileClip(video_path)

    # 获取总帧数和帧率
    fps = clip.fps
    duration = clip.duration
    total_frames = int(fps * duration)

    # 逐帧提取并保存
    for i in range(total_frames):
        # 计算当前帧的时间（秒）
        t = i / fps

        # 获取帧并保存
        frame = clip.get_frame(t)
        frame_path = os.path.join(output_folder, f"{prefix}_{i:05d}.{ext}")

        # 使用 PIL 保存帧（支持多种格式）
        from PIL import Image
        img = Image.fromarray(frame)
        img.save(frame_path)

        # 打印进度
        if i % 100 == 0:
            print(f"已提取 {i}/{total_frames} 帧")

    clip.close()
    print(f"完成！共提取 {total_frames} 帧到 {output_folder}")


# 使用示例
extract_all_frames("output_moviepy1.mp4", "output_moviepy1")