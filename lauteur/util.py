from HTMLParser import HTMLParser
import re
from bs4 import BeautifulSoup

def make_soup(html):
  return BeautifulSoup(html)

# html stripping
class MLStripper(HTMLParser):
  def __init__(self):
    self.reset()
    self.fed = []

  def handle_data(self, d):
    self.fed.append(d)

  def get_data(self):
    return ''.join(self.fed)

def strip_tags(html):
  """
  string tags and clean text from html.
  """
  s = MLStripper()
  s.feed(html)
  raw_text = s.get_data()
  raw_text = re.sub(r'\n|\t|\r', ' ', raw_text)
  return re.sub('\s+', ' ', raw_text).strip()