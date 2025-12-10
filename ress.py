'''*uv init --bare
uv venv
.\.venv\Scripts\activate
uv add (whatever packages u want)
  - example: uv add numpy
uv sync
 
deactivate:
uv .\venv\Scripts\deactivate
'''

import sqlite3

print(sqlite3.sqlite_version)