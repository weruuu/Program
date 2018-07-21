# import json
# from collections import defaultdict
# from collections import Counter
# def get_counts2(sequence):
#     counts = defaultdict(int)
#     for x in sequence:
#         counts[x] += 1
#     return counts
# path = '/Users/eviless/Downloads/pydata-book-2nd-edition/datasets/bitly_usagov/example.txt'
# records = [json.loads(line) for line in open(path)]
# timezone = [rec['tz'] for rec in records if 'tz' in rec]
# counts = Counter(timezone)
# counts.most_common(10)

from pandas import DataFrame