import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib import parse
import time

def make_link(sl, tl, text):
    link_google_translator = f'https://translate.google.co.kr/?hl=ko&sl={sl}&tl={tl}&text={parse.quote(text)}&op=translate'
    link_papago = f'https://papago.naver.com/?sk={sl}&tk={tl}&hn=0&st={parse.quote(text)}'
    
    return link_google_translator, link_papago

def get_result(link):
    chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]

    try:
        driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe')  
    except:
        chromedriver_autoinstaller.install(True)
        driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe')
    driver.get(link)
    time.sleep(1)
    if link[8] == 't': #구글 번역기
        result = driver.find_element(By.CLASS_NAME, 'Q4iAWc').text
    if link[8] == 'p': #파파고
        result = driver.find_element(By.ID, 'txtTarget').text
    return result

if __name__ == '__main__':
    link = make_link('ko', 'en', '안녕하세요')[0]
    get_result(link)