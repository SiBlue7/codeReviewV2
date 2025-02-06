# Project Code Review

## Introduction

This project is designed to automate the code review process for any projects. It analyzes the codebase and provides feedback on code quality, style, and potential issues.

## Features

- TODO : à compléter

## Installation

To install the project, clone the repository and install the required dependencies:

```bash
git clone https://github.com/yourusername/codeReviewV2.git
cd codeReviewV2
pip install -r requirements.txt
```

## Usage

To run the code review, you need to change the config.json file and execute the following command:

```bash
python main.py
```

## Documentation

Documention is made with [Sphinx](https://www.sphinx-doc.org/en/master/index.html)

If you want to run the documentation, go to docs folder using :

```bash
cd path_to_docs_folder
```

If the .rst file are missing in the source folder use the following command to generate them :

```bash
sphinx-apidoc -o source/ project_path
```

Then use the following command to build the documentation file :

1. On windows

```bash
.\make.bat html
```

2. On linux/mac

```bash
make html
```

## Error

- If you get the error [WinError 3] Le chemin d’accès spécifié est introuvable try the following steps from [StackOverflow](https://stackoverflow.com/questions/29557760/long-paths-in-python-on-windows) :

```
Just Follow my steps and long path will be enabled.

1.Open start menu and search for "Registry Editor"

2."Run as Administrator" and click "yes"

3.Export The Backup. Click the file option on the top left corner and Export the backup of the Registry Data in a the file of you choice.(Done)

4.Now Expend the "HKEY_LOCAL_MACHINE" Folder

5.Expend "System" Folder.

6.Expend "CurrentControlSet" Folder.

7.Expend "Control" Folder.

8.Expend "FileSystem" Folder.

9.You see a list of files in "FileSystem" Folder.

10.Find "LongPathEnabled" File and double click on it.

11.Change the data "Value Data" from 0 to 1 and click OK.

Now Your long Path Is Enabled. Congratulations
```
