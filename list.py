from client import get_client

mturk = get_client()

response = mturk.list_hits(MaxResults=100)
for hit in response["HITs"]:
    print(f"HIT ID: {hit['HITId']}")
    print(f"Title: {hit['Title']}")
    print(f"Description: {hit['Description']}")
    print(f"Status: {hit['HITStatus']}")
    print(f"HIT Type ID: {hit['HITTypeId']}")
    print(
        f"Assignments Available / Pending / Completed | Max: {hit['NumberOfAssignmentsAvailable']} / {hit['NumberOfAssignmentsPending']} / {hit['NumberOfAssignmentsCompleted']} | {hit['MaxAssignments']}"
    )
    print(
        f"URL: https://workersandbox.mturk.com/mturk/preview?groupId={hit['HITTypeId']}"
    )
    print("-" * 40)

print(f"Number of HITs: {len(response['HITs'])}")
