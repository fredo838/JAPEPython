from selenium import webdriver
# from selenium.webdriver import ActionChains
# import selenium.common.exceptions

class Driver:
  def __init__(self): 
    self.driver = webdriver.Firefox()
    self.homophone_site = "http://www.homophone.com/random"
    self.synonym_site = "http://www.thesaurus.com/browse/"
    self.xpaths = {
    "homophs":"/html/body/div[3]/div[2]/div[1]/div[1]/h3",
    "first_homoph":"/html/body/div[3]/div[2]/div[2]/div[1]/div/div/span",
    "first_homoph_nounity":"/html/body/div[3]/div[2]/div[2]/div[1]/div/div/ol/li[1]/span",
    "second_homoph":"/html/body/div[3]/div[2]/div[2]/div[2]/div/div/span",
    "scond_homoph_nounity":"/html/body/div[3]/div[2]/div[2]/div[2]/div/div/ol/li[1]/span",
    "most_relevant_synonym":"/html/body/div[2]/div[2]/div[1]/div/div[3]/div[2]/div[2]/div[3]/div/ul[1]/li[1]/a/span[1]"
    }

  def get_random_homophones(self):
    self.driver.get(self.homophone_site)
    # words = self.driver.find_element_by_xpath(self.xpaths["homophs"])
    first_word = self.driver.find_element_by_xpath(self.xpaths["first_homoph"]).get_attribute("innerHTML")
    first_word_nounity = self.driver.find_element_by_xpath(self.xpaths["first_homoph_nounity"]).get_attribute("innerHTML")
    second_word = self.driver.find_element_by_xpath(self.xpaths["second_homoph"]).get_attribute("innerHTML")
    second_word_nounity = self.driver.find_element_by_xpath(self.xpaths["scond_homoph_nounity"]).get_attribute("innerHTML")
    return first_word,first_word_nounity,second_word,second_word_nounity

  def get_specific_random_homophones(self,nounity1,nounity2):
    while(True):
      first_word,first_word_nounity,second_word,second_word_nounity = self.get_random_homophones()
      print(first_word_nounity,second_word_nounity)
      if (first_word_nounity == nounity1 and second_word_nounity == nounity2):
        return first_word,first_word_nounity,second_word,second_word_nounity
      elif (first_word_nounity == nounity2 and second_word_nounity == nounity1):
        return second_word,second_word_nounity,first_word,first_word_nounity
        
  def get_synonym(self,input_word):
    self.driver.get(self.synonym_site+input_word)
    most_relevant_synonym = self.driver.find_element_by_xpath(self.xpaths["most_relevant_synonym"]).get_attribute("innerHTML")
    return most_relevant_synonym     
    

