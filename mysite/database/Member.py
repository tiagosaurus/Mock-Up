class Member:
    def __init__(self, user_id, first_name, last_name, email, pw, cc_num, post_id,
                 points, visibility, invited_by, type, login_time, logout_time, date_created,
                 birthday, address, phone_number):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.pw = pw
        self.cc_num = cc_num
        self.post_id = post_id
        self.points = points
        self.visibility = visibility
        self.invited_by = invited_by
        self.type = type
        self.login_time = login_time
        self.logout_time = logout_time
        self.date_created = date_created
        self.birthday = birthday
        self.address = address
        self.phone_number = phone_number
