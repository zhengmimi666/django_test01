# # coding=utf-8
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# selenium = webdriver.Chrome()
# # selenium.implicitly_wait(10)
# selenium.get("http://127.0.0.1:8000/polls/1/results/")
# front_vote_number = selenium.find_elements(By.XPATH,"//div[@class='progress']/p")[0].text
#
# selenium.get("http://127.0.0.1:8000/polls/")
# # selenium.find_element(By.LINK_TEXT,"what's up?").click()
# selenium.find_element(By.ID,"1").click()
# selenium.find_element(By.XPATH,"//input[@type='radio' and @value='1']").click() #not much
# selenium.find_element(By.ID,"voteButton").click()  #boteButton
# after_vote_number = selenium.find_elements(By.XPATH,"//div[@class='progress']/p")[0].text  #boteButton
# print(after_vote_number)
# assert int(after_vote_number) == int(front_vote_number)+1
#
#
#
# selenium.quit()
