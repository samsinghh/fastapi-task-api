from sqlalchemy.orm import Session
from . import models

def create_task_dao(db: Session, task_data):
    new_task = models.Task(**task_data.model_dump())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def get_tasks_dao(db: Session):
    return db.query(models.Task).all()

def get_task_by_id_dao(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()

def update_task_dao(db: Session, task, update_data):
    update_values = update_data.model_dump(exclude_unset=True)
    for key, value in update_values.items():
        setattr(task, key, value)
    db.commit()
    db.refresh(task)
    return task

def delete_task_dao(db: Session, task):
    db.delete(task)
    db.commit()
