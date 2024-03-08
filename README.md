# polling_system
A Simple Polling Web Application using Django

## Project Overview

**Problem:** Create a Simple Polling Web Application using Django.

**Description:**
You are tasked with building a basic polling application where users can create, view, and vote on polls. The application should have the following features:
- View all available polls.
- View details of a specific poll.
- Vote on a poll option.

**Implementation:**
To implement this, follow these steps:
- Create a new Django project using django-admin startproject projectname.
- Create a new Django app using python manage.py startapp polls.
- Define models for polls and poll options in the polls/models.py file. For example:
Poll -> question, date published
Choice -> poll, choice_text, votes

- Register the Poll and Choice models in the polls/admin.py file to make them accessible in the Django admin interface.
- Create views for handling actions related to polls in the polls/views.py file. Define functions for listing all polls, viewing details of a specific poll, and voting on a poll option.
- Define URL patterns in the polls/urls.py file to map URLs to the views created in step 5.
- Create HTML templates for rendering the list of available polls, details of a specific poll, and voting form for a poll.
- Implement form handling in the views to process user input for voting on a poll option.
- Use Django's built-in form handling and CSRF protection to handle form submissions securely.
- Include links and buttons in the HTML templates to navigate between different pages and vote on poll options.
- Style the web application using CSS to improve the user interface and experience.

This project will help you understand Django's core concepts, including models, views, templates, URLs, and forms, while also introducing you to handling user input and interactions in Django applications. You can further enhance this project by adding features such as user authentication, restricting multiple votes from the same user, and displaying poll results in real-time.

## Notes
`get_object_or_404` expects only one object to be returned. If more than one are present/returned, it will give an error (`Exception Type: MultipleObjectsReturned`).

This error occurs when `get()` method of a queryset returns more than one object when it's expected to return only one.