class Member:
    def __init__(self, filter_id: list(), original_image, filtered_image, filter_used: bool,
                 is_flagged: bool, image_type: str, by_admin: bool):
        self.filter_id = filter_id
        self.original_image = original_image
        self.filtered_image = filtered_image
        self.filter_used = filter_used
        self.is_flagged = is_flagged
        self.type = image_type
        self.by_admin = by_admin
