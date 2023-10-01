import { Component, OnInit } from '@angular/core';
import { TaskService } from '../task.service';
import { Task } from '../task.model';

@Component({
  selector: 'app-todo-list',
  templateUrl: './todo-list.component.html',
  styleUrls: ['./todo-list.component.css'],
})
export class TodoListComponent implements OnInit {
  tasks: Task[] = [];

  constructor(private taskService: TaskService) {}

  ngOnInit(): void {
    this.tasks = this.taskService.getTasks();
  }

  markCompleted(task: Task): void {
    task.completed = !task.completed;
    this.taskService.updateTask(task);
  }

  editTask(task: Task): void {
    task.isEditing = true;
  }

  saveEditedTask(task: Task): void {
    if (task.title.trim() === '') {
      // Handle form validation error (e.g., display an error message)
      return;
    }

    task.isEditing = false;
    this.taskService.updateTask(task);
  }

  cancelEdit(task: Task): void {
    task.isEditing = false;
  }

  deleteTask(task: Task): void {
    this.taskService.deleteTask(task.id);
    this.tasks = this.taskService.getTasks();
  }
}
