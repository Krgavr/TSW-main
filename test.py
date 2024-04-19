from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5000/pridej")

nova_pizza = "UJEPska"
cena_pizzy = "500"

driver.find_element(By.NAME, "nazev").clear()
driver.find_element(By.NAME, "nazev").send_keys(nova_pizza)
driver.find_element(By.NAME, "cena").clear()
driver.find_element(By.NAME, "cena").send_keys(cena_pizzy)
driver.find_element(By.TAG_NAME, "button").click()

driver.get("http://127.0.0.1:5000/picy")
info_posledni_pizzy = driver.find_element(By.XPATH, "//ol/li[last()]").text 
print(info_posledni_pizzy)
assert info_posledni_pizzy == f"{nova_pizza}: {cena_pizzy}"

#driver.find_element(By.NAME, "nazev").clear()
#driver.find_element(By.NAME, "nazev").send_keys("kybl")
#driver.find_element(By.NAME, "mnozstvi").clear()
#driver.find_element(By.NAME, "mnozstvi").send_keys("2")

#driver.find_element(By.TAG_NAME, "button").click()
#print(driver.title)
#assert "Pepes pizza-Home page" in driver.title

#driver.find_element(By.LINK_TEXT, "Picy").click()

#nadpis_druhe_urovne = driver.find_element(By.TAG_NAME, "h2").text
#assert nadpis_druhe_urovne == "Nabídka pic"

#info_prvni_pizzy = driver.find_element(By.XPATH, "//ol/li[1]").text #XPATH indexuje od 1
#info_druha_pizza = driver.find_element(By.XPATH, "//ol/li[2]").text
#assert info_prvni_pizzy == "čoky: 123"
#assert info_druha_pizza == "piko: 823"
#print(info_prvni_pizzy)
#print(info_druha_pizza)
#print(nadpis_druhe_urovne)
driver.close()