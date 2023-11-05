from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class WebdriverGlobalConfig:
  def __init__(self):
    self.options = Options()

  def init_options(self):
    options = self.options
    # Prod options
    options.add_argument("headless")
    options.add_argument("disable-gpu")
    options.add_argument("no-sandbox")
    # Dev options
    # options.add_experimental_option("detach", False)
    # options.add_argument("--window-size=1920,1200")
    return options

  def driver(self, options, url):
    driver = webdriver.Chrome(options)
    driver.get(url)
    return driver