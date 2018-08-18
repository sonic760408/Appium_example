# coding:utf-8
import os
from time import sleep

import unittest

from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction

# Returns abs path relative to this file and not cwd
from wheel.signatures.djbec import By

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


# Test Case
class AndroidTests(unittest.TestCase):
    # Setup emulator env.
    def setUp(self):

        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8.0'
        desired_caps['deviceName'] = 'N5_26'
        desired_caps['autoGrantPermissions'] = 'true'
        desired_caps["unicodeKeyboard"] = 'True'
        desired_caps["resetKeyboard"] = 'True'
        desired_caps["automationName"] = 'UiAutomator2'
        desired_caps['app'] = PATH(
            './apk/app-release_test.apk'
        )

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def atest_login(self):
        sleep(5)
        # self.driver.switch_to_alert().accept()

        #el1 = self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
        #el1.click()
        # self.driver.find_element_by_xpath("//android.widget.Button[@text='允許']").click()
        self.driver.background_app(1)  # focus app background
        sleep(1)

        try:
            el = self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
            el.click()
        except NoSuchElementException:
            print("No element found")

        el = self.driver.find_element_by_id("com.tintin.tintinapp:id/img_btn_member")
        el.click()
        sleep(1)
        self.driver.find_element_by_id("com.tintin.tintinapp:id/img_btn_member_info").click()
        sleep(1)

        el = self.driver.find_element_by_id("com.tintin.tintinapp:id/txt_login_id")
        el.send_keys("sonicmax")
        '''self.driver.hide_keyboard()'''
        el2 = self.driver.find_element_by_id("com.tintin.tintinapp:id/txt_login_pw")
        el2.send_keys("umbrella99")
        self.driver.hide_keyboard()
        self.driver.find_element_by_id("com.tintin.tintinapp:id/btn_login").click()
        sleep(1)

    def test_edit(self):

        # self.driver.switch_to_alert().accept()

        #el1 = self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
        #el1.click()
        # self.driver.find_element_by_xpath("//android.widget.Button[@text='允許']").click()
        #self.driver.background_app(1)  # focus app background
        sleep(3)

        try:
            el = self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
            el.click()
        except NoSuchElementException:
            print("No element found")

        el = self.driver.find_element_by_id("com.tintin.tintinapp:id/img_btn_member")
        el.click()
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_id("com.tintin.tintinapp:id/img_btn_member_info").click()
        self.driver.implicitly_wait(1)

        el = self.driver.find_element_by_id("com.tintin.tintinapp:id/txt_login_id")
        el.send_keys("sonicmax")
        '''self.driver.hide_keyboard()'''
        el2 = self.driver.find_element_by_id("com.tintin.tintinapp:id/txt_login_pw")
        el2.send_keys("umbrella99")
        #self.driver.hide_keyboard()
        self.driver.find_element_by_id("com.tintin.tintinapp:id/btn_login").click()

        self.driver.implicitly_wait(1)
        el = self.driver.find_element_by_id("com.tintin.tintinapp:id/img_btn_member_info")
        el.click()
        self.driver.implicitly_wait(1)

        el = self.driver.find_element_by_id("com.tintin.tintinapp:id/txt_mberinfo_name")
        el.click()
        self.driver.implicitly_wait(1)
        el = self.driver.find_element_by_id("com.tintin.tintinapp:id/txt_username")
        el.click()
        el.clear()
        self.driver.implicitly_wait(1)
        el.send_keys('陳平之')
        el = self.driver.find_element_by_id("com.tintin.tintinapp:id/btn_confirm")
        el.click()
        sleep(2)
        try:
            el = self.driver.find_element_by_id("com.tintin.tintinapp:id/rlayout_mberinfo_birth")
            el.click()
        except NoSuchElementException:
            print("2 No element found")

        sleep(1)

        try:
            el = self.driver.find_element_by_class_name('android.widget.DatePicker')
        except NoSuchElementException:
            print("2-1 No element found")

        self.driver.find_element_by_xpath("//android.widget.NumberPicker[@index='0']").send_keys("2000")

        el = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout"
                                               "/android.widget.LinearLayout/android.widget.FrameLayout"
                                               "/android.widget.FrameLayout/android.widget.FrameLayout"
                                               "/android.support.v7.widget.LinearLayoutCompat"
                                               "/android.widget.FrameLayout/android.widget.FrameLayout"
                                               "/android.widget.RelativeLayout/android.widget.DatePicker"
                                               "/android.widget.LinearLayout/android.widget.LinearLayout"
                                               "/android.widget.NumberPicker[0]")
        el.send_keys("2000")
        el = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout"
                                               "/android.widget.LinearLayout/android.widget.FrameLayout"
                                               "/android.widget.FrameLayout/android.widget.FrameLayout"
                                               "/android.support.v7.widget.LinearLayoutCompat"
                                               "/android.widget.FrameLayout/android.widget.FrameLayout"
                                               "/android.widget.RelativeLayout/android.widget.DatePicker"
                                               "/android.widget.LinearLayout/android.widget.LinearLayout"
                                               "/android.widget.NumberPicker[2]")
        el.send_keys("2")
        el = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout"
                                               "/android.widget.LinearLayout/android.widget.FrameLayout"
                                               "/android.widget.FrameLayout/android.widget.FrameLayout"
                                               "/android.support.v7.widget.LinearLayoutCompat"
                                               "/android.widget.FrameLayout/android.widget.FrameLayout"
                                               "/android.widget.RelativeLayout/android.widget.DatePicker"
                                               "/android.widget.LinearLayout/android.widget.LinearLayout"
                                               "/android.widget.NumberPicker[3]")
        el.send_keys("03")
        el = self.driver.find_element_by_id("com.tintin.tintinapp:id/btn_confirm")
        el.click()
        sleep(1)

        try:
            el = self.driver.find_element_by_id("com.tintin.tintinapp:id/rlayout_mberinfo_address")
            el.click()
        except NoSuchElementException:
            print("2-1 No element found")
            self.driver.implicitly_wait(1)

        spinner = self.driver.find_element_by_id("com.tintin.tintinapp:id/sp_city").click()
        self.driver.implicitly_wait(1)
        # find a UI element with text = value_to_select
        # and click on it

        # self.driver.execute_script("mobile: scrollTo", {"element": spinner.id})

        self.driver.swipe(255, 750, 255, 1500, 500)

        self.driver.implicitly_wait(1)

        select = self.driver.find_element_by_android_uiautomator('new UiSelector().text("{my_value_to_select}")'.format(
            my_value_to_select="新竹市"
        ))
        select.click()

        #self.select_dropdown("com.tintin.tintinapp:id/sp_city", "新竹市", 400, 100)
        self.select_dropdown("com.tintin.tintinapp:id/sp_city_code", "東區", -1, -1)

        el = self.driver.find_element_by_id("com.tintin.tintinapp:id/txt_address")
        el.click()
        el.clear()
        self.driver.tap([(321, 1684)],100)
        el.send_keys("新竹市東區光復路123號")

        el = self.driver.find_element_by_id("com.tintin.tintinapp:id/cbox_check_foreign")
        el.click()

        self.driver.find_element_by_id("com.tintin.tintinapp:id/btn_confirm").click()
        self.driver.implicitly_wait(1)

        try:
            el = self.driver.find_element_by_id("com.tintin.tintinapp:id/rlayout_mberinfo_email1")
            el.click()
        except NoSuchElementException:
            print("3 No element found")

        self.driver.implicitly_wait(1)

        el = self.driver.find_element_by_id("com.tintin.tintinapp:id/txt_email1")
        el.clear()
        el.send_keys("max@norbelbaby.com")
        el = self.driver.find_element_by_id("com.tintin.tintinapp:id/btn_confirm")
        el.click()

        try:
            el = self.driver.find_element_by_id("com.tintin.tintinapp:id/rlayout_mberinfo_email2")
            el.click()
        except NoSuchElementException:
            print("4 No element found")

        self.driver.implicitly_wait(1)

        el = self.driver.find_element_by_id("com.tintin.tintinapp:id/txt_email2")
        el.clear()
        el.send_keys("wesker760408@hotmail.com")
        el = self.driver.find_element_by_id("com.tintin.tintinapp:id/btn_confirm")
        el.click()

        self.driver.swipe(100, 500, 100, 200, 500)

        try:
            el = self.driver.find_element_by_id("com.tintin.tintinapp:id/rlayout_mberinfo_tel")
            el.click()
        except NoSuchElementException:
            print("5 No element found")

        self.driver.implicitly_wait(1)

        el = self.driver.find_element_by_id("com.tintin.tintinapp:id/txt_telno_header")
        el.clear()
        el.send_keys("02")
        el = self.driver.find_element_by_id("com.tintin.tintinapp:id/txt_telno")
        el.clear()
        el.send_keys("23456789")
        el = self.driver.find_element_by_id("com.tintin.tintinapp:id/btn_confirm")
        el.click()

        try:
            el = self.driver.find_element_by_id("com.tintin.tintinapp:id/rlayout_mberinfo_mobile")
            el.click()
        except NoSuchElementException:
            print("6 No element found")

        self.driver.implicitly_wait(1)

        el = self.driver.find_element_by_id("com.tintin.tintinapp:id/txt_mobile")
        el.clear()
        el.send_keys("0900999999")
        el = self.driver.find_element_by_id("com.tintin.tintinapp:id/btn_confirm")
        el.click()
        self.driver.implicitly_wait(1)

        self.driver.swipe(100, 500, 100, 300, 500)

        self.driver.find_element_by_id("com.tintin.tintinapp:id/rlayout_mberinfo_career").click()
        self.select_dropdown("com.tintin.tintinapp:id/sp_career", 200, 400,"電子業")
        self.driver.find_element_by_id("com.tintin.tintinapp:id/btn_confirm").click()

        '''
        self.driver.find_element_by_id("com.tintin.tintinapp:id/btn_confirm")
        sleep(1)
        '''

    def atest_forgetpwd(self):
        sleep(5)
        try:
            el = self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
            el.click()
        except NoSuchElementException:
            print("No element found")

        self.driver.background_app(1)  # focus app background
        sleep(1)

        el = self.driver.find_element_by_id("com.tintin.tintinapp:id/img_btn_member")
        el.click()
        sleep(1)
        self.driver.find_element_by_id("com.tintin.tintinapp:id/img_btn_member_info").click()
        sleep(1)
        self.driver.find_element_by_id("com.tintin.tintinapp:id/btn_forget_pw").click()
        sleep(1)

        el = self.driver.find_element_by_id("com.tintin.tintinapp:id/txt_forgetpwd_email1")
        el.send_keys("sonic760408@gmail.com")
        '''self.driver.hide_keyboard()'''
        el2 = self.driver.find_element_by_id("com.tintin.tintinapp:id/txt_forgetpwd_idno")
        el2.send_keys("E123345007")
        #self.driver.hide_keyboard()
        sleep(5)
        self.driver.find_element_by_id("com.tintin.tintinapp:id/btn_confirm").click()
        sleep(3)
        self.driver.back()

        '''self.driver.find_element_by_xpath(self, "android.widget.ImageButton[@content-desc=\"向上瀏覽\"")'''

        self.driver.back()
        self.driver.back()
        self.driver.swipe(470, 500, 470, 100, 500)
        sleep(1)
        self.driver.swipe(470, 500, 470, 100, 500)
        sleep(1)
        self.driver.swipe(470, 500, 470, 100, 500)
        sleep(1)
        self.driver.swipe(470, 100, 470, 500, 500)
        sleep(1)

    def tearDown(self):
        # end the session
        self.driver.quit()

    def select_dropdown(self, dropdown_id, value_to_select, startloc, endloc):
        # get the spinner and click on it
        spinner = self.driver.find_element_by_id(dropdown_id)
        spinner.click()
        sleep(1)
        # find a UI element with text = value_to_select
        # and click on it

        # self.driver.execute_script("mobile: scrollTo", {"element": spinner.id})

        if (startloc != -1) and (endloc != -1):
            self.driver.swipe(200, startloc, 200, endloc, 500)

        #spinner.send_keys(value_to_select)

        #self.driver.scroll(value_to_select)

        sleep(1)

        select = self.driver.find_element_by_android_uiautomator('new UiSelector().text("{my_value_to_select}")'.format(
            my_value_to_select=value_to_select
        ))
        select.click()

    def isElement(self, identifyBy, c):
        '''
        Determine whether elements exist
        Usage:
        isElement(By.XPATH,"//a")
        '''
        sleep(1)
        flag = None
        try:
            if identifyBy == "id":
                # self.driver.implicitly_wait(60)
                self.driver.find_element_by_id(c)
            elif identifyBy == "xpath":
                # self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath(c)
            elif identifyBy == "class":
                self.driver.find_element_by_class_name(c)
            elif identifyBy == "link text":
                self.driver.find_element_by_link_text(c)
            elif identifyBy == "partial link text":
                self.driver.find_element_by_partial_link_text(c)
            elif identifyBy == "name":
                self.driver.find_element_by_name(c)
            elif identifyBy == "tag name":
                self.driver.find_element_by_tag_name(c)
            elif identifyBy == "css selector":
                self.driver.find_element_by_css_selector(c)
            flag = True
        except NoSuchElementException:
            flag = False
        finally:
            return flag

if __name__ == '__main__':
    # Runtime
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTests)
    unittest.TextTestRunner(verbosity=4).run(suite)