# Securing Django Application with HTTPS

## Objective
Enhance the security of your Django application by configuring it to handle secure HTTPS connections and enforce HTTPS redirects for all HTTP requests. This ensures that data transmitted between the client and server is encrypted, maintaining confidentiality and integrity while adhering to best practices for secure web communication.

---

## Task Description
This task involves configuring your Django application to fully support and enforce HTTPS, including:

- Redirecting all HTTP requests to HTTPS.
- Enforcing security-related HTTP headers.
- Securing cookies to be transmitted only over HTTPS.
- Setting up SSL/TLS in the deployment environment.

---

## Step 1: Configure Django for HTTPS Support

Modify your `settings.py` to enforce HTTPS and enable HTTP Strict Transport Security (HSTS).

```python
# Redirect all HTTP requests to HTTPS
SECURE_SSL_REDIRECT = True

# HTTP Strict Transport Security (HSTS)
# Tell browsers to only access your site via HTTPS for one year (in seconds)
SECURE_HSTS_SECONDS = 31536000

# Apply HSTS policy to all subdomains
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# Allow your domain to be included in browser preload lists for HSTS
SECURE_HSTS_PRELOAD = True
