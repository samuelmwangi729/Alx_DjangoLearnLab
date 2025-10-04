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

## 💬 Comment System

### Features:
- Add comments to blog posts
- Edit or delete your own comments
- All users can view comments on posts

### URL Patterns:
- `/posts/<post_id>/comments/new/` - Create a comment
- `/comments/<comment_id>/edit/` - Edit a comment
- `/comments/<comment_id>/delete/` - Delete a comment

### Permissions:
- Only logged-in users can comment
- Only comment authors can edit or delete their comments
- All users (authenticated or not) can view comments

### How to Comment:
1. Log in to your account
2. Open a blog post
3. Scroll to the bottom and submit the comment form
