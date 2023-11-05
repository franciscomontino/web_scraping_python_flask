from selenium.webdriver.common.by import By
from classes import card_data

Card = card_data.CardData

def search_card(driver, cardName):
  result_list = []

  try:
    print("Searching in Card Kingdom...")
    ## Search card
    driver.find_element(By.ID, "header-search-input").send_keys(cardName)
    driver.find_element(By.CLASS_NAME, "input-icon").click()

    # Get list of cards found
    data_list = driver.find_elements(By.CLASS_NAME, "productItemWrapper.productCardWrapper")

    # For each card get the data
    for card_data in data_list:
      name = card_data.find_element(By.CLASS_NAME, "productDetailTitle")
      edition = card_data.find_element(By.CLASS_NAME, "productDetailSet").find_element(By.TAG_NAME, "a")
      showAvailable = card_data.find_element(By.CSS_SELECTOR, "li.itemAddToCart.active")
      price = showAvailable.find_element(By.CLASS_NAME, "stylePrice")
      try:
        available = showAvailable.find_element(By.CLASS_NAME, "styleQty")
      except:
        available = showAvailable.find_element(By.CLASS_NAME, "outOfStockNotice")
      image_url = card_data.find_element(By.CLASS_NAME, "card-image").get_attribute("src")
      card_url = card_data.find_element(By.CSS_SELECTOR, "a.card-link").get_attribute("href")

      # Add card to cards array
      new_card = Card(name.text, edition.text, price.text, available.text, image_url, card_url)
      result_list.append(new_card.__dict__)

    return result_list
  except Exception as e:
    print(e)
    return []
