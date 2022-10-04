import urllib
from urllib.request import urlopen
import json

records = []

# total pages - 3
for page_count in range(1,4):
    response = urlopen(f"https://jsonmock.hackerrank.com/api/article_users?page={page_count}")
    response = json.load(response)
    print(response)
    records.extend(response["data"])

sorted_records = sorted(records, key=lambda x: x["submission_count"] if x["submission_count"] else -1, reverse=True)
print("\n")
print("Top two users with most number of submissions")

for rec in sorted_records[0:2]:
    print(rec)
    print("#Top two users with most number of submissions:-"+rec["username"] + "-" +  str(rec["submission_count"]))
