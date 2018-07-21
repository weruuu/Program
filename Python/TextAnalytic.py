import json
path = '/Users/eviless/Downloads/pydata-book-2nd-edition/datasets/bitly_usagov/example.txt'
records = [json.loads(line) for line in open(path)]
from pandas import DataFrame
frame = DataFrame(records)
clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unkown'
tz_counts = clean_tz.value_counts()
tz_counts[:10].plot(kind = 'barh',rot = 0)