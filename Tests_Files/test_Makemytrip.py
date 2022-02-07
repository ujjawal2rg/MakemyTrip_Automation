import time

import pytest
from selenium import webdriver


#@pytest.mark.usefixtures("setup")
from selenium.webdriver.support.select import Select

from Utlities.BaseClass import BaseClass


class Test_FlightSearch(BaseClass):

    #@pytest.mark.smoke
    def test_st01(self):
        print("Page Title :",self.driver.title)
        print("Page Url :",self.driver.current_url)

        time.sleep(5)

        fr = self.driver.find_element_by_xpath("//span[contains(text(),'From')]")
        fr.click()
        ls=self.driver.find_element_by_css_selector("input[placeholder='From']")
        #ls=driver.find_element_by_css_selector("body.desktop.in:nth-child(2) div.bgGradient div.minContainer div.widgetSection.appendBottom40.primaryTraveler div.fsw.widgetOpen div.fsw_inner:nth-child(1) div.fsw_inputBox.searchCity.inactiveWidget.activeWidget:nth-child(1) div:nth-child(2) div:nth-child(1) div.hsw_autocomplePopup.autoSuggestPlugin div.react-autosuggest__container.react-autosuggest__container--open > input.react-autosuggest__input.react-autosuggest__input--open")
        ls.send_keys("pat")
        time.sleep(5)
        fsel=self.driver.find_element_by_css_selector("ul[class='react-autosuggest__suggestions-list'] li[id='react-autowhatever-1-section-0-item-0']")
        fsel.click()
        time.sleep(3)
        #to city
        to = self.driver.find_element_by_xpath("//span[contains(text(),'To')]")
        to.click()
        #tol=driver.find_element_by_css_selector("body.desktop.in:nth-child(2) div.bgGradient div.minContainer div.widgetSection.appendBottom40.primaryTraveler div.fsw.widgetOpen div.fsw_inner:nth-child(1) div.fsw_inputBox.searchToCity.inactiveWidget.activeWidget:nth-child(3) div:nth-child(2) div:nth-child(1) div.hsw_autocomplePopup.autoSuggestPlugin.makeFlex.column.spaceBetween div.react-autosuggest__container.react-autosuggest__container--open > input.react-autosuggest__input.react-autosuggest__input--open")
        tol=self.driver.find_element_by_css_selector("input[placeholder='To']")

        tol.send_keys("jai")
        time.sleep(5)
        tsel=self.driver.find_element_by_css_selector("ul[class='react-autosuggest__suggestions-list'] li[id='react-autowhatever-1-section-0-item-0']").click()

#for date

        dt=self.driver.find_element_by_xpath("//span[contains(text(),'DEPARTURE')]")
        dt.click()
        time.sleep(3)
        cdt=self.driver.find_element_by_css_selector("div[aria-label='Fri Feb 04 2022']").click()

#for search
        fd=self.driver.find_element_by_xpath("//a[contains(text(),'Search')]").click()

        print("Test Case passed Flight Search page open !")
        print("HTML Report is also generated !")

        time.sleep(3)
        self.driver.save_screenshot("C:\Screenshot\MakemyTrip.png")

