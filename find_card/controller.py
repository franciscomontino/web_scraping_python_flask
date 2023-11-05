from config import webdriver_global_config, env
from web_scrap import card_kingndom, starcitygames
from utils.main import find_cheapest_card

# Get env
new_env = env.Env().__dict__
ck_url = new_env.get("ck_url")
scg_url = new_env.get("scg_url")

def search_all(cardName):
  try:
    # Class config instance
    GlobalConfig = webdriver_global_config.WebdriverGlobalConfig
    new_config = GlobalConfig()
    options = new_config.init_options()

    # Instances of class config
    driver_ck = new_config.driver(options, ck_url)
    driver_scg = new_config.driver(options, scg_url)

    # Search results
    card_kingndom_result = card_kingndom.search_card(driver_ck, cardName)
    starcitygames_result = starcitygames.search_card(driver_scg, cardName)

    all_results = card_kingndom_result + starcitygames_result
    cheapest_card = find_cheapest_card(all_results)
    
    response = dict(
      cheapest_card = cheapest_card,
      all_results = all_results,
    )

    return response
  
  except Exception as e:
    print(e)
    return
