# Get cards with stock
def filter_by_stock(list):
  try:
    return [i for i in list if (i['available'] != "Out of stock." and i['available'] != "Out of stock")]
  except:
    return []

def get_cheaper(list):
  try:
    # Fix prices removing symbols and converting it into float
    for i in list:
      i.update({"price": float(i["price"].replace("$", ""))})

    # Return dict of card with lower price
    index = min(range(len(list)), key=lambda i: list[i]["price"])
    return list[index]
  except:
    return {}

# This method looks into all results and return the cheapest card found
def find_cheapest_card(result_array):
  data = filter_by_stock(result_array)
  return get_cheaper(data)
