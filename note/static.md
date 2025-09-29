# Here's a summary of the process for adding static files in Django:

## 🧾 Django Static Files Setup Summary

1. **Create a `static` folder** inside your app directory to store CSS, JS, and image files.

2. **Update `settings.py`**:
   - Set `STATIC_URL = '/static/'`
   - Add `STATICFILES_DIRS = [BASE_DIR / "static"]` if using a global static folder.

3. **Use static files in templates**:
   - Load static tag: `{% load static %}`
   - Link files:  ```html
     <link rel="stylesheet" href="{% static 'myapp/style.css' %}">```

4. **Run the server** and verify that your styles/scripts are loading correctly.
