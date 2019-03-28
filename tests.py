import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from helpers import set_fields, close_alerts


class CompetitionTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Safari()
        self.driver.get("https://lamp.ii.us.edu.pl/~mtdyd/zawody/")

    def test_if_person_below_age_ten_is_not_qualified(self):
        set_fields(self.driver, date="20-04-2018")
        close_alerts()
        assert "Brak kwalifikacji" in driver.page_source

    def test_if_person_between_ten_and_eleven_is_skrzat(self):
        set_fields(self.driver, date="20-04-2008", parent_approval=True, doctor_approval=True)
        close_alerts()
        assert "zostal zakwalifikowany do kategorii Skrzat"  in driver.page_source

    def test_if_person_between_twelve_and_therteen_is_mlodzik(self):
        set_fields(self.driver, date="20-04-2006", parent_approval=True, doctor_approval=True)
        close_alerts()
        assert "zostal zakwalifikowany do kategorii Mlodzik"  in driver.page_source 

    def test_if_person_between_fourteen_and_seventeen_is_junior(self):
        set_fields(self.driver, date="20-04-2004", parent_approval=True, doctor_approval=True)
        close_alerts()
        assert "zostal zakwalifikowany do kategorii Junior"  in driver.page_source

    def test_if_person_between_eighteen_and_sixty_four_is_dorosly(self):
        set_fields(self.driver, date="20-04-1990")
        close_alerts()
        assert "zostal zakwalifikowany do kategorii Dorosly"  in driver.page_source

    def test_if_person_age_is_greater_than_sixty_five_is_senior(self):
        set_fields(self.driver, date="20-04-2008", parent_approval=True)
        close_alerts()
        assert "zostal zakwalifikowany do kategorii Senior"  in driver.page_source

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
