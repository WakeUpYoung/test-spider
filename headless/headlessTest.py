import time

from headless.MyHeadless import MyHeadless

if __name__ == '__main__':
    headless = MyHeadless('https://login.tmall.com')
    driver = headless.getDriver(False)
    driver.maximize_window()
    driver.get(headless.url)
    print('等待页面载入成功')
    time.sleep(5)
    driver.switch_to.frame('J_loginIframe')
    login_info = driver.find_element_by_css_selector('#J_QRCodeLogin > div.login-title')
    print('the info is',str(login_info.text))
    if str(login_info.text) == '手机扫码，安全登录':
        login_with_text = driver.find_element_by_css_selector('#J_QRCodeLogin > div.login-links > a.forget-pwd.J_Quick2Static')
        login_with_text.click()

    username_input = driver.find_element_by_css_selector('#TPL_username_1')
    password_input = driver.find_element_by_css_selector('#TPL_password_1')
    login_button = driver.find_element_by_css_selector('#J_SubmitStatic')
    username_input.clear()
    username_input.send_keys('13820552740')
    password_input.send_keys('wang254841204')
    # login_button.click()
    # print('正在登录...')
    time.sleep(2)

    driver.save_screenshot('tmao.png')
    # driver.close()

