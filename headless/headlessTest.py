import time

from headless.MyHeadless import MyHeadless
from PIL import Image

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
    print('the panel info is', str(login_info.text))
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
        # 用户名
        username_input = driver.find_element_by_css_selector('#pl_login_logged > div > div:nth-child(2) > div > input')
        # 密码
        password_input = driver.find_element_by_css_selector('#pl_login_logged > div > div:nth-child(3) > div > input')
        # checkbox
        check_box = driver.find_element_by_css_selector('#login_form_savestate')
        # 登录按钮
        login_btn = driver.find_element_by_css_selector('#pl_login_logged > div > div:nth-child(7) > div:nth-child(1) > a')
        username_input.clear()
        username_input.send_keys('13820552740')
        password_input.send_keys('wang60589537')
        check_box.click()
        login_btn.click()

        time.sleep(5)

        verify_img = None
        no_img = True
        while no_img:
            try:
                verify_img = driver.find_element_by_css_selector('#pl_login_logged > div > div:nth-child(4) > div > a.code > img')
                no_img = False
            except driver.NoSuchElementException as e:
                print("验证码没有出现在页面上，重新登录以显示")
                login_btn.click()
                time.sleep(3)
        img_location = verify_img.location
        img_size = verify_img.size
        left = img_location['x']
        top = img_location['y']
        right = left + img_size['width']
        bottom = top + img_size['height']

        screen_shot = 'full_screen.png'
        driver.save_screenshot(screen_shot)
        # 保存当前验证码
        crop = Image.open(screen_shot).crop((left, top, right, bottom))
        crop.show()

    # driver.close()

