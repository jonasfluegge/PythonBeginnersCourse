import requests

search_term = input('Please enter a search term: ')


def get_itunes_data():
    req = requests.get('https://itunes.apple.com/search/?term='+search_term+'&entity=album')
    if req.status_code == 200:
        response = req.json()
        resultCount = response['resultCount']
        res = response['results']
        res_data = True, resultCount, res
    else:
        res_data = False, 0, []
    return res_data


isSuccess, count, results = get_itunes_data()

if isSuccess:
    print(f'The search returned {count} results.')
    for data in results:
        print(f"Artist: {data['artistName']} - Album: {data['collectionName']} - Track Count: {data['trackCount']}")