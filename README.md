py-alexa
========

A python API for querying the Alexa Web Information Service. Right now, all it does is fetch and return the categorical
data for sites.

Usage
=====

Simply set your `AWS_ACCESS_KEY_ID` and `SECRET_AWS_ACCESS_KEY` environment variables to your AWS credentials
(bear in mind that AWIS doesn't support IAM credentials) and then instantiate a `Request` object like so:

```python
    with open('sites.csv', 'wb') as file:
        writer = csv.writer(file)
        writer.writerow(['url', 'name', 'overall_rank', 'overall_rating', 'category'])
        for category in ['Top/Shopping', 'Top/Recreation', 'Top/Business']:
            query['Path'] = category
            for count in range(1, 5000, 20):
                query['Start'] = count
                for s in request.sites(query):
                    s.append(category)
                    writer.writerow(s)
```

You can provide more options to the `query` based on the documentation found at:

http://docs.aws.amazon.com/AlexaWebInfoService/latest/

Right now, all this module supports is the CategoryListings action. More will be added as needed.
