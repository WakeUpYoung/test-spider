from headless.MyHeadless import MyHeadless
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def get_element(driver, by, tag_name, time_out=10):
    expect_element = expected.presence_of_element_located((by, tag_name))
    return WebDriverWait(driver, time_out, ignored_exceptions=NoSuchElementException).until(expect_element, "time out")


if __name__ == '__main__':
    t_url = "https://detail.tmall.com/item.htm?spm=a230r.1.14.48.2822476ehRVzj6&id=570269376065&ns=1&abbucket=19"
    t_login_frame = 'sufei-dialog-content'

    headless = MyHeadless(url=t_url)
    driver = headless.getDriver(False)
    driver.maximize_window()
    driver.get(headless.url)
    driver.switch_to_frame(t_login_frame)
    user_name_input = get_element(driver, By.CSS_SELECTOR, '#TPL_username_1')
    password_input = get_element(driver, By.CSS_SELECTOR, '#TPL_password_1')
    user_name_input.send_key('13820552740')
    password_input.send_key('wang254841204')

    webdriver_false = """ Object.defineProperties(navigator,{
                 webdriver:{
                   get: () => false
                 }
               })"""
    # 让webdriver = false
    driver.execute_script(script=webdriver_false)

    comment_num = get_element(driver, By.CSS_SELECTOR, '#J_TabBar > li:nth-child(2) > a > em')
    print(comment_num.text)
