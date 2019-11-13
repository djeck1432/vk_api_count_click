import requests
import datetime
import matplotlib.pyplot as plt


def amount_days(period):
    today = datetime.datetime.now()
    dates = []
    for i in range(1,period+1):
        new_time = today - datetime.timedelta(days=i)
        new_utc_date = new_time.timestamp()
        foramted_utc_date = int(new_utc_date)
        formated_date = new_time.strftime("%Y,%m,%d")
        dates.append([formated_date,foramted_utc_date])
    return dates


def get_total_count(period):
    amount_of_clicks = []
    data_in_utc = amount_days(period)
    for day,utc in data_in_utc:
        start_time = utc
        payload = {'q':'Coca-cola','start_time':start_time,'access_token':'f87d9340f87d9340f87d93401af8104018ff87df87d9340a5bf91f22e578dd209437994','v':'5.103'}
        url = 'https://api.vk.com/method/newsfeed.search'
        response = requests.post(url,data=payload)
        amount_of_clicks.append(response.json()['response']['total_count'])
    return amount_of_clicks

graph = get_total_count(8)

plt.bar(range(1,8),graph)
plt.xlabel('Day')
plt.ylabel('Count')
plt.show()
