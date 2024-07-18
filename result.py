import os

import boto3
from dotenv import load_dotenv

load_dotenv()
# MTurkクライアントの作成
mturk = boto3.client(
    "mturk",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name="us-east-1",
    endpoint_url="https://mturk-requester-sandbox.us-east-1.amazonaws.com",
)

hit_id = "3RZS0FBRXY4BKGCL5ZZ9Y4RVTG7CPL"
# 結果を取得するためのコード
item = {"hit_id": hit_id}

# HITのステータスを取得
hit = mturk.get_hit(HITId=item["hit_id"])
item["status"] = hit["HIT"]["HITStatus"]

# ワーカーによって提出されたアサインメントのリストを取得
assignmentsList = mturk.list_assignments_for_hit(
    HITId=item["hit_id"], AssignmentStatuses=["Submitted", "Approved"], MaxResults=10
)

# 提出されたアサインメントを取得し、結果にカウントを保持
assignments = assignmentsList["Assignments"]
item["assignments_submitted_count"] = len(assignments)

# 結果を出力
print(f"HIT Status: {item['status']}")
print(f"Number of Assignments Submitted: {item['assignments_submitted_count']}")

# 提出されたアサインメントの詳細を一覧表示
for assignment in assignments:
    assignment_id = assignment["AssignmentId"]
    worker_id = assignment["WorkerId"]
    answer_xml = assignment["Answer"]
    print(f"Assignment ID: {assignment_id}")
    print(f"Worker ID: {worker_id}")
    print(f"Answer: {answer_xml}")
    print("-----")
