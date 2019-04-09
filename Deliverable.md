# Low Level Design

## Basic Implementation

### Database and Libraries

Our database of choice is PostgreSQL. We are using the psycopg library as an adapter to make PostgreSQL work with our Django project. 

### Public API

We have a singular DBAdaptor class that backend teams can create an instance of in their classes to instantiate and manipulate various objects in the system. This adaptor class gives backend teams access to:
   - add methods:
   
      | Return Type | Method Call                                                          |
      |-------------|----------------------------------------------------------------------|
      | Boolean     | add_object_type(object_param_1, object_param_2, ..., object_param_n) |
      
      - Take in several required parameters
      - Access relevant DB table
      - Input required parameters from method call into the table
      - Returns a boolean indicating whether or not the data object was successfully added
   - get methods:
   
      | Return Type | Method Call             |
      |-------------|-------------------------|
      | Object      | get_object_type(obj_id) |
      
      - Take in an id
      - Pull all relevant fields from database table
      - Create an instance of the object
      - Returns instance of the relevant object
   - set methods:
   
      | Return Type | Method Call                                                                  |
      |-------------|------------------------------------------------------------------------------|
      | Object      | set_object_type(self, optional_change_param_1, ..., optional_change_param_n) |
      
      - Take in a set of optional parameters that want to be changed
      - Generate an instance of the specified object (call get_object)
      - Update relevant fields of object, leaving non-specified fields the same as before
      - Return an instance of the updated object
   - remove methods:
   
      | Return Type | Method Call                |
      |-------------|----------------------------|
      | Boolean     | remove_object_type(obj_id) |
      
      - Take in an object id
      - Access relevant DB table and remove object and all associated fields from DB
      - Returns a boolean indicating whether or not the deletion occurred successfully
      
#### Member API

| Return Type | Method Call                                                                                                                |
|-------------|----------------------------------------------------------------------------------------------------------------------------|
| Member      | add_member(self, user_id, first_name, last_name, email, pw, cc_num, invited_by, user_type, birthday, address, phone number, date_created)                                                                                                                              |           
| Member      | get_member(self, obj_id)                                                                                                   |
| Boolean     | set_member(self, new_information: dict(), obj_id)                                                                          | 
| Boolean     | remove_member(self, obj_id)                                                                                                |
      
#### Post API

| Return Type | Method Call                                                          |
|-------------|----------------------------------------------------------------------|
| Post        | add_post(self, post_information: dict())                             |
| Boolean     | set_post(self, new_information: dict(), obj_id)                      |
| Boolean     | remove_post(self, obj_id)                                            |


#### Comment API

| Return Type | Method Call                                        |
|-------------|----------------------------------------------------|
| Comment     | add_comment(self, comment_information: dict())     |
| Comment     | get_comment(self, obj_id)                          |
| Boolean     | set_comment(self, new_information: dict(), obj_id) |
| Boolean     | remove_comment(self, obj_id)                       | 

#### Image API

| Return Type | Method Call                                                          |
|-------------|----------------------------------------------------------------------|
| Image       | add_image(self, image_information: dict())                           |
| Image       | get_image(self, obj_id)                                              |
| Image       | set_image(self, new_information: dict(), obj_id)                     |
| Boolean     | remove_image(self, obj_id)                                           |

#### Filter API

| Return Type | Method Call                                                          |
|-------------|----------------------------------------------------------------------|
| Boolean     | add_filter(self, filter_information: dict())                         |
| Filter      | get_filter(self, obj_id) |
| Boolean     | set_filter(self, new_information: dict(), obj_id)                            |
| Boolean     | remove_filter(self, obj_id) |

### Credit Card API

| Return Type | Method Call                                                          |
|-------------|----------------------------------------------------------------------|
| Boolean     | add_object_type(object_param_1, object_param_2, ..., object_param_n) |
| Object      | get_object_type(obj_id) |
| Object      | set_object_type(self, optional_change_param_1, ..., optional_change_param_n) |
| Boolean     | remove_object_type(obj_id) |

### Private API

We currently have private constructors that can only be accessed through private method calls in our DBAdaptor class 
which instantiate instances of:
   - Member objects
   - Post objects
   - Image objects
   - Comment objects
   - Credit Card objects
   - 
   objects

## Testing Plans

### Unit Testing

Currently we have unit tests set up that test:

   1.a. Adding a new member to the database then retrieving it immediately after.
   
   2.a. Retrieving a previously existing member from DB and instantiating an instance of a Member object.
        Then testing this against a premade Member object to ensure that the object parameters are identical.
      
   2.b. Attempt to retrieve a non-existing member object.
        Ensure that a null value is returned - indicating that this member does not exist in the system. 
       
   3.a. Retrieving a previously existing member from DB.
        Changing one specific parameter associated with the Member object.
        Retrieving the same member from the DB after the changes have been made.
        Ensuring that this instance of the member is identical to a premade member object with the desired values in each parameter.
      
   3.b. Retrieving a previously existing member from DB.
        Changing multiple specific parameters associated with the Member object.
        Retrieving the same member from the DB after the changes have been made.
        Ensuring that this instance of the member is identical to a premade member object with the desired values in each parameter.
      
   4.a. Deleting an instance of a previously existing member and ensuring that the boolean returned correctly indicates whether or not
        the member is actually gone from the DB table.
      
   4.b. Deleting a non-existing member from the DB and ensuring that the remove method returns false and correctly handles a non-               existing object in the system. 
      
As we continue developing our adaptor we plan to develop similar tests for each different object in the system.

More specifically, we will create almost identical tests for:
   - Image objects
   - Post objects
   - Comment objects
   - Filter Objects
   - Credit card objects
As well as more specific unit tests for each individual object once they are fully implemented in the system. 

Some edges cases we are looking out for:
   - Checking to make sure objects exist in the system before attempting to create instances of them.
   - Making sure duplicate objects are not created.
   - Making sure duplicate objects can not be created through changing the parameters of a different object with the set methods.

### Integration Testing

As we develop our current project we have to run the database servers and our basic Django project off of a localhost server. As the 
Web Server teams get farther into development we will look to test our currently functioning DBAdaptor class with it being hosted on a 
universal server that can be accessed simultaneously by any team member or members of the backend teams. As such, we will work
with backend teams to retest our current test suite to ensure that the public API is functioning correctly for the purposes of the 
backend teams. 





