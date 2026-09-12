"""
Credentials for SauceDemo test users.

IMPORTANT: In real projects this file would be added to .gitignore
and never committed to the repository. Instead, credentials would be
stored in environment variables, CI/CD secrets, or a secret manager
(e.g., HashiCorp Vault, AWS Secrets Manager, GitHub Actions Secrets).

This file is committed here ONLY for demonstration purposes
of a practice project.
"""

# --- SauceDemo users ---
STANDARD_USER = {
    "username": "standard_user",
    "password": "secret_sauce",
}

LOCKED_OUT_USER = {
    "username": "locked_out_user",
    "password": "secret_sauce",
}

WRONG_PASSWORD_USER = {
    "username": "standard_user",
    "password": "wrong_password",
}
