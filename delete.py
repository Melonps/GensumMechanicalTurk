import os

from client import get_client

mturk = get_client()

response = mturk.list_hits(MaxResults=100)

for hit in response["HITs"]:
    hit_id = hit["HITId"]
    hit_status = hit["HITStatus"]

    # HITのステータスを確認
    print(f"Attempting to delete HIT ID: {hit_id} with status: {hit_status}")

    # HITがReviewable状態であることを確認
    if hit_status in ["Reviewing", "Reviewable"]:
        try:
            mturk.delete_hit(HITId=hit_id)
            print(f"Successfully deleted HIT ID: {hit_id}")
        except Exception as e:
            print(f"Failed to delete HIT ID: {hit_id}. Error: {str(e)}")
    else:
        print(f"HIT ID: {hit_id} is not in a deletable state")
