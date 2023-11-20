# SDLang

StartupDayLang is a language developed to analyse the day of multiple squads inside a startup company.

## EBNF

```
STRUCTURE = "START_SPRINT", PROGRAM , "END_SPRINT"

PROGRAM = { STATEMENT }

STATEMENT = CONDITIONAL | LOOP | CHANGE_STATUS | NEW_TASK | LINK | ASSIGNMENT

BLOCK = "{", { STATEMENT }, "}";

CONDITIONAL = "if", "(" BOOLEAN_EXPRESSION, [{"and" | "or", BOOLEAN_EXPRESSION}] ")", BLOCK, [ "else", "{", BLOCK, "}," ];

LOOP = "for", IDENTIFIER, "in tasks from", IDENTIFIER, BLOCK

CHANGE_STATUS = "set", STRING, "from", IDENTIFIER, "to", TASK_STATUS

NEW_TASK = "task", STRING, "to", IDENTIFIER, "is", TASK_STATUS, "has priority", NUMBER

LINK = IDENTIFIER, "add" | "remove", IDENTIFIER

ASSIGNMENT = IDENTIFIER_TYPE, IDENTIFIER

TASK_PROP = IDENTIFIER, ".", TASK_OPTION

TASK_OPTION = ( "name" | "owner" | "status", "priority")

BOOLEAN_EXPRESSION = TASK_PROP | NUMBER, ("==", | "!=", "<", ">" , "<=" , ">=" ), STRING | TASK_STATUS | NUMBER;

IDENTIFIER = LETTER, { LETTER | DIGIT | "_" };

TASK_STATUS = ( "to-do" | "doing" | "done" );

IDENTIFIER_TYPE = ( "squad" | "employee");

NUMBER = DIGIT, { DIGIT }

LETTER = ( a | ... | z | A | ... | Z ) ;

DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 );

STRING = '"', {LETTER}+, '"'
```

## Example

```
START_SPRINT

# Entities

squad Website
squad AI

employee Rodrigo
employee Joao
employee Marcos
employee Pedro


# Link employee to squad

Website add Rodrigo
Website add Joao

AI add Rodrigo
AI add Marcos
AI add Pedro
AI remove Rodrigo


# Tasks

task "Start front-page" to Rodrigo is "to-do"
task "Start backend" to Joao is "to-do"

task "Create model" to Marcos is "to-do"
task "Clean data" to Pedro is "to-do"


# Status
set "Develop front-page" from Rodrigo to "done"
set "Develop backend" from Joao to "doing"


# Loop and conditional
for task in tasks from Rodrigo {
  if (task.name == "Develop front-page") {
    if (task.status == "done") {
      print(task.owner + " ended " + task.name)
      task "Deploy website" to Rodrigo is "to-do"
    }
    else {
      print(task.owner + " is late on " + task.name)
    }
  }
}

END_SPRINT
```