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

    headless = MyHeadless(url=t_url)
    driver = headless.getDriver(False)
    driver.maximize_window()
    driver.get(headless.url)
    webdriver_false = """ Object.defineProperties(navigator,{
                 webdriver:{
                   get: () => false
                 }
               })"""
    # 让webdriver = false
    driver.execute_script(script=webdriver_false)
    login_link = driver.find_element_by_css_selector('#login-info > a.sn-login')
    if login_link.text == '请登录':
        login_link.click()
    user_label = get_element(driver, By.CSS_SELECTOR,
                          '#login-info > span:nth-child(1) > a.j_Username.j_UserNick.sn-user-nick', 60)
    print(user_label.text)

    goods_name = driver.find_element_by_css_selector('#J_DetailMeta > div.tm-clear > div.tb-property > div > div.tb-detail-hd > h1')
    print("商品名称:", goods_name)
    comment_num = get_element(driver, By.CSS_SELECTOR, '#J_TabBar > li:nth-child(2) > a > em')
    print("评论数:",comment_num.text)
    comment_content = driver.find_element_by_css_selector('#J_TabBar > li.tm-selected > a')
    # 点击评论
    comment_content.click()
    tbody = driver.find_elements_by_xpath('//*[@id="J_Reviews"]/div/div[6]/table/tbody/tr')
    for tr in tbody:
        comment_text = tr.find_elements_by_xpath('td/div/div')
        print(comment_text)
