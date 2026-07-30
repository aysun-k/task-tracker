# Task Tracker CLI

A command line task management application written in Python.

## Features

- Add tasks
- Update tasks
- Delete tasks
- Mark tasks as in-progress
- Mark tasks as done
- List all tasks
- Filter tasks by status

## Available Commands

Add a task:

task-cli add "Buy groceries"

Update a task:

task-cli update 1 "Buy groceries and cook dinner"

Delete a task:

task-cli delete 1

Mark a task as in-progress:

task-cli mark-in-progress 1

Mark a task as done:

task-cli mark-done 1

List all tasks:

task-cli list

List completed tasks:

task-cli list done

List unfinished tasks:

task-cli list todo

List in-progress tasks:

task-cli list in-progress

## Project Structure

task-tracker/
│
├── src/
│   └── main.py
│
├── README.md
└── .gitignore

## Data Storage

Tasks will be stored locally in a JSON file.

## Technologies

- Python
- JSON
- Command Line Interface (CLI)