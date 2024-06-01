import streamlit as st
from pytube import YouTube


# Function to download video
def download_video(url, only_audio):
    yt = YouTube(url)
    if only_audio:
        stream = yt.streams.filter(only_audio=True).first()
        filename = stream.download()
        return filename
    else:
        stream = yt.streams.get_highest_resolution()
        filename = stream.download()
        return filename


# Streamlit app
st.title("YouTube Video Downloader")

url = st.text_input("Enter YouTube URL")

if url:
    st.write("Choose format to download:")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Download Audio"):
            try:
                filename = download_video(url, only_audio=True)
                st.success(f"Downloaded audio: {filename}")
                with open(filename, "rb") as file:
                    st.download_button("Download Audio File", file, file_name=filename)
            except Exception as e:
                st.error(f"Error: {e}")

    with col2:
        if st.button("Download Video"):
            try:
                filename = download_video(url, only_audio=False)
                st.success(f"Downloaded video: {filename}")
                with open(filename, "rb") as file:
                    st.download_button("Download Video File", file, file_name=filename)
            except Exception as e:
                st.error(f"Error: {e}")
