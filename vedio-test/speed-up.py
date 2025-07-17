from moviepy.editor import VideoFileClip


def speed_up_video_with_audio(input_path, output_path, speed=10):
    # 加载视频
    clip = VideoFileClip(input_path)

    # 加速视频和音频（速度×10，时长÷10）
    fast_clip = clip.speedx(factor=speed)

    # 保存加速后的视频
    fast_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
    clip.close()
    print(f"视频加速完成：{input_path} -> {output_path}")


# 使用示例
speed_up_video_with_audio("2.3 折线图.mp4", "output_moviepy1000.mp4", speed=100)