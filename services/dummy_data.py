from xml.dom import NotFoundErr
from connexion import NoContent
import logging
import uuid

TASKS = [
      {
        "id": str(uuid.uuid4()),
        "task": 'task1',
        "assignee": 'assignee1000',
        "status": 'completed'
      },
      {
        "id": str(uuid.uuid4()),
        "task": 'task2',
        "assignee": 'assignee1001',
        "status": 'completed'
      },
      {
        "id": str(uuid.uuid4()),
        "task": 'task3',
        "assignee": 'assignee1002',
        "status": 'completed'
      },
      {
        "id": str(uuid.uuid4()),
        "task": 'task4',
        "assignee": 'assignee1000',
        "status": 'completed'
      }
    ]

def get_todos(limit=None, task_status=None):
  return [task for task in TASKS if not task_status or task['status'] == task_status][:limit]

def add_todo(task):
    task["id"] = str(uuid.uuid4())
    TASKS.append(task)
    return TASKS, 201

def edit_todo(new_task):
    try:
        TASKS.remove(next(current_task for current_task in TASKS if current_task.get('id') == new_task.get('id')))
        TASKS.append(new_task)
        return new_task, 200
    except StopIteration:
        logging.info('Task with id %s not found' % new_task.get('id'))
    return NoContent, 404

def delete_todo(task_id):
    try:
        TASKS.remove(next(task for task in TASKS if task.get('id') == task_id))    
        return NoContent, 204
    except StopIteration:
        logging.info('Task withid %s not found' % task_id)
    return NoContent, 404
    