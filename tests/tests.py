import unittest
import os

import lauteur


TEST_DIR = os.path.abspath(os.path.dirname(__file__))
FIXTURES_DIR = os.path.join(TEST_DIR, 'fixtures')


class Tests(unittest.TestCase):
  
  def test_from_string(self):
    string = 'By: Brian Abelson ,and Michael H. Keller & Dr. Stijn Debrouwere IV'
    result = ['Brian Abelson', 'Michael H Keller', 'DR Stijn Debrouwere IV']
    
    assert(str(lauteur.from_string(string)) == str(result))

  def test_from_html(self):
    with open(os.path.join(FIXTURES_DIR, 'test.html'), 'rb') as f:
      html = f.read()
    print html
    result = ['Michiko Kakutani']
    assert(str(lauteur.from_html(html)) == str(result))
