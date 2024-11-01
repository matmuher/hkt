


sessions_info = """
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  session_id STRING NOT NULL UNIQUE,
  access_token STRING NOT NULL,
  expires_at TIMESTAMP NOT NULL
);
"""

