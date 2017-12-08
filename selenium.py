import time
from lxml import etree

from selenium import webdriver
import re


class MyzteSpider():
    def __init__(self):
        # self.driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any','--load-images=false'])
        self.driver = webdriver.Chrome()

    def find_myzte(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://www.baidu.com")
        driver.find_element_by_id("kw").send_keys("手机商城")
        driver.find_element_by_id("su").click()
        time.sleep(3)
        driver.save_screenshot("手机商城.png")

        while True:
            html = driver.page_source
            pattern = re.compile(r"中兴手机商城")
            result = pattern.findall(html)
            if len(result) != 0:
                break
            else:
                driver.find_element_by_link_text("下一页>").click()
                time.sleep(3)
                # driver.save_screenshot("find.png")

    def enter_myzte(self):
        driver = self.driver
        currentWin = driver.current_window_handle
        driver.find_element_by_partial_link_text("中兴").click()
        time.sleep(3)
        handles = driver.window_handles
        for i in handles:
            if currentWin == i:
                continue
            else:
                # 关闭原来页面，将driver与新的页面绑定起来
                driver.close()
                driver.switch_to_window(i)
                time.sleep(3)
                driver.save_screenshot("enter1.png")

    def enter_tianji(self):
        driver = self.driver
        print(driver.find_element_by_xpath("/html/head/title").get_attribute("innerText"))
        # 使用lxml提取标题
        # html = etree.HTML(driver.page_source)
        # title = html.xpath("/html/head/title/text()")[0]
        # print(title)
        currentWin = driver.current_window_handle
        driver.find_element_by_partial_link_text("天机系列").click()
        time.sleep(3)
        handles = driver.window_handles
        for i in handles:
            if currentWin == i:
                continue
            else:
                # 关闭原来页面，将driver与新的页面绑定起来
                driver.close()
                driver.switch_to_window(i)
                time.sleep(3)
                driver.save_screenshot("enter2.png")

    def parse_list(self):
        driver = self.driver
        phone_list = driver.find_elements_by_xpath("//h3/a")
        for phone in phone_list:
            currentWin = driver.current_window_handle
            phone.click()
            time.sleep(3)
            self.parse_details(driver)
            driver.back()



    def parse_details(self,driver):
        # driver.find_elements_by_tag_name("h1").text
        pass


if __name__ == '__main__':
    zte = MyzteSpider()
    zte.find_myzte()
    zte.enter_myzte()
    zte.enter_tianji()
    zte.parse_list()
    zte.driver.close()