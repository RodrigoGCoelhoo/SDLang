%{
#include <stdio.h>
#include <stdlib.h>
#include "f1.tab.h"
extern int yywrap();
int is_identified = 0;
%}

%{
#define YYEOF 0
%}

%%
"\n"                            { return NEWLINE; }
"START_SPRINT"                  { printf("START_SPRINT: %s \n", yytext); return START_SPRINT; }
"END_SPRINT"                    { printf("END_SPRINT: %s \n", yytext); return END_SPRINT; }
"if"                            { printf("IF: %s \n", yytext); return IF; }
"else"                          { printf("ELSE: %s \n", yytext); return ELSE; }
"for"                           { printf("FOR: %s \n", yytext); return FOR; }
"set"                           { printf("SET: %s \n", yytext); return SET; }
"to"                            { printf("TO: %s \n", yytext); return TO; }
"from"                          { printf("FROM: %s \n", yytext); return FROM; }
"task"                          { printf("TASK: %s \n", yytext); return TASK; }
"is"                            { printf("IS: %s \n", yytext); return IS; }
"add"                           { printf("ADD: %s \n", yytext); return ADD; }
"remove"                        { printf("REMOVE: %s \n", yytext); return REMOVE; }
"in tasks from"                 { printf("IN_TASKS_FROM: %s \n", yytext); return IN_TASKS_FROM; }
"has_priority"                  { printf("HAS_PRIORITY: %s \n", yytext); return HAS_PRIORITY; }
"name|owner|status|priority"    { printf("TASK_OPTION: %s \n", yytext); return TASK_OPTION; }
"to-do|doing|done"              { printf("TASK_STATUS: %s \n", yytext); return TASK_STATUS; }
"squad|employee"                { printf("IDENTIFIER_TYPE: %s \n", yytext); return IDENTIFIER_TYPE; }

"."                             { printf("DOT: %s \n", yytext); return DOT; }
","                             { printf("COMMA: %s \n", yytext); return COMMA; }
"("                             { printf("OPEN_PARENTHESIS: %s \n", yytext); return OPEN_PARENTHESIS; }
")"                             { printf("CLOSE_PARENTHESIS: %s \n", yytext); return CLOSE_PARENTHESIS; }
"{"                             { printf("OPEN_BRACES: %s \n", yytext); return OPEN_BRACES; }
"}"                             { printf("CLOSE_BRACES: %s \n", yytext); return CLOSE_BRACES; }
"["                             { printf("OPEN_BRACKETS: %s \n", yytext); return OPEN_BRACKETS; }
"]"                             { printf("CLOSE_BRACKETS: %s \n", yytext); return CLOSE_BRACKETS; }

[a-zA-Z]+                       { printf("STRING: %s \n", yytext); return STRING; }
[0-9]+                          { printf("CONUMBERMMA: %s \n", yytext); return NUMBER; }
[a-zA-Z0-9_]+                   { printf("IDENTIFIER: %s \n", yytext); return IDENTIFIER; }
%%
