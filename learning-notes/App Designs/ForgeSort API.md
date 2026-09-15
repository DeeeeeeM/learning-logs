# ForgeSort API — Backend Development Task

## Objective

Build a FastAPI backend for ForgeSort that exposes the existing Smart Organizer and Duplicate Reporter core logic through HTTP endpoints.

The API should not contain the file-processing algorithms themselves. It should validate requests, call the existing ForgeSort core functions, and return structured JSON responses.

---

## Phase 1 — Create the FastAPI application

### Task

Create the basic API application and confirm it runs successfully.

### Requirements

- Create the FastAPI app.
    
- Add a simple root or health endpoint.
    
- Run the application locally.
    
- Confirm the automatically generated API documentation works.
    

### Expected result

The server starts successfully and you can open the FastAPI Swagger documentation.

### Learn

- FastAPI application setup
    
- route decorators
    
- GET endpoints
    
- development server
    

Docs:  
[https://fastapi.tiangolo.com/tutorial/first-steps/](https://fastapi.tiangolo.com/tutorial/first-steps/)

---

# Phase 2 — Create the request schema

## Task

Create a request model that accepts a folder path.

The API needs to receive something conceptually like:

folder_path → path to the directory ForgeSort should process

### Requirements

Create a Pydantic model for requests containing:

- folder path
    

For now, both Organizer and Duplicate Reporter may reuse the same basic folder request model.

### Questions your API should eventually answer

- Was a folder path provided?
    
- Does the path exist?
    
- Is the path actually a directory?
    
- Can ForgeSort access it?
    

### Learn

- Pydantic BaseModel
    
- request bodies
    
- field types
    
- validation
    

Docs:  
[https://fastapi.tiangolo.com/tutorial/body/](https://fastapi.tiangolo.com/tutorial/body/)

---

# Phase 3 — Validate folder input

## Task

Prevent invalid paths from reaching the ForgeSort core.

### Requirements

Before running an operation:

CHECK folder path

IF path does not exist  
return an appropriate error

IF path exists but is not a directory  
return an appropriate error

OTHERWISE  
continue

### Expected API behavior

Invalid request:

folder_path → nonexistent folder

Response conceptually:

error  
folder does not exist

Another invalid request:

folder_path → file instead of directory

Response:

error  
path must be a directory

### Learn

- HTTPException
    
- HTTP status codes
    
- Path.exists()
    
    - Path.is_dir()
        

Docs:  
[https://fastapi.tiangolo.com/tutorial/handling-errors/](https://fastapi.tiangolo.com/tutorial/handling-errors/)

---

# Phase 4 — Build the Duplicate Reporter endpoint

## Task

Create the first real ForgeSort endpoint.

Recommended endpoint:

POST /duplicates

### Request

folder_path

### Backend flow

RECEIVE request  
↓  
validate folder  
↓  
scan_files(folder)  
↓  
check_duplicate(files)  
↓  
convert result into API response  
↓  
return JSON

### Important

Do not rewrite duplicate detection inside the API.

The API should call your existing functions.

Conceptually:

API layer  
↓  
scan_files()  
↓  
check_duplicate()

---

# Phase 5 — Preserve duplicate groups

## Task

Keep duplicate files grouped by matching content.

Your core currently produces groups conceptually like:

[  
[file A, file B],  
[file C, file D, file E]  
]

Do not flatten this inside the core.

### Why

The API needs to know:

Group 1  
file A  
file B

Group 2  
file C  
file D  
file E

Otherwise it cannot tell which files match each other.

---

# Phase 6 — Create Duplicate Reporter response schemas

## Task

Create structured response models.

Suggested structure:

DuplicateFile  
name  
path  
size

DuplicateGroup  
files  
file_count  
size

DuplicateScanResponse  
scanned_files  
duplicate_group_count  
duplicate_file_count  
groups

### Example conceptual response

scanned_files: 120

duplicate_group_count: 2

duplicate_file_count: 5

groups:

```
Group 1
    size: 2 MB

    files:
        photo.jpg
        photo_copy.jpg

Group 2
    size: 5 MB

    files:
        video.mp4
        video_copy.mp4
        video_backup.mp4
```

### Learn

- nested Pydantic models
    
- response_model
    
- lists of models
    

Docs:  
[https://fastapi.tiangolo.com/tutorial/response-model/](https://fastapi.tiangolo.com/tutorial/response-model/)

---

# Phase 7 — Calculate duplicate statistics

## Task

Add useful reporting information.

### Add

- number of files scanned
    
- number of duplicate groups
    
- number of files involved in duplicate groups
    
- file size per group
    

Later:

- wasted disk space
    

### Wasted-space concept

Suppose:

3 identical files  
each 100 MB

Only one copy is necessary.

Potential wasted space:

2 × 100 MB  
= 200 MB

Conceptually:

# wasted space

(group file count - 1)  
×  
file size

Do this later, after the basic endpoint works.

---

# Phase 8 — Build the Organizer endpoint

## Task

Expose the Smart Organizer.

Recommended endpoint:

POST /organize

### Request

folder_path

### Backend flow

RECEIVE folder  
↓  
validate folder  
↓  
scan_files(folder)  
↓  
organize_files(files, folder)  
↓  
return operation result

### Important difference

Unlike the Duplicate Reporter, this endpoint modifies the filesystem.

Because of that, treat it more carefully.

---

# Phase 9 — Improve organizer core return values

## Task

Your current organizer mainly performs actions.

For an API, you will eventually want the core to return information about what happened.

Conceptually:

OrganizerResult

files_scanned  
files_moved  
files_skipped  
operations

Each operation could contain:

original path  
destination path  
category  
status

Possible statuses:

moved  
skipped  
failed

Do not build all of this immediately.

Start with counts.

---

# Phase 10 — Add a preview / dry-run organizer endpoint

## Task

Before allowing file movement through an API, add a safer preview mode.

Conceptually:

POST /organize/preview

Flow:

scan files  
↓  
classify files  
↓  
calculate destinations  
↓  
DO NOT move anything  
↓  
return planned operations

Example response:

photo.jpg  
→ Images/photo.jpg

report.pdf  
→ Documents/report.pdf

song.mp3  
→ Audio/song.mp3

### Why this is valuable

It separates:

planning

from:

executing

That is a very useful backend design pattern for filesystem applications.

---

# Phase 11 — Handle file conflicts

## Task

Define API behavior when the destination already exists.

For v1:

IF destination exists  
skip file

Return that information in the response.

Conceptually:

file:  
photo.jpg

status:  
skipped

reason:  
destination already exists

Do not silently ignore conflicts.

---

# Phase 12 — Standardize API errors

## Task

Make errors predictable.

Examples:

400  
invalid request

404  
folder does not exist

409  
file conflict, if you later decide conflicts should block operations

500  
unexpected server-side failure

Keep error messages understandable.

Do not expose internal tracebacks to API users.

---

# Phase 13 — Test the Duplicate Reporter API

## Required test cases

### Test 1

Valid folder with no duplicates

Expected:  
empty duplicate groups

### Test 2

Two identical files

Expected:  
one duplicate group

### Test 3

Three identical files

Expected:  
one group containing three files

### Test 4

Same file size but different contents

Expected:  
not duplicates

### Test 5

Invalid folder

Expected:  
appropriate API error

### Test 6

File path supplied instead of directory

Expected:  
appropriate API error

---

# Phase 14 — Test the Organizer API

## Required test cases

### Test 1

Normal mixed files

Expected:  
files moved into correct categories

### Test 2

Unknown extension

Expected:  
Other Files

### Test 3

Destination folder already exists

Expected:  
folder reused

### Test 4

Destination file already exists

Expected:  
skip

### Test 5

Empty folder

Expected:  
successful response with zero processed files

---

# Phase 15 — Keep the architecture separated

The final architecture should conceptually look like:

ForgeSort Core

```
scan_files
organize_files
calculate_hash
check_duplicate

    ↓
```

ForgeSort API

```
validation
request models
response models
HTTP errors
routes

    ↓
```

Clients

```
CLI
PySide6
external API client
```

The FastAPI layer should never become the place where the actual duplicate or organizer algorithms live.

---

# Recommended build order

1. FastAPI app starts
    
2. Request model
    
3. Path validation
    
4. POST /duplicates
    
5. Duplicate response model
    
6. Duplicate statistics
    
7. API tests
    
8. POST /organize/preview
    
9. POST /organize
    
10. Organizer response structure
    
11. Conflict reporting
    
12. Organizer API tests
    
13. Error cleanup
    
14. API documentation cleanup
    

Do not build authentication, databases, Docker, async workers, deployment, or PySide6 integration yet.

Get these two APIs working cleanly first.