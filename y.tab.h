/* A Bison parser, made by GNU Bison 2.3.  */

/* Skeleton interface for Bison's Yacc-like parsers in C

   Copyright (C) 1984, 1989, 1990, 2000, 2001, 2002, 2003, 2004, 2005, 2006
   Free Software Foundation, Inc.

   This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 2, or (at your option)
   any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program; if not, write to the Free Software
   Foundation, Inc., 51 Franklin Street, Fifth Floor,
   Boston, MA 02110-1301, USA.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* Tokens.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
   /* Put the tokens into the symbol table, so that GDB and other debuggers
      know about them.  */
   enum yytokentype {
     START_SPRINT = 258,
     END_SPRINT = 259,
     NEWLINE = 260,
     IF = 261,
     ELSE = 262,
     FOR = 263,
     SET = 264,
     TO = 265,
     FROM = 266,
     IS = 267,
     TASK = 268,
     ADD = 269,
     REMOVE = 270,
     IN_TASKS_FROM = 271,
     HAS_PRIORITY = 272,
     TASK_OPTION = 273,
     TASK_STATUS = 274,
     IDENTIFIER_TYPE = 275,
     DOT = 276,
     COMMA = 277,
     OPEN_PARENTHESIS = 278,
     CLOSE_PARENTHESIS = 279,
     OPEN_BRACES = 280,
     CLOSE_BRACES = 281,
     OPEN_BRACKETS = 282,
     CLOSE_BRACKETS = 283,
     STRING = 284,
     NUMBER = 285,
     IDENTIFIER = 286
   };
#endif
/* Tokens.  */
#define START_SPRINT 258
#define END_SPRINT 259
#define NEWLINE 260
#define IF 261
#define ELSE 262
#define FOR 263
#define SET 264
#define TO 265
#define FROM 266
#define IS 267
#define TASK 268
#define ADD 269
#define REMOVE 270
#define IN_TASKS_FROM 271
#define HAS_PRIORITY 272
#define TASK_OPTION 273
#define TASK_STATUS 274
#define IDENTIFIER_TYPE 275
#define DOT 276
#define COMMA 277
#define OPEN_PARENTHESIS 278
#define CLOSE_PARENTHESIS 279
#define OPEN_BRACES 280
#define CLOSE_BRACES 281
#define OPEN_BRACKETS 282
#define CLOSE_BRACKETS 283
#define STRING 284
#define NUMBER 285
#define IDENTIFIER 286




#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
# define YYSTYPE_IS_TRIVIAL 1
#endif

extern YYSTYPE yylval;

