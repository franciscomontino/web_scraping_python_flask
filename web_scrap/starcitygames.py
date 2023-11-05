from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from classes import card_data

Card = card_data.CardData

def search_card(driver, cardName):
  result_list = []

  try:
    print("Searching in SCG...")
    ## Search card
    driver.find_element(By.ID, "search_query").send_keys(cardName)
    driver.find_element(By.ID, "search_query").send_keys(Keys.ENTER)

    # Wait for the content
    wait = WebDriverWait(driver, 10)
    element_location = (By.ID, "hawkitemlist")
    wait.until(EC.visibility_of_element_located(element_location))

    # Get list of cards found
    data_list = driver.find_elements(By.CLASS_NAME, "hawk-results-item")

    # For each card get the data
    for card_data in data_list:
      name = card_data.find_element(By.CLASS_NAME, "item-title-link")
      edition = card_data.find_element(By.CLASS_NAME, "item-category-link")
      price = card_data.find_element(By.CLASS_NAME, "price-wrapper")
      available = card_data.find_element(By.CLASS_NAME, "stock-count")
      image_url = card_data.find_element(By.CLASS_NAME, "item-image").get_attribute("src")
      card_url = card_data.find_element(By.CSS_SELECTOR, "a.item-title-link").get_attribute("href")

      # Add card to cards array
      new_card = Card(name.text, edition.text, price.text, available.text, image_url, card_url)
      result_list.append(new_card.__dict__)

    return result_list

  except Exception as e:
    print(e)
    return []