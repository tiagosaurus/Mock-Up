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


## Class Diagram

![alt-text](https://github.com/320-group4/High-Level-Requirements/blob/master/er1.png)


## Equivalence Classes

# Input
Testing input into one table would represent testing inputs into all the tables because since all the tables are set up the same and the only differences being that they hold different data, if we can prove we can insert into one table, then we have proved that we can insert into all the tables.

# Output
Testing outputs is the same is inputs, if we can prove that we can get an output from one table then we have proved that we can get an output from all the tables.

# Updating
Updating is also the same, updating one datapoint from one table proves that we can update something from all the tables.

# Deleting
Finally, proving we can delete something from one table proves we can delete something from all the tables.


## Edge Cases

   1. Ensure inserting into a table does the right thing
   1.a. Make sure data is what we want it to be
      -CC num is 16 digites
      -birthday month is between 1-12
      -Birthday day is 1-30
      -Make sure user type is either Member, Admin, or Idol
      -Make sure CVV is either 3 or 4 digits
      -Expiration data must be valid date
      
   1.b. Make sure it has an id so that we can update/delete this row
   1.c. Make sure all the coloumns were trying to insert are there
   
   2. Ensure fetching from a table returns the right thing
   2.a. Make sure id is valid
   2.b. Make sure the column we're fetching is actually in the table
   2.c. Make sure the column we're fetching is filled in and has data in it
   
   3. Ensure updating a table updates the right thing
   3.a. Make sure that column exists
   3.b. Make sure that id is valid
   3.c. Make sure all our data is valid (see 1.a.)
   
   4. Ensure deleting from a table entry will delete it properly
   4.a. Make sure id is valid



