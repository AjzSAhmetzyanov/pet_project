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

cookies = {
    'lang': 'ru',
    'city_path': 'moscow',
    'phonesIdent': '4e957da8c854eddd1206b107327b2639a48bda9c0376c16fa93677d277038e54a%3A2%3A%7Bi%3A0%3Bs%3A11%3A%22phonesIdent%22%3Bi%3A1%3Bs%3A36%3A%22ebc14c93-0de7-4b96-81db-cca4277fefa1%22%3B%7D',
    'cartUserCookieIdent_v3': '066ea3df7194c39af1c33108f73e99305445267de595e9d936bf1da6d0695758a%3A2%3A%7Bi%3A0%3Bs%3A22%3A%22cartUserCookieIdent_v3%22%3Bi%3A1%3Bs%3A36%3A%22e1838e05-bce1-3d5d-9639-1f76a4c394e5%22%3B%7D',
    '_gcl_au': '1.1.1769402233.1687152784',
    'rrpvid': '514393665157779',
    'PHPSESSID': '77a3d6063def3e5ebd1ae05913401664',
    'tmr_lvid': 'd31b8ac6291611090dbad5635c274b09',
    'tmr_lvidTS': '1687152784780',
    '_ym_uid': '1687152785781607891',
    '_ym_d': '1687152785',
    'rcuid': '648d7872ef0b6f85d3a3e9ef',
    'current_path': '605bfdc517d7e9e23947448a9bf1ce16ac36b884434a3fdb10db053793c50392a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22current_path%22%3Bi%3A1%3Bs%3A115%3A%22%7B%22city%22%3A%2230b7c1f3-03fb-11dc-95ee-00151716f9f5%22%2C%22cityName%22%3A%22%5Cu041c%5Cu043e%5Cu0441%5Cu043a%5Cu0432%5Cu0430%22%2C%22method%22%3A%22manual%22%7D%22%3B%7D',
    '_csrf': '2215566cad29db7d4b82817167355e5a41de8f04d7183110890bbb19874b7586a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22EVOgtvpxzikgAfqy5rdvNj5er36VAV4v%22%3B%7D',
    '_gid': 'GA1.2.1759671824.1687265202',
    '_ym_isad': '2',
    '_ym_visorc': 'b',
    'qrator_jsr': '1687277798.116.6LhJ0P7tgdmyde1T-ic1kgpn909l96hptik8a6mg5eu1cgua2-00',
    'qrator_jsid': '1687277798.116.6LhJ0P7tgdmyde1T-g9d7s2cr4ttv897d32fgrlsq3pmh8lrh',
    'tmr_detect': '0%7C1687277860129',
    '_gat_UA-8349380-2': '1',
    '_gat': '1',
    '_gat_%5Bobject%20Object%5D': '1',
    'rr-testCookie': 'testvalue',
    '_ga_FLS4JETDHW': 'GS1.1.1687271156.5.1.1687277922.55.0.0',
    '_ga': 'GA1.1.487180927.1687152784',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8',
    'Connection': 'keep-alive',
    # 'Cookie': 'lang=ru; city_path=moscow; phonesIdent=4e957da8c854eddd1206b107327b2639a48bda9c0376c16fa93677d277038e54a%3A2%3A%7Bi%3A0%3Bs%3A11%3A%22phonesIdent%22%3Bi%3A1%3Bs%3A36%3A%22ebc14c93-0de7-4b96-81db-cca4277fefa1%22%3B%7D; cartUserCookieIdent_v3=066ea3df7194c39af1c33108f73e99305445267de595e9d936bf1da6d0695758a%3A2%3A%7Bi%3A0%3Bs%3A22%3A%22cartUserCookieIdent_v3%22%3Bi%3A1%3Bs%3A36%3A%22e1838e05-bce1-3d5d-9639-1f76a4c394e5%22%3B%7D; _gcl_au=1.1.1769402233.1687152784; rrpvid=514393665157779; PHPSESSID=77a3d6063def3e5ebd1ae05913401664; tmr_lvid=d31b8ac6291611090dbad5635c274b09; tmr_lvidTS=1687152784780; _ym_uid=1687152785781607891; _ym_d=1687152785; rcuid=648d7872ef0b6f85d3a3e9ef; current_path=605bfdc517d7e9e23947448a9bf1ce16ac36b884434a3fdb10db053793c50392a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22current_path%22%3Bi%3A1%3Bs%3A115%3A%22%7B%22city%22%3A%2230b7c1f3-03fb-11dc-95ee-00151716f9f5%22%2C%22cityName%22%3A%22%5Cu041c%5Cu043e%5Cu0441%5Cu043a%5Cu0432%5Cu0430%22%2C%22method%22%3A%22manual%22%7D%22%3B%7D; _csrf=2215566cad29db7d4b82817167355e5a41de8f04d7183110890bbb19874b7586a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22EVOgtvpxzikgAfqy5rdvNj5er36VAV4v%22%3B%7D; _gid=GA1.2.1759671824.1687265202; _ym_isad=2; _ym_visorc=b; qrator_jsr=1687277798.116.6LhJ0P7tgdmyde1T-ic1kgpn909l96hptik8a6mg5eu1cgua2-00; qrator_jsid=1687277798.116.6LhJ0P7tgdmyde1T-g9d7s2cr4ttv897d32fgrlsq3pmh8lrh; tmr_detect=0%7C1687277860129; _gat_UA-8349380-2=1; _gat=1; _gat_%5Bobject%20Object%5D=1; rr-testCookie=testvalue; _ga_FLS4JETDHW=GS1.1.1687271156.5.1.1687277922.55.0.0; _ga=GA1.1.487180927.1687152784',
    'Referer': 'https://www.dns-shop.ru/catalog/eb53394d63f878ee/noutbuki-i-aksessuary/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
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
        response = await session.get('https://www.dns-shop.ru/catalog/17a892f816404e77/noutbuki/', cookies=cookies, headers=headers)
        soup = BeautifulSoup(await response.text(), 'lxml')
        # pages_count = int(soup.find("div", class_="pagination-container").find_all("a")[-1].text)
        tasks = []

        for page in range(1, 3):

                task = asyncio.create_task(get_page_data(session, page))
                tasks.append(task)

        await asyncio.gather(*tasks)
        print(str(time.time() - start_time) + " : sec")


def main():
    asyncio.run(gather_data())
    print(temp)


if __name__ == '__main__':
    main()

