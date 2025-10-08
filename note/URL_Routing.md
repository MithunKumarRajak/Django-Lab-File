
## 🐍 Summary: Django 404 Error – `/course` Not Found

### ❗ Problem

You tried to access `http://127.0.0.1:8000/course`, but Django returned a **404 error** because this URL was **not defined** in your `urlpatterns`.

### 🔍 Cause

Your `urls.py` only had:

```python
urlpatterns = [
    path('', views.course, name='course'),
]
```

This setup only matches the **root URL** (`/`), not `/course`.

### ✅ Solution

Update your `urls.py` to include the `/course` path:

```python
urlpatterns = [
    path('course/', views.course, name='course'),
]
```

Now, visiting `/course` will correctly route to the `course` view.

### 💡 Suggestions

- Always define every URL you want to access.
- Use meaningful prefixes like `'course/'`, `'learn/'`, etc.
- Ensure the corresponding view exists in `views.py`.
- Restart the Django server after changes.
- Use `{% url %}` or `reverse()` to avoid hardcoding URLs.

---
