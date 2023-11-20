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
