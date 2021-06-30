# contact_app
A simple django app with basic auth and crud operations

possible calls:

1) GET https://workex.herokuapp.com/auth/users/   (?page=pg_no)

return list of users with their details in pagination format

2 contacts per page as of now

2)GET  https://workex.herokuapp.com/auth/users/user_name

username can be both name and username in email id

suppose sourr@gmail.com, then sourr is username

3)POST https://workex.herokuapp.com/auth/users/

Add data to app,

body = 
{
    "email": "manu@deloitte.com",
    "name": "Manoj Q",
    "phone_number": "3456872345",
    "address": "Mumbai"
}

4)POST https://workex.herokuapp.com/auth/users/user_name/search

body = {"email":"manu@gmail.com"}

return the object whole email address is the provided one

5)Patch https://workex.herokuapp.com/auth/users/

body = { 
   fields to be updated
}

6)Delete https://workex.herokuapp.com/auth/users/
body = {
object key:val pairs
} 
the object which u want to delete

7)Delete https://workex.herokuapp.com/auth/users/email_user_name/delete

no body, will delete successfully email id with username provided
