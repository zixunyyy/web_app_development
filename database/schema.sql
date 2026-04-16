CREATE TABLE IF NOT EXISTS task (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    status TEXT NOT NULL DEFAULT 'To Do',
    priority TEXT DEFAULT 'Medium',
    due_date DATE,
    tags TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
