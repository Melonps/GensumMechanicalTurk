from client import get_client

mturk = get_client()

assignment_id = "338JKRMM2SXN90S5Q0GNCG25BXNAH9"
feed_back = "Thank you for your work"

response = mturk.approve_assignment(
    AssignmentId=assignment_id, RequesterFeedback=feed_back, OverrideRejection=False
)

print(response)
