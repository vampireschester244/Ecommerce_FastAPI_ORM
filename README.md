# Ecommerce REST API store
## Tech Stack
 - Fast API
 - SQL Lite/MySQL
 - ORM
 - HTML
 
 ## API Capabilites
 - User registration
 - Pydantic validation for serialize and de-serialize the API requests 
 - JWT authentication with OAuth2 security
 - Tortoise ORM
 - CRUD
 - Email verification for login
 - JWT Login
 - File Upload
 
 ## API Usage 
  * Users
    - Ability to register and login users for performing actions on their ecommerce business and products.
    - Triggering email notification to registered users and confirm verification in order to login.
    - Providing security constraints like OAuth2 with Password (and hashing), Bearer with JWT tokens to the registered users in order to ensure secure data handling.
  * Business
    - Ability for the registered users to create/read/update/delete their business entities
    - File/Image upload functionality for their profile logo
  * Products
    - To create, read, update and delete products by respective business owners
    - To view all products for end-user
    - Ability for business owners to upload images/files of each product in the ecommerce store through this API
    - Create discounts and expiry of discounts for the products for the festive season or any special occasion.
 
