from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
import time

def main():
    # Chrome 브라우저를 headless 모드로 실행
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # headless 모드 설정
    driver = webdriver.Chrome(options=chrome_options)

    # 웹 페이지 열기
    url = input("다운로드할 웹 페이지 URL을 입력하세요: ")
    driver.get(url)

    # 페이지 로드를 위해 충분한 시간을 기다림 (예: 5초)
    time.sleep(5)

    # "사진 다운로드" 버튼을 찾아 클릭
    image_button = driver.find_element(By.XPATH, '//button[contains(@class, "flex items-center")]//p[text()="영상 다운로드"]')
    image_button.click()

    # 이미지 다운로드 시간을 위해 충분한 시간을 기다림 (예: 5초)
    time.sleep(5)

    # 다운로드된 이미지 파일 이동
    downloaded_image_path = os.path.join(os.getcwd(), "downloaded_image.jpg")
    os.rename(os.path.expanduser("~") + "/Downloads/QR.jpg", downloaded_image_path)
    
    print(f"이미지가 {downloaded_image_path} 파일로 다운로드되었습니다.")

    # 드라이버 종료
    driver.quit()

if __name__ == "__main__":
    main()
