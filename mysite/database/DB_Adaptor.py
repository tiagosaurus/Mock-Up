import Member
import Post
import Comment


class InvalidObjectTypeException(Exception):
    pass


class DBAdaptor:
    def __init__(self, obj_type):
        self.obj_type = obj_type

    types = ['member', 'image', 'filtered image', 'post', 'comment', 'url', 'shortened url', 'filter', 'sponsored item']

    def get_type(self):
        if self.obj_type not in types:
            raise InvalidObjectTypeException('Did input valid object type. Valid object types are:'
                                             'member'
                                             'image'
                                             'filtered image'
                                             'post'
                                             'comment'
                                             'url'
                                             'shortened url'
                                             'filter'
                                             'sponsored item')
        return self.obj_type

    def add_member(self, member_information: dict()) -> bool:
        # Take in a dictionary
        # Create new object
        # Add to DB
        pass

    def get_member(self, obj_id):
        # Return Member obj from DB
        pass

    def set_member(self, new_information: dict(), obj_id) -> bool:
        # Allow information about a member to be set in database
        # Takes dictionary as input - Keys should be what parameters need to be changed
        # Values are information being changed
        # Returns true if information change was successful
        # False otherwise
        pass

    def remove_member(self, obj_id) -> bool:
        # Returns true if member removal was successful
        # False otherwise
        pass

    def add_post(self, post_information: dict()) -> bool:
        # Take in a dictionary
        # Create new object
        # Add to DB
        pass

    def get_post(self, obj_id):
        # Return Post obj from DB
        pass

    def set_post(self, new_information: dict(), obj_id) -> bool:
        # Allow information about an object to be set in database
        # Takes dictionary as input - Keys should be what parameters need to be changed
        # Values are information being changed
        # Returns true if information change was successful
        # False otherwise
        pass

    def remove_post(self, obj_id) -> bool:
        # Returns true if removal was successful
        # False otherwise
        pass

    def add_comment(self, comment_information: dict()) -> bool:
        # Take in a dictionary
        # Create new object
        # Add to DB
        pass

    def get_comment(self, obj_id):
        # Return comment obj from DB
        pass

    def set_comment(self, new_information: dict(), obj_id) -> bool:
        # Allow information about an object to be set in database
        # Takes dictionary as input - Keys should be what parameters need to be changed
        # Values are information being changed
        # Returns true if information change was successful
        # False otherwise
        pass

    def remove_comment(self, obj_id) -> bool:
        # Returns true if removal was successful
        # False otherwise
        pass

    def add_url(self, url_information: dict()) -> bool:
        # Take in a dictionary
        # Create new object
        # Add to DB
        pass

    def get_url(self, obj_id):
        # Return URl obj from DB
        pass

    def set_url(self, new_information: dict(), obj_id) -> bool:
        # Allow information about an object to be set in database
        # Takes dictionary as input - Keys should be what parameters need to be changed
        # Values are information being changed
        # Returns true if information change was successful
        # False otherwise
        pass

    def remove_url(self, obj_id) -> bool:
        # Returns true if removal was successful
        # False otherwise
        pass

    def add_shortened_url(self, shortened_url_information: dict()) -> bool:
        # Take in a dictionary
        # Create new object
        # Add to DB
        pass

    def get_shortened_url(self, obj_id):
        # Return shortened url obj from DB
        pass

    def set_shortened_url(self, new_information: dict(), obj_id) -> bool:
        # Allow information about an object to be set in database
        # Takes dictionary as input - Keys should be what parameters need to be changed
        # Values are information being changed
        # Returns true if information change was successful
        # False otherwise
        pass

    def remove_shortened_url(self, obj_id) -> bool:
        # Returns true if removal was successful
        # False otherwise
        pass

    def add_image(self, image_information: dict()) -> bool:
        # Take in a dictionary
        # Create new object
        # Add to DB
        pass

    def get_image(self, obj_id):
        # Return image obj from DB
        pass

    def set_image(self, new_information: dict(), obj_id) -> bool:
        # Allow information about an object to be set in database
        # Takes dictionary as input - Keys should be what parameters need to be changed
        # Values are information being changed
        # Returns true if information change was successful
        # False otherwise
        pass

    def remove_image(self, obj_id) -> bool:
        # Returns true if removal was successful
        # False otherwise
        pass

    def add_filtered_image(self, filtered_image_information: dict()) -> bool:
        # Take in a dictionary
        # Create new object
        # Add to DB
        pass

    def get_filtered_image(self, obj_id):
        # Return filtered image obj from DB
        pass

    def set_filtered_image(self, new_information: dict(), obj_id) -> bool:
        # Allow information about an object to be set in database
        # Takes dictionary as input - Keys should be what parameters need to be changed
        # Values are information being changed
        # Returns true if information change was successful
        # False otherwise
        pass

    def remove_filtered_image(self, obj_id) -> bool:
        # Returns true if removal was successful
        # False otherwise
        pass

    def add_filter(self, filter_information: dict()) -> bool:
        # Take in a dictionary
        # Create new object
        # Add to DB
        pass

    def get_filter(self, obj_id):
        # Return filter obj from DB
        pass

    def set_filter(self, new_information: dict(), obj_id) -> bool:
        # Allow information about an object to be set in database
        # Takes dictionary as input - Keys should be what parameters need to be changed
        # Values are information being changed
        # Returns true if information change was successful
        # False otherwise
        pass

    def remove_filter(self, obj_id) -> bool:
        # Returns true if removal was successful
        # False otherwise
        pass

    def add_sponsored_item(self, sponsored_item_information: dict()) -> bool:
        # Take in a dictionary
        # Create new object
        # Add to DB
        pass

    def get_sponsored_item(self, obj_id):
        # Return Post obj from DB
        pass

    def set_sponsored_item(self, new_information: dict(), obj_id) -> bool:
        # Allow information about an object to be set in database
        # Takes dictionary as input - Keys should be what parameters need to be changed
        # Values are information being changed
        # Returns true if information change was successful
        # False otherwise
        pass

    def remove_sponsored_item(self, obj_id) -> bool:
        # Returns true if removal was successful
        # False otherwise
        pass

