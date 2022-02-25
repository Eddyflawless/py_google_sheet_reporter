import unittest
from app import db, read, write, api
import main
from dotenv import load_dotenv

from main import getEnv
from pathlib import Path
load_dotenv(dotenv_path = Path('.env'))

class TestExample(unittest.TestCase):

    def setUp(self):
        pass


if __name__ == "__main__":
    unittest.main()
