# Django Blog Application

A full-featured blog application built with Django 5.2, featuring CRUD operations, user authentication, and class-based views.

## Features

- 📝 Create, Read, Update, and Delete blog articles
- 👤 User authentication and authorization
- 🔒 Protected routes (login required for creating articles)
- 📱 Responsive design with clean UI
- 📅 Article publishing dates
- ✍️ Author attribution
- 🎨 Custom styled templates

## Tech Stack

- **Django**: 5.2.8
- **Django REST Framework**: 3.16.1+
- **Django REST Framework SimpleJWT**: 5.5.1+
- **Python**: 3.12+
- **Database**: SQLite (default)

## Project Structure

```
unv-django-101/
├── blog/                   # Main blog application
│   ├── models.py          # Article model
│   ├── views.py           # Class-based and function-based views
│   ├── forms.py           # Article forms
│   ├── urls.py            # Blog URL patterns
│   └── templates/         # Blog templates
│       └── blog/
│           ├── article_list.html
│           ├── article_detail.html
│           ├── article_form.html
│           └── article_confirm_delete.html
├── conf/                  # Project configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── fun/                   # Additional app
├── mentees/              # Additional app
├── manage.py             # Django management script
└── requirements.txt      # Project dependencies
```

## Installation

### Prerequisites

- Python 3.12 or higher
- uv package manager (recommended) or pip

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/sazedulhaque/unv-django-101.git
   cd unv-django-101
   ```

2. **Install dependencies**

   Using `uv` (recommended):
   ```bash
   uv sync
   ```

   Or using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Apply database migrations**
   ```bash
   uv run manage.py migrate
   # or
   python manage.py migrate
   ```

4. **Create a superuser**
   ```bash
   uv run manage.py createsuperuser
   # or
   python manage.py createsuperuser
   ```

5. **Run the development server**
   ```bash
   uv run manage.py runserver
   # or
   python manage.py runserver
   ```

6. **Access the application**
   - Main application: http://localhost:8000/
   - Admin panel: http://localhost:8000/admin/

## Usage

### Blog Features

- **View Articles**: Navigate to the homepage to see all published articles
- **Create Article**: Click "Create New Article" (requires authentication)
- **View Details**: Click on any article title to view full details
- **Update Article**: Click "Update" on any article (requires authentication)
- **Delete Article**: Click "Delete" and confirm (requires authentication)

### URL Patterns

- `/` - Article list view
- `/article/new/` - Create new article (login required)
- `/article/detail/<id>/` - Article detail view
- `/article/update/<id>/` - Update article
- `/article/delete/<id>/` - Delete article confirmation

### Authentication Flow

- Unauthenticated users attempting to create articles are redirected to:
  ```
  /admin/login/?next=/article/new/
  ```
- After successful login, users are redirected back to the article creation page

## Development

### Running Tests

```bash
uv run manage.py test
# or
python manage.py test
```

### Code Style

The project follows PEP 8 guidelines with a line length limit of 79 characters.

### Making Migrations

After modifying models:
```bash
uv run manage.py makemigrations
uv run manage.py migrate
```

## Models

### Article Model

```python
- title: CharField (max_length=200)
- content: TextField
- author: ForeignKey(User)
- published_date: DateTimeField (auto_now_add=True)
```

## Views

The application uses both function-based and class-based views:

- `ArticleListView` - Display all articles
- `ArticleCreateView` - Create new articles (with auth check)
- `ArticleDetailView` - Display single article
- `ArticleUpdateView` - Update existing articles
- `ArticleDeleteView` - Delete articles with confirmation

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is for educational purposes.

## Contact

- Repository: https://github.com/sazedulhaque/unv-django-101
- Author: Sazedul Haque

## Acknowledgments

- Django Documentation
- Django REST Framework
- University Learning Project
