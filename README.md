# Django_Blog_Api_With_JWT_Token
This is a simple Blog API showcasing JSON WEB TOKEN AUTHENTICATION for DJANGO

# Installation
Install using pip...
<code>pip install django-jwt-auth</code>

# Usage
You can use POSTMAN for testing this.

<code>SIGN UP</code>
<pre>METHOD = POST 
URL = http://127.0.0.1:8000/sign_up/
BODY = username,email,password</pre>

<code>LOGIN</code>
<pre>METHOD = POST
URL = http://127.0.0.1:8000/login/
BODY = username, password</pre>

After you login you will be provided with token,
You must use this token for further authentication. 

<code>list user blogs</code>
<pre>METHOD = POST
URL = http://127.0.0.1:8000/list_user_blog/
No BODY parameters
HEADERS = Content-Type = application/json, Authorization = JWT { YOUR_JWT_TOKEN }
</pre>


<code>create a blog</code>
<pre>METHOD = POST
URL = http://127.0.0.1:8000/create_blog/
BODY = title, description
HEADERS = Content-Type = application/json, Authorization = JWT { YOUR_JWT_TOKEN }
</pre>

