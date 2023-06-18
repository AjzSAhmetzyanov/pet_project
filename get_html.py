import requests

cookies = {
    'lang': 'ru',
    'PHPSESSID': '412740a6ca76ba3d8ff309a81b4e0b26',
    'cartUserCookieIdent_v3': 'b611419eff1d5d4acb2ba01148e2be4a1311832507f17fcc7b309c4b8a781638a%3A2%3A%7Bi%3A0%3Bs%3A22%3A%22cartUserCookieIdent_v3%22%3Bi%3A1%3Bs%3A36%3A%2242a1b947-2e5c-33ba-ac36-9e2e47956d22%22%3B%7D',
    'phonesIdent': 'd24ba292f28de045ad955d5e6a4430377b095f41b19b8e6320a56fc8e685a3b2a%3A2%3A%7Bi%3A0%3Bs%3A11%3A%22phonesIdent%22%3Bi%3A1%3Bs%3A36%3A%22e4c18612-e9cc-40cc-b1b8-3b2256bc08c0%22%3B%7D',
    '_gid': 'GA1.2.1433954782.1687110980',
    '_gcl_au': '1.1.1776523216.1687110981',
    '_ym_uid': '1687110982982147384',
    '_ym_d': '1687110982',
    'tmr_lvid': '4496557623f7a3a2aaac969e5f41d137',
    'tmr_lvidTS': '1687110982546',
    '_ym_isad': '2',
    'city_path': 'kazan',
    'current_path': '0e2725c9274cf653d41cb76144c4d7fafe50cd9cbb28f12b7003ce57fae1839ca%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22current_path%22%3Bi%3A1%3Bs%3A115%3A%22%7B%22city%22%3A%2255506b55-0565-11df-9cf0-00151716f9f5%22%2C%22cityName%22%3A%22%5Cu041a%5Cu0430%5Cu0437%5Cu0430%5Cu043d%5Cu044c%22%2C%22method%22%3A%22manual%22%7D%22%3B%7D',
    '_csrf': '78f159e2d690d0bd00f696141570356f692dea0ae5aea87841663929f145e211a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%222ezIg_M7byXpSJv5YO2-WsWp64tDwnL2%22%3B%7D',
    'rrpvid': '153457539511767',
    'rcuid': '648f45779144efaeaf29dda6',
    'qrator_jsid': '1687110960.800.vlwEeE8id7ZugpIK-v4qcsee877jg79g95ce3ss1mbg75abvp',
    '_ga_FLS4JETDHW': 'GS1.1.1687113503.2.0.1687113503.60.0.0',
    '_ga': 'GA1.2.915581245.1687110980',
    '_ym_visorc': 'b',
    'tmr_detect': '0%7C1687113507269',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': 'lang=ru; PHPSESSID=412740a6ca76ba3d8ff309a81b4e0b26; cartUserCookieIdent_v3=b611419eff1d5d4acb2ba01148e2be4a1311832507f17fcc7b309c4b8a781638a%3A2%3A%7Bi%3A0%3Bs%3A22%3A%22cartUserCookieIdent_v3%22%3Bi%3A1%3Bs%3A36%3A%2242a1b947-2e5c-33ba-ac36-9e2e47956d22%22%3B%7D; phonesIdent=d24ba292f28de045ad955d5e6a4430377b095f41b19b8e6320a56fc8e685a3b2a%3A2%3A%7Bi%3A0%3Bs%3A11%3A%22phonesIdent%22%3Bi%3A1%3Bs%3A36%3A%22e4c18612-e9cc-40cc-b1b8-3b2256bc08c0%22%3B%7D; _gid=GA1.2.1433954782.1687110980; _gcl_au=1.1.1776523216.1687110981; _ym_uid=1687110982982147384; _ym_d=1687110982; tmr_lvid=4496557623f7a3a2aaac969e5f41d137; tmr_lvidTS=1687110982546; _ym_isad=2; city_path=kazan; current_path=0e2725c9274cf653d41cb76144c4d7fafe50cd9cbb28f12b7003ce57fae1839ca%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22current_path%22%3Bi%3A1%3Bs%3A115%3A%22%7B%22city%22%3A%2255506b55-0565-11df-9cf0-00151716f9f5%22%2C%22cityName%22%3A%22%5Cu041a%5Cu0430%5Cu0437%5Cu0430%5Cu043d%5Cu044c%22%2C%22method%22%3A%22manual%22%7D%22%3B%7D; _csrf=78f159e2d690d0bd00f696141570356f692dea0ae5aea87841663929f145e211a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%222ezIg_M7byXpSJv5YO2-WsWp64tDwnL2%22%3B%7D; rrpvid=153457539511767; rcuid=648f45779144efaeaf29dda6; qrator_jsid=1687110960.800.vlwEeE8id7ZugpIK-v4qcsee877jg79g95ce3ss1mbg75abvp; _ga_FLS4JETDHW=GS1.1.1687113503.2.0.1687113503.60.0.0; _ga=GA1.2.915581245.1687110980; _ym_visorc=b; tmr_detect=0%7C1687113507269',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://www.dns-shop.ru/catalog/17a892f816404e77/noutbuki/', cookies=cookies, headers=headers)

with open('dns.html', 'w') as resp:
    resp.write(response.text)
