Real-time Chat Application
==========================

Introduction
------------

This real-time chat application, powered by the combination of Django and WebSockets, enables users to create and join rooms, fostering real-time communication among individuals within those rooms. The application prioritizes user security through its robust authentication system, ensuring that only registered users can access the chat functionality.

Features
--------

-   Seamless real-time communication between users within a room

-   Exclusive room joining via provided links

-   Comprehensive authentication system for user protection

-   User-initiated room creation for personalized chat spaces

Installation
------------

2.  Install Django and the necessary Python libraries.

4.  Create a Django project and configure the database settings.

6.  Set up a development server to facilitate local testing and previewing of the application.

Usage
-----

### Joining a Room

To join a room, users must obtain the room's unique link that you can copy from the chat window in the group (your friend must be in the group in order to copy the link). This hash can be acquired directly from the room creator or by clicking on the provided room link. Once the hash is acquired, users can join the room by visiting the following URL:

### Creating a Room

To create a room, click on the "Create Room" button located on the homepage. Enter a title for the new room and click the "Create" button. The application will generate a unique hash for the room and redirect the user to the room page.

### Real-time Communication

Upon joining a room, users can engage in real-time communication with other room members by typing messages into the chat box and pressing Enter. These messages will be broadcast to all users within the room, enabling seamless communication.

Authentication
--------------

The application employs Django's built-in authentication system for user account management. To register an account, click on the "Register" link on the homepage. To log in, click on the "Login" link and provide your username and password.

Deployment
----------

For deployment of the application to a production environment, consider using web hosting services like Heroku or PythonAnywhere. These services require configuring the web server to handle the Django application and utilizing a WebSocket server like Daphne.

Contributing
------------

We welcome contributions to the application's development. Feel free to fork the repository and submit pull requests to share your improvements.
