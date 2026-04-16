from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

# 此處提供 SQLAlchemy db 實例參考
# 實際開發中這通常會在 app/extensions.py 或 app/__init__.py 中初始化並被匯入
db = SQLAlchemy()

class Task(db.Model):
    __tablename__ = 'task'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(50), nullable=False, default='To Do')
    priority = db.Column(db.String(50), default='Medium')
    due_date = db.Column(db.Date, nullable=True)
    tags = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    @classmethod
    def create(cls, title, description=None, status='To Do', priority='Medium', due_date=None, tags=None):
        """新增任務"""
        new_task = cls(
            title=title,
            description=description,
            status=status,
            priority=priority,
            due_date=due_date,
            tags=tags
        )
        db.session.add(new_task)
        db.session.commit()
        return new_task

    @classmethod
    def get_all(cls):
        """取得所有任務"""
        return cls.query.all()

    @classmethod
    def get_by_id(cls, task_id):
        """用 ID 取得單筆任務"""
        return cls.query.get(task_id)

    def update(self, **kwargs):
        """更新任務屬性"""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        db.session.commit()
        return self

    def delete(self):
        """刪除任務"""
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'<Task {self.id}: {self.title}>'
