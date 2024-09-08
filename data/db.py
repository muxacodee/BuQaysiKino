import sqlite3


class Database:
    def __init__(self, db_name='users.db'):
        self.db_name = db_name
        self.initialize_db()

    def initialize_db(self):
        """Initialize the database and create the users table if it doesn't exist."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id BIGINT UNIQUE
                )
            ''')
            conn.commit()

    def check_user(self, user_id):
        """Check if a user already exists in the database."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
            row = cursor.fetchone()
            return row is not None

    def add_user(self, user_id):
        """Add a new user ID to the database."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute('INSERT INTO users (user_id) VALUES (?)', (user_id,))
                conn.commit()
            except sqlite3.IntegrityError:
                # User ID already exists
                pass

    def get_all_users(self):
        """Retrieve all user IDs from the database."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT user_id FROM users')
            return [row[0] for row in cursor.fetchall()]
