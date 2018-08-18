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
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

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

        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'iOS',
                'platformVersion': '11.0',
                'deviceName': 'iPhone X',
            })


        '''
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app_ipa,
                'platformName': 'iOS',
                'platformVersion': '11.2',
                'deviceName': 'Hsieh_iPhone',
                'xcodeConfigFile': config,
                'udid': '54497de27036b691eb86c6aec0264f6e57d2de9a'
            })
        '''

        # WebDriverWait(self.driver, 3).until(
        #    expected_conditions.presence_of_element_located
        #    ((By.ID, 'com.android.packageinstaller:id/permission_allow_button')), message='not find')

    # Find elements
    # def test_find_elements_alert(self):
    #    el = self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
    #    el.click()
    #    self.assertIsNotNone(el) #Pass if exist

    # Find elements scanerio

    '''
    def alert_interaction(self):
        # go to the alerts section
        self.driver.find_element_by_name('Alert Views').click()
        triggerOk = self.driver.find_element_by_accessibility_id("Simple")

        # TOFIX: Looks like alert object is not proper state
        # something to do with UIActionSheet vs. UIAlertView?
        # triggerOk = elements[0]
        triggerOk.click()
        alert = self.driver.switch_to.alert

        # dismiss alert
        alert.accept()

        # trigger modal alert with cancel & ok buttons
        triggerOkCancel = self.driver.find_element_by_accessibility_id("Okay / Cancel")
        triggerOkCancel.click()
        alert = self.driver.switch_to.alert

        # check if title of alert is correct
        self.assertEqual(alert.text, "A Short Title Is Best A message should be a short, complete sentence.")
        alert.accept()
    '''

    '''
    #scanerio 1
    def test_find_elements_main(self):
        sleep(10)
        #self.driver.switch_to.alert.accept()
        #self.wait.until(ExpectedConditions.alertIsPresent());

        #self.driver.switch_to_alert().accept()

        # check if title of alert is correct
        #self.assertEqual(alert.text, "A Short Title Is Best A message should be a short, complete sentence.")
        #alert.accept()

        #self.driver.find_element_by_name("Allow").click()
        sleep(2)
        el = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"ic m member\"]")
        el.click()
        self.assertIsNotNone(el) #Pass if exist
        self.driver.back()
        sleep(2)
        el = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"ic m sales\"]")
        el.click()
        self.assertIsNotNone(el) #Pass if exist
        self.driver.back()
        sleep(2)
        el = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"ic m dm\"]")
        el.click()
        self.assertIsNotNone(el) #Pass if exist
        self.driver.back()
        sleep(2)
        el = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"ic m event\"]")
        el.click()
        self.assertIsNotNone(el) #Pass if exist
        self.driver.back()
        sleep(2)
        el = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"ic m fb\"]")
        el.click()
        self.assertIsNotNone(el) #Pass if exist
        self.driver.back()
        sleep(2)
        el = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"ic m shop\"]")
        el.click()
        self.assertIsNotNone(el) #Pass if exist
        self.driver.back()
    '''

    '''
    #scanerio 2
    def test_find_elements_member(self):
        sleep(10)
        #self.driver.switch_to_alert().accept()
        sleep(2)
        el = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"ic m member\"]")
        el.click()
        sleep(2)
        el = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"ic m ecoupon\"]")
        el.click()
        self.assertIsNotNone(el) #Pass if exist
        self.driver.back()
        sleep(6)
        el = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"ic m redcard\"]")
        el.click()
        self.assertIsNotNone(el) #Pass if exist
        sleep(2)
        self.driver.back()
        sleep(2)
        el = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"ic m mberinfo\"]")
        el.click()
        self.assertIsNotNone(el) #Pass if exist
        self.driver.back()
        sleep(2)
        el = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"ic m ecmrp\"]")
        el.click()
        self.assertIsNotNone(el) #Pass if exist
    '''
    '''
    #scenario 3
    def test_slide_bar(self):
        sleep(15)
        el = self.driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='Navigate up']")
        el.click()
        el = self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='回主畫面']")
        el.click()

        sleep(2)

        el = self.driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='Navigate up']")
        el.click()
        el = self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='會員專區']")
        el.click()

        sleep(2)

        el = self.driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='Navigate up']")
        el.click()
        el = self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='特價品']")
        el.click()

        sleep(2)

        el = self.driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='Navigate up']")
        el.click()
        el = self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='型錄']")
        el.click()

        sleep(2)

        el = self.driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='Navigate up']")
        el.click()
        el = self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='活動']")
        el.click()

        sleep(2)

        el = self.driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='Navigate up']")
        el.click()
        el = self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='各地分店']")
        el.click()

        sleep(2)

        #slide down
        el = self.driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='Navigate up']")
        el.click()
        element_to_tap = self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='各地分店']")
        element_to_drag_to = self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='型錄']")
        self.driver.scroll(element_to_tap, element_to_drag_to)

        sleep(2)

        el = self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='丁丁官方網站']")
        el.click()

        sleep(2)

        el = self.driver.find_element_by_id("com.tintin.tintinapp:id/img_btn_exit")
        el.click()
        sleep(2)
        self.driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='Navigate up']").click()

        sleep(2)

        element_to_tap = self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='各地分店']")
        element_to_drag_to = self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='型錄']")
        self.driver.scroll(element_to_tap, element_to_drag_to)

        sleep(2)

        el = self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='丁丁官方粉絲團']")
        el.click()

        sleep(2)

        el = self.driver.find_element_by_id("com.tintin.tintinapp:id/img_btn_exit")
        el.click()
        self.driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='Navigate up']").click()

        sleep(2)

        element_to_tap = self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='各地分店']")
        element_to_drag_to = self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='型錄']")
        self.driver.scroll(element_to_tap, element_to_drag_to)

        sleep(2)

        el = self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='丁丁官方粉絲團']")
        el.click()

        sleep(2)

        el = self.driver.find_element_by_id("com.tintin.tintinapp:id/img_btn_exit")
        el.click()
        self.driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='Navigate up']").click()

        sleep(2)

        element_to_tap = self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='各地分店']")
        element_to_drag_to = self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='型錄']")
        self.driver.scroll(element_to_tap, element_to_drag_to)

        sleep(2)

        el = self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='訊息通知']")
        el.click()

        sleep(2)

        el = self.driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='Navigate up']")
        el.click()
        element_to_tap = self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='各地分店']")
        element_to_drag_to = self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='型錄']")
        self.driver.scroll(element_to_tap, element_to_drag_to)

        sleep(5)

        el = self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='聯絡我們']")
        el.click()

        sleep(2)

        el = self.driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='Navigate up']")
        el.click()

        sleep(2)

        el = self.driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='Navigate up']")
        el.click()
        element_to_tap = self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='各地分店']")
        element_to_drag_to = self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='型錄']")
        self.driver.scroll(element_to_tap, element_to_drag_to)

        sleep(2)

        el = self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='設定']")
        el.click()

        self.assertIsNotNone(el) #Pass if exist

    #scenario 4
    def test_sales(self):

        sleep(15)

        el = self.driver.find_element_by_id("com.tintin.tintinapp:id/img_btn_sales")
        el.click()
        self.assertIsNotNone(el) #Pass if exist
        sleep(5)

        #click
        el = self.driver.find_element_by_id("com.tintin.tintinapp:id/img_btn_sales")
        el.click()
        self.assertIsNotNone(el) #Pass if exist
        el = self.driver.find_element_by_id("com.tintin.tintinapp:id/img_btn_sales_catalog")
        el.click()
        self.assertIsNotNone(el) #Pass if exist
        el = self.driver.find_element_by_id("com.tintin.tintinapp:id/img_btn_sales_item")
        el.click()
        self.assertIsNotNone(el) #Pass if exist

        sleep(2)

        #drag down
        el = self.driver.find_element_by_id("com.tintin.tintinapp:id/img_btn_sales")
        el.click()
        sleep(2)

        #self.driver.swipe(start_x, start_y, end_x, end_y, duration)
        self.driver.swipe(470, 500, 470, 100, 500)
        sleep(1)
        self.driver.swipe(470, 500, 470, 100, 500)
        sleep(1)
        self.driver.swipe(470, 500, 470, 100, 500)
        sleep(1)
        self.driver.swipe(470, 500, 470, 100, 500)
        sleep(1)

        #choose one
        #TouchAction().tap(x=300, y=300).release()
        #self.driver.tap([(300,300)], 500)

        #x = self.driver.get_window_size()['width']
        #y = self.driver.get_window_size()['height']

        #x = int(x * 0.1)
        #y = int(y * 0.1)

        #self.driver.swipe(x, y, x, y,1) 


        #self.driver.swipe(350, 400, 350, 400, 1)
        self.driver.tap([(500, 1500)], 500)
        sleep(3)

        #go to login
        el = self.driver.find_element_by_id("com.tintin.tintinapp:id/btn_submit").click()

        sleep(3)

        #login
        self.driver.find_element_by_id("com.tintin.tintinapp:id/txt_login_id").send_keys("anonymous")
        self.driver.find_element_by_id("com.tintin.tintinapp:id/txt_login_pw").send_keys("norbel18")
        self.driver.hide_keyboard()
        self.driver.find_element_by_id("com.tintin.tintinapp:id/btn_login").click()

        sleep(5)

        self.driver.swipe(470, 500, 470, 50, 50)
        sleep(1)
        self.driver.swipe(470, 900, 470, 50, 50)
        sleep(1)
        self.driver.swipe(470, 50, 470, 200, 50)
        sleep(3)

        el = self.driver.find_element_by_id("com.tintin.tintinapp:id/img_btn_exit")
        el.click()
        sleep(2)

        el = self.driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='Navigate up']")
        el.click()
        sleep(2)

        self.driver.swipe(470, 1300, 470, 100, 500)
        sleep(1)
        self.driver.swipe(470, 1300, 470, 100, 500)
        sleep(1)
        self.driver.swipe(470, 200, 470, 500, 500)
        sleep(1)

        self.driver.tap([(700, 1500)], 500)

        sleep(3)

        #go to login
        self.driver.find_element_by_id("com.tintin.tintinapp:id/btn_submit").click()
        sleep(3)

        self.driver.swipe(470, 900, 470, 50, 50)
        sleep(1)
        self.driver.swipe(470, 200, 470, 500, 500)
        sleep(1)

        el = self.driver.find_element_by_id("com.tintin.tintinapp:id/img_btn_exit")
        el.click()
        sleep(2)

        el = self.driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='Navigate up']")
        el.click()
        sleep(2)

        #sales catalog
        el = self.driver.find_element_by_id("com.tintin.tintinapp:id/img_btn_sales_catalog")
        el.click()
        self.assertIsNotNone(el) #Pass if exist

        self.driver.find_element_by_id("com.tintin.tintinapp:id/sp_catalog").click()
        sleep(3)
        #self.driver.find_element_by_xpath("//android.widget.FrameLayout[0]/android.widget.ListView[0]/[@text='紙尿褲']").click()

        #index start with 1, not 0
        self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.TextView[2]").click()
        #self.driver.find_element_by_xpath("//android.widget.ListView[0]/android.widget.TextView[1]").click()
        #self.driver.find_element_by_name("紙尿褲").click()
        sleep(2)

        self.driver.swipe(470, 900, 470, 50, 50)
        sleep(1)
        self.driver.swipe(470, 200, 470, 500, 500)
        sleep(3)

        self.driver.swipe(470, 900, 470, 0, 50)
        sleep(1)
        self.driver.swipe(470, 0, 470, 900, 50)
        self.driver.tap([(700, 1500)], 500)
        sleep(1)
        el = self.driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='Navigate up']")
        el.click()
        sleep(2)

        el = self.driver.find_element_by_id("com.tintin.tintinapp:id/img_btn_sales_catalog")
        el.click()
        self.assertIsNotNone(el) #Pass if exist

        self.driver.find_element_by_id("com.tintin.tintinapp:id/sp_catalog").click()
        sleep(3)
        self.driver.find_element_by_xpath(
            "//android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.TextView[9]").click()
        #self.driver.find_element_by_xpath("//android.widget.FrameLayout[0]/android.widget.ListView[0]/[@text='車床、汽座及寢具']").click()
        sleep(2)

        self.driver.swipe(470, 900, 470, 0, 50)
        sleep(1)
        self.driver.swipe(470, 0, 470, 900, 50)
        self.driver.tap([(700, 1500)], 500)
        sleep(1)
        el = self.driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='Navigate up']")
        el.click()
        sleep(2)

        el = self.driver.find_element_by_id("com.tintin.tintinapp:id/img_btn_sales_item")
        el.click()
        self.assertIsNotNone(el)  # Pass if exist

        self.driver.find_element_by_id("com.tintin.tintinapp:id/edittext_item_name").send_keys("12")
        sleep(1)
        self.driver.find_element_by_id("com.tintin.tintinapp:id/btn_sales_item_search").click()
        sleep(2)

        self.driver.swipe(470, 900, 470, 0, 50)
        sleep(1)
        self.driver.swipe(470, 0, 470, 900, 50)
        self.driver.tap([(700, 1500)], 500)
        sleep(1)
        el = self.driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='Navigate up']")
        el.click()
        sleep(2)

        el = self.driver.find_element_by_id("com.tintin.tintinapp:id/img_btn_sales_item")
        el.click()
        self.assertIsNotNone(el)  # Pass if exist

        self.driver.find_element_by_id("com.tintin.tintinapp:id/edittext_item_name").send_keys("aaa")
        sleep(1)

        self.driver.swipe(470, 900, 470, 0, 50)
        sleep(1)
        self.driver.swipe(470, 0, 470, 900, 50)
        self.driver.tap([(700, 1500)], 500)
        sleep(1)
        el = self.driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='Navigate up']")
        el.click()
        sleep(2)

        el = self.driver.find_element_by_id("com.tintin.tintinapp:id/img_btn_sales_item")
        el.click()
        self.assertIsNotNone(el)  # Pass if exist

        self.driver.find_element_by_id("com.tintin.tintinapp:id/edittext_item_name").send_keys("ardo")
        sleep(1)
        self.driver.find_element_by_id("com.tintin.tintinapp:id/btn_sales_item_search").click()
        sleep(2)

        self.driver.swipe(470, 900, 470, 0, 50)
        sleep(1)
        self.driver.swipe(470, 0, 470, 900, 50)
        sleep(1)
        el = self.driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='Navigate up']")
        el.click()
        sleep(2)

    #scenario 5
    def test_dm(self):

        sleep(15)

        el = self.driver.find_element_by_id("com.tintin.tintinapp:id/img_btn_dm")
        el.click()

        #swipe it
        sleep(10)

        self.driver.swipe(900, 300, 20, 300, 1000)
        sleep(1)
        self.driver.swipe(900, 300, 20, 300, 1000)
        sleep(1)
        self.driver.swipe(900, 300, 20, 300, 1000)
        sleep(1)
        self.driver.swipe(300, 300, 900, 300, 1000)
        sleep(1)
        self.driver.swipe(300, 300, 900, 300, 1000)
        sleep(1)


        self.driver.find_element_by_id("com.tintin.tintinapp:id/rlayout_rpage").click()
        sleep(3)
        self.driver.find_element_by_id("com.tintin.tintinapp:id/rlayout_rpage").click()
        sleep(3)
        self.driver.find_element_by_id("com.tintin.tintinapp:id/rlayout_lpage").click()
        sleep(3)

        #zoom
        el = self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.ImageView[1]")
        #el = self.driver.find_element_by_id("com.tintin.tintinapp:id/dm_view_pager").click()
        #el = self.driver.find_element_by_xpath("//android.support.v4.view.ViewPager[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]")

        #self.driver.pinch(element=el, percent=300, steps=50)

        #self.driver.pinch(element=el, percent=50, steps=50)

        #self.driver.pinch(element=el, percent=50, steps=50)

    def test_event(self):

        sleep(15)

        el = self.driver.find_element_by_id("com.tintin.tintinapp:id/img_btn_event")
        el.click()

        #swipe it

        self.driver.swipe(300, 1000, 300, 200, 1000)
        sleep(1)
        self.driver.swipe(300, 1000, 300, 200, 1000)
        sleep(1)
        self.driver.swipe(300, 200, 300, 600, 1000)
        sleep(1)

        #click
        self.driver.tap([(300, 600)], 500)
        sleep(3)

        el = self.driver.find_element_by_id("com.tintin.tintinapp:id/img_btn_exit")
        el.click()
        sleep(2)

        self.driver.swipe(300, 1000, 300, 100, 1000)
        sleep(1)

        self.driver.tap([(500, 400)], 500)
        sleep(3)

        el = self.driver.find_element_by_id("com.tintin.tintinapp:id/img_btn_exit")
        el.click()
        sleep(2)

        self.driver.back()

    def test_fb(self):
        sleep(15)
        el = self.driver.find_element_by_id("com.tintin.tintinapp:id/img_btn_fb")
        el.click()
        sleep(5)
        self.driver.swipe(300, 1000, 300, 200, 1000)
        self.driver.swipe(300, 1000, 300, 100, 1000)
        self.driver.swipe(300, 200, 300, 600, 1000)
        sleep(1)

        el = self.driver.find_element_by_id("com.tintin.tintinapp:id/img_btn_exit")
        el.click()

    def test_shop(self):
        sleep(15)
        self.driver.find_element_by_id("com.tintin.tintinapp:id/img_btn_shop").click()
        sleep(2)
        self.driver.find_element_by_id("com.tintin.tintinapp:id/img_btn_allshopslist").click()
        sleep(2)
        self.driver.find_element_by_id("com.tintin.tintinapp:id/img_btn_allshopsmap").click()
        sleep(2)
        self.driver.swipe(300, 1000, 300, 200, 1000)
        self.driver.swipe(300, 1000, 300, 100, 1000)

        sleep(1)
        self.driver.find_element_by_id("com.tintin.tintinapp:id/img_btn_allshopslist").click()
        sleep(2)

        #self.driver.find_element_by_id("com.tintin.tintinapp:id/rlayout_map").click()
        self.driver.tap([(900, 1200)], 500)
        sleep(3)

        self.driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='Navigate up']").click()
        sleep(2)

        self.driver.swipe(500, 1000, 500, 50, 1000)


        self.driver.find_element_by_id("com.tintin.tintinapp:id/sp_city").click()
        sleep(1)
        self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.TextView[4]").click()

        sleep(1)
        self.driver.swipe(500, 1000, 500, 50, 1000)
        sleep(1)

        self.driver.find_element_by_id("com.tintin.tintinapp:id/sp_city").click()
        sleep(1)
        self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.TextView[7]").click()

        self.driver.swipe(500, 1000, 500, 50, 1000)
        sleep(1)

        self.driver.find_element_by_id("com.tintin.tintinapp:id/sp_city").click()
        sleep(1)
        self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.TextView[5]").click()

        self.driver.swipe(500, 1000, 500, 50, 1000)
        sleep(1)

    def test_contact(self):
        sleep(15)
        self.driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='Navigate up']").click()
        element_to_tap = self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='各地分店']")
        element_to_drag_to = self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='型錄']")
        self.driver.scroll(element_to_tap, element_to_drag_to)

        sleep(3)
        self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='聯絡我們']").click()
        self.driver.find_element_by_id("com.tintin.tintinapp:id/cardview_contact_us").click()
        self.driver.back()

        sleep(2)
        self.driver.find_element_by_id("com.tintin.tintinapp:id/cardview_contact_mail").click()
        self.driver.back()

        sleep(2)
        self.driver.find_element_by_id("com.tintin.tintinapp:id/cardview_contact_message").click()

        sleep(1)
        self.driver.find_element_by_id("com.tintin.tintinapp:id/edittext_message_name").send_keys("test")
        self.driver.hide_keyboard()
        self.driver.find_element_by_id("com.tintin.tintinapp:id/edittext_message_orderid").send_keys("0000000000")
        self.driver.hide_keyboard()
        self.driver.find_element_by_id("com.tintin.tintinapp:id/edittext_message_tel").send_keys("07-0000000")
        self.driver.hide_keyboard()
        self.driver.find_element_by_id("com.tintin.tintinapp:id/edittext_message_email").send_keys("test@test.com")
        self.driver.hide_keyboard()
        self.driver.find_element_by_id("com.tintin.tintinapp:id/edittext_message_question").send_keys("test test test test \n test test test \n test test \n test ")
        self.driver.hide_keyboard()
        self.driver.find_element_by_id("com.tintin.tintinapp:id/btn_contact_us_submit").click()

        sleep(2)
        self.driver.back()

    def test_set(self):
        sleep(15)
        self.driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='Navigate up']").click()
        element_to_tap = self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='各地分店']")
        element_to_drag_to = self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='特價品']")
        self.driver.scroll(element_to_tap, element_to_drag_to)
        sleep(1)
        self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='設定']").click()
        sleep(1)
        el = self.driver.find_element_by_id("android:id/list").click()
        el.find_element_by_xpath(el + "/android.widget.LinearLayout[2]")
        el.click()
        el.find_element_by_xpath(el + "/android.widget.LinearLayout[3]")
        el.click()
        self.driver.back()
        el.find_element_by_xpath(el + "/android.widget.LinearLayout[4]")
        el.click()
        self.driver.back()
        el.find_element_by_xpath(el + "/android.widget.LinearLayout[5]")
        el.click()
        self.driver.back()
        el.find_element_by_xpath(el + "/android.widget.LinearLayout[9]")
        el.click()
        self.driver.back()
    '''

    def tearDown(self):
        # end the session
        self.driver.quit()

    def isElementPresent(self, locator):
        try:
            self.driver.find_element_by_xpath(locator)
        except NoSuchElementException:
            print ('No such thing')
            return False
        return True


if __name__ == '__main__':
    # Runtime
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTests)
    unittest.TextTestRunner(verbosity=4).run(suite)