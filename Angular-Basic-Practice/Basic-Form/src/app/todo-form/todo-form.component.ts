import { Component, Output, EventEmitter } from '@angular/core';
import { Task } from '../task.model';
import { TaskService } from '../task.service';

@Component({
  selector: 'app-todo-form',
  templateUrl: './todo-form.component.html',
  styleUrls: ['./todo-form.component.css'],
})
export class TodoFormComponent {
  @Output() taskAdded = new EventEmitter<Task>();

  newTask: Task = {
    id: 0,
    title: '',
    description: '',
    completed: false,
  };

  constructor(private taskService: TaskService) {}

  onSubmit(): void {
    if (this.newTask.title.trim() === '') {
      // Handle form validation error (e.g., display an error message)
      return;
    }
    this.taskService.addTask(this.newTask);
    this.taskAdded.emit(this.newTask);
    this.newTask = {
      id: 0,
      title: '',
      description: '',
      completed: false,
    };
  }
}
