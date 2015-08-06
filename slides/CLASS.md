### MelbDjango School - Lesson Four

Django Forms & Testing

---

### WIFI

Common Code / cc&20!4@

---

### HTML Forms

- One of the ways users can interact with your application
- Data entered by the user is sent to the server for processing
- Always surrounded by `<form>...</form>` (in valid HTML)
- text, radio, file, select, textarea, submit, etc.

---

### Reminder: GET vs POST

- Forms are submitted via GET or POST

- Quick reminder:
  - Using GET puts the form content in the URL (no passwords!)
  - Use POST for anything that changes the database

---

### Django Forms

- Django helps with the rendering and processing of HTML forms

- There are two different types of forms provided:
  - `django.forms.Form`
  - `django.forms.ModelForm`

- Using Django Forms simplifies the use of HTML forms
- Helps your create more secure web applications

---

### Quick example

- Imagine a HTML form that looks like this:

```
<form>
  <input type="text" name="name" value="">
  <input type="submit" value="Say Hello">
</form>
```

---

### Quick example

- We can create a very simple Django form:

```
from django import forms

class HelloWorldForm(forms.Form):
    name = forms.CharField()
```

---
### Form Fields

---

### Form Widgets

---

### Form Validation

is_valid

---

### Adding other Validators

---

### Custom Validation

---

### Cleaning Fields

---

### Form Errors

---

### Using Forms

- Instantiating
- Putting forms into a template
- Accessing the data
- Returning if there is an error

---

### CSRF

---

### Testing

- Why Django tests are _rad_
- Why we're introducing tests now
- (because you must have tests in your assignment)
