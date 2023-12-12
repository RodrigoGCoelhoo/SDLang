# Sprint
Author: Rodrigo Guimarães Coelho

Sprint is a language developed to manage the day of multiple squads inside a Startup. With this language you can create squads, add employees, create tasks and trigger new tasks based on task states.

[Presentation](https://www.canva.com/design/DAF2wo-a-M8/EI4QroQKJXPqn08d_lG5IQ/view?utm_content=DAF2wo-a-M8&utm_campaign=designshare&utm_medium=link&utm_source=editor#8)

## Summary
1. [EBNF](#ebnf)
2. [Example code](#example-code)
3. [How to run it?](#how-to-run-it)
4. [Outputs](#outputs)

## EBNF

```
STRUCTURE = "START_SPRINT", PROGRAM , "END_SPRINT"

PROGRAM = { STATEMENT }

STATEMENT = CONDITIONAL | LOOP | CHANGE_STATUS | NEW_TASK | LINK | ASSIGNMENT

BLOCK = "{", { STATEMENT }, "}";

CONDITIONAL = "if", "(" BOOLEAN_EXPRESSION, [{"and" | "or", BOOLEAN_EXPRESSION}] ")", BLOCK, [ "else", "{", BLOCK, "}," ];

LOOP = "for", IDENTIFIER, "in tasks from", IDENTIFIER, BLOCK

CHANGE_STATUS = "set", STRING, "from", IDENTIFIER, "to", TASK_STATUS

NEW_TASK = "task", STRING, "to", IDENTIFIER, "on", IDENTIFIER, "is", TASK_STATUS

LINK = IDENTIFIER, "add" | "remove", IDENTIFIER

ASSIGNMENT = IDENTIFIER_TYPE, IDENTIFIER

TASK_PROP = IDENTIFIER, ".", TASK_OPTION

TASK_OPTION = ( "name" | "owner" | "status")

BOOLEAN_EXPRESSION = TASK_PROP | NUMBER, ("==", | "!=", "<", ">" , "<=" , ">=" ), STRING | TASK_STATUS | NUMBER;

IDENTIFIER = LETTER, { LETTER | DIGIT | "_" };

TASK_STATUS = ( "to-do" | "doing" | "done" );

IDENTIFIER_TYPE = ( "squad" | "employee");

NUMBER = DIGIT, { DIGIT }

LETTER = ( a | ... | z | A | ... | Z ) ;

DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 );

STRING = '"', {LETTER}+, '"'
```

## Example code

For the following example we are creating 2 squads, allocating 4 employees and adding a single task for each employee. After the setup phase we change the status of 2 tasks and then we iterate over all tasks from a specific employee to check if he has ended or not its task. If yes, we then add another task.

```
START_SPRINT

// Entities

squad Website
squad AI

employee Rodrigo
employee Joao
employee Marcos
employee Pedro


// Link employee to squad

Website add Rodrigo
Website add Joao

AI add Rodrigo
AI add Marcos
AI add Pedro
AI remove Rodrigo


// Tasks

task "Start front-page" to Rodrigo on Website is "TODO"
task "Start backend" to Joao on Website is "TODO"

task "Create model" to Marcos on AI is "TODO"
task "Clean data" to Pedro on AI is "TODO"


// Status
set "Start front-page" from Rodrigo on Website to "DONE"
set "Start backend" from Joao on Website to "DOING"


// Loop
for t in tasks from Rodrigo {
  if (t.name == "Develop front-page") {
    if (t.status == "DONE") {
      print(t.owner + " ended '" + t.name + "'")
      task "Deploy website" to Rodrigo on Website is "TODO"
    }
  }
}

END_SPRINT
```

## How to run it?
1. Create a file with extension ```.sprint``` inside ```compiler``` folder
2. Run inside ```compiler``` folder:
```
  python main.py ./[YOUR_FILE_NAME].sprint
```
- You can pass the flag ```-v``` or ```--verbose```  to have a more verbose output

## Outputs
For the example code, here you can check the two different outputs.
```
# Regular

Rodrigo ended 'Start front-page'
```

```
# Verbose

Sprint started

Created squad 'Website'
Created squad 'AI'
Created employee 'Rodrigo'
Created employee 'Joao'
Created employee 'Marcos'
Created employee 'Pedro'
Added employee 'Rodrigo' to squad 'Website'
Added employee 'Joao' to squad 'Website'
Added employee 'Rodrigo' to squad 'AI'
Added employee 'Marcos' to squad 'AI'
Added employee 'Pedro' to squad 'AI'
Removed employee 'Rodrigo' from squad 'AI'
Created task 'Start front-page' for employee 'Rodrigo' in squad 'Website' with status 'TODO'
Created task 'Start backend' for employee 'Joao' in squad 'Website' with status 'TODO'
Created task 'Create model' for employee 'Marcos' in squad 'AI' with status 'TODO'
Created task 'Clean data' for employee 'Pedro' in squad 'AI' with status 'TODO'
Updated task 'Start front-page' from 'Rodrigo' in squad 'Website' to status 'DONE'
Updated task 'Start backend' from 'Joao' in squad 'Website' to status 'DOING'
Rodrigo ended 'Start front-page'
Created task 'Deploy website' for employee 'Rodrigo' in squad 'Website' with status 'TODO'

Sprint ended
```