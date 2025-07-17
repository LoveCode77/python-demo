from moviepy.editor import VideoFileClip
import os


def get_video_metadata(video_path):
    # 基础信息（MoviePy直接获取）
    clip = VideoFileClip(video_path)
    metadata = {
        "文件路径": video_path,
        "文件大小": f"{os.path.getsize(video_path) / 1024 / 1024:.2f} MB",  # 转换为MB
        "时长": f"{clip.duration:.2f} 秒",
        "分辨率": f"{clip.size[0]}x{clip.size[1]} (宽x高)",
        "帧率": f"{clip.fps:.2f} FPS",
        "是否有音频": "是" if clip.audio else "否",
    }

    # 音频详细信息（若存在）
    if clip.audio:
        audio = clip.audio
        metadata.update({
            "音频采样率": f"{audio.fps} Hz",
            "音频声道数": audio.nchannels,
            "音频时长": f"{audio.duration:.2f} 秒",
        })

    # 调用FFmpeg获取更底层的元数据（如编码格式、比特率等）
    try:
        from moviepy.video.io.ffmpeg_reader import ffmpeg_parse_infos
        ffmpeg_info = ffmpeg_parse_infos(video_path)
        metadata.update({
            "视频编码": ffmpeg_info["video_codec"],
            "音频编码": ffmpeg_info.get("audio_codec", "无"),
            "视频比特率": f"{ffmpeg_info.get('video_bitrate', 0) / 1000:.2f} kbps",
            "音频比特率": f"{ffmpeg_info.get('audio_bitrate', 0) / 1000:.2f} kbps",
            "旋转角度": f"{ffmpeg_info.get('rotation', 0)}°",  # 视频旋转信息
            "格式": ffmpeg_info["format"],  # 容器格式（如mp4、avi）
        })
    except:
        # 若FFmpeg信息获取失败，忽略这部分
        pass

    clip.close()
    return metadata


# 打印所有信息
video_path = "2.3 折线图.mp4"
metadata = get_video_metadata(video_path)
for key, value in metadata.items():
    print(f"{key}：{value}")