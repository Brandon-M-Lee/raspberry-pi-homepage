import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib import parse

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]

try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe')  
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe')

def make_link(sl, tl, text):
    link_google_translator = f'https://translate.google.co.kr/?hl=ko&sl={sl}&tl={tl}&text={parse.quote(text)}&op=translate'
    link_papago = f'https://papago.naver.com/?sk={sl}&tk={tl}&hn=0&st={parse.quote(text)}'
    
    return link_google_translator, link_papago

def get_result(link):
    driver.get(link)
    if link[8] == 't': #구글 번역기
        result = driver.find_element(By.XPATH, '//*[@id="ow167"]/div[1]/span[1]/span/span').text
        print(result)

if __name__ == '__main__':
    link = make_link('ko', 'en', '안녕하세요')[0]
    get_result(link)