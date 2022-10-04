import urllib
from urllib.request import urlopen
import json

records = []

# total pages - 5
for page_count in range(1,6):
    response = urlopen(f"https://jsonmock.hackerrank.com/api/articles?page={page_count}")
    response = json.load(response)
    print(response)
    records.extend(response["data"])

sorted_records = sorted(records, key=lambda x: x["num_comments"] if x["num_comments"] else -1, reverse=True)
print("\n")
print("TOP TWO TITLES WITH MOST NUMBER OF COMMENTS")

for rec in sorted_records[0:2]:
    print(rec)
    print("#Top two titles based on most number of comments:-"+rec["title"] + "-" +  str(rec["num_comments"]))
