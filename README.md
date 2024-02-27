# eParser

eParser is a Python utility library for managing and converting eBooks into text. It provides fast access to eBook metadata and text contents, allowing you to create and store eBook objects.

## Installation

You can install eParser using pip: (not yet uploaded)

```
pip install eparser
```

## eBook Object

The eBook object is a dictionary with the following format:

```py
{
  Title: "Lord of the Mysteries",
  Author: "Cuttlefish That Loves Diving",
  Description: "Waking up to be faced with a string of mysteries...",
  Genres: ["Action", "Adventure", "Drama", "Fantasy", "Historical", "Horror", "Mature", "Mystery", "Psychological", "Seinen", "Supernatural"],
  Chapters: {
    1: "Chapter 1: In the beginning..."",
    2: ...
  }
}
```

## Usage

The library has two main functions:

```get_ebook()``` which creates an eBook based on the given ePUB.

```py
import eparser 

# File path leading to the ePUB File
epub_file_path = "some/path.epub"

# Name for the extraction folder
ebook_name = "New eBook"

# Create an eBook
eBook = eparser.get_ebook(epub_file_path, ebook_name)

# Get metadata or book contents
print(eBook.get_title())

# Obtain first chapter
print(eBook.get_chapter(1))

# Specify the directory for the extraction -- default set to current directory
out_directory = "some/other/directory"
eBook = eparser.get_ebook(epub_file_path, ebook_name, out_directory)
```

```process_epub()``` which extracts the contents of an ePUB and provides a list of chapter filenames, as well as the ```content.opf```. It also provides the path to the extraction folder and the path to the ```content.opf``` file.

```py
# Path to ePUB
epub_file_path = "some/path.epub"

# Name of the extraction folder
folder_name = "Fire"

# OPTIONAL: Out directory for extraction folder -- initialized to current directory
out_directory = "some/directory/"

# Process ePUB
filenames, folder_path, opf_path = process_epub(epub_file_path, folder_name, out_directory)
```

You can also manually set eBook metadata and contents:

```py
# Set eBook title, author, description, and genres
title = "New Title"
author = "Author"
description = "Description for the eBook"
genres = ["Action", "Thriller", "Drama", "English"]
eBook.set_title(title)
eBook.set_author(author)
eBook.set_description(description)
eBook.set_genres(genres)
```

## Note

Any ePUB used must be of Standard or OEBPS format.

## Todo

The parsing and extraction functions no longer differentiates between Standard and OEBPS. 

Add a utility function that converts the eBook to JSON or YAML.

