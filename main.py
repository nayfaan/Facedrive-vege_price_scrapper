import services.startDriver
from services.startDriver import *

def initiate_driver(driver, url):
    driver.get(url)
    
'''def output_csv(ids):
    with open('output/output_obj.txt', 'w', newline='') as csvfile:
        output = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in ids:
            output.writerow(row)
            print(row)'''

def scrap(driver):
    items = driver.find_elements_by_css_selector(".elementor-portfolio-item")
    #.get_attribute("href")
    urls = []
    for item in items:
        urls.append(item.get_attribute("href"))
        print(urls)
    
    price_list = {}
    for url in urls:
        try:
            driver.get(url)
            price_list[url] = driver.find_element_by_css_selector(".amount")
        except Exception as e:
            print (e)
    
    print(price_list)
    
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
