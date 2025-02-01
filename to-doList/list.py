def main():
    tasks=[]
    
        
    while True:
        print("\n========To-Do List=======")
        print("1.Add Task")
        print("2.Show Tasks")
        print("3.Mark Task As Done")
        print("4.Exit")
        
        choise=input("Enter your choice: ")
        if choise in ('1','2','3','4'):
            try:
                if choise=='1':
                    print()
                    n_tasks=int(input("How many tasks you want to add ? "))
                    
                    for _ in range(n_tasks):
                        task=input("Enter the task: ")
                        tasks.append({"task": task , "done": False})
                        print("Task added successfully")
                
                elif choise=='2':
                    print('\nTasks: ')
                    for index , task in enumerate(tasks):
                            status="Done" if task["done"] else "Not Done"
                            print(f'{index+1}.{task["task"]} - {status}')
                    
                elif choise=='3':
                    task_index = int(input("Enter the task number to mark as done: ")) - 1
                    if 0 <= task_index < len(tasks):
                            tasks[task_index]["done"] = True
                            print(f"Task {tasks[task_index]} is done!")
                    else:
                            print("The task number doesnt exist. try again")
                            
                elif choise=='4':
                        print("GoodbYE!!!!")
                        break
                else:
                        print("something went wrong.try another choice.")
        
            except ValueError:
                print("Please enter a valid number")
                
      
                
if __name__ == "__main__":
    main()