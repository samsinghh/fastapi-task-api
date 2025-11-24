from sqlalchemy.orm import Session
from fastapi import HTTPException

from .schemas import TaskCreate, TaskUpdate
from .dao import (
    create_task_dao,
    get_task_by_id_dao,
    get_tasks_dao,
    update_task_dao,
    delete_task_dao,
)

def create_task_controller(db: Session, task_data: TaskCreate):
    return create_task_dao(db, task_data)

def get_tasks_controller(db: Session):
    return get_tasks_dao(db)

def get_task_by_id_controller(db: Session, task_id: int):
    task = get_task_by_id_dao(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

def update_task_controller(db: Session, task_id: int, task_data: TaskUpdate):
    task = get_task_by_id_dao(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return update_task_dao(db, task, task_data)

def delete_task_controller(db: Session, task_id: int):
    task = get_task_by_id_dao(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    delete_task_dao(db, task)
    return {"detail": "Task deleted successfully"}
