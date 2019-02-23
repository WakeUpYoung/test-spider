import time

from headless.MyHeadless import MyHeadless

if __name__ == '__main__':
    t_url = "https://login.taobao.com/member/login.jhtml"
    headless = MyHeadless(url=t_url)
    driver = headless.getDriver(False)
    driver.maximize_window()
    driver.get(headless.url)
    time.sleep(1)
    # 天猫的登录页面是在Iframe里的
    # driver.switch_to.frame('J_loginIframe')
    login_info = driver.find_element_by_css_selector('#J_QRCodeLogin > div.login-title')
    print('the info is', str(login_info.text))
    if str(login_info.text) == '手机扫码，安全登录':
        login_with_text = driver.find_element_by_css_selector('#J_QRCodeLogin > div.login-links > '
                                                              'a.forget-pwd.J_Quick2Static')
        # 点击 使用密码登录
        login_with_text.click()

    login_with_blog = driver.find_element_by_css_selector('#J_OtherLogin > a.weibo-login')
    # 点击使用微博登录
    login_with_blog.click()

    time.sleep(1)

    blog_text = driver.find_element_by_css_selector('#pl_login_logged > div > div.info_list.login_host > div')
    # 如果出现快速登陆
    if str(blog_text.text) == '微博帐号登录':
        username_input = driver.find_element_by_css_selector('#pl_login_logged > div > div:nth-child(2) > div > input')
        password_input = driver.find_element_by_css_selector('#pl_login_logged > div > div:nth-child(3) > div > input')
        check_box = driver.find_element_by_css_selector('#login_form_savestate')
        login_btn = driver.find_element_by_css_selector('#pl_login_logged > div > div:nth-child(7) > div:nth-child(1) > a')
        username_input.clear()
        username_input.send_keys('13820552740')
        password_input.send_keys('wang60589537')
        check_box.click()
        login_btn.click()

    print('正在登录...')
    time.sleep(2)

    driver.save_screenshot('tmao.png')
    # driver.close()

