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

| Return Type | Method Call                                                                                                                |
|-------------|----------------------------------------------------------------------------------------------------------------------------|
| Member      | add_member(self, user_id, first_name, last_name, email, pw, cc_num, invited_by, user_type, birthday, address, phone number, date_created)                                                                                                                              |           
| Member      | get_member(self, obj_id)                                                                                                   |
| Boolean     | set_member(self, new_information: dict(), obj_id)                                                                          | 
| Boolean     | remove_member(self, obj_id)  
      
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
| Filter      | get_filter(self, obj_id)                                             |
| Boolean     | set_filter(self, new_information: dict(), obj_id)                    |
| Boolean     | remove_filter(self, obj_id)                                          |

### Credit Card API

| Return Type | Method Call                                                                  |
|-------------|------------------------------------------------------------------------------|
| CreditCard  | add_object_type(object_param_1, object_param_2, ..., object_param_n)         |
| CreditCard  | get_object_type(obj_id)                                                      |
| CreditCard  | set_object_type(self, optional_change_param_1, ..., optional_change_param_n) |
| Boolean     | remove_object_type(obj_id)                                                   |

### Private API

We currently have private constructors that can only be accessed through private method calls in our DBAdaptor class 
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

## Equivalence Testing/Partioning

After we have implemented our unit testings for each unit method, we decided to proceed towards an equivalence testing suite. As a recap, the goal of equivalence testings is to split up the input domain ranges of each method into equivalent partitions, so as to only test on one possible object in that partition.  The idea is that by ensuring tests on one object in that range the method calls will work for all possible obejcts in that domain space.  There is one fatal problem with this testing method which is that just because two objects are supposed to be in the same class and act the same, doesn't necessarily mean that they will.  Thus, equivalence testing could miss those cases. Equivalence testing is typically performed on inputs due to having a larger domain of values, and not typically performed on outputs due to methods usually returning one type.  This will also help us pick out edge cases for we will have effectively mapped out all the domain ranges.  

For our database implementation, each user is very unique for every person has their own, separate data.  For example, the values of possible ranges for attribute fields for The Member object such as name, email, date created, etc. can effectively be whatever the user or person wants (with the exception to some edge cases detailed earlier).  There isn't really much room to set up different equivalence classes/partitions since the users are all pretty similar but with different data.  The only case we thought of that would be partition into different equivalence classes is Member's user_type attribute which can be Member, Idol, or Admin.  However, the testing approach for those differing fields would not be different. Thus, the way we have decided to approach the equivalence class testing for the database is to just basically give one equivalence class for each object such as Member, Post, Comment, Etc.  By testing on say two or three instances of those classes, we can show that the methods for add, get, set, and remove work for all objects in that equivalence class or basically the whole object.


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

## About Each Test

# Member tests

test_create()
Here we are testing is we can create a new Member, and we check to see if these changes take place in the database.  We first instantiating a new Member using out create function in our Member object.  We then test to see if that new Member variable we just created is an instance of Member, just to make sure that it was created correctly.  Lastly we test to see if the total count of Members in out database is 1, ensuring that 1 Member was successfully added into the Member table.  It is important to note here that when we instantiated our Member object, we set it to be a "Member" object, but this could have been of type "Admin" or "Idol" since these do the same function as a member.  By testing this works for Member, this proves that it will also work for Idol and Admin as well.

test_class_create()
This test is similar to the last one, except that it is testing if a second Member object is being added to the Member table in the database.  We first start by creating a new Member.  We then test if this new member object created is an instance of a Member object.  Then lastly we test to see if this Member object was added to the Member table in the database by checking to see if the total objects in the table is equal to 2.

test_get_specific_data()
In this test we are testing to see if we can get data from the database.  We first make a new Member with a name of "user_name".  We then call for the username of that variable we just created using the <memebr>.data['username'] to retrieve the user name of the variable before the dot.  We then check this username agaist the username that we used when creating the Member, "user_name", to see if the username of the created Member is the same as the user name we used to create the member.
   
test_get_byid()
This test is designed to test that we can retrieve data from the tables using the ID of each row.  We first start by creating a new Member with the user name "new-user".  We then get the ID if this member by using the same <member>.data['id'] call we made earlier, but this same asking for the "id" field.  We then make a call asking for the whole Member object by making the call Member.objects.get(id=new_member_id).data()['username'], passing in the id we just retrieved into the id field to that the get call can return back the whole Member object.  With this Member object, we can use <member>.data()['username'] again, but only asking for the user name.  Lastly we check to see if this user name is equal to the name "new-user" which we used at the beginning to set the name of the new Member.
   
test_edit()
This test is testing if we can make an edit to the Member object.  We first start by creating a new Member object, and setting its user name to "new-user".  We then change its user name by calling the call <member>.set_username("USER") but pass in a different name to what we oroginially made it to be.  After this we have to call the user name of this member from the Member table by using the same call <member>.data['username'].  We then test to see if this username is equal to "USER".
   
test_set_points()
This test is to show that we can change the point value of each member quickly and easily.  We start off by creating a new Member, but leaving out the points field and not defining it in the Member creation.  We then take this member and call the method set_points(), and set the amount of points to whetever, we can set it to 1.  When we retrieve the amount of points that the member has, and check to see that it equals 1.

test_delete()
Here we are testing to see if we can create and delete a Member successfully.  We start by creating a new member, then checking to see if it is in the table by calling Member.objects.count() and seeing if that returns a 1.  We then retrieve the id of that object in the table, and delete this by calling Member.objects.filter(id=id).delete(), this will delete the object in the table of that id.  Lastly we call the Member count again and check to see if it is now back at 0, to show that this Member has successfully been deleted.

test_remove_method()
This test is testing to see if our remove method is working properly.  This remove_member() methond is defined in our Models.py.  We start off by first creating a member, then once this is complete we remove the member using the function remove_member().  We then test to see if the count of the Members table is equal to 0.

test_inviteby()
In this test, we are testing to see if we can propery retireve the person who the member was invited by.  We start off by creating two members, one is an idol and the other is a member in which we add the idol as the person who the member was invited by.  We then retrieve the user that invited the member, and extract the user name from that user.  We then test to see  if this user name is equal to the user name of the idol.

# Post Tests

test_create()
We start this test by creating a new Member object as well as a new Post object.  We first test to see if this post object is an instance of a Post.  Lastly we test to see if there is a Post object in the Post table, showing that a post has been successfully added to the post table.  It is important to note that since we were able to successfully create the post with information added to the user field, we do not have to test that all fields work because we now know they work.

test_writer()
The point to this test is to test to make sure that the writer of the post is the writer we set it to.  We start here by first creating a new Member and a new Post with the Member as the author.  Then we excract the user_id from the post, to find out who the user was who wrote it.  We then use this id to extract the username from the Member object, and test this user name agaist the name we used to create the Member.  

test_set_urls()
This test is testing that we can change the url of the post successfully.  Being able to do this proves that we can also change every other field in the Post object successfully, because when changing anything in the Post object we just perform the same operation.  So doing it once would prove that we can do it for all of them.  We first start off by creating a Member object and a Post object.  We then define the url of the post to be www.cooltest.com using our set_urls function defined in Models.py.  After this we extract the url name from the post, and test this against the name www.cooltest.com.

