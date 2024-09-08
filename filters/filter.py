import os
import requests
from bs4 import BeautifulSoup


def is_valid_id(movie_id):
    try:
        int(movie_id)
        return True
    except ValueError:
        return False


def get_instagram_video_link(ddinstagram_link):
    try:
        response = requests.get(ddinstagram_link)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            video_url = soup.find('meta', property='og:video')
            if video_url and video_url['content']:
                return "https://ddinstagram.com" + video_url['content']

        return None
    except Exception as e:
        print(f"Xatolik yuz berdi: {str(e)}")
        return None
