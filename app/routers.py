from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .schemas import TaskCreate, TaskUpdate, TaskRead
from .database import get_db
from .controller import (
    create_task_controller,
    get_tasks_controller,
    get_task_by_id_controller,
    update_task_controller,
    delete_task_controller
)

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("", response_model=TaskRead)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task_controller(db, task)

@router.get("", response_model=list[TaskRead])
def get_tasks(db: Session = Depends(get_db)):
    return get_tasks_controller(db)

@router.get("/{task_id}", response_model=TaskRead)
def get_task(task_id: int, db: Session = Depends(get_db)):
    return get_task_by_id_controller(db, task_id)

@router.put("/{task_id}", response_model=TaskRead)
def update_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    return update_task_controller(db, task_id, task)

@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    return delete_task_controller(db, task_id)