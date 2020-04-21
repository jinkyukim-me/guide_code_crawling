import urllib.request
from bs4 import BeautifulSoup

def main():
    # URL 데이터를 가져올 사이트 url 입력
    url = "https://himchanyoon1992.tistory.com/1"
    # URL 에 있는 HTML 코드를 soup에 저장합니다.
    soup = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")
    print(crawl_contents(soup))

def crawl_contents(html) :
    comments = []
    # 댓글 부분을 찾아서 list에 하나씩 댓글을 삽입합니다.
    for comment in html.find_all("span", class_="txt_reply"):
        comments.append(comment.text)
    # list를 반환합니다.
    return comments

if __name__ == "__main__":
    main()