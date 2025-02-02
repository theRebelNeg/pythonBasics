import os

File_name='ToDo.txt'

def load_tasks():
    """Load tasks from the file."""
    tasks = []
    if os.path.exists(File_name):
        with open(File_name, "r") as file:
            for line in file:
                line = line.strip()
                if line:  # Only process non-empty lines
                    parts = line.split(" | ")
                    # print(parts)
                    if len(parts) == 3:  # Ensure the line has exactly 3 values
                        task, due_date, done_str = parts
                        done = True if done_str == "True" else False
                        tasks.append({"task": task, "done": done, "due_date": due_date})
                    else:
                        print(f"Skipping invalid line: {line}")
    return tasks

def save_tasks(tasks):
    with open(File_name,"w") as file:
        for task_info in tasks:
            file.write(f"{task_info['task']} | {task_info['due_date']} | {task_info['done']}\n")

def display_tasks(tasks):
    
                        
    if not tasks:
        print("no tasks are available now")
    else:
        for i , task_info  in enumerate(tasks , start=1):
            status = "Done" if task_info["done"] else "Not Done"
            print(f"{i}.{task_info['task']} (due:{task_info['due_date']}) - {status}")
            

def add_task(tasks):
    print()
    n_tasks=int(input("How many tasks you want to add ? "))
                    
    for _ in range(n_tasks):
        task=input("Enter the task: ")
        due_date=input("Enter the due date for the task : ")

        tasks.append({"task": task , "done": False,"due_date":due_date})
        print("Task added successfully")
        save_tasks(tasks)
        print("tasks are added successfully!!!!")
                    

def markDone(tasks):
    task_index = int(input("Enter the task number to mark as done: ")) - 1
    if 0 <= task_index < len(tasks):
            tasks[task_index]["done"] = True
            task_name=tasks[task_index]["task"]
            print(f"Task {task_name} is done!")
    else:
            print("The task number doesnt exist. try again")
          
def delete_task(tasks):
    display_tasks(tasks)
    
    if tasks:
        try:
            task_num=int(input('Enter the task number to delete: '))-1
            if 0<=task_num<len(tasks):
                removed_task=tasks.pop(task_num)
                save_tasks(tasks)
                print(f"Task {removed_task['task']} removed")
            else:
                print("please enter a valid task number")
        except ValueError:
            print("please enter a valid number")
            


def main():
    tasks=load_tasks()

    while True:
        print("\nTo-Do List App")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4.Update the Task")
        print("5. Exit")
        
        choise=input("Enter your choice: ")
        if choise in ('1','2','3','4'):
            try:
                if choise=='1':
                    
                    display_tasks(tasks)
                
                elif choise=='2':
                    add_task(tasks)
                    
                elif choise=='3':
                    delete_task(tasks)
                    
                elif choise=='4':
                    markDone(tasks)
                            
                elif choise=='5':
                        print("GoodbYE!!!!")
                        break
                else:
                        print("something went wrong.try another choice.")
        
            except ValueError:
                print("Please enter a valid number")
                
      
                
if __name__ == "__main__":
    main()