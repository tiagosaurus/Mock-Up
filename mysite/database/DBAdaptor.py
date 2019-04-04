class InvalidObjectTypeException(exception):
    pass


class DBAdaptor:
    def __init__(self, obj_type: str):
        self.obj_type = obj_type.lower()

    types = ['member', 'image', 'filtered image', 'post', 'comment', 'url', 'shortened url', 'filter', 'sponsored item']

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

    if self.obj_type == 'member':

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

    elif self.obj_type == 'post':

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

    elif self.obj_type == 'comment':

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

    elif self.obj_type == 'url':

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

    elif self.obj_type == 'shortened url':

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

    elif self.obj_type == 'image':

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

    elif self.obj_type == 'filtered image':

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

    # Not sure if I need the next few objects past this point
    elif self.obj_type == 'filter':

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

    elif self.obj_type == 'sponsored item':

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

    else:
        raise InvalidObjectTypeException('No Valid Object Type Passed In')
