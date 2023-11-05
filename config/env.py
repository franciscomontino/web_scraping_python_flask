import os
from dotenv import load_dotenv

load_dotenv()

class Env:
  _instance = None

  def __new__(cls):
    if cls._instance is None:
      cls._instance = super(Env, cls).__new__(cls)
    return cls._instance
  
  def __init__(self):
    self.port = os.getenv("PORT")
    self.debug = os.getenv("DEBUG")
    self.ck_url = os.getenv("CK_URL")
    self.scg_url = os.getenv("SCG_URL")