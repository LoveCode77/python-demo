from moviepy.editor import VideoFileClip, concatenate_videoclips
import os


def concat_videos(input_files, output_file, method="compose"):
    """按顺序拼接多个视频"""
    # 加载所有视频片段
    clips = [VideoFileClip(f) for f in input_files if os.path.exists(f)]

    # 拼接视频（method="compose" 确保分辨率统一）
    final_clip = concatenate_videoclips(clips, method=method)

    # 保存结果
    final_clip.write_videofile(output_file, codec="libx264")

    # 释放资源
    for clip in clips:
        clip.close()
    final_clip.close()

    print(f"视频拼接完成：{output_file}")


# 使用示例
input_files = ["2.3 折线图.mp4", "2.3 折线图.mp4", "2.3 折线图.mp4"]
concat_videos(input_files, "output_concat.mp4")