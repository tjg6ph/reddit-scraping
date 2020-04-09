import csv

def parse_urls_from_csv(csv_file='posts_master.csv'):
    """Given a csv, return the URLs contained in it"""


    base_url = 'http://reddit.com'
    urls = []

    with open(csv_file) as csv_in:
        csv_reader = csv.reader(csv_in, delimiter=',')
        for row in list(csv_reader)[1:]:
            urls.append(base_url + row[7])
    
    return urls


print(parse_urls_from_csv())