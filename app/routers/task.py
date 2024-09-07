from fastapi import APIRouter, Depends, status, HTTPException

from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from typing import Annotated

from app.models import *
from sqlalchemy import insert
from app.schemas import CreateUser, CreateTask

from slugify import slugify
from sqlalchemy import select
from sqlalchemy import update, delete
router = APIRouter(prefix="/task", tags=["task"])

@router.get("/")
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task).where(Task.id >= 0)).all()
    return tasks

@router.get("/task_id")
async def task_by_id(db: Annotated[Session, Depends(get_db)], task_id: int):
    task = db.scalars(select(Task).where(Task.id == task_id))
    if task is None:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Task was not found'
        )

    else:
        return db.scalars(select(Task).where(Task.id == task_id))


@router.post("/create")
async def create_task(db: Annotated[Session, Depends(get_db)], create_task: CreateTask, user_id: int):
    db.execute(insert(Task).values(
                            title=create_task.title,
                            content=create_task.content,
                            priority=create_task.priority,
                            completed=create_task.completed,
                            user_id=create_task.user_id,
                            slug=slugify(create_task.title)))
    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }

@router.put("/update")
async def update_task(db: Annotated[Session, Depends(get_db)], task_slug: str,
                      update_task_model: CreateTask):
    task_update = db.scalar(select(Task).where(Task.slug == task_slug))
    if task_update is None:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There is no task found'
        )

    db.execute(update(Task).where(Task.slug == task_slug)
        .values(title=update_task_model.title,
                content=update_task_model.content,
                priority=update_task_model.priority,
                completed=update_task_model.completed,
                user_id=update_task_model.user,
                slug=slugify(update_task_model.title))
    )

    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Task update is successful'
    }

@router.delete("/delete")
async def delete_task(db: Annotated[Session, Depends(get_db)], task_id: int):
    task_delete = db.scalar(select(Task).where(Task.id == task_id))
    if task_delete is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There is no task found'
        )
    db.execute(delete(Task).where(Task.id == task_id))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Task delete is successful'
    }