import requests
import datetime
from fake_useragent import UserAgent


def get_skin_data(item_code):
    """The method to get the data from the skin website."""

    result = process_buff_data(get_buff_data(item_code),item_code)
    print(result)

def get_random_user_agent():
    """get random user agent."""
    user_agent = UserAgent()
    return user_agent.random

def get_buff_data(item_code):
    """The method to get the data from the buff website."""

    headers = {
        "User-Agent": get_random_user_agent(),
    }

    buff_url = f'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id={item_code}&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&_=1694073994211'

    try:
        response = requests.get(buff_url, headers=headers)
        response_json = response.json()
        return response_json
    except Exception:
        return Exception


def process_buff_data(buff_data, code):
    """The method to process the data from the buff website."""
    base_data = buff_data['data']['goods_infos']
    current_datetime = datetime.datetime.now()

    item_data = {
        'time': current_datetime.strftime("%Y-%m-%d %H:%M:%S"),
        'goods_id': next(iter(base_data)),
        'name': base_data[f'{next(iter(base_data))}']['name'],
        'steam_price': base_data[f'{code}']['steam_price_cny'],
        'buff_price': buff_data['data']['items'][0]['price'],
        'lowest_bargain_price': buff_data["data"]["items"][0]["lowest_bargain_price"]
    }
    return item_data

if __name__ == '__main__':
    get_skin_data(927991)