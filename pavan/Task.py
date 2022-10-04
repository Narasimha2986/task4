import requests

page_count = 1
records = []

# total pages - 5
while page_count < 6:
    response = requests.get(f"https://jsonmock.hackerrank.com/api/articles?page={page_count}")
    response = response.json()
    records.extend(response["data"])
    page_count += 1

sorted_records = sorted(records, key=lambda x: x["num_comments"] if x["num_comments"] else -1, reverse=True)

print("Top two titles with most number of comments")
print("*******************************************")
for rec in sorted_records[0:2]:
    print(rec["title"] + "-" +  str(rec["num_comments"]))

