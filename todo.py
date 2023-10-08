import tkinter
import tkinter.messagebox
import pickle

root = tkinter.Tk()
root.title("To Do List")

def add_task():
    task = user_input.get()

    if (task.replace(' ','') != ""):
        listbox_tasks.insert(tkinter.END, task)
        user_input.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title = "Warning!", message = "Taskbar is empty. Please enter a task.")

def delete_task():
    try:
        task_index = listbox_tasks.curselection()
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title = "Warning!", message = "No task selected to delete.")

def delete_all_tasks():
    listbox_tasks.delete(0,tkinter.END)

def load_tasks():
    try:
        if(listbox_tasks.get(0) == ""):
            tasks = pickle.load(open("tasks.dat", "rb"))
            for task in tasks:
                listbox_tasks.insert(tkinter.END, task)
        else:
            tkinter.messagebox.showwarning(title = "Warning!", message = "There are still tasks in the ListBox.")
    except:
        tkinter.messagebox.showwarning(title = "Warning!", message = "No save file located.")

def save_tasks():
    tasks = listbox_tasks.get(0,listbox_tasks.size())
    pickle.dump(tasks, open("tasks.dat","wb"))

#GUI
frame_task = tkinter.Frame(root)
frame_task.pack()

task_scrollbar = tkinter.Scrollbar(frame_task)
task_scrollbar.pack(side = tkinter.RIGHT, fill = tkinter.Y)

listbox_tasks = tkinter.Listbox(frame_task, height = 10, width = 50)
listbox_tasks.pack()

listbox_tasks.config(yscrollcommand=task_scrollbar.set)
task_scrollbar.config(command=listbox_tasks.yview)

user_input = tkinter.Entry(root, width = 50)
user_input.pack()

add_task_button = tkinter.Button(root, text = "Add Task", width = 43, command = add_task)
add_task_button.pack()

delete_task_button = tkinter.Button(root, text = "Delete Task", width = 43, command = delete_task)
delete_task_button.pack()

delete_all_tasks_button = tkinter.Button(root, text = "Delete All Tasks", width = 43, command = delete_all_tasks)
delete_all_tasks_button.pack()

load_tasks_button = tkinter.Button(root, text = "Load Tasks", width = 43, command = load_tasks)
load_tasks_button.pack()

save_tasks_button = tkinter.Button(root, text = "Save Tasks", width = 43, command = save_tasks)
save_tasks_button.pack()




root.mainloop()