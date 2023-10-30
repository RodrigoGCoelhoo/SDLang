# SDLang

StartupDayLang is a language developed to analyse the day of multiple squads inside a startup company.

## EBNF

```
PROGRAM = (DAY, "/", MONTH, "/", YEAR), BLOCK, "end";

BLOCK = "{", { STATEMENT, "," }, "}";

EMPLOYEE_STATEMENT = "for", EMPLOYEE, "in", SQUAD;

FUNCTIONS_DECLARATION = "IDENTIFIER(ARGUMENT, { ARGUMENT }) {TASKS_STATEMENTS};"

ARGUMENT = IDENTIFIER | DIGIT | BOOLEAN | ANY;

CONDITIONAL = "if", "(" BOOLEAN_EXPRESSION, ")", "{", BLOCK, "},", [ "else", "{", BLOCK, "}," ];

VARIABLES_DECLARATION = IDENTIFIER, ":", IDENTIFIER_TYPE, "is a", EMPLOYEE_ROLE, "part of", IDENTIFIER;

DAY = DIGIT, { DIGIT };

MONTH = DIGIT, { DIGIT };

YEAR = DIGIT, DIGIT, DIGIT, DIGIT;

BOOLEAN_EXPRESSION = IDENTIFIER, ("==", | "!=", | ">", | "<", | ">=", | "<="), IDENTIFIER;

ARITHMETIC_EXPRESSION = EXPRESSION, ("+", | "-", | "*", | "/"), EXPRESSION;

IDENTIFIER = LETTER, { LETTER | DIGIT | "_" };

TASK_TYPE = ( "development" | "management" | "design" | "test" | "sales" );

EMPLOYEE_ROLE = ( "developer" | "manager" | "designer" | "tester" | "seller" );

TASK_STATUS = ( "to-do" | "doing" | "done" );

IDENTIFIER_TYPE = ( "squad" | "employee" | "company");

NUMBER = DIGIT, { DIGIT } ;

LETTER = ( a | ... | z | A | ... | Z ) ;

DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 );
```