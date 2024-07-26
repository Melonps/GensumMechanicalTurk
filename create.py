from client import get_client

mturk = get_client()

# アカウントのバランスを確認
balance = mturk.get_account_balance()
print("Account balance: {}".format(balance["AvailableBalance"]))

# HTMLファイルのパス
html_file_path = "templete/HIT.html"

# HTMLファイルを読み込む
with open(html_file_path, "r", encoding="utf-8") as html_file:
    html_layout = html_file.read()

QUESTION_XML = """<HTMLQuestion xmlns="http://mechanicalturk.amazonaws.com/AWSMechanicalTurkDataSchemas/2011-11-11/HTMLQuestion.xsd">
        <HTMLContent><![CDATA[{}]]></HTMLContent>
        <FrameHeight>1000</FrameHeight>
        </HTMLQuestion>"""
question_xml = QUESTION_XML.format(html_layout)


task_attributes = {
    "MaxAssignments": 2,
    "LifetimeInSeconds": 600,  # How long the task will be available on the MTurk website (4 hours)
    "AssignmentDurationInSeconds": 300,  # How long will Workers have to complete each item (5 minutes)
    "Reward": "0.05",  # The reward you will offer Workers for each response
    "Title": "kakehi survey Tests",
    "Description": "Provide the species of iris in each image",
    "Keywords": "classification, image",
}

# HITを作成してsandboxに公開
response = mturk.create_hit(**task_attributes, Question=question_xml)
hit_id = response["HIT"]["HITId"]
hit_type_id = response["HIT"]["HITTypeId"]
print("HITId: {}".format(hit_id))
print(
    "You can view the HIT here: https://workersandbox.mturk.com/mturk/preview?groupId={}".format(
        hit_type_id
    )
)
