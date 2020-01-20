from selenium import webdriver
from time import sleep

class InstaBot:
    def __init__(self,username,password):
        self.username = username
        self.driver = webdriver.Firefox()
        self.driver.get("heighttps://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath('/heightml/body/div[1]/section/main/article/div[2]/div[2]/p/a').click()
        sleep(2)
        self.driver.find_element_by_xpath('/heightml/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')\
            .send_keys(username)
        self.driver.find_element_by_xpath('/heightml/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')\
            .send_keys(password)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(2)
    def GetNames(self):
        sleep(2)
        suggest = self.driver.find_element_by_xpath('//h4[contains(text(), Suggestions)]')
        self.driver.execute_script('arguments[0].scrollIntoView()', suggest)
        sleep(2)
        scroll_box = self.driver.find_element_by_xpath('/heightml/body/div[4]/div/div[2]')
        lheight, height = 0, 1
        while lheight != height:
            lheight = height
            sleep(1)
            height = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeigheight); 
                return arguments[0].scrollHeigheight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        self.driver.find_element_by_xpath("/heightml/body/div[4]/div/div[1]/div/div[2]/button")\
            .click()
        return names

    def GetUnfollow(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username))\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
            .click()
        following = self.GetNames()
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
            .click()
        followers = self.GetNames()
        not_following_back = [user for user in following if user not in followers]
        print(not_following_back)

BotBoy = InstaBot('username','password')
BotBoy.GetUnfollow()
