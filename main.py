import services.startDriver
from services.startDriver import *
import re

def initiate_driver(driver, url):
    driver.get(url)
    
def output_txt(price_list):
    CLEANR = re.compile('<.*?>')
    
    with open('output/output_obj.txt', 'w', newline='') as txtfile:
        txtfile.write("{")
        for key, value in price_list.items():
            txtfile.write('"%s": "%s",\n' % (key, re.sub(CLEANR, '', value)))
        txtfile.write("}")

def scrap(driver):
    items = driver.find_elements_by_css_selector(".elementor-portfolio-item > a")
    #.get_attribute("href")
    urls = []
    for item in items:
        urls.append(item.get_attribute("href"))
    
    price_list = {}
    for url in urls:
        try:
            driver.get(url)
            price_list[url] = driver.find_element_by_css_selector(".amount").get_attribute("innerHTML")
        except Exception as e:
            print (e)
    
    print(price_list)
    output_txt(price_list)
    
def run():
    driver = services.startDriver.start()
    initiate_driver(driver, "https://facedrivesupply.com/vege")
    try:
        scrap(driver)
    except Exception as e:
        print (e)
    finally:
        driver.close()

if __name__ == "__main__":
    run()
