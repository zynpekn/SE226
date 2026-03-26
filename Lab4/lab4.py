tasks = {}
x =  int ( input ( 'Pleas enter the number of tasks: '))

for a in range ( 0 , x ) :
    name = input ( ' Please enter a task name: ')
    numberOfDependencies = int ( input ( 'How many dependencies for ' + name + '? '))
    dependencies = [] 

    for i in range ( numberOfDependencies ) :
        dep = ( input("Enter dependency " + str (i+1) + " :" ))
        dependencies.append(dep)

    tasks[name] = dependencies 


print("Task Structure:")
for task,dependencies in tasks.items():
    print (str(task) + '->'+str( dependencies))


print("Task with no dependencies")
initial_tasks = [task for task , dependencies in tasks.items if len(dependencies)==0]
if initial_tasks:
    for t in initial_tasks:
        print (t)
else :
    print ("None")


completed = set()
execution_order = []

print ("Execution Order: ")
step = 1 

while len(completed < len(tasks)):
    progress= False 
    for task , dependencies in tasks.items() :
        if task not in completed and all ( dep in completed for dep in dependencies):
            execution_order.append(task)
            completed.add(task)
            print("Step " + step + " task " + task )
            step+=1
            progress = True

    if not progress :
        print( "No task can be started.")
        print("Error, Circular dependency detected.")
        print("These tasks could not be completed.")

        for task in tasks:
            if task not in completed:
                print (task )
            break 

if len(completed) == len(tasks):
    print ("All tasks completed.") 


