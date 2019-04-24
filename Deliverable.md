# Low Level Design

## Basic Implementation

### Database and Libraries

Our database of choice is PostgreSQL. We are using the psycopg library as an adapter to make PostgreSQL work with our Django project. 

### Public API

We have a singular DBAdaptor class that backend teams can create an instance of in their classes to instantiate and manipulate various objects
in the system. This adaptor class gives backend teams access to:
   - add methods:
   
      | Return Type | Method Call                                                          |
      |-------------|----------------------------------------------------------------------|
      | Object      | add_object_type(object_param_1, object_param_2, ..., object_param_n) |
      
      - Take in several required parameters
      - Access relevant DB table
      - Input required parameters from method call into the table
      - Returns an instance of the newly added object
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

| Return Type | Method Call                                                          |
|-------------|----------------------------------------------------------------------|
| Member     | add_object_type(object_param_1, object_param_2, ..., object_param_n) |

| Return Type | Method Call             |
|-------------|-------------------------|
| Member      | get_object_type(obj_id) |

| Return Type | Method Call                                                                  |
|-------------|------------------------------------------------------------------------------|
| Member      | set_object_type(self, optional_change_param_1, ..., optional_change_param_n) |
      
| Return Type | Method Call                |
|-------------|----------------------------|
| Boolean     | remove_object_type(obj_id) |
      
#### Post API

| Return Type | Method Call                                                          |
|-------------|----------------------------------------------------------------------|
| Post     | add_object_type(object_param_1, object_param_2, ..., object_param_n) |

| Return Type | Method Call             |
|-------------|-------------------------|
| Post      | get_object_type(obj_id) |

| Return Type | Method Call                                                                  |
|-------------|------------------------------------------------------------------------------|
| Post      | set_object_type(self, optional_change_param_1, ..., optional_change_param_n) |
      
| Return Type | Method Call                |
|-------------|----------------------------|
| Boolean     | remove_object_type(obj_id) |

#### Comment API

| Return Type | Method Call                                                          |
|-------------|----------------------------------------------------------------------|
| Comment     | add_object_type(object_param_1, object_param_2, ..., object_param_n) |

| Return Type | Method Call             |
|-------------|-------------------------|
| Comment      | get_object_type(obj_id) |

| Return Type | Method Call                                                                  |
|-------------|------------------------------------------------------------------------------|
| Comment      | set_object_type(self, optional_change_param_1, ..., optional_change_param_n) |
      
| Return Type | Method Call                |
|-------------|----------------------------|
| Boolean     | remove_object_type(obj_id) |

#### Image API

| Return Type | Method Call                                                          |
|-------------|----------------------------------------------------------------------|
| Image     | add_object_type(object_param_1, object_param_2, ..., object_param_n) |

| Return Type | Method Call             |
|-------------|-------------------------|
| Image      | get_object_type(obj_id) |

| Return Type | Method Call                                                                  |
|-------------|------------------------------------------------------------------------------|
| Image      | set_object_type(self, optional_change_param_1, ..., optional_change_param_n) |
      
| Return Type | Method Call                |
|-------------|----------------------------|
| Image     | remove_object_type(obj_id) |

#### Filter API

| Return Type | Method Call                                                          |
|-------------|----------------------------------------------------------------------|
| Filter     | add_object_type(object_param_1, object_param_2, ..., object_param_n) |

| Return Type | Method Call             |
|-------------|-------------------------|
| Filter      | get_object_type(obj_id) |

| Return Type | Method Call                                                                  |
|-------------|------------------------------------------------------------------------------|
| Filter      | set_object_type(self, optional_change_param_1, ..., optional_change_param_n) |
      
| Return Type | Method Call                |
|-------------|----------------------------|
| Boolean     | remove_object_type(obj_id) |

### Credit Card API

| Return Type | Method Call                                                          |
|-------------|----------------------------------------------------------------------|
| CreditCard     | add_object_type(object_param_1, object_param_2, ..., object_param_n) |

| Return Type | Method Call             |
|-------------|-------------------------|
| CreditCard      | get_object_type(obj_id) |

| Return Type | Method Call                                                                  |
|-------------|------------------------------------------------------------------------------|
| CreditCard      | set_object_type(self, optional_change_param_1, ..., optional_change_param_n) |
      
| Return Type | Method Call                |
|-------------|----------------------------|
| Boolean     | remove_object_type(obj_id) |

### Private API

We currently have private constructors that can only be accessed through privae method calls in our DBAdaptor class 
which instantiate instances of:
   - Member objects
   - Post objects
   - Image objects
   - Comment objects
   - Credit Card objects
   - Filter objects
   
#### Member

| Return Type       | Method Call                |
|-------------      |----------------------------|
| Member Object     | Member(self, user_id, first_name, last_name, email, pw, cc_num, post_id, points, visibility, invited_by, user_type, login_time, logout_time, date_created, birthday, address, phone_number) |
                
#### Comment 

| Return Type       | Method Call                |
|-------------      |----------------------------|
| Comment Object    | Comment(self, replies, post_id, user_id, content, date_created, by_admin) |

#### Post

| Return Type       | Method Call                |
|-------------      |----------------------------|
| Post Object       | Post(self, comments, image_id, user_id, urls, shortened_urls, date_created, date_modified, is_flagged, points_given, content, by_admin) |

#### Image

| Return Type       | Method Call                |
|-------------      |----------------------------|
| Image Object      | Image(self, filter_id, original_image_id, is_flagged, by_admin) |

#### Filter

| Return Type       | Method Call                |
|-------------      |----------------------------|
| Filter Object     | Filter(self, filter_id, preview_url) |

#### Credit Card

| Return Type       | Method Call                |
|-------------      |----------------------------|
| Credit Card Object| CreditCard(self, card_num, cvv, holder_name, exp_date, date_added, currently_used, user_id) |


## Testing Plans

### Unit Testing

Currently we have unit tests set up that test:

   1.a. Adding a new member to the database and saving the returned object in a member variable.
        Fetching a different instance of that object in the database.
        Checking that the two instances are equal to one another. 
   
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

## Test Descriptions

Here is the Low Level Documentation of what each specific test is doing.  

# Image Test Cases

Helper Functions: As is the case with the other object classes, we need to be able to create instances of each object and associated      objects following it in the hierarchy for testing purposes. For the Image test cases, we create the following helper functions:
   - Create Member: 
      - Pre-Conditions/Params: Name, invitedBy (optional param)
      - Post-Conditions: Returns a Member object with the following params set: visibility, invited_by, email, password, username,                                points, user_type, is_verified, birthday, and address.
   - Create Post: 
      - Pre-Conditions: Content, User (optional)
      - Post-Conditions: Returns a Post object with the following params set: user, url, is_flagged,content, and by_admin.
   - Create Image:
      - Pre-Conditions: User, post, image.
      - Post-Conditions: Returns a Image object with the following params set: user, post, current_image, is_flagged, and by_admin.

Case 1: Creating Image
   This case tests that the creation of an image works as intended. It works by creating a member and post object first, and using those    created objects as parameters to make an Image object.  There is another image variable that is essentially a temporary photo file      object created to test for comparisons
   
   Assert Statements:
      - Test that the image variable is the same instance/object as that image built through our API's create call.  
      - Test that the object count is equal to one.  Basically, to ensure create didn't make a duplicate. 

Case 2: Creating Image Test # 2
   This case tests that the creation of an image actually works by adding the new image to the database. It is essentially the same as      test case #1, but is ensuring that our API create call adds data to the database
   
   Assert Statements:
      - Test that the image variable is the same instance/object as that image built through our API's create call.  
      - Test that the object count is equal to two.  Basically, to ensure our first test case actually added to the database.  
      
Case 3: Getting Image attribute
  This case tests that the API get call works as intended to retrieve the Image data for a specific attribute.  We will test that the     original_image_id matches to what is in the database.  It works by first creating the respective Member and Post Objects with that the   Image object uses as parameters for creation.  We then get the original_image_id and do an assert statement to ensure they are equal. 
  
  Assert Statements:
      - Test that the original_image_id recieved from GET call is actually the ID specified.  
  
Case 4: Setting Image attribute
   This case tests that the API set call works as intended to update the associated attribute field for the Image object to be changed.    It works by first creating the respective Member and Post Objects with that the Image object uses as parameters for creation.  Then,    a new image ID is set and this is compared to the associated original_image_id that is retrieved from the database.
   
   Assert Statements:
      -Test that the updated original_image_id was reflected in the database and is equivalent. 

Case 5: Deleting Image attribute
   This case tests that the API delete call works as intended to remove the associated Image is removed from the database. After            creation of the image, we do an assert statement to see that the image is in the database.  We then delete the image with the use of    it's orignal_image_id.  Finally, we check to see that the database is empty as it should be
   
   Assert Statements:
      -Test that the number of Image objects in database is 1 after creation.
 
# Filter Test Cases
Helper Functions: As is the case with the other object classes, we need to be able to create instances of each object and associated    objects following it in the hierarchy for testing purposes. For the Image test cases, we create the following helper functions:
   - Create Member: 
      - Pre-Conditions/Params: Name, invitedBy (optional param)
      - Post-Conditions: Returns a Member object with the following params set: visibility, invited_by, email, password, username,                                points, user_type, is_verified, birthday, and address.
   - Create Post: 
      - Pre-Conditions: Content, User (optional)
      - Post-Conditions: Returns a Post object with the following params set: user, url, is_flagged,content, and by_admin.
   - Create Image:
      - Pre-Conditions: User, post, image.
      - Post-Conditions: Returns a Image object with the following params set: user, post, current_image, is_flagged, and by_admin.
   - Create Filter:
      - Pre-Conditions: Image
      - Post-Conditions: Returns a Filter object with the following params set: image, filter_name.
      
Case 1: Creating a Filter Object
   This case tests that the creation of an Filter object works as intended. It works by creating a member, post, and image object first,    and using those created objects as parameters to make an Filter object.  There is another filter variable that is essentially a          temporary photo filter object created to test for comparisons.
   
   Assert Statements:
      - Test that the filter variable is the same instance/object as that filter built through our API's create call.  
      - Test that the object count is equal to one.  Basically, to ensure create didn't make a duplicate. 
 
 Case 2: Setting a Filter Object's Attribute
   This case test that the updating of a filter object works as intended.  We will be testing it by changing the filter_id attribute and    ensuring that it is changed in the database as well.
   
   Assert Statements:
      - Test that the updated filter_id was reflected in the database and is equivalent. 

## Class Diagram

![alt-text](https://github.com/320-group4/High-Level-Requirements/blob/master/er1.png)


