# Mainframe

A command-line collaboration and group-management system built with Python.

Mainframe started as a school project and gradually developed into a larger personal project. It explores how a centralised workspace could handle multiple users, groups, shared files, communication and project organisation through a terminal-based interface.

## Features

- **User Accounts** — Sign-up, login, account profiles and user settings.
- **Groups** — Create and manage groups, assign administrative roles, invite members and organise shared workspaces.
- **File Management** — Create folders and organise files within group workspaces.
- **Mail System** — Send and receive messages through an internal inbox and outbox.
- **Contracts** — Create and manage group-related contracts.
- **Project Timeline** — Visualise and organise project schedules and assigned work.
- **User Profiles** — Maintain user information and account preferences.
- **Access Control** — Different permissions for group owners, administrators and members.

## Installation

Mainframe requires Python and Colorama.

```bash
pip install colorama
```

Tkinter is also required for file-dialog functionality. It is included with most standard Python installations.

## Usage

Clone the repository:

```bash
git clone https://github.com/Venexs/Mainframe.git
cd Mainframe
```

Run the program:

```bash
python main.py
```

On Windows, you can alternatively launch `Main.bat`.

After starting the program, log in or create an account. Enter `?` or `Help` to view the available commands.

## Project Structure

```text
Mainframe/
│
├── main.py
├── test.py
├── Main.bat
├── format.txt
│
├── Client/
│   ├── Files/
│   │   ├── Logins/
│   │   ├── Userpref/
│   │   └── Ver_control.csv
│   └── PerLog/
│
├── Server/
│   ├── Main Files/
│   │   ├── userdata.csv
│   │   └── Ver_control.csv
│   ├── Open Files/
│   └── Mainframe.csv
│
└── README.md
```

## Technical Details

| Component | Technology |
|---|---|
| Language | Python |
| Interface | Command-line |
| Terminal styling | Colorama |
| Data storage | CSV and Pickle |
| File selection | Tkinter |
| File operations | Python standard library |

## Development

Mainframe is an ongoing personal project. New features and improvements are added as I learn and experiment with different programming concepts.

Contributions and suggestions are welcome. For larger changes, please open an issue before submitting a pull request.
