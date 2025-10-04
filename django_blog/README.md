# Blog Post Management Features

## Features
- **Create Post**: Authenticated users can create new blog posts.
- **Read Posts**: All users (authenticated or not) can read posts.
- **Update Post**: Only post authors can update their posts.
- **Delete Post**: Only post authors can delete their posts.

## URL Endpoints
- `/posts/` – List all blog posts
- `/posts/new/` – Create a new post
- `/posts/<int:pk>/` – View post details
- `/posts/<int:pk>/edit/` – Edit a post
- `/posts/<int:pk>/delete/` – Delete a post

## Access Control
- Auth required to create, edit, or delete posts.
- Only authors can modify their own posts.
- Posts can be read by anyone.

