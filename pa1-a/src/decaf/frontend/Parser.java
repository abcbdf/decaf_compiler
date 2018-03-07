//### This file created by BYACC 1.8(/Java extension  1.13)
//### Java capabilities added 7 Jan 97, Bob Jamison
//### Updated : 27 Nov 97  -- Bob Jamison, Joe Nieten
//###           01 Jan 98  -- Bob Jamison -- fixed generic semantic constructor
//###           01 Jun 99  -- Bob Jamison -- added Runnable support
//###           06 Aug 00  -- Bob Jamison -- made state variables class-global
//###           03 Jan 01  -- Bob Jamison -- improved flags, tracing
//###           16 May 01  -- Bob Jamison -- added custom stack sizing
//###           04 Mar 02  -- Yuval Oren  -- improved java performance, added options
//###           14 Mar 02  -- Tomas Hurka -- -d support, static initializer workaround
//###           14 Sep 06  -- Keltin Leung-- ReduceListener support, eliminate underflow report in error recovery
//### Please send bug reports to tom@hukatronic.cz
//### static char yysccsid[] = "@(#)yaccpar	1.8 (Berkeley) 01/20/90";






//#line 11 "Parser.y"
package decaf.frontend;

import decaf.tree.Tree;
import decaf.tree.Tree.*;
import decaf.error.*;
import java.util.*;
//#line 25 "Parser.java"
interface ReduceListener {
  public boolean onReduce(String rule);
}




public class Parser
             extends BaseParser
             implements ReduceListener
{

boolean yydebug;        //do I want debug output?
int yynerrs;            //number of errors so far
int yyerrflag;          //was there an error?
int yychar;             //the current working character

ReduceListener reduceListener = null;
void yyclearin ()       {yychar = (-1);}
void yyerrok ()         {yyerrflag=0;}
void addReduceListener(ReduceListener l) {
  reduceListener = l;}


//########## MESSAGES ##########
//###############################################################
// method: debug
//###############################################################
void debug(String msg)
{
  if (yydebug)
    System.out.println(msg);
}

//########## STATE STACK ##########
final static int YYSTACKSIZE = 500;  //maximum stack size
int statestk[] = new int[YYSTACKSIZE]; //state stack
int stateptr;
int stateptrmax;                     //highest index of stackptr
int statemax;                        //state when highest index reached
//###############################################################
// methods: state stack push,pop,drop,peek
//###############################################################
final void state_push(int state)
{
  try {
		stateptr++;
		statestk[stateptr]=state;
	 }
	 catch (ArrayIndexOutOfBoundsException e) {
     int oldsize = statestk.length;
     int newsize = oldsize * 2;
     int[] newstack = new int[newsize];
     System.arraycopy(statestk,0,newstack,0,oldsize);
     statestk = newstack;
     statestk[stateptr]=state;
  }
}
final int state_pop()
{
  return statestk[stateptr--];
}
final void state_drop(int cnt)
{
  stateptr -= cnt; 
}
final int state_peek(int relative)
{
  return statestk[stateptr-relative];
}
//###############################################################
// method: init_stacks : allocate and prepare stacks
//###############################################################
final boolean init_stacks()
{
  stateptr = -1;
  val_init();
  return true;
}
//###############################################################
// method: dump_stacks : show n levels of the stacks
//###############################################################
void dump_stacks(int count)
{
int i;
  System.out.println("=index==state====value=     s:"+stateptr+"  v:"+valptr);
  for (i=0;i<count;i++)
    System.out.println(" "+i+"    "+statestk[i]+"      "+valstk[i]);
  System.out.println("======================");
}


//########## SEMANTIC VALUES ##########
//## **user defined:SemValue
String   yytext;//user variable to return contextual strings
SemValue yyval; //used to return semantic vals from action routines
SemValue yylval;//the 'lval' (result) I got from yylex()
SemValue valstk[] = new SemValue[YYSTACKSIZE];
int valptr;
//###############################################################
// methods: value stack push,pop,drop,peek.
//###############################################################
final void val_init()
{
  yyval=new SemValue();
  yylval=new SemValue();
  valptr=-1;
}
final void val_push(SemValue val)
{
  try {
    valptr++;
    valstk[valptr]=val;
  }
  catch (ArrayIndexOutOfBoundsException e) {
    int oldsize = valstk.length;
    int newsize = oldsize*2;
    SemValue[] newstack = new SemValue[newsize];
    System.arraycopy(valstk,0,newstack,0,oldsize);
    valstk = newstack;
    valstk[valptr]=val;
  }
}
final SemValue val_pop()
{
  return valstk[valptr--];
}
final void val_drop(int cnt)
{
  valptr -= cnt;
}
final SemValue val_peek(int relative)
{
  return valstk[valptr-relative];
}
//#### end semantic value section ####
public final static short VOID=257;
public final static short BOOL=258;
public final static short INT=259;
public final static short STRING=260;
public final static short CLASS=261;
public final static short COMPLEX=262;
public final static short NULL=263;
public final static short EXTENDS=264;
public final static short THIS=265;
public final static short WHILE=266;
public final static short FOR=267;
public final static short SUPER=268;
public final static short IF=269;
public final static short ELSE=270;
public final static short RETURN=271;
public final static short BREAK=272;
public final static short NEW=273;
public final static short DO=274;
public final static short OD=275;
public final static short PRINT=276;
public final static short READ_INTEGER=277;
public final static short READ_LINE=278;
public final static short DCOPY=279;
public final static short SCOPY=280;
public final static short CASE=281;
public final static short DEFAULT=282;
public final static short PRINTCOMP=283;
public final static short LITERAL=284;
public final static short IDENTIFIER=285;
public final static short AND=286;
public final static short OR=287;
public final static short STATIC=288;
public final static short INSTANCEOF=289;
public final static short LESS_EQUAL=290;
public final static short GREATER_EQUAL=291;
public final static short EQUAL=292;
public final static short NOT_EQUAL=293;
public final static short SEPARATOR=294;
public final static short UMINUS=295;
public final static short EMPTY=296;
public final static short YYERRCODE=256;
final static short yylhs[] = {                           -1,
    0,    1,    1,    3,    4,    5,    5,    5,    5,    5,
    5,    5,    2,    6,    6,    7,    7,    7,    9,    9,
   10,   10,    8,    8,   11,   12,   12,   13,   13,   13,
   13,   13,   13,   13,   13,   13,   13,   13,   14,   14,
   14,   26,   26,   23,   23,   25,   24,   24,   24,   24,
   24,   24,   24,   24,   24,   24,   24,   24,   24,   24,
   24,   24,   24,   24,   24,   24,   24,   24,   24,   24,
   24,   24,   24,   24,   24,   24,   24,   24,   24,   28,
   28,   27,   27,   31,   31,   32,   32,   33,   34,   29,
   29,   35,   30,   16,   17,   20,   15,   36,   36,   18,
   18,   19,   21,   22,
};
final static short yylen[] = {                            2,
    1,    2,    1,    2,    2,    1,    1,    1,    1,    1,
    2,    3,    6,    2,    0,    2,    2,    0,    1,    0,
    3,    1,    7,    6,    3,    2,    0,    1,    2,    1,
    1,    1,    2,    2,    2,    2,    2,    1,    3,    1,
    0,    2,    0,    2,    4,    5,    1,    1,    1,    3,
    3,    3,    3,    3,    3,    3,    3,    3,    3,    3,
    3,    3,    3,    2,    2,    2,    2,    2,    3,    3,
    1,    1,    4,    4,    8,    4,    5,    6,    5,    1,
    1,    1,    0,    3,    1,    2,    0,    2,    3,    2,
    0,    4,    4,    5,    9,    1,    6,    2,    0,    2,
    1,    4,    4,    4,
};
final static short yydefred[] = {                         0,
    0,    0,    0,    3,    0,    2,    0,    0,   14,   18,
    0,    7,    8,    6,   10,    0,    9,    0,   13,   16,
    0,    0,   17,   11,    0,    4,    0,    0,    0,    0,
   12,    0,   22,    0,    0,    0,    0,    5,    0,    0,
    0,   27,   24,   21,   23,    0,   81,   71,    0,    0,
   72,    0,    0,   96,    0,   87,    0,    0,    0,    0,
    0,    0,    0,   80,    0,    0,    0,    0,   25,    0,
    0,    0,   28,   38,   26,    0,   30,   31,   32,    0,
    0,    0,    0,    0,    0,    0,    0,    0,   49,    0,
    0,    0,   47,    0,   48,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
   65,   66,   67,   29,   33,   34,   35,   36,   37,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,   42,    0,    0,    0,    0,    0,    0,
    0,    0,   86,    0,    0,    0,   69,   70,    0,    0,
    0,    0,    0,    0,   63,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,   76,    0,    0,  104,   88,    0,
  102,   73,   74,    0,  103,    0,    0,   45,    0,    0,
   94,    0,    0,   77,   89,    0,   91,    0,   79,   46,
    0,    0,   97,    0,   78,    0,   98,    0,    0,    0,
   90,    0,    0,    0,   75,   95,    0,    0,   93,   92,
};
final static short yydgoto[] = {                          2,
    3,    4,   73,   21,   34,    8,   11,   23,   35,   36,
   74,   46,   75,   76,   77,   78,   79,   80,   81,   82,
   83,   84,   93,   86,   95,   88,  189,   89,  204,  210,
  146,   98,  143,  144,  211,  203,
};
final static short yysindex[] = {                      -241,
 -264,    0, -241,    0, -237,    0, -228,  -75,    0,    0,
  198,    0,    0,    0,    0, -227,    0, -125,    0,    0,
   13,  -90,    0,    0,  -87,    0,   36,  -13,   37, -125,
    0, -125,    0,  -85,   41,   40,   44,    0,  -37, -125,
  -37,    0,    0,    0,    0,    5,    0,    0,   60,   61,
    0,   63,  296,    0,  451,    0,   64,   67,   68,   76,
   77,   83,   87,    0,   89,  296,  296,   86,    0,  296,
  296,  296,    0,    0,    0,   28,    0,    0,    0,   79,
   85,   88,   90,   94,   93,  907,    0, -137,    0,  296,
  296,  296,    0,  907,    0,  123,   73,  296,  296,  114,
  125,  296,  296,  296,  296,  296,  -29,  -29, -118,  469,
    0,    0,    0,    0,    0,    0,    0,    0,    0,  296,
  296,  296,  296,  296,  296,  296,  296,  296,  296,  296,
  296,  296,  296,    0,  296,  131,  493,  113,  505,  135,
  106,  544,    0, -251,  907,  -22,    0,    0,  566,  577,
  601,    8,  639,  137,    0,  907,  764,  943,   18,   18,
  -32,  -32,   78,   78,  -29,  -29,  -29,   18,   18,  727,
  296,   38,  296,   38,    0,  757,   38,    0,    0,  296,
    0,    0,    0,   56,    0, -105,  296,    0,  143,  146,
    0,  836,  -78,    0,    0,  907,    0,  152,    0,    0,
  296,   38,    0, -245,    0,  153,    0,  138,  139,   80,
    0,   38,  296,  296,    0,    0,  860,  896,    0,    0,
};
final static short yyrindex[] = {                         0,
    0,    0,  201,    0,   84,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,  150,    0,    0,  169,
    0,  169,    0,    0,    0,  170,    0,    0,    0,    0,
    0,    0,    0,    0,    0,  -36,    0,    0,    0,    0,
    0,    0,   -5,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,  -73,  -73,  -73,    0,  -73,
  -73,  -73,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,  931,    0,  442,    0,    0,  -73,
  -36,  -73,    0,  154,    0,    0,    0,  -73,  -73,    0,
    0,  -73,  -73,  -73,  -73,  -73,  115,  144,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,  -73,
  -73,  -73,  -73,  -73,  -73,  -73,  -73,  -73,  -73,  -73,
  -73,  -73,  -73,    0,  -73,   52,    0,    0,    0,    0,
  -73,    0,    0,    0,   12,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,   -8,   47,  -12,  877,  953,
  124,  464,  784,  965,  380,  404,  433,  994, 1020,    0,
  -25,  -36,  -73,  -36,    0,    0,  -36,    0,    0,  -73,
    0,    0,    0,    0,    0,    0,  -73,    0,    0,  173,
    0,    0,  -33,    0,    0,   26,    0,    0,    0,    0,
  -16,  -36,    0,    0,    0,    0,    0,    0,    0,    0,
    0,  -36,  -73,  -73,    0,    0,    0,    0,    0,    0,
};
final static short yygindex[] = {                         0,
    0,  212,  205,    4,   24,    0,    0,    0,  186,    0,
   27,    0,  176,  -83,    0,    0,    0,    0,    0,    0,
    0,    0,  453, 1224,  503,    0,    0,   15,    0,    0,
  -96,    0,    0,    0,    0,    0,
};
final static int YYTABLESIZE=1438;
static short yytable[];
static { yytable();}
static void yytable(){
yytable = new short[]{                         99,
   28,   99,   99,   28,  131,   28,   99,  138,  152,  129,
  127,   99,  128,  134,  130,   83,  134,   47,  181,    1,
    5,  180,   41,  178,   41,   99,    7,  133,   62,  132,
   99,   62,   39,   33,   22,   33,  208,   67,   64,   72,
   71,   25,  179,   44,   68,   62,   62,   10,  185,   66,
   39,  180,   85,  101,  131,   85,    9,   24,  135,  129,
  127,  135,  128,  134,  130,   43,   84,   45,   70,   84,
   67,   26,   72,   71,  190,   30,   32,   68,   97,   31,
   62,   39,   66,   40,   41,   42,  114,   61,   44,   99,
   61,   99,   44,   44,   44,   44,   44,   44,   44,   90,
   91,   70,   92,   99,   61,   61,  100,  101,  135,   44,
   44,   44,   44,   44,  131,  102,  103,  206,   67,  129,
   72,   71,  104,  134,  130,   68,  105,   42,  106,   69,
   66,   12,   13,   14,   15,   16,   17,  115,   67,   61,
   72,   71,   44,  116,   44,   68,  117,  136,  118,   70,
   66,   64,  119,  120,  147,   64,   64,   64,   64,   64,
   42,   64,  140,  141,   55,  148,  154,   55,  135,   70,
  171,  173,   64,   64,   64,  175,   64,  187,  197,  198,
   68,   55,   55,  200,   68,   68,   68,   68,   68,  180,
   68,  202,  205,  212,   27,  213,  214,   29,   31,   38,
    1,   68,   68,   68,  215,   68,   15,   64,    5,   20,
   19,   43,  100,   82,    6,   20,   55,   37,  209,    0,
    0,    0,    0,   99,   99,   99,   99,   99,   99,   99,
    0,   99,   99,   99,   99,   99,   68,   99,   99,   99,
   99,   99,   99,   99,   99,   99,   99,   99,   43,   99,
   99,   99,    0,    0,    0,   99,    0,  123,  124,   43,
   99,   12,   13,   14,   15,   16,   17,   47,   43,   48,
   49,   50,   51,   52,   62,   53,   54,   55,   56,   43,
   57,   58,   59,   60,   61,   62,    0,   63,   64,    0,
    0,    0,    0,   65,   12,   13,   14,   15,   16,   17,
   47,    0,   48,   49,   50,   51,   52,    0,   53,   54,
   55,   56,    0,   57,   58,   59,   60,   61,   62,    0,
   63,   64,   19,    0,    0,    0,   65,    0,   67,    0,
   72,   71,   61,   61,    0,   68,    0,   44,   44,    0,
   66,   44,   44,   44,   44,    0,  109,  191,   47,  193,
   48,    0,  195,   51,    0,    0,    0,    0,   55,   70,
    0,    0,   58,   59,   60,   61,   62,    0,   47,   64,
   48,    0,    0,   51,   65,    0,    0,  207,   55,    0,
    0,    0,   58,   59,   60,   61,   62,  216,    0,   64,
    0,    0,    0,    0,   65,    0,    0,    0,    0,    0,
   64,   64,    0,    0,   64,   64,   64,   64,    0,   55,
   55,    0,    0,    0,    0,    0,   52,    0,    0,    0,
   52,   52,   52,   52,   52,    0,   52,    0,    0,   68,
   68,    0,    0,   68,   68,   68,   68,   52,   52,   52,
   53,   52,    0,    0,   53,   53,   53,   53,   53,    0,
   53,    0,    0,    0,   12,   13,   14,   15,   16,   17,
    0,   53,   53,   53,    0,   53,    0,    0,    0,   54,
    0,    0,   52,   54,   54,   54,   54,   54,   48,   54,
    0,    0,   40,   48,   48,   18,   48,   48,   48,    0,
   54,   54,   54,    0,   54,    0,   53,    0,   85,    0,
   40,   48,    0,   48,   56,  131,    0,   56,    0,  155,
  129,  127,    0,  128,  134,  130,    0,    0,    0,    0,
    0,   56,   56,    0,    0,   54,    0,    0,  133,  131,
  132,    0,   48,  172,  129,  127,    0,  128,  134,  130,
    0,  131,    0,   85,    0,  174,  129,  127,   87,  128,
  134,  130,  133,    0,  132,    0,   56,    0,   47,  135,
   48,    0,    0,   51,  133,    0,  132,    0,   55,    0,
    0,    0,   58,   59,   60,   61,   62,    0,    0,   64,
  131,    0,    0,  135,   65,  129,  127,    0,  128,  134,
  130,    0,    0,   87,    0,  135,    0,    0,    0,    0,
    0,  177,  131,  133,    0,  132,  182,  129,  127,    0,
  128,  134,  130,  131,    0,    0,    0,  183,  129,  127,
    0,  128,  134,  130,   85,  133,   85,  132,    0,   85,
    0,    0,    0,    0,  135,    0,  133,  131,  132,    0,
    0,  184,  129,  127,    0,  128,  134,  130,    0,    0,
    0,    0,    0,   85,   85,    0,  135,    0,    0,    0,
  133,    0,  132,    0,   85,   52,   52,  135,    0,   52,
   52,   52,   52,    0,   87,  131,   87,    0,    0,   87,
  129,  127,  186,  128,  134,  130,    0,    0,    0,   53,
   53,  135,    0,   53,   53,   53,   53,    0,  133,    0,
  132,    0,    0,   87,   87,    0,    0,   12,   13,   14,
   15,   16,   17,    0,   87,    0,    0,    0,   54,   54,
    0,    0,   54,   54,   54,   54,    0,   48,   48,  135,
    0,   48,   48,   48,   48,   96,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,   56,
   56,    0,    0,    0,  121,  122,    0,    0,  123,  124,
  125,  126,    0,  131,    0,    0,    0,    0,  129,  127,
    0,  128,  134,  130,    0,    0,    0,    0,  121,  122,
    0,    0,  123,  124,  125,  126,  133,    0,  132,    0,
  121,  122,    0,  131,  123,  124,  125,  126,  129,  127,
  131,  128,  134,  130,    0,  129,  127,    0,  128,  134,
  130,    0,    0,    0,    0,    0,  133,  135,  132,  188,
    0,    0,    0,  133,   50,  132,   50,   50,   50,  121,
  122,    0,    0,  123,  124,  125,  126,    0,    0,    0,
    0,   50,   50,   50,    0,   50,    0,  135,    0,  194,
    0,  121,  122,    0,  135,  123,  124,  125,  126,    0,
    0,    0,  121,  122,    0,    0,  123,  124,  125,  126,
    0,    0,  131,    0,    0,    0,   50,  129,  127,    0,
  128,  134,  130,    0,    0,    0,  121,  122,    0,    0,
  123,  124,  125,  126,  201,  133,  131,  132,    0,    0,
    0,  129,  127,    0,  128,  134,  130,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,   59,  219,  133,
   59,  132,    0,    0,  121,  122,  135,    0,  123,  124,
  125,  126,  131,    0,   59,   59,    0,  129,  127,    0,
  128,  134,  130,  131,    0,    0,    0,    0,  129,  127,
  135,  128,  134,  130,  220,  133,    0,  132,    0,    0,
    0,    0,    0,    0,    0,    0,  133,   47,  132,   59,
    0,    0,   47,   47,    0,   47,   47,   47,    0,  131,
    0,    0,    0,    0,  129,  127,  135,  128,  134,  130,
   47,    0,   47,   60,    0,    0,   60,  135,    0,    0,
    0,    0,  133,    0,  132,   51,    0,   51,   51,   51,
   60,   60,  121,  122,    0,    0,  123,  124,  125,  126,
    0,   47,   51,   51,   51,    0,   51,    0,    0,    0,
    0,    0,    0,  135,   58,    0,    0,   58,    0,    0,
    0,    0,  121,  122,    0,   60,  123,  124,  125,  126,
    0,   58,   58,  123,  124,  125,  126,   51,    0,    0,
   57,    0,    0,   57,    0,    0,    0,    0,    0,   50,
   50,    0,    0,   50,   50,   50,   50,   57,   57,    0,
    0,    0,    0,    0,    0,    0,   58,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,   57,    0,    0,    0,    0,    0,    0,    0,
    0,  121,  122,    0,    0,  123,  124,  125,  126,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,  121,  122,    0,    0,  123,
  124,  125,  126,    0,    0,    0,    0,    0,    0,    0,
    0,    0,   59,   59,    0,    0,    0,    0,   59,   59,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,  121,  122,    0,    0,  123,  124,  125,  126,    0,
    0,    0,  121,  122,    0,    0,  123,  124,  125,  126,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,   47,   47,    0,    0,
   47,   47,   47,   47,    0,    0,    0,    0,  121,    0,
    0,    0,  123,  124,  125,  126,    0,    0,   60,   60,
    0,    0,    0,    0,   60,   60,    0,    0,    0,    0,
   51,   51,    0,    0,   51,   51,   51,   51,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,   94,    0,    0,   58,
   58,    0,    0,    0,    0,   58,   58,    0,    0,  107,
  108,  110,    0,  111,  112,  113,    0,    0,    0,    0,
    0,    0,    0,    0,    0,   57,   57,    0,    0,    0,
    0,   57,   57,  137,    0,  139,    0,    0,    0,    0,
    0,  142,  145,    0,    0,  149,  150,  151,  145,  153,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,  156,  157,  158,  159,  160,  161,  162,
  163,  164,  165,  166,  167,  168,  169,    0,  170,    0,
    0,    0,    0,    0,  176,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,  145,    0,  192,    0,    0,    0,
    0,    0,    0,  196,    0,    0,    0,    0,    0,    0,
  199,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,  217,  218,
};
}
static short yycheck[];
static { yycheck(); }
static void yycheck() {
yycheck = new short[] {                         33,
   91,   35,   36,   91,   37,   91,   40,   91,  105,   42,
   43,   45,   45,   46,   47,   41,   46,  263,   41,  261,
  285,   44,   59,  275,   41,   59,  264,   60,   41,   62,
   64,   44,   41,   30,   11,   32,  282,   33,  284,   35,
   36,   18,  294,   40,   40,   58,   59,  123,   41,   45,
   59,   44,   41,   59,   37,   44,  285,  285,   91,   42,
   43,   91,   45,   46,   47,   39,   41,   41,   64,   44,
   33,   59,   35,   36,  171,   40,   40,   40,   55,   93,
   93,   41,   45,   44,   41,  123,   59,   41,   37,  123,
   44,  125,   41,   42,   43,   44,   45,   46,   47,   40,
   40,   64,   40,   40,   58,   59,   40,   40,   91,   58,
   59,   60,   61,   62,   37,   40,   40,  201,   33,   42,
   35,   36,   40,   46,   47,   40,   40,  123,   40,  125,
   45,  257,  258,  259,  260,  261,  262,   59,   33,   93,
   35,   36,   91,   59,   93,   40,   59,  285,   59,   64,
   45,   37,   59,   61,   41,   41,   42,   43,   44,   45,
  123,   47,   40,   91,   41,   41,  285,   44,   91,   64,
   40,   59,   58,   59,   60,   41,   62,   41,  123,  285,
   37,   58,   59,   41,   41,   42,   43,   44,   45,   44,
   47,  270,   41,   41,  285,   58,   58,  285,   93,  285,
    0,   58,   59,   60,  125,   62,  123,   93,   59,   41,
   41,  285,   59,   41,    3,   11,   93,   32,  204,   -1,
   -1,   -1,   -1,  257,  258,  259,  260,  261,  262,  263,
   -1,  265,  266,  267,  268,  269,   93,  271,  272,  273,
  274,  275,  276,  277,  278,  279,  280,  281,  285,  283,
  284,  285,   -1,   -1,   -1,  289,   -1,  290,  291,  285,
  294,  257,  258,  259,  260,  261,  262,  263,  285,  265,
  266,  267,  268,  269,  287,  271,  272,  273,  274,  285,
  276,  277,  278,  279,  280,  281,   -1,  283,  284,   -1,
   -1,   -1,   -1,  289,  257,  258,  259,  260,  261,  262,
  263,   -1,  265,  266,  267,  268,  269,   -1,  271,  272,
  273,  274,   -1,  276,  277,  278,  279,  280,  281,   -1,
  283,  284,  125,   -1,   -1,   -1,  289,   -1,   33,   -1,
   35,   36,  286,  287,   -1,   40,   -1,  286,  287,   -1,
   45,  290,  291,  292,  293,   -1,  261,  172,  263,  174,
  265,   -1,  177,  268,   -1,   -1,   -1,   -1,  273,   64,
   -1,   -1,  277,  278,  279,  280,  281,   -1,  263,  284,
  265,   -1,   -1,  268,  289,   -1,   -1,  202,  273,   -1,
   -1,   -1,  277,  278,  279,  280,  281,  212,   -1,  284,
   -1,   -1,   -1,   -1,  289,   -1,   -1,   -1,   -1,   -1,
  286,  287,   -1,   -1,  290,  291,  292,  293,   -1,  286,
  287,   -1,   -1,   -1,   -1,   -1,   37,   -1,   -1,   -1,
   41,   42,   43,   44,   45,   -1,   47,   -1,   -1,  286,
  287,   -1,   -1,  290,  291,  292,  293,   58,   59,   60,
   37,   62,   -1,   -1,   41,   42,   43,   44,   45,   -1,
   47,   -1,   -1,   -1,  257,  258,  259,  260,  261,  262,
   -1,   58,   59,   60,   -1,   62,   -1,   -1,   -1,   37,
   -1,   -1,   93,   41,   42,   43,   44,   45,   37,   47,
   -1,   -1,   41,   42,   43,  288,   45,   46,   47,   -1,
   58,   59,   60,   -1,   62,   -1,   93,   -1,   46,   -1,
   59,   60,   -1,   62,   41,   37,   -1,   44,   -1,   41,
   42,   43,   -1,   45,   46,   47,   -1,   -1,   -1,   -1,
   -1,   58,   59,   -1,   -1,   93,   -1,   -1,   60,   37,
   62,   -1,   91,   41,   42,   43,   -1,   45,   46,   47,
   -1,   37,   -1,   91,   -1,   41,   42,   43,   46,   45,
   46,   47,   60,   -1,   62,   -1,   93,   -1,  263,   91,
  265,   -1,   -1,  268,   60,   -1,   62,   -1,  273,   -1,
   -1,   -1,  277,  278,  279,  280,  281,   -1,   -1,  284,
   37,   -1,   -1,   91,  289,   42,   43,   -1,   45,   46,
   47,   -1,   -1,   91,   -1,   91,   -1,   -1,   -1,   -1,
   -1,   58,   37,   60,   -1,   62,   41,   42,   43,   -1,
   45,   46,   47,   37,   -1,   -1,   -1,   41,   42,   43,
   -1,   45,   46,   47,  172,   60,  174,   62,   -1,  177,
   -1,   -1,   -1,   -1,   91,   -1,   60,   37,   62,   -1,
   -1,   41,   42,   43,   -1,   45,   46,   47,   -1,   -1,
   -1,   -1,   -1,  201,  202,   -1,   91,   -1,   -1,   -1,
   60,   -1,   62,   -1,  212,  286,  287,   91,   -1,  290,
  291,  292,  293,   -1,  172,   37,  174,   -1,   -1,  177,
   42,   43,   44,   45,   46,   47,   -1,   -1,   -1,  286,
  287,   91,   -1,  290,  291,  292,  293,   -1,   60,   -1,
   62,   -1,   -1,  201,  202,   -1,   -1,  257,  258,  259,
  260,  261,  262,   -1,  212,   -1,   -1,   -1,  286,  287,
   -1,   -1,  290,  291,  292,  293,   -1,  286,  287,   91,
   -1,  290,  291,  292,  293,  285,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,  286,
  287,   -1,   -1,   -1,  286,  287,   -1,   -1,  290,  291,
  292,  293,   -1,   37,   -1,   -1,   -1,   -1,   42,   43,
   -1,   45,   46,   47,   -1,   -1,   -1,   -1,  286,  287,
   -1,   -1,  290,  291,  292,  293,   60,   -1,   62,   -1,
  286,  287,   -1,   37,  290,  291,  292,  293,   42,   43,
   37,   45,   46,   47,   -1,   42,   43,   -1,   45,   46,
   47,   -1,   -1,   -1,   -1,   -1,   60,   91,   62,   93,
   -1,   -1,   -1,   60,   41,   62,   43,   44,   45,  286,
  287,   -1,   -1,  290,  291,  292,  293,   -1,   -1,   -1,
   -1,   58,   59,   60,   -1,   62,   -1,   91,   -1,   93,
   -1,  286,  287,   -1,   91,  290,  291,  292,  293,   -1,
   -1,   -1,  286,  287,   -1,   -1,  290,  291,  292,  293,
   -1,   -1,   37,   -1,   -1,   -1,   93,   42,   43,   -1,
   45,   46,   47,   -1,   -1,   -1,  286,  287,   -1,   -1,
  290,  291,  292,  293,   59,   60,   37,   62,   -1,   -1,
   -1,   42,   43,   -1,   45,   46,   47,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   41,   59,   60,
   44,   62,   -1,   -1,  286,  287,   91,   -1,  290,  291,
  292,  293,   37,   -1,   58,   59,   -1,   42,   43,   -1,
   45,   46,   47,   37,   -1,   -1,   -1,   -1,   42,   43,
   91,   45,   46,   47,   59,   60,   -1,   62,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   60,   37,   62,   93,
   -1,   -1,   42,   43,   -1,   45,   46,   47,   -1,   37,
   -1,   -1,   -1,   -1,   42,   43,   91,   45,   46,   47,
   60,   -1,   62,   41,   -1,   -1,   44,   91,   -1,   -1,
   -1,   -1,   60,   -1,   62,   41,   -1,   43,   44,   45,
   58,   59,  286,  287,   -1,   -1,  290,  291,  292,  293,
   -1,   91,   58,   59,   60,   -1,   62,   -1,   -1,   -1,
   -1,   -1,   -1,   91,   41,   -1,   -1,   44,   -1,   -1,
   -1,   -1,  286,  287,   -1,   93,  290,  291,  292,  293,
   -1,   58,   59,  290,  291,  292,  293,   93,   -1,   -1,
   41,   -1,   -1,   44,   -1,   -1,   -1,   -1,   -1,  286,
  287,   -1,   -1,  290,  291,  292,  293,   58,   59,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   93,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   93,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,  286,  287,   -1,   -1,  290,  291,  292,  293,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,  286,  287,   -1,   -1,  290,
  291,  292,  293,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,  286,  287,   -1,   -1,   -1,   -1,  292,  293,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,  286,  287,   -1,   -1,  290,  291,  292,  293,   -1,
   -1,   -1,  286,  287,   -1,   -1,  290,  291,  292,  293,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,  286,  287,   -1,   -1,
  290,  291,  292,  293,   -1,   -1,   -1,   -1,  286,   -1,
   -1,   -1,  290,  291,  292,  293,   -1,   -1,  286,  287,
   -1,   -1,   -1,   -1,  292,  293,   -1,   -1,   -1,   -1,
  286,  287,   -1,   -1,  290,  291,  292,  293,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   53,   -1,   -1,  286,
  287,   -1,   -1,   -1,   -1,  292,  293,   -1,   -1,   66,
   67,   68,   -1,   70,   71,   72,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,  286,  287,   -1,   -1,   -1,
   -1,  292,  293,   90,   -1,   92,   -1,   -1,   -1,   -1,
   -1,   98,   99,   -1,   -1,  102,  103,  104,  105,  106,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,  120,  121,  122,  123,  124,  125,  126,
  127,  128,  129,  130,  131,  132,  133,   -1,  135,   -1,
   -1,   -1,   -1,   -1,  141,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,  171,   -1,  173,   -1,   -1,   -1,
   -1,   -1,   -1,  180,   -1,   -1,   -1,   -1,   -1,   -1,
  187,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,  213,  214,
};
}
final static short YYFINAL=2;
final static short YYMAXTOKEN=296;
final static String yyname[] = {
"end-of-file",null,null,null,null,null,null,null,null,null,null,null,null,null,
null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,
null,null,null,"'!'",null,"'#'","'$'","'%'",null,null,"'('","')'","'*'","'+'",
"','","'-'","'.'","'/'",null,null,null,null,null,null,null,null,null,null,"':'",
"';'","'<'","'='","'>'",null,"'@'",null,null,null,null,null,null,null,null,null,
null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,
null,"'['",null,"']'",null,null,null,null,null,null,null,null,null,null,null,
null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,
null,null,"'{'",null,"'}'",null,null,null,null,null,null,null,null,null,null,
null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,
null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,
null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,
null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,
null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,
null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,
null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,
null,null,null,null,null,null,null,null,null,"VOID","BOOL","INT","STRING",
"CLASS","COMPLEX","NULL","EXTENDS","THIS","WHILE","FOR","SUPER","IF","ELSE",
"RETURN","BREAK","NEW","DO","OD","PRINT","READ_INTEGER","READ_LINE","DCOPY",
"SCOPY","CASE","DEFAULT","PRINTCOMP","LITERAL","IDENTIFIER","AND","OR","STATIC",
"INSTANCEOF","LESS_EQUAL","GREATER_EQUAL","EQUAL","NOT_EQUAL","SEPARATOR",
"UMINUS","EMPTY",
};
final static String yyrule[] = {
"$accept : Program",
"Program : ClassList",
"ClassList : ClassList ClassDef",
"ClassList : ClassDef",
"VariableDef : Variable ';'",
"Variable : Type IDENTIFIER",
"Type : INT",
"Type : VOID",
"Type : BOOL",
"Type : COMPLEX",
"Type : STRING",
"Type : CLASS IDENTIFIER",
"Type : Type '[' ']'",
"ClassDef : CLASS IDENTIFIER ExtendsClause '{' FieldList '}'",
"ExtendsClause : EXTENDS IDENTIFIER",
"ExtendsClause :",
"FieldList : FieldList VariableDef",
"FieldList : FieldList FunctionDef",
"FieldList :",
"Formals : VariableList",
"Formals :",
"VariableList : VariableList ',' Variable",
"VariableList : Variable",
"FunctionDef : STATIC Type IDENTIFIER '(' Formals ')' StmtBlock",
"FunctionDef : Type IDENTIFIER '(' Formals ')' StmtBlock",
"StmtBlock : '{' StmtList '}'",
"StmtList : StmtList Stmt",
"StmtList :",
"Stmt : VariableDef",
"Stmt : SimpleStmt ';'",
"Stmt : IfStmt",
"Stmt : WhileStmt",
"Stmt : ForStmt",
"Stmt : ReturnStmt ';'",
"Stmt : PrintStmt ';'",
"Stmt : BreakStmt ';'",
"Stmt : PrintCompStmt ';'",
"Stmt : DoStmt ';'",
"Stmt : StmtBlock",
"SimpleStmt : LValue '=' Expr",
"SimpleStmt : Call",
"SimpleStmt :",
"Receiver : Expr '.'",
"Receiver :",
"LValue : Receiver IDENTIFIER",
"LValue : Expr '[' Expr ']'",
"Call : Receiver IDENTIFIER '(' Actuals ')'",
"Expr : LValue",
"Expr : Call",
"Expr : Constant",
"Expr : Expr '+' Expr",
"Expr : Expr '-' Expr",
"Expr : Expr '*' Expr",
"Expr : Expr '/' Expr",
"Expr : Expr '%' Expr",
"Expr : Expr EQUAL Expr",
"Expr : Expr NOT_EQUAL Expr",
"Expr : Expr '<' Expr",
"Expr : Expr '>' Expr",
"Expr : Expr LESS_EQUAL Expr",
"Expr : Expr GREATER_EQUAL Expr",
"Expr : Expr AND Expr",
"Expr : Expr OR Expr",
"Expr : '(' Expr ')'",
"Expr : '-' Expr",
"Expr : '@' Expr",
"Expr : '$' Expr",
"Expr : '#' Expr",
"Expr : '!' Expr",
"Expr : READ_INTEGER '(' ')'",
"Expr : READ_LINE '(' ')'",
"Expr : THIS",
"Expr : SUPER",
"Expr : DCOPY '(' Expr ')'",
"Expr : SCOPY '(' Expr ')'",
"Expr : CASE '(' Expr ')' '{' ACaseList DefaultExpr '}'",
"Expr : NEW IDENTIFIER '(' ')'",
"Expr : NEW Type '[' Expr ']'",
"Expr : INSTANCEOF '(' Expr ',' IDENTIFIER ')'",
"Expr : '(' CLASS IDENTIFIER ')' Expr",
"Constant : LITERAL",
"Constant : NULL",
"Actuals : ExprList",
"Actuals :",
"ExprList : ExprList ',' Expr",
"ExprList : Expr",
"DoBranchList : DoBranchList DoBranch",
"DoBranchList :",
"DoBranch : DoSubStmt SEPARATOR",
"DoSubStmt : Expr ':' Stmt",
"ACaseList : ACaseList ACaseExpr",
"ACaseList :",
"ACaseExpr : Constant ':' Expr ';'",
"DefaultExpr : DEFAULT ':' Expr ';'",
"WhileStmt : WHILE '(' Expr ')' Stmt",
"ForStmt : FOR '(' SimpleStmt ';' Expr ';' SimpleStmt ')' Stmt",
"BreakStmt : BREAK",
"IfStmt : IF '(' Expr ')' Stmt ElseClause",
"ElseClause : ELSE Stmt",
"ElseClause :",
"ReturnStmt : RETURN Expr",
"ReturnStmt : RETURN",
"PrintStmt : PRINT '(' ExprList ')'",
"PrintCompStmt : PRINTCOMP '(' ExprList ')'",
"DoStmt : DO DoBranchList DoSubStmt OD",
};

//#line 513 "Parser.y"
    
	/**
	 * 打印当前归约所用的语法规则<br>
	 * 请勿修改。
	 */
    public boolean onReduce(String rule) {
		if (rule.startsWith("$$"))
			return false;
		else
			rule = rule.replaceAll(" \\$\\$\\d+", "");

   	    if (rule.endsWith(":"))
    	    System.out.println(rule + " <empty>");
   	    else
			System.out.println(rule);
		return false;
    }
    
    public void diagnose() {
		addReduceListener(this);
		yyparse();
	}
//#line 713 "Parser.java"
//###############################################################
// method: yylexdebug : check lexer state
//###############################################################
void yylexdebug(int state,int ch)
{
String s=null;
  if (ch < 0) ch=0;
  if (ch <= YYMAXTOKEN) //check index bounds
     s = yyname[ch];    //now get it
  if (s==null)
    s = "illegal-symbol";
  debug("state "+state+", reading "+ch+" ("+s+")");
}





//The following are now global, to aid in error reporting
int yyn;       //next next thing to do
int yym;       //
int yystate;   //current parsing state from state table
String yys;    //current token string


//###############################################################
// method: yyparse : parse input and execute indicated items
//###############################################################
int yyparse()
{
boolean doaction;
  init_stacks();
  yynerrs = 0;
  yyerrflag = 0;
  yychar = -1;          //impossible char forces a read
  yystate=0;            //initial state
  state_push(yystate);  //save it
  while (true) //until parsing is done, either correctly, or w/error
    {
    doaction=true;
    //if (yydebug) debug("loop"); 
    //#### NEXT ACTION (from reduction table)
    for (yyn=yydefred[yystate];yyn==0;yyn=yydefred[yystate])
      {
      //if (yydebug) debug("yyn:"+yyn+"  state:"+yystate+"  yychar:"+yychar);
      if (yychar < 0)      //we want a char?
        {
        yychar = yylex();  //get next token
        //if (yydebug) debug(" next yychar:"+yychar);
        //#### ERROR CHECK ####
        //if (yychar < 0)    //it it didn't work/error
        //  {
        //  yychar = 0;      //change it to default string (no -1!)
          //if (yydebug)
          //  yylexdebug(yystate,yychar);
        //  }
        }//yychar<0
      yyn = yysindex[yystate];  //get amount to shift by (shift index)
      if ((yyn != 0) && (yyn += yychar) >= 0 &&
          yyn <= YYTABLESIZE && yycheck[yyn] == yychar)
        {
        //if (yydebug)
          //debug("state "+yystate+", shifting to state "+yytable[yyn]);
        //#### NEXT STATE ####
        yystate = yytable[yyn];//we are in a new state
        state_push(yystate);   //save it
        val_push(yylval);      //push our lval as the input for next rule
        yychar = -1;           //since we have 'eaten' a token, say we need another
        if (yyerrflag > 0)     //have we recovered an error?
           --yyerrflag;        //give ourselves credit
        doaction=false;        //but don't process yet
        break;   //quit the yyn=0 loop
        }

    yyn = yyrindex[yystate];  //reduce
    if ((yyn !=0 ) && (yyn += yychar) >= 0 &&
            yyn <= YYTABLESIZE && yycheck[yyn] == yychar)
      {   //we reduced!
      //if (yydebug) debug("reduce");
      yyn = yytable[yyn];
      doaction=true; //get ready to execute
      break;         //drop down to actions
      }
    else //ERROR RECOVERY
      {
      if (yyerrflag==0)
        {
        yyerror("syntax error");
        yynerrs++;
        }
      if (yyerrflag < 3) //low error count?
        {
        yyerrflag = 3;
        while (true)   //do until break
          {
          if (stateptr<0 || valptr<0)   //check for under & overflow here
            {
            return 1;
            }
          yyn = yysindex[state_peek(0)];
          if ((yyn != 0) && (yyn += YYERRCODE) >= 0 &&
                    yyn <= YYTABLESIZE && yycheck[yyn] == YYERRCODE)
            {
            //if (yydebug)
              //debug("state "+state_peek(0)+", error recovery shifting to state "+yytable[yyn]+" ");
            yystate = yytable[yyn];
            state_push(yystate);
            val_push(yylval);
            doaction=false;
            break;
            }
          else
            {
            //if (yydebug)
              //debug("error recovery discarding state "+state_peek(0)+" ");
            if (stateptr<0 || valptr<0)   //check for under & overflow here
              {
              return 1;
              }
            state_pop();
            val_pop();
            }
          }
        }
      else            //discard this token
        {
        if (yychar == 0)
          return 1; //yyabort
        //if (yydebug)
          //{
          //yys = null;
          //if (yychar <= YYMAXTOKEN) yys = yyname[yychar];
          //if (yys == null) yys = "illegal-symbol";
          //debug("state "+yystate+", error recovery discards token "+yychar+" ("+yys+")");
          //}
        yychar = -1;  //read another
        }
      }//end error recovery
    }//yyn=0 loop
    if (!doaction)   //any reason not to proceed?
      continue;      //skip action
    yym = yylen[yyn];          //get count of terminals on rhs
    //if (yydebug)
      //debug("state "+yystate+", reducing "+yym+" by rule "+yyn+" ("+yyrule[yyn]+")");
    if (yym>0)                 //if count of rhs not 'nil'
      yyval = val_peek(yym-1); //get current semantic value
    if (reduceListener == null || reduceListener.onReduce(yyrule[yyn])) // if intercepted!
      switch(yyn)
      {
//########## USER-SUPPLIED ACTIONS ##########
case 1:
//#line 53 "Parser.y"
{
						tree = new Tree.TopLevel(val_peek(0).clist, val_peek(0).loc);
					}
break;
case 2:
//#line 59 "Parser.y"
{
						yyval.clist.add(val_peek(0).cdef);
					}
break;
case 3:
//#line 63 "Parser.y"
{
                		yyval.clist = new ArrayList<Tree.ClassDef>();
                		yyval.clist.add(val_peek(0).cdef);
                	}
break;
case 5:
//#line 73 "Parser.y"
{
						yyval.vdef = new Tree.VarDef(val_peek(0).ident, val_peek(1).type, val_peek(0).loc);
					}
break;
case 6:
//#line 79 "Parser.y"
{
						yyval.type = new Tree.TypeIdent(Tree.INT, val_peek(0).loc);
					}
break;
case 7:
//#line 83 "Parser.y"
{
                		yyval.type = new Tree.TypeIdent(Tree.VOID, val_peek(0).loc);
                	}
break;
case 8:
//#line 87 "Parser.y"
{
                		yyval.type = new Tree.TypeIdent(Tree.BOOL, val_peek(0).loc);
                	}
break;
case 9:
//#line 91 "Parser.y"
{
               			yyval.type = new Tree.TypeIdent(Tree.COMPLEX, val_peek(0).loc);
               		}
break;
case 10:
//#line 95 "Parser.y"
{
                		yyval.type = new Tree.TypeIdent(Tree.STRING, val_peek(0).loc);
                	}
break;
case 11:
//#line 99 "Parser.y"
{
                		yyval.type = new Tree.TypeClass(val_peek(0).ident, val_peek(1).loc);
                	}
break;
case 12:
//#line 103 "Parser.y"
{
                		yyval.type = new Tree.TypeArray(val_peek(2).type, val_peek(2).loc);
                	}
break;
case 13:
//#line 109 "Parser.y"
{
						yyval.cdef = new Tree.ClassDef(val_peek(4).ident, val_peek(3).ident, val_peek(1).flist, val_peek(5).loc);
					}
break;
case 14:
//#line 115 "Parser.y"
{
						yyval.ident = val_peek(0).ident;
					}
break;
case 15:
//#line 119 "Parser.y"
{
                		yyval = new SemValue();
                	}
break;
case 16:
//#line 125 "Parser.y"
{
						yyval.flist.add(val_peek(0).vdef);
					}
break;
case 17:
//#line 129 "Parser.y"
{
						yyval.flist.add(val_peek(0).fdef);
					}
break;
case 18:
//#line 133 "Parser.y"
{
                		yyval = new SemValue();
                		yyval.flist = new ArrayList<Tree>();
                	}
break;
case 20:
//#line 141 "Parser.y"
{
                		yyval = new SemValue();
                		yyval.vlist = new ArrayList<Tree.VarDef>(); 
                	}
break;
case 21:
//#line 148 "Parser.y"
{
						yyval.vlist.add(val_peek(0).vdef);
					}
break;
case 22:
//#line 152 "Parser.y"
{
                		yyval.vlist = new ArrayList<Tree.VarDef>();
						yyval.vlist.add(val_peek(0).vdef);
                	}
break;
case 23:
//#line 159 "Parser.y"
{
						yyval.fdef = new MethodDef(true, val_peek(4).ident, val_peek(5).type, val_peek(2).vlist, (Block) val_peek(0).stmt, val_peek(4).loc);
					}
break;
case 24:
//#line 163 "Parser.y"
{
						yyval.fdef = new MethodDef(false, val_peek(4).ident, val_peek(5).type, val_peek(2).vlist, (Block) val_peek(0).stmt, val_peek(4).loc);
					}
break;
case 25:
//#line 169 "Parser.y"
{
						yyval.stmt = new Block(val_peek(1).slist, val_peek(2).loc);
					}
break;
case 26:
//#line 175 "Parser.y"
{
						yyval.slist.add(val_peek(0).stmt);
					}
break;
case 27:
//#line 179 "Parser.y"
{
                		yyval = new SemValue();
                		yyval.slist = new ArrayList<Tree>();
                	}
break;
case 28:
//#line 186 "Parser.y"
{
						yyval.stmt = val_peek(0).vdef;
					}
break;
case 29:
//#line 191 "Parser.y"
{
                		if (yyval.stmt == null) {
                			yyval.stmt = new Tree.Skip(val_peek(0).loc);
                		}
                	}
break;
case 39:
//#line 208 "Parser.y"
{
						yyval.stmt = new Tree.Assign(val_peek(2).lvalue, val_peek(0).expr, val_peek(1).loc);
					}
break;
case 40:
//#line 212 "Parser.y"
{
                		yyval.stmt = new Tree.Exec(val_peek(0).expr, val_peek(0).loc);
                	}
break;
case 41:
//#line 216 "Parser.y"
{
                		yyval = new SemValue();
                	}
break;
case 43:
//#line 223 "Parser.y"
{
                		yyval = new SemValue();
                	}
break;
case 44:
//#line 229 "Parser.y"
{
						yyval.lvalue = new Tree.Ident(val_peek(1).expr, val_peek(0).ident, val_peek(0).loc);
						if (val_peek(1).loc == null) {
							yyval.loc = val_peek(0).loc;
						}
					}
break;
case 45:
//#line 236 "Parser.y"
{
                		yyval.lvalue = new Tree.Indexed(val_peek(3).expr, val_peek(1).expr, val_peek(3).loc);
                	}
break;
case 46:
//#line 242 "Parser.y"
{
						yyval.expr = new Tree.CallExpr(val_peek(4).expr, val_peek(3).ident, val_peek(1).elist, val_peek(3).loc);
						if (val_peek(4).loc == null) {
							yyval.loc = val_peek(3).loc;
						}
					}
break;
case 47:
//#line 251 "Parser.y"
{
						yyval.expr = val_peek(0).lvalue;
					}
break;
case 50:
//#line 257 "Parser.y"
{
                		yyval.expr = new Tree.Binary(Tree.PLUS, val_peek(2).expr, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 51:
//#line 261 "Parser.y"
{
                		yyval.expr = new Tree.Binary(Tree.MINUS, val_peek(2).expr, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 52:
//#line 265 "Parser.y"
{
                		yyval.expr = new Tree.Binary(Tree.MUL, val_peek(2).expr, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 53:
//#line 269 "Parser.y"
{
                		yyval.expr = new Tree.Binary(Tree.DIV, val_peek(2).expr, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 54:
//#line 273 "Parser.y"
{
                		yyval.expr = new Tree.Binary(Tree.MOD, val_peek(2).expr, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 55:
//#line 277 "Parser.y"
{
                		yyval.expr = new Tree.Binary(Tree.EQ, val_peek(2).expr, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 56:
//#line 281 "Parser.y"
{
                		yyval.expr = new Tree.Binary(Tree.NE, val_peek(2).expr, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 57:
//#line 285 "Parser.y"
{
                		yyval.expr = new Tree.Binary(Tree.LT, val_peek(2).expr, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 58:
//#line 289 "Parser.y"
{
                		yyval.expr = new Tree.Binary(Tree.GT, val_peek(2).expr, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 59:
//#line 293 "Parser.y"
{
                		yyval.expr = new Tree.Binary(Tree.LE, val_peek(2).expr, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 60:
//#line 297 "Parser.y"
{
                		yyval.expr = new Tree.Binary(Tree.GE, val_peek(2).expr, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 61:
//#line 301 "Parser.y"
{
                		yyval.expr = new Tree.Binary(Tree.AND, val_peek(2).expr, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 62:
//#line 305 "Parser.y"
{
                		yyval.expr = new Tree.Binary(Tree.OR, val_peek(2).expr, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 63:
//#line 309 "Parser.y"
{
                		yyval = val_peek(1);
                	}
break;
case 64:
//#line 313 "Parser.y"
{
                		yyval.expr = new Tree.Unary(Tree.NEG, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 65:
//#line 317 "Parser.y"
{
                		yyval.expr = new Tree.Unary(Tree.AT, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 66:
//#line 321 "Parser.y"
{
                		yyval.expr = new Tree.Unary(Tree.DOL, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 67:
//#line 325 "Parser.y"
{
                		yyval.expr = new Tree.Unary(Tree.POUND, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 68:
//#line 329 "Parser.y"
{
                		yyval.expr = new Tree.Unary(Tree.NOT, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 69:
//#line 333 "Parser.y"
{
                		yyval.expr = new Tree.ReadIntExpr(val_peek(2).loc);
                	}
break;
case 70:
//#line 337 "Parser.y"
{
                		yyval.expr = new Tree.ReadLineExpr(val_peek(2).loc);
                	}
break;
case 71:
//#line 341 "Parser.y"
{
                		yyval.expr = new Tree.ThisExpr(val_peek(0).loc);
                	}
break;
case 72:
//#line 345 "Parser.y"
{
                		yyval.expr = new Tree.SuperExpr(val_peek(0).loc);
                	}
break;
case 73:
//#line 349 "Parser.y"
{
                		yyval.expr = new Tree.DcopyExpr(val_peek(3).loc, val_peek(1).expr);
                	}
break;
case 74:
//#line 353 "Parser.y"
{
                		yyval.expr = new Tree.ScopyExpr(val_peek(3).loc, val_peek(1).expr);
                	}
break;
case 75:
//#line 357 "Parser.y"
{
                		yyval.expr = new Tree.CaseExpr(val_peek(7).loc, val_peek(5).expr, val_peek(2).elist, val_peek(1).expr);
                	}
break;
case 76:
//#line 361 "Parser.y"
{
                		yyval.expr = new Tree.NewClass(val_peek(2).ident, val_peek(3).loc);
                	}
break;
case 77:
//#line 365 "Parser.y"
{
                		yyval.expr = new Tree.NewArray(val_peek(3).type, val_peek(1).expr, val_peek(4).loc);
                	}
break;
case 78:
//#line 369 "Parser.y"
{
                		yyval.expr = new Tree.TypeTest(val_peek(3).expr, val_peek(1).ident, val_peek(5).loc);
                	}
break;
case 79:
//#line 373 "Parser.y"
{
                		yyval.expr = new Tree.TypeCast(val_peek(2).ident, val_peek(0).expr, val_peek(0).loc);
                	}
break;
case 80:
//#line 379 "Parser.y"
{
						yyval.expr = new Tree.Literal(val_peek(0).typeTag, val_peek(0).literal, val_peek(0).loc);
					}
break;
case 81:
//#line 383 "Parser.y"
{
						yyval.expr = new Null(val_peek(0).loc);
					}
break;
case 83:
//#line 390 "Parser.y"
{
                		yyval = new SemValue();
                		yyval.elist = new ArrayList<Tree.Expr>();
                	}
break;
case 84:
//#line 397 "Parser.y"
{
						yyval.elist.add(val_peek(0).expr);
					}
break;
case 85:
//#line 401 "Parser.y"
{
                		yyval.elist = new ArrayList<Tree.Expr>();
						yyval.elist.add(val_peek(0).expr);
                	}
break;
case 86:
//#line 408 "Parser.y"
{
						yyval.slist.add(val_peek(0).stmt);
					}
break;
case 87:
//#line 412 "Parser.y"
{
						yyval = new SemValue();
						yyval.slist = new ArrayList<Tree>();
					}
break;
case 88:
//#line 418 "Parser.y"
{
						yyval.stmt = new Tree.DoBranch(val_peek(1).loc, val_peek(1).stmt);
					}
break;
case 89:
//#line 423 "Parser.y"
{
						yyval.stmt = new Tree.DoSubStmt(val_peek(2).loc, val_peek(2).expr, val_peek(0).stmt);
					}
break;
case 90:
//#line 428 "Parser.y"
{
						yyval.elist.add(val_peek(0).expr);
					}
break;
case 91:
//#line 432 "Parser.y"
{
                		yyval = new SemValue();
                		yyval.elist = new ArrayList<Tree.Expr>();
                	}
break;
case 92:
//#line 439 "Parser.y"
{
						yyval.expr = new Tree.ACaseExpr(val_peek(3).loc, val_peek(3).expr, val_peek(1).expr);
					}
break;
case 93:
//#line 445 "Parser.y"
{
						yyval.expr = new Tree.DefaultExpr(val_peek(3).loc, val_peek(1).expr);
					}
break;
case 94:
//#line 451 "Parser.y"
{
						yyval.stmt = new Tree.WhileLoop(val_peek(2).expr, val_peek(0).stmt, val_peek(4).loc);
					}
break;
case 95:
//#line 457 "Parser.y"
{
						yyval.stmt = new Tree.ForLoop(val_peek(6).stmt, val_peek(4).expr, val_peek(2).stmt, val_peek(0).stmt, val_peek(8).loc);
					}
break;
case 96:
//#line 463 "Parser.y"
{
						yyval.stmt = new Tree.Break(val_peek(0).loc);
					}
break;
case 97:
//#line 469 "Parser.y"
{
						yyval.stmt = new Tree.If(val_peek(3).expr, val_peek(1).stmt, val_peek(0).stmt, val_peek(5).loc);
					}
break;
case 98:
//#line 475 "Parser.y"
{
						yyval.stmt = val_peek(0).stmt;
					}
break;
case 99:
//#line 479 "Parser.y"
{
						yyval = new SemValue();
					}
break;
case 100:
//#line 485 "Parser.y"
{
						yyval.stmt = new Tree.Return(val_peek(0).expr, val_peek(1).loc);
					}
break;
case 101:
//#line 489 "Parser.y"
{
                		yyval.stmt = new Tree.Return(null, val_peek(0).loc);
                	}
break;
case 102:
//#line 495 "Parser.y"
{
						yyval.stmt = new Print(val_peek(1).elist, val_peek(3).loc);
					}
break;
case 103:
//#line 501 "Parser.y"
{
						yyval.stmt = new PrintComp(val_peek(1).elist, val_peek(3).loc);
					}
break;
case 104:
//#line 506 "Parser.y"
{
						yyval.stmt = new Tree.DoStmt(val_peek(3).loc, val_peek(2).slist, val_peek(1).stmt);
					}
break;
//#line 1410 "Parser.java"
//########## END OF USER-SUPPLIED ACTIONS ##########
    }//switch
    //#### Now let's reduce... ####
    //if (yydebug) debug("reduce");
    state_drop(yym);             //we just reduced yylen states
    yystate = state_peek(0);     //get new state
    val_drop(yym);               //corresponding value drop
    yym = yylhs[yyn];            //select next TERMINAL(on lhs)
    if (yystate == 0 && yym == 0)//done? 'rest' state and at first TERMINAL
      {
      //if (yydebug) debug("After reduction, shifting from state 0 to state "+YYFINAL+"");
      yystate = YYFINAL;         //explicitly say we're done
      state_push(YYFINAL);       //and save it
      val_push(yyval);           //also save the semantic value of parsing
      if (yychar < 0)            //we want another character?
        {
        yychar = yylex();        //get next character
        //if (yychar<0) yychar=0;  //clean, if necessary
        //if (yydebug)
          //yylexdebug(yystate,yychar);
        }
      if (yychar == 0)          //Good exit (if lex returns 0 ;-)
         break;                 //quit the loop--all DONE
      }//if yystate
    else                        //else not done yet
      {                         //get next state and push, for next yydefred[]
      yyn = yygindex[yym];      //find out where to go
      if ((yyn != 0) && (yyn += yystate) >= 0 &&
            yyn <= YYTABLESIZE && yycheck[yyn] == yystate)
        yystate = yytable[yyn]; //get new state
      else
        yystate = yydgoto[yym]; //else go to new defred
      //if (yydebug) debug("after reduction, shifting from state "+state_peek(0)+" to state "+yystate+"");
      state_push(yystate);     //going again, so push state & val...
      val_push(yyval);         //for next action
      }
    }//main loop
  return 0;//yyaccept!!
}
//## end of method parse() ######################################



//## run() --- for Thread #######################################
//## The -Jnorun option was used ##
//## end of method run() ########################################



//## Constructors ###############################################
//## The -Jnoconstruct option was used ##
//###############################################################



}
//################### END OF CLASS ##############################
