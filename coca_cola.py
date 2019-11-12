import requests
import datetime
import matplotlib.pyplot as plt


def amount_days(period):
    today = datetime.datetime.now()
    list_of_date = []
    for i in range(1,period+1):
        new_time = today - datetime.timedelta(days=i)
        new_utc_date_float = new_time.timestamp()
        new_utc_date_int = int(new_utc_date_float)
        formated_date = new_time.strftime("%Y,%m,%d")
        list_of_date.append([formated_date,new_utc_date_float,new_utc_date_int])
    return list_of_date


def get_total_count(period):
    list_of_amount = []
    utc_list = amount_days(period)
    for day in range(1,len(utc_list)):
        x = utc_list[day][2]
        payload = {'q':'Coca-cola','start_time':x,'access_token':'f87d9340f87d9340f87d93401af8104018ff87df87d9340a5bf91f22e578dd209437994','v':'5.103'}
        url = 'https://api.vk.com/method/newsfeed.search'
        response = requests.post(url,data=payload)
        list_of_amount.append(response.json()['response']['total_count'])
    return list_of_amount

graph = get_total_count(8)

plt.bar(range(1,8),graph)
plt.xlabel('Day')
plt.ylabel('Count')
plt.show()
