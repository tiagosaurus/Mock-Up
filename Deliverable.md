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


## Class Diagram

![alt-text](https://github.com/320-group4/High-Level-Requirements/blob/master/er1.png)


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

