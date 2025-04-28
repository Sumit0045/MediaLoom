
# ------------------------- Send Media -------------------------#
async def send_media(app, channel_id, file_path, media_type):
    try:
        if media_type == "photo":
            sent = await app.send_photo(channel_id, photo=file_path)
        elif media_type == "video":
            sent = await app.send_video(channel_id, video=file_path)
        elif media_type == "audio":
            sent = await app.send_audio(channel_id, audio=file_path)
        elif media_type == "gif":
            sent = await app.send_animation(channel_id, animation=file_path)
        return sent
    except Exception as e:
        print(f"Error: {e}")
        return None




