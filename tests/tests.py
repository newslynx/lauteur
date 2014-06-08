import unittest
import os

import lauteur

TEST_DIR = os.path.abspath(os.path.dirname(__file__))
FIXTURES_DIR = os.path.join(TEST_DIR, 'fixtures')

class Tests(unittest.TestCase):
  
  def test_from_string(self):
    string = 'By: Brian Abelson ,and Michael H. Keller & Dr. Stijn Debrouwere IV'
    truth = ['Brian Abelson', 'Michael H Keller', 'DR Stijn Debrouwere IV']
    test = lauteur.from_string(string)
    assert(str(test) == str(truth))

  def test_from_html(self):
    with open(os.path.join(FIXTURES_DIR, 'test.html'), 'rb') as f:
      html = f.read()
    truth = ['Michiko Kakutani']
    test = lauteur.from_html(html)
    try:
      assert(str(test) == str(truth))
    except AssertionError:
      print "FAILED ON", test 
      print "SHOULD HAVE BEEN", truth

