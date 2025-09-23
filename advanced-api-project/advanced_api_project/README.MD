# 📚 Book API - Django REST Framework

This API provides CRUD operations for managing books and authors using Django and Django REST Framework.

---

## 🔗 API Endpoints

| Method | Endpoint                  | Description               | Auth Required |
|--------|---------------------------|---------------------------|---------------|
| GET    | /api/books/               | List all books            | ❌ No         |
| GET    | /api/books/<id>/          | Get book by ID            | ❌ No         |
| POST   | /api/books/create/        | Create a new book         | ✅ Yes        |
| PUT    | /api/books/<id>/update/   | Update a book             | ✅ Yes        |
| DELETE | /api/books/<id>/delete/   | Delete a book             | ✅ Yes        |

---

## 🔒 Permissions

- **Read (GET)**: Available to everyone (authenticated or not)
- **Write (POST, PUT, DELETE)**: Requires authentication
- Custom permission class used: `IsAuthenticatedOrReadOnly`

---

## 🧠 Features

- Generic class-based views (ListAPIView, RetrieveAPIView, CreateAPIView, etc.)
- Custom validation for `publication_year` to prevent future dates.
- Permissions to restrict unsafe methods.
- Related author connection using foreign key.

---

## 🧪 Testing the API

You can test with tools like:

- 🧪 [Postman](https://www.postman.com/)
- 🧪 `curl`
- 🧪 Browsable API from Django REST Framework

---

## 🧰 Setup Instructions

1. Install dependencies:

```bash
pip install django djangorestframework
