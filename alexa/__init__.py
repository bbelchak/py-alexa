import os

ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
SERVICE_HOST = "awis.amazonaws.com"


if __name__ == "__main__":
    from api.request import Request
    request = Request()
    total = 1000
    query = {'ResponseGroup': 'Listings',
             'Action': 'CategoryListings',
             'Path': 'Top/Business',
             'SortBy': 'Popularity',
             'Recursive': 'True'}
    for count in range(1, total, 20):
        query['Start'] = count
        for s in request.sites(query):
            print s
