class Member:
    def __init__(self, replies, post_id, user_id, username, content, date_created, by_admin):
        self.replies = replies
        self.post_id = post_id
        self.user_id = user_id
        self.username = username
        self.content = content
        self.date_created = date_created
        self.by_admin = by_admin
