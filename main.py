# import the tkinter library
import tkinter as tk
from tkinter import Tk
from tkinter import messagebox

# import the functions from the other file
from program_manager import load_tasks_json, save_tasks_json

# read the json file and store the data in a python list
list_of_tasks = load_tasks_json()


# this function gets the index of an item in the list_box
def get_item_index():
    # get a tuple of the selected items
    task_index_tuple = listbox_tasks.curselection()
    if not task_index_tuple:
        messagebox.showwarning(title="Warning!",
                               message="You must Select a task")
        # returns nothing to exit the function because an error happened
        return
    # return the index if no error happened
    return task_index_tuple[0]


# this function add tasks to the list_box and saves the new task to the json file
def add_task():
    # get the task from the entry box
    task_name = entry_task.get()
    # make sure the task is not an empty string
    if task_name.strip() == "":
        messagebox.showwarning(title="Warning!",
                               message="You must enter a task")
        # return nothing and exit the function because an error happened
        return

    # Add the task to the list box
    listbox_tasks.insert(tk.END, task_name + " - Not Done")
    # clear the entry box
    entry_task.delete(0, tk.END)

    # add the task to the list of tasks
    list_of_tasks.append({"task_name": task_name, "is_task_done": False})

    # update the json file
    save_tasks_json(list_of_tasks)


# this function marks a task as complete in the list_box and the json file
def mark_task_as_done():

    # get index of the selected task
    task_index = get_item_index()
    # when the function return nothing it actually returns the value None so this means an error happened so we can just exit the function
    if task_index == None: return
    # mark the task as done
    list_of_tasks[task_index]['is_task_done'] = True
    # get the task's name
    task_name = listbox_tasks.get(task_index)
    # delete the task from the list box
    listbox_tasks.delete(task_index)
    # replace "Not " with an empty string in the task name and insert it in the same position as the task originally was
    listbox_tasks.insert(task_index, task_name.replace("Not ", ""))
    # update the json file
    save_tasks_json(list_of_tasks)


# this function deletes a task from the list box and from the json file
def delete_task():
    """
    # get a tuple of the selected items
    task_index_tuple = listbox_tasks.curselection()
    if not task_index_tuple:
        messagebox.showwarning(title="Warning!", message="You must Select a task")
    else:
        listbox_tasks.delete(task_index_tuple[0])
        list_of_tasks.pop(task_index_tuple[0])
        save_tasks_json(list_of_tasks)
    """
    # get index of the selected task
    task_index = get_item_index()
    # when the function return nothing it actually returns the value None so this means an error happened so we can just exit the function
    if task_index == None: return
    # delete the item from the
    listbox_tasks.delete(task_index)
    # delete the item from the list of tasks
    list_of_tasks.pop(task_index)
    # update the json file
    save_tasks_json(list_of_tasks)


# this function
def populate_list_box():
    for task in list_of_tasks:
        if task["is_task_done"]:
            task_status = "Done"
        else:
            task_status = "Not Done"
        listbox_tasks.insert(tk.END, f"{task['task_name']} - {task_status}")


# create the app
root = Tk()

# give the app a name
root.title("To Do List")

# create a frame
frame_tasks = tk.Frame()
frame_tasks.pack()

# create a list box inside the frame
listbox_tasks = tk.Listbox(frame_tasks, height=10, width=50)
listbox_tasks.pack(side='left')

# create a scroll bar for to scroll through the list box
scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side='right', fill='y')

# configure the scroll bar and the listbox
listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

# create an entry text box
entry_task = tk.Entry(root, width=50)
entry_task.pack()

# Create Buttons
# make a add task button and assign add_task function to it
add_task_button = tk.Button(root,
                            text="Add task",
                            width="48",
                            command=add_task)
add_task_button.pack()

# make a mark task as done button and assign mark_task_as_done function to it
mark_task_as_done_button = tk.Button(root,
                                     text="Mark task as Done",
                                     width="48",
                                     command=mark_task_as_done)
mark_task_as_done_button.pack()

# make a delete task button and assign delete_task function to it
delete_task_button = tk.Button(root,
                               text="Delete task",
                               width="48",
                               command=delete_task)
delete_task_button.pack()

# finally populate the list box with the info from the json file
populate_list_box()
root.mainloop()
