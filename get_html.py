# import aiohttp
# import aiofiles
# import asynch
# import asyncio
# import lxml
# from fake_useragent import UserAgent
# from bs4 import BeautifulSoup
# import requests
# import time
# from aiocsv import AsyncWriter
import csv

# ua = UserAgent()

# headers = {
#     'Referer': 'https://www.dns-shop.ru/',
#     'Upgrade-Insecure-Requests': '1',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
#     'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"macOS"',
# }

# temp = []

# async def get_page_data(session, page):
#     url = f"https://www.dns-shop.ru/catalog/17a892f816404e77/noutbuki/?p={page}"
#     async with session.get(url=url, headers=headers) as response:
#         response_text = await response.text()
#         soup = BeautifulSoup(response_text, 'lxml')
        
#         laptops = soup.find_all("div", class_="catalog-product ui-button-widget")
#         for i in range(0, len(laptops)):
            
#             try:
#                 diagonal = laptops[i].find_all("span")[1].text.split()[0]
#                 name = (laptops[i].find_all("span")[1].text.split()[2],laptops[i].find_all("span")[1].text.split()[3])
#                 color = laptops[i].find_all("span")[1].text.split()[4]
#                 matrix = (laptops[i].find_all("span")[1].text.split()[5],laptops[i].find_all("span")[1].text.split()[6])

#                 fields = ['diagonal', 'name', 'color', 'matrix', 'page']
#             except IndexError:
#                 i += 1
                
#                 temp.append(
#                     [
#                     diagonal, name, color, matrix, page 
#                     ]
#                 )

#             with open('data.csv', 'w') as f:
#                 # using csv.writer method from CSV package
#                 write = csv.writer(f)
#                 write.writerow(fields)
#                 write.writerows(temp)

#             # async with aiofiles.open('data.csv', 'w') as f:
#             #     writer = AsyncWriter(f)
#             #     await writer.writerow(['diagonal', diagonal])
#             #     await writer.writerow(['name', name])
#             #     await writer.writerow(['color', color])
#             #     await writer.writerow(['matrix', matrix])
#             #     await writer.writerow(['page', page])



# async def gather_data():
#     start_time = time.time()
#     async with aiohttp.ClientSession() as session:
#         response = await session.get('https://www.dns-shop.ru/catalog/17a892f816404e77/noutbuki/', headers=headers)
#         soup = BeautifulSoup(await response.text(), 'lxml')
#         # pages_count = int(soup.find("div", class_="pagination-container").find_all("a")[-1].text)
#         tasks = []

#         for page in range(1, 3):

#                 task = asyncio.create_task(get_page_data(session, page))
#                 tasks.append(task)

#         await asyncio.gather(*tasks)
#         print(str(time.time() - start_time) + " : sec")


# def main():
#     asyncio.run(gather_data())
#     print(temp)


# if __name__ == '__main__':
#     main()

# users_data = [
#     ("user_name", "user_address"),
#     ["user1", "address1"],
#     ["user2", "address2"],
#     ["user3", "address3"],
# ]

# with open("data.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerows(
#         users_data
#     )

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
import time


options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

# options.add_argument("--headless")

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)
stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

for page in range(1,3):
    domain = "https://www.russiadiscovery.ru/"
    url = f"https://www.russiadiscovery.ru/tours/trekkingi/?page={page}"
    driver.get(url)

    blocks = driver.find_element(By.CLASS_NAME, "tourListUL")
    posts = blocks.find_elements(By.TAG_NAME, "li")

    for post in posts:
        title = post.find_element(By.CLASS_NAME, "tourList__title").find_element(By.TAG_NAME, "a").get_attribute("href")
        print(title)

# time.sleep(5)
# driver.quit()