
# Django Project – Technical Summary of Issues & Fixes

This document summarizes the key technical problems encountered while building a multi-app Django project (with apps like `display`, `registration`, etc.) and the solutions applied.

---

## 1️⃣ TemplateDoesNotExist Error

**Issue:**  
Django raised:

```

TemplateDoesNotExist at /registration/
registration/index.html

```

**Cause:**  

- The HTML template was not in the correct location.
- Django could not find the template because of a **wrong directory structure**.

**Fix:**  

- Created the template inside the app’s `templates/<app_name>/` directory.
- Correct path example:

```

project\_root/
└─ registration/
└─ templates/
└─ registration/
└─ index.html

````

- In `settings.py`, ensured:

```python
INSTALLED_APPS = [
    'registration',
    ...
]
````

---

## 2️⃣ URL & Path Mismatches

**Issue:**
Some pages loaded a blank screen or returned 404 errors.

**Cause:**

- Incorrect path in `fetch()` calls or wrong URL pattern in `urls.py`.
- Example: Frontend called `/fruit_student/api/` but backend used a different name.

**Fix:**

- Matched `fetch()` URLs with Django `path()` definitions:

```javascript
fetch("/fruit_student/api/")
```

```python
path("fruit_student/api/", views.fruit_student_api, name="fruit_student_api")
```

---

## 3️⃣ API Data Not Rendering in Browser

**Issue:**
API endpoint returned correct JSON (e.g., fruits and students) but template page showed only headings.

**Cause:**

- JavaScript fetch worked, but HTML was static before the data was appended.

**Fix:**

- Verified that `fetch()` logic was correct:

```javascript
.then(data => {
    const fruitList = document.getElementById("fruit-list");
    data.fruits.forEach(fruit => {
        const li = document.createElement("li");
        li.textContent = fruit;
        fruitList.appendChild(li);
    });
});
```

- Ensured `script` was placed **at the bottom** of the template so DOM elements existed.

---

## 4️⃣ App Directory Confusion

**Issue:**
Multiple apps (e.g., `display`, `registration`) made it confusing to locate templates and static files.

**Fix:**

- Maintained a **consistent structure**:

```
project/
├─ manage.py
├─ db.sqlite3
├─ registration/
│  ├─ views.py
│  ├─ urls.py
│  └─ templates/registration/index.html
├─ display/
│  └─ templates/display/fruit_api.html
└─ view_demo/   # main project settings
```

- Used `app_name/templates/app_name/` format for every app.

---

## 5️⃣ GitHub Deployment & README

**Issue:**
Needed to upload a multi-app Django project to GitHub.

**Steps Taken:**

1. Initialized a git repository:

   ```bash
   git init
   git add .
   git commit -m "Initial Django project commit"
   ```

2. Created a GitHub repo and pushed:

   ```bash
   git remote add origin <repo_url>
   git push -u origin main
   ```

3. Added a `README.md` for documentation:

   - Explained project setup
   - Listed dependencies (`Django`, `sqlite3`)
   - Added run instructions

## 🔑 Key Takeaways

- ✅ **Template Location Matters**: Always store templates as `templates/<app_name>/name.html`.
- ✅ **URL Consistency**: API paths in JavaScript must match Django `urls.py`.
- ✅ **App Structure**: Keep each app self-contained for easy maintenance.
- ✅ **Documentation**: Add a `README.md` to guide me .
