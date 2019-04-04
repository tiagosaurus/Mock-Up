class Post:
    def __init__(self, post_id, comment_id, image_id, user_id, username, url, shortened_url, date_created,
                 date_modified, is_flagged, points_given, content, by_admin, type):
        self.post_id = post_id
        self.comment_id = comment_id
        self.image_id = image_id
        self.user_id = user_id
        self.username = username
        self.url = url
        self.shortened_url = shortened_url
        self.date_created = date_created
        self.date_modified = date_modified
        self.is_flagged = is_flagged
        self.points_given = points_given
        self.content = content
        self.by_admin = by_admin
        self.type = type
