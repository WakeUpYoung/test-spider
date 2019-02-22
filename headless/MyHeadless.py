from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


class MyHeadless:
    __driverPath = r'C:\Users\Ste\AppData\Local\Google\Chrome\Application\chromedriver.exe'
    url = 'https://www.baidu.com'

    def __init__(self, url):
        self.url = url

    '''
    获取Driver
    :arg option 默认为True 当为True时,不显示操作界面
    '''

    def getDriver(self, options=True):
        chrome_options = Options()

        # 注释该语句即可视化看到运行过程
        if options:
            chrome_options.add_argument("--headless --disable-gpu")
            chrome_options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                        'Chrome/71.0.3578.98 Safari/537.36"')

        driver = webdriver.Chrome(
            executable_path=self.__driverPath,
            options=chrome_options)
        return driver

