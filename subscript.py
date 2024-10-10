import requests
from bs4 import BeautifulSoup
import streamlit as st

# https://www.gpters.org/nocode/post/automatically-receive-summaries-youtube-6lwfhg5ZLhSG9lr


# 함수: YouTube 채널 URL에서 채널 ID 추출
def get_channel_id_from_url(url):
    try:
        # URL에서 채널 ID 추출 (SSL 검증 비활성화)
        response = requests.get(url, verify=False)

        if response.status_code != 200:
            return f"Error: Unable to access the channel page. Status code: {response.status_code}"

        # HTML 파싱
        soup = BeautifulSoup(response.text, 'html.parser')

        # 메타 태그에서 채널 ID 추출
        channel_id_meta = soup.find("meta", {"itemprop": "channelId"})
        if channel_id_meta:
            return channel_id_meta["content"]

        # 대체 방법: 링크에서 채널 ID 추출
        for link in soup.find_all('a'):
            href = link.get('href')
            if href and 'channel/' in href:
                return href.split('channel/')[1]

        return "채널 ID를 찾을 수 없습니다."
    except Exception as e:
        return f"Error: {str(e)}"


# Streamlit 앱 제목 설정
st.title("YouTube 채널 ID 및 RSS 피드 생성기")

# 사용자로부터 유튜브 채널 URL 입력 받기
channel_url = st.text_input("유튜브 채널 URL을 입력하세요 (예: https://www.youtube.com/channel/UCxxxxxx)")

# 채널 ID 확인 및 RSS 피드 생성 버튼
if st.button("채널 ID 및 RSS 피드 생성"):
    if channel_url:
        # 채널 ID 가져오기
        # channel_id = get_channel_id_from_url(channel_url)
        channel_id = 'UChlv4GSd7OQl3js-jkLOnFA'
        if "Error" in channel_id:
            st.error(f"채널 ID를 가져오는 중 오류가 발생했습니다: {channel_id}")
        else:
            st.success(f"채널 ID: {channel_id}")
            rss_feed_url = f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"
            st.write(f"RSS 피드 URL: {rss_feed_url}")
            st.code(rss_feed_url, language='plaintext')
    else:
        st.warning("유튜브 채널 URL을 입력해주세요.")
