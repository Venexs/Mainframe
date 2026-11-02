# Mainframe

A Python-based terminal application built around the idea of having your own workspace. Users can create Mainframes, organise folders, manage access, and communicate through an internal mail system.

This started as a school project and gradually became a side project where I experiment with things I've learned along the way.

## Features

- **User Accounts** — Sign up and log in with a user account.
- **Mainframes** — Create and manage separate workspaces, each with its own name, description, and colour theme.
- **Folder Management** — Create folders and organise files within a Mainframe.
- **Access Levels** — Mainframe members can be assigned different roles, including Normal, Manager, and Admin.
- **Internal Mail** — Send and receive messages, including Mainframe invitations.
- **User Settings** — Change account settings and configure the main data folder.

## Installation

You'll need Python installed on Windows.

Install the required packages:

```bash
pip install colorama pillow
```

Tkinter is also required for file selection. It is included with most standard Windows Python installations.

## Usage

Clone or download the repository, then run:

```bash
python main.py
```

Alternatively, run `Mainframe.bat` from the project folder.

After starting the program, sign up or log in. You can use the available menu options to navigate through the application.

## Project Structure

```text
Mainframe/
├── Files/
├── Mainframes/
├── main.py
├── MainframeTemplate.py
├── Mainframe.bat
└── Icon.ico
```

- `main.py` handles account access and the Mainframe selection screen.
- `MainframeTemplate.py` contains the workspace, folder, mail, and settings functions.
- `Files/` stores account and application data.
- `Mainframes/` stores workspace information and folders.

## Notes

This is an ongoing personal project. Some features may be incomplete or have bugs, and the code is still being developed.

The application currently uses local files for its data storage. It is not a networked client-server application.

