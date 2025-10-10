### 📌 Posts API

- `GET /api/posts/`: List all posts (paginated)
- `POST /api/posts/`: Create new post (auth required)
- `GET /api/posts/{id}/`: Retrieve single post
- `PUT /api/posts/{id}/`: Update post (owner only)
- `DELETE /api/posts/{id}/`: Delete post (owner only)

🔍 Supports search:  
`/api/posts/?search=keyword`

### 💬 Comments API

- `GET /api/comments/`: List all comments (paginated)
- `POST /api/comments/`: Add comment (auth required)
- `GET /api/comments/{id}/`: Retrieve a comment
- `PUT /api/comments/{id}/`: Update (owner only)
- `DELETE /api/comments/{id}/`: Delete (owner only)
