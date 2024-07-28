# 0x02. Session Authentication

## Back-end Authentication
**Weight:** 1

**Project Duration:** 
- **Start:** Jul 10, 2024 6:00 AM
- **End:** Jul 12, 2024 6:00 AM

An auto review will be launched at the deadline.

**Auto QA review:**
- Mandatory: 0.0/135
- Optional: 0.0/46
- Altogether: 0.0%
- Calculation: 0.0% + (0.0% * 0.0%) == 0.0%

## In a Nutshell…
In this project, you will implement a Session Authentication. You are not allowed to install any other module.

In the industry, you should not implement your own Session authentication system and use a module or framework that does it for you (like in Python-Flask: Flask-HTTPAuth). Here, for learning purposes, we will walk through each step of this mechanism to understand it by doing.

## Resources
Read or watch:
- [REST API Authentication Mechanisms](#) - Only the session auth part
- [HTTP Cookie](#)
- [Flask](#)
- [Flask Cookie](#)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- What authentication means
- What session authentication means
- What Cookies are
- How to send Cookies
- How to parse Cookies

## Requirements

### Python Scripts
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` style (version 2.5)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class, or method (the length of it will be verified)

## What is Session Authentication?
Session authentication is a method of verifying and maintaining the identity of a user across multiple interactions (or sessions) with a web application.

### How Session Authentication Works
1. **User Login**: The user provides credentials which the server verifies.
2. **Session Creation**: The server creates a session and generates a unique session ID.
3. **Session Storage**: Session data is stored on the server.
4. **Session ID Transmission**: The session ID is sent to the client as a cookie.
5. **Subsequent Requests**: The client sends the session ID with each request.
6. **Session Expiration**: Sessions expire after a certain period or inactivity.

### Advantages
- **State Management**: Maintains state information between requests.
- **Security**: Hard to guess session IDs.
- **User Experience**: Users stay logged in as they navigate.

## What are Cookies?
Cookies are small pieces of data sent from a website and stored on the user's device by the user's web browser.

### Types of Cookies
- **Session Cookies**: Temporary cookies erased when the browser is closed.
- **Persistent Cookies**: Remain on the device for a set period.
- **First-Party Cookies**: Set by the website the user is visiting.
- **Third-Party Cookies**: Set by domains other than the one the user is visiting.

### Key Uses
- **Session Management**: Keep users logged in.
- **Personalization**: Store user preferences.
- **Tracking and Analytics**: Collect data about user behavior.

### Cookie Attributes
- **Name and Value**
- **Domain**
- **Path**
- **Expires/Max-Age**
- **Secure**
- **HttpOnly**
- **SameSite**

### Security Considerations
- **Cookie Theft**: Use HTTPS to protect cookies.
- **Cross-Site Scripting (XSS)**: Set `HttpOnly` attribute.
- **Cross-Site Request Forgery (CSRF)**: Use `SameSite` attribute.

## How to Send Cookies
Cookies are sent using the `Set-Cookie` HTTP header in server responses.

### Example (Python Flask):
```python
from flask import Flask, make_response

app = Flask(__name__)

@app.route('/setcookie')
def set_cookie():
    resp = make_response("Cookie Set")
    resp.set_cookie('username', 'John Doe')
    return resp

if __name__ == '__main__':
    app.run(debug=True)

