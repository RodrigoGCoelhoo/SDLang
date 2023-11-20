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
     IF = 260,
     ELSE = 261,
     FOR = 262,
     SET = 263,
     TO = 264,
     FROM = 265,
     IS = 266,
     TASK = 267,
     ADD = 268,
     REMOVE = 269,
     IN_TASKS_FROM = 270,
     HAS_PRIORITY = 271,
     TASK_OPTION = 272,
     TASK_STATUS = 273,
     IDENTIFIER_TYPE = 274,
     DOT = 275,
     COMMA = 276,
     OPEN_PARENTHESIS = 277,
     CLOSE_PARENTHESIS = 278,
     OPEN_BRACES = 279,
     CLOSE_BRACES = 280,
     OPEN_BRACKETS = 281,
     CLOSE_BRACKETS = 282,
     STRING = 283,
     NUMBER = 284,
     IDENTIFIER = 285
   };
#endif
/* Tokens.  */
#define START_SPRINT 258
#define END_SPRINT 259
#define IF 260
#define ELSE 261
#define FOR 262
#define SET 263
#define TO 264
#define FROM 265
#define IS 266
#define TASK 267
#define ADD 268
#define REMOVE 269
#define IN_TASKS_FROM 270
#define HAS_PRIORITY 271
#define TASK_OPTION 272
#define TASK_STATUS 273
#define IDENTIFIER_TYPE 274
#define DOT 275
#define COMMA 276
#define OPEN_PARENTHESIS 277
#define CLOSE_PARENTHESIS 278
#define OPEN_BRACES 279
#define CLOSE_BRACES 280
#define OPEN_BRACKETS 281
#define CLOSE_BRACKETS 282
#define STRING 283
#define NUMBER 284
#define IDENTIFIER 285




#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
# define YYSTYPE_IS_TRIVIAL 1
#endif

extern YYSTYPE yylval;

