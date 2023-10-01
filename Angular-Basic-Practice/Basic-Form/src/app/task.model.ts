// task.model.ts
// task.model.ts
export interface Task {
  id: number;
  title: string;
  description: string;
  completed: boolean;
  isEditing?: boolean; // Add this property
}
