import aiohttp
import aiofiles
import asynch
import asyncio
import lxml
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import requests
import time
from aiocsv import AsyncWriter
import csv

ua = UserAgent()

import requests

cookies = {
    'qrator_jsr': '1687608417.517.xX0CLZGKHXLUPnG6-qtn1eqcfcivvetc033u7h7nrkvk5cqcg-00',
    'qrator_ssid': '1687608417.671.5fVqbUc2TXUAQszg-lhd5srfopn18hid4q8fcc2avjpi4ak7k',
    'qrator_jsid': '1687608417.517.xX0CLZGKHXLUPnG6-jb1guashfk8lna3ur1df2s3cprmaekfp',
    'city_path': 'moscow',
    'lang': 'ru',
    'PHPSESSID': '5e792ceb1232010dc5a82285cd5edc10',
    'current_path': '9565a5103f36ecea17597b8bfe0de40efdc12ecd83502fc6a8abccb573ee963ba%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22current_path%22%3Bi%3A1%3Bs%3A116%3A%22%7B%22city%22%3A%2230b7c1f3-03fb-11dc-95ee-00151716f9f5%22%2C%22cityName%22%3A%22%5Cu041c%5Cu043e%5Cu0441%5Cu043a%5Cu0432%5Cu0430%22%2C%22method%22%3A%22default%22%7D%22%3B%7D',
    '_csrf': 'c92062feb9393741c5cfd17f7b204018f7317d683a43f22bc6b9ccd1ec2a1d43a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22BHOuPp3LkfpdoX1KZNh1dpWqJom1nBRN%22%3B%7D',
    'rrpvid': '361492072988346',
    'cartUserCookieIdent_v3': '70f29ea1f50d51c0a3e17adfcf17477773a91b0715ffff42d97633feb2d38a62a%3A2%3A%7Bi%3A0%3Bs%3A22%3A%22cartUserCookieIdent_v3%22%3Bi%3A1%3Bs%3A36%3A%229d96230f-4f92-3645-b530-255354dcb5eb%22%3B%7D',
    'phonesIdent': '2249b6c6eb269f20f4d1b613e70ef6497128dd36d66af35fae8dd0a899ea7af7a%3A2%3A%7Bi%3A0%3Bs%3A11%3A%22phonesIdent%22%3Bi%3A1%3Bs%3A36%3A%227a3ddfad-9f61-44c9-a876-0375e62aeb07%22%3B%7D',
    '_gcl_au': '1.1.1498203796.1687608419',
    '_ga_FLS4JETDHW': 'GS1.1.1687608419.1.1.1687608688.49.0.0',
    '_ga': 'GA1.2.366971458.1687608419',
    'rcuid': '6496dc63cd70f2a251141915',
    '_gid': 'GA1.2.434793197.1687608420',
    'tmr_lvid': '52a5ad164da9d4d38f7fff2037376a03',
    'tmr_lvidTS': '1687608419575',
    '_ym_uid': '1687608420704199433',
    '_ym_d': '1687608420',
    '_ym_visorc': 'b',
    '_ym_isad': '2',
    'tmr_detect': '0%7C1687608692885',
    '_gat': '1',
    '_gat_%5Bobject%20Object%5D': '1',
    '_gat_UA-8349380-2': '1',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:108.0) Gecko/20100101 Firefox/108.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.dns-shop.ru/catalog/eb53394d63f878ee/noutbuki-i-aksessuary/',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Connection': 'keep-alive',
    # 'Cookie': 'qrator_jsr=1687608417.517.xX0CLZGKHXLUPnG6-qtn1eqcfcivvetc033u7h7nrkvk5cqcg-00; qrator_ssid=1687608417.671.5fVqbUc2TXUAQszg-lhd5srfopn18hid4q8fcc2avjpi4ak7k; qrator_jsid=1687608417.517.xX0CLZGKHXLUPnG6-jb1guashfk8lna3ur1df2s3cprmaekfp; city_path=moscow; lang=ru; PHPSESSID=5e792ceb1232010dc5a82285cd5edc10; current_path=9565a5103f36ecea17597b8bfe0de40efdc12ecd83502fc6a8abccb573ee963ba%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22current_path%22%3Bi%3A1%3Bs%3A116%3A%22%7B%22city%22%3A%2230b7c1f3-03fb-11dc-95ee-00151716f9f5%22%2C%22cityName%22%3A%22%5Cu041c%5Cu043e%5Cu0441%5Cu043a%5Cu0432%5Cu0430%22%2C%22method%22%3A%22default%22%7D%22%3B%7D; _csrf=c92062feb9393741c5cfd17f7b204018f7317d683a43f22bc6b9ccd1ec2a1d43a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22BHOuPp3LkfpdoX1KZNh1dpWqJom1nBRN%22%3B%7D; rrpvid=361492072988346; cartUserCookieIdent_v3=70f29ea1f50d51c0a3e17adfcf17477773a91b0715ffff42d97633feb2d38a62a%3A2%3A%7Bi%3A0%3Bs%3A22%3A%22cartUserCookieIdent_v3%22%3Bi%3A1%3Bs%3A36%3A%229d96230f-4f92-3645-b530-255354dcb5eb%22%3B%7D; phonesIdent=2249b6c6eb269f20f4d1b613e70ef6497128dd36d66af35fae8dd0a899ea7af7a%3A2%3A%7Bi%3A0%3Bs%3A11%3A%22phonesIdent%22%3Bi%3A1%3Bs%3A36%3A%227a3ddfad-9f61-44c9-a876-0375e62aeb07%22%3B%7D; _gcl_au=1.1.1498203796.1687608419; _ga_FLS4JETDHW=GS1.1.1687608419.1.1.1687608688.49.0.0; _ga=GA1.2.366971458.1687608419; rcuid=6496dc63cd70f2a251141915; _gid=GA1.2.434793197.1687608420; tmr_lvid=52a5ad164da9d4d38f7fff2037376a03; tmr_lvidTS=1687608419575; _ym_uid=1687608420704199433; _ym_d=1687608420; _ym_visorc=b; _ym_isad=2; tmr_detect=0%7C1687608692885; _gat=1; _gat_%5Bobject%20Object%5D=1; _gat_UA-8349380-2=1',
}

temp = []

async def get_page_data(session, page):
    url = f"https://www.dns-shop.ru/catalog/17a892f816404e77/noutbuki/?p={page}"
    async with session.get(url=url, headers=headers, cookies=cookies) as response:
        response_text = await response.text()
        soup = BeautifulSoup(response_text, 'lxml')
        
        laptops = soup.find_all("div", class_="catalog-product ui-button-widget")
        for i in range(0, len(laptops)):
            
            try:
                diagonal = laptops[i].find_all("span")[1].text.split()[0]
                name = (laptops[i].find_all("span")[1].text.split()[2],laptops[i].find_all("span")[1].text.split()[3])
                color = laptops[i].find_all("span")[1].text.split()[4]
                matrix = (laptops[i].find_all("span")[1].text.split()[5],laptops[i].find_all("span")[1].text.split()[6])

                fields = ['diagonal', 'name', 'color', 'matrix', 'page']
            except IndexError:
                i += 1
                
                temp.append(
                    [
                    diagonal, name, color, matrix, page 
                    ]
                )

            with open('data.csv', 'w') as f:
                # using csv.writer method from CSV package
                write = csv.writer(f)
                write.writerow(fields)
                write.writerows(temp)

            # async with aiofiles.open('data.csv', 'w') as f:
            #     writer = AsyncWriter(f)
            #     await writer.writerow(['diagonal', diagonal])
            #     await writer.writerow(['name', name])
            #     await writer.writerow(['color', color])
            #     await writer.writerow(['matrix', matrix])
            #     await writer.writerow(['page', page])



async def gather_data():
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        # response = await session.get('https://www.dns-shop.ru/catalog/17a892f816404e77/noutbuki/', headers=headers)
        # soup = BeautifulSoup(await response.text(), 'lxml')
        # pages_count = int(soup.find("div", class_="pagination-container").find_all("a")[-1].text)
        tasks = []

        for page in range(0, 6):

                task = asyncio.create_task(get_page_data(session, page))
                tasks.append(task)

        await asyncio.gather(*tasks)
        print(str(time.time() - start_time) + " : sec")


def main():
    asyncio.run(gather_data())
    print(temp)


if __name__ == '__main__':
    main()

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

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium_stealth import stealth
# import time


# options = webdriver.ChromeOptions()
# options.add_argument("start-maximized")
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
# driver = webdriver.Chrome(options=options)
# stealth(driver,
#         languages=["en-US", "en"],
#         vendor="Google Inc.",
#         platform="Win32",
#         webgl_vendor="Intel Inc.",
#         renderer="Intel Iris OpenGL Engine",
#         fix_hairline=True,
#         )

# for page in range(1,3):
#     domain = "https://www.russiadiscovery.ru/"
#     url = f"https://www.russiadiscovery.ru/tours/trekkingi/?page={page}"
#     driver.get(url)

#     blocks = driver.find_element(By.CLASS_NAME, "tourListUl")
#     posts = blocks.find_elements(By.TAG_NAME, "li")

#     for post in posts:
#         title = post.find_element(By.CLASS_NAME, "tourList__title").find_element(By.TAG_NAME, "a").get_attribute("href")
#         print(title)

# time.sleep(5)
# driver.quit()

# import pandas as pd
# import os
# import numpy as np
# np.set_printoptions(precision=4)
# import catboost
# from catboost import * 
# from catboost import datasets

# (train_df, test_df) = catboost.datasets.amazon()
# X = train_df.drop("ACTION", axis=1)
# y = train_df["ACTION"]

# cat_features = list(range(0, X.shape[1]))

# dataset_dir = "./amazon"

# if not os.path.exists(dataset_dir):
#     os.makedirs(dataset_dir)   
    
# train_df.to_csv(os.path.join(dataset_dir, 'train.tsv'), 
#                 index=False, sep='\t', header=False)

# test_df.to_csv(os.path.join(dataset_dir, 'test.tsv'), 
#               index=False, sep='\t', header=False)

# train_df.to_csv(os.path.join(dataset_dir, 'train.csv'),
#                 index=False, sep=',', header=True)

# test_df.to_csv(os.path.join(dataset_dir, 'test.csv'),
#               index=False, sep=',', header=True)

# from catboost.utils import create_cd

# feature_names = dict()

# create_cd(
#     label=0,
#     cat_features=list(range(1, train_df.columns.shape[0])),
#     feature_names=feature_names,
#     output_path=os.path.join(dataset_dir, 'train.cd')
# )

# pool1 = Pool(data=X, label=y, cat_features=cat_features)

# pool2 = Pool(
#     data=os.path.join(dataset_dir, 'train.csv'),
#     delimiter=',',
#     column_description=os.path.join(dataset_dir, 'train.cd'),
#     has_header=True
# )

# pool3 = Pool(data=X, cat_features=cat_features)

# X_prepared = X.values.astype(str).astype(object)

# pool4 = Pool(
#     data=FeaturesData(
#         cat_feature_data=X_prepared,
#         cat_feature_names=list(X)
#     ),
#     label=y.values
# )

# # print("Dataset shape")
# # print(f"Dataset 1: {str(pool1.shape)}")
# # print(f"Dataset 2: {str(pool2.shape)}")
# # print(f"Dataset 3: {str(pool3.shape)}")
# # print(f"Dataset 4: {str(pool4.shape)}")
# # print()
# # print("Column names")
# # print(f"Dataset 1: {pool1.get_feature_names()}")
# # print(f"Dataset 2: {pool2.get_feature_names()}")
# # print(f"Dataset 3: {pool3.get_feature_names()}")
# # print(f"Dataset 4: {pool4.get_feature_names()}")

# from sklearn.model_selection import train_test_split

# X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.45, random_state=42)

# from catboost import CatBoostClassifier

# model = CatBoostClassifier(
#     iterations=200,
#     random_seed=63,
#     learning_rate=0.15,
#     custom_loss=['AUC', 'Accuracy']
# )

# model.fit(X_train, y_train,
#         cat_features=cat_features,
#         eval_set=(X_test, y_test),
#         verbose=False,
#         plot=True
# )

# # print(f"Model is fitted: {str(model.is_fitted())}")
# # print(f"Model params: {model.get_params()}")
