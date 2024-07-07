class Queue:
    def __init__(self):
        self.queue = []

    def addq(self,v):
        self.queue.append(v)

    def delq(self, v):
        self.queue.remove(v)
    
    def searchq(self,v):
        return v in self.queue
        
    def isempty(self):
        return(self.queue == [])
    
    def __str__(self):
        return(str(self.queue))

class task_manager:
    def __init__(self):    
        self.q = Queue()
        with open('audit_log', 'w') as f:
            f.write("Task Management Activity Log\n\n")
        f.close()

        
    def add_task(self,s):
        if self.q.searchq(s):
            self.log_activity(f'Create {s} : unsuccessful')
            raise Exception(f'{s} : already exists')            
        
        else:
            self.q.addq(s)
            self.log_activity(f'Create {s} : successful')

    def del_task(self,s):
        if self.q.searchq(s):
            self.q.delq(s)
            self.log_activity(f'Delete {s} : successful')

        else:
            self.log_activity(f'Delete {s} : unsuccessful')
            raise Exception(f'{s} : does not exist thus deletion not possible')

    def search_task(self, s):
        if self.q.searchq(s):
            self.log_activity(f'Search {s} : successful')
        else:
            self.log_activity(f'Search {s} : unsuccessful')
            raise Exception(f'{s} : does not exists')

    def log_activity(self, message):
        with open('audit_log', 'a') as f:
            f.write(message + '\n')
        f.close()
    
    def print_tasks(self):
        if self.q.isempty():
            print('No tasks left')
        else:
            print(self.q)
    
class Solution:
    t = task_manager()
    try:
        choice = int(input('Welcome to Task Manager!\nPress 1 to add a task\nPress 2 to delete a task\nPress 3 to search for a task\nPress 4 to view all tasks\nPress 5 to exit\nEnter choice: '))
        while choice != 5:
            try:
                if choice == 1:
                    s = input('Enter task you want to add: ')
                    t.add_task(s)
                    print('Task added to queue')

                elif choice == 2:
                    s = input('Enter the task you want to delete: ')
                    t.del_task(s)
                    print('Task deleted from queue')
                
                elif choice == 3:
                    s = input('Enter the task you want to search for: ')
                    t.search_task(s)
                    print('Task is present in queue')  

                elif choice == 4:
                    print('Following tasks are left: ')
                    t.print_tasks()

            except Exception as e:
                        print(e) 
                
            choice = int(input('\n\nPress 1 to add a task\nPress 2 to delete a task\nPress 3 to search for a task\nPress 4 to view all tasks\nPress 5 to exit\nEnter choice: '))

        print('Thank you for using Task Manager')

    except:
        print('Wrong choice, program terminated')
 