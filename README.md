## Article/Chat/Navigation Example using Django and SQLite

# Prerequisites:
- Python3.6

# Optionally Install Dependencies (handled by run script if python3.6 is installed):
- `python3.6 -m pip install -r Requirements.txt`

# Run it
    ./run.sh

# View it
- Open browser to `localhost:8000`

# Application Details
- Article routing is handled by `article_app/url.py` (imported via `url.py`)
- Article routing exposes these endpoints:
```
urlpatterns = [
    path('', views.index, name='index'),
    path('article/<article_id>', views.article, name='article'),
    path('article/<article_id>/comment', views.add_comment, name='add-comment')
]
```
- Templates exposed from `example/templates/` directory.
- Static files hosted from `example/static/` directory (contains JS/CSS/Favicon/etc)
- The `article_app/views.py` handles rendering data for the article application, and uses `article_app/controller.py` for the more non-view related functionality.
- Article Comments are stored in SQLite, and are relational to their article-uuid (uses `uuid` value from `article_app/content_api.json`)
- Each article only displays the comments for that article
- Comments are persisted
- `example/texmplates/article.html` contains the JavaScript required for sending messages and re-ordering stocks (could be moved to a static file).