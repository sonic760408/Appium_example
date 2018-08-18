# coding:utf-8
import os
from time import sleep

import unittest

from appium import webdriver
from appium.webdriver.webelement import WebElement
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

        app = os.path.abspath('./apk/TinTinApp_iOS.app')
        app_ipa = os.path.abspath('./apk/TinTinApp_iOS.ipa')
        config = os.path.abspath('./config.xcconfig')

        desired_caps = {}

        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '11.2'
        desired_caps['deviceName'] = 'iPhone X'
        desired_caps['app'] = app
        desired_caps['xcodeConfigFile'] = config


        '''
        desired_caps['udid'] = '54497de27036b691eb86c6aec0264f6e57d2de9a'
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '11.2'
        desired_caps['deviceName'] = 'Hsieh_iPhone'
        desired_caps['app'] = app_ipa
        desired_caps['xcodeConfigFile'] = config
        '''

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


    #Aborted
    '''
    def test_reg(self):
        sleep(5)
        self.driver.switch_to.alert.accept()
        sleep(3)
        #el1 = self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
        #el1.click()
        # self.driver.find_element_by_xpath("//android.widget.Button[@text='允許']").click()
        self.driver.background_app(1)  # focus app background
        sleep(1)

        # self.driver.find_element_by_xpath("com.android.packageinstaller:id/permission_allow_button")

        #el0 = self.driver.find_element_by_xpath("//android.view.ViewGroup[1]/android.widget.RelativeLayout[2]/android.widget.ImageView[1]")
        #el0.tap()
        #el0.clear()
        # self.assertIsNotNone(el)
        # action.tap(el, 100, 60).perform()
        #self.driver.swipe(100, 60, 100, 60)
        #sleep(2)
        el = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"ic m member\"]")
        el.click()
        sleep(1)
        self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"ic m mberinfo\"]").click()
        sleep(1)
        self.driver.find_element_by_accessibility_id("還沒有帳號嗎? 立即註冊").click()
        sleep(1)

        #el.send_keys("sonicmax")
        #sleep(1)
        #self.driver.find_element_by_id("com.tintin.tintinapp:id/btn_confirm").click()
        #sleep(1)

        #self.driver.back()
        #sleep(2)
        #self.driver.find_element_by_id("com.tintin.tintinapp:id/rlayout_mberinfo_mberno").click()
    '''
    '''
    def test_forgetpwd(self):
        sleep(5)
        self.driver.switch_to_alert().accept()

        #el1 = self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
        #el1.click()
        # self.driver.find_element_by_xpath("//android.widget.Button[@text='允許']").click()
        #self.driver.background_app(1)  # focus app background
        sleep(1)

        el = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"ic m member\"]")
        el.click()
        sleep(1)
        self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"ic m mberinfo\"]").click()
        sleep(1)
        self.driver.find_element_by_accessibility_id("忘記密碼").click()
        sleep(1)

        \'''
        self.driver.switch_to_alert()

        el = self.driver.find_element_by_xpath("//XCUIElementTypeAlert[@name=\"請填妥以下資料後, 將會重新寄送密碼重設連結到您設定的信箱\"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther").click()
        #el = self.driver.find_element_by_class_name("XCUIElementTypeTextField")
        el.send_keys("sonic760408@gmail.com")
        self.driver.hide_keyboard()
        #el2 = self.driver.find_element_by_class_name("XCUIElementTypeTextField")
        el2 = self.driver.find_element_by_xpath("//XCUIElementTypeAlert[@name=\"請填妥以下資料後, 將會重新寄送密碼重設連結到您設定的信箱\"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther").click()
        el2.send_keys("E123345007")
        self.driver.hide_keyboard()
        sleep(5)
        self.driver.find_element_by_accessibility_id("確定").click()
        sleep(3)
        self.driver.back()
        \'''
    '''

    def test_zoomit(self):
        sleep(5)
        self.driver.switch_to.alert.accept()
        sleep(3)
        #el1 = self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
        #el1.click()
        # self.driver.find_element_by_xpath("//android.widget.Button[@text='允許']").click()
        self.driver.background_app(1)  # focus app background
        sleep(1)
        el = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"ic m dm\"]")
        el.click()
        sleep(5)
        self.driver.swipe(470, 500, 30, 500, 500)
        sleep(1)
        self.driver.swipe(470, 500, 30, 500, 500)
        sleep(1)

        #pinch
        #self.driver.execute_script('mobile: scroll', {'direction': 'down'})

        #els = self.driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"丁丁連鎖藥妝\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeScrollView/XCUIElementTypeScrollView/XCUIElementTypeImage")
        #els = self.driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"丁丁連鎖藥妝\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeScrollView/XCUIElementTypeScrollView")

        els = self.driver.find_element_by_xpath("//XCUIElementTypeOther[@name=\"img_slide\"]/XCUIElementTypeScrollView/XCUIElementTypeScrollView")
        #a1 = TouchAction(self.driver)
        #a1.press(els) \
        #    .wait(10).move_to(x=153, y=346).move_to(x=82, y=232).release().perform()

        #a2 = TouchAction(self.driver)
        #a2.press(els) \
        #    .wait(10).move_to(x=212, y=450).move_to(x=302, y=467).release().perform()

        #ma = MultiAction(self.driver, els)
        #ma.add(a1, a2)

        #self.driver.execute_script("mobile: twoFingerTap", ma)
        #ma.perform()

        #zoom
        #self.driver.zoom(els, percent=400, steps=5)
        #print(" ZOOM it \n")
        #sleep(3)
        #self.driver.pinch(els, percent=400, steps=50)

        sleep(3)

        ma = self.driver.find_element_by_xpath("//XCUIElementTypeOther[@name=\"img_slide\"]/XCUIElementTypeScrollView/XCUIElementTypeScrollView/XCUIElementTypeImage")
        print(" Scale in \n")
        self.driver.execute_script('mobile: pinch', {'scale': '3.0', 'velocity': '1.1', 'element': ma})
        print(" Scale out \n")
        sleep(3)
        self.driver.execute_script('mobile: pinch', {'scale': '0.1', 'velocity': '-1.1', 'element': ma})
        sleep(3)
        self.driver.execute_script('mobile: pinch', {'scale': '0.1', 'velocity': '-1.1', 'element': ma})
        sleep(3)

    '''
    def test_shop(self):
        sleep(5)
        self.driver.switch_to.alert.accept()
        sleep(3)
        self.driver.tap([(33, 68)], 500)
        sleep(1)
        self.driver.find_element_by_accessibility_id("您好").click()
        sleep(1)
        self.driver.find_element_by_accessibility_id("txt_login_account").send_keys("anonymous")
        self.driver.find_element_by_accessibility_id("txt_login_pwd").send_keys("norbel18")
        self.driver.hide_keyboard()
        self.driver.find_element_by_accessibility_id("登入").click()
        sleep(3)
        self.driver.find_element_by_accessibility_id("ic m sales").click()
        sleep(4)
        self.driver.swipe(235, 724, 230, 180, 500)
        self.driver.swipe(250, 600, 220, 200, 500)
        self.driver.swipe(250, 410, 280, 550, 500)
        sleep(1)
        self.driver.tap([(100, 410)], 500)
        sleep(1)
        self.driver.swipe(235, 724, 230, 180, 500)
        self.driver.find_element_by_accessibility_id("前往購物網頁").click()
        sleep(5)
        # self.driver.swipe(171, 650, 150, 180, 1000)
        # self.driver.swipe(171, 650, 150, 180, 1000)
        # self.driver.swipe(200, 300, 250, 450, 500)

        element_to_tap = self.driver.find_element_by_xpath("//XCUIElementTypeImage[@name=\"丁丁連鎖藥妝\"]")
        element_to_drag_to = self.driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name=\"商品規格：\"]")
        self.driver.scroll(element_to_tap, element_to_drag_to)
        sleep(1)
        element_to_tap = self.driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name=\"回上頁\"]")
        element_to_drag_to = self.driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name=\"商品規格：\"]")
        self.driver.scroll(element_to_tap, element_to_drag_to)
        sleep(1)

        self.driver.tap([(29, 67)], 500)  # exit web
        sleep(1)
    '''

    def tearDown(self):
        # end the session
        self.driver.quit()

if __name__ == '__main__':
    # Runtime
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTests)
    unittest.TextTestRunner(verbosity=4).run(suite)