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

### Private API

We currently have private constructors that can only be accessed through privae method calls in our DBAdaptor class 
which instantiate instances of:
   - Member objects
   - Post objects
   - Image objects
   - Comment objects
   - Credit Card objects
   - Filter objects

## Testing Plans

### Unit Testing

Currently we have unit tests set up that test:
   1. Adding a new member to the database then retrieving it immediately after.
   2a. Retrieving a previously existing member from DB and instantiating an instance of a Member object.
      Then testing this against a premade Member object to ensure that the object parameters are identical.
   2b. Attempt to retrieve a non-existing member object.
       Ensure that a null value is returned - indicating that this member does not exist in the system. 
   3a. Retrieving a previously existing member from DB.
      Changing one specific parameter associated with the Member object.
      Retrieving the same member from the DB after the changes have been made.
      Ensuring that this instance of the member is identical to a premade member object with the desired values in each parameter.
   3b. Retrieving a previously existing member from DB.
      Changing multiple specific parameters associated with the Member object.
      Retrieving the same member from the DB after the changes have been made.
      Ensuring that this instance of the member is identical to a premade member object with the desired values in each parameter.
   4. Deleting an instance of a previously existing member and ensuring that the boolean returned correctly indicates whether or not
      the member is actually gone from the DB table.
   4b. Deleting a non-existing member from the DB and ensuring that the remove method returns false and correctly handles a non-existing
      object in the system. 
      
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





