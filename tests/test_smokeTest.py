# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

class TestSmokeTest():
  def setup_method(self, method):
    options = Options()
    options.add_argument("--headless=new")
    self.driver = webdriver.Chrome(options=options)
    self.vars = {}

  def teardown_method(self, method):
    self.driver.quit()

  def test_homepageLogoTitle(self):
    self.driver.get("http://127.0.0.1:5501/teton/1.6/index.html")
    self.driver.set_window_size(1311, 816)
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".header-logo img")
    assert len(elements) > 0
    assert self.driver.find_element(By.CSS_SELECTOR, ".header-title > h1").text == "Teton Idaho"
    assert self.driver.find_element(By.CSS_SELECTOR, ".header-title > h2").text == "Chamber of Commerce"
    assert self.driver.title == "Teton Idaho CoC"

  def test_adminUsernamePassword(self):
    self.driver.get("http://127.0.0.1:5501/teton/1.6/index.html")
    self.driver.set_window_size(1178, 816)
    self.driver.find_element(By.LINK_TEXT, "Admin").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".myinput:nth-child(2)").text == "Username:"
    elements = self.driver.find_elements(By.ID, "username")
    assert len(elements) > 0
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").send_keys("incorrect")
    self.driver.find_element(By.ID, "password").send_keys("incorrect")
    self.driver.find_element(By.CSS_SELECTOR, ".mysubmit:nth-child(4)").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".errorMessage"), "Invalid username and password."))

  def test_directorGridList(self):
    self.driver.get("http://127.0.0.1:5501/teton/1.6/index.html")
    self.driver.set_window_size(1287, 816)
    self.driver.find_element(By.LINK_TEXT, "Directory").click()
    self.driver.find_element(By.ID, "directory-grid").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".gold-member:nth-child(9) > p:nth-child(2)").text == "Teton Turf and Tree"
    self.driver.find_element(By.ID, "directory-list").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".gold-member:nth-child(9) > p:nth-child(2)").text == "Teton Turf and Tree"

  def test_homepageSpotlightsJoin(self):
    self.driver.get("http://127.0.0.1:5501/teton/1.6/index.html")
    self.driver.set_window_size(1235, 816)
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight1")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight2")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.LINK_TEXT, "Join Us")
    assert len(elements) > 0
    self.driver.find_element(By.LINK_TEXT, "Join Us").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "section > h3").text == "Welcome to the Teton Chamber of Commerce Signup Wizard!"

  def test_joinpageDataEntry(self):
    self.driver.get("http://127.0.0.1:5501/teton/1.6/index.html")
    self.driver.set_window_size(1295, 816)
    self.driver.find_element(By.LINK_TEXT, "Join").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".myinput:nth-child(2)").text == "First Name"
    elements = self.driver.find_elements(By.NAME, "fname")
    assert len(elements) > 0
    self.driver.find_element(By.NAME, "fname").send_keys("Diego")
    self.driver.find_element(By.NAME, "lname").send_keys("Vasquez")
    self.driver.find_element(By.NAME, "bizname").send_keys("Vasquez\'s Rest")
    self.driver.find_element(By.NAME, "biztitle").send_keys("Waiter")
    self.driver.find_element(By.NAME, "submit").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".myinput:nth-child(2)").text == "Email"
    elements = self.driver.find_elements(By.NAME, "email")
    assert len(elements) > 0
