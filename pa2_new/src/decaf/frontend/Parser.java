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
public final static short COMPLEX=261;
public final static short CLASS=262;
public final static short CASE=263;
public final static short DEFAULT=264;
public final static short NULL=265;
public final static short EXTENDS=266;
public final static short THIS=267;
public final static short WHILE=268;
public final static short FOR=269;
public final static short SUPER=270;
public final static short IF=271;
public final static short ELSE=272;
public final static short RETURN=273;
public final static short BREAK=274;
public final static short NEW=275;
public final static short PRINT=276;
public final static short PRINTCOMP=277;
public final static short READ_INTEGER=278;
public final static short READ_LINE=279;
public final static short LITERAL=280;
public final static short IDENTIFIER=281;
public final static short AND=282;
public final static short OR=283;
public final static short STATIC=284;
public final static short INSTANCEOF=285;
public final static short LESS_EQUAL=286;
public final static short GREATER_EQUAL=287;
public final static short EQUAL=288;
public final static short NOT_EQUAL=289;
public final static short SPLIT=290;
public final static short DCOPY=291;
public final static short SCOPY=292;
public final static short DO=293;
public final static short OD=294;
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
   24,   24,   24,   24,   24,   24,   24,   24,   24,   29,
   29,   31,   30,   28,   28,   27,   27,   32,   32,   16,
   17,   21,   15,   33,   33,   18,   18,   19,   20,   22,
   34,   34,   35,
};
final static short yylen[] = {                            2,
    1,    2,    1,    2,    2,    1,    1,    1,    1,    1,
    2,    3,    6,    2,    0,    2,    2,    0,    1,    0,
    3,    1,    7,    6,    3,    2,    0,    1,    2,    1,
    1,    1,    2,    2,    2,    2,    2,    1,    3,    1,
    0,    2,    0,    2,    4,    5,    1,    1,    1,    3,
    3,    3,    3,    3,    3,    3,    3,    3,    3,    3,
    3,    3,    3,    2,    2,    2,    2,    2,    3,    3,
    1,    1,    4,    4,    4,    5,    6,    5,    8,    2,
    0,    4,    4,    1,    1,    1,    0,    3,    1,    5,
    9,    1,    6,    2,    0,    2,    1,    4,    4,    3,
    3,    1,    3,
};
final static short yydefred[] = {                         0,
    0,    0,    0,    3,    0,    2,    0,    0,   14,   18,
    0,    7,    8,    6,   10,    9,    0,    0,   13,   16,
    0,    0,   17,   11,    0,    4,    0,    0,    0,    0,
   12,    0,   22,    0,    0,    0,    0,    5,    0,    0,
    0,   27,   24,   21,   23,    0,    0,   85,   71,    0,
    0,   72,    0,    0,   92,    0,    0,    0,    0,    0,
   84,    0,    0,    0,    0,    0,    0,    0,   25,    0,
    0,    0,   28,   38,   26,    0,   30,   31,   32,    0,
    0,    0,    0,    0,    0,    0,    0,    0,   49,    0,
    0,    0,    0,   47,    0,   48,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,  102,    0,    0,
    0,    0,    0,    0,    0,   29,   33,   34,   35,   36,
   37,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,   42,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,   69,   70,    0,
    0,    0,    0,    0,  100,    0,   63,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,   75,    0,    0,
   98,   99,    0,   73,   74,  103,  101,    0,   45,    0,
    0,   81,   90,    0,    0,   76,    0,    0,   78,   46,
    0,    0,    0,   93,   77,    0,    0,    0,   80,    0,
   94,    0,    0,   79,    0,    0,    0,   91,   83,   82,
};
final static short yydgoto[] = {                          2,
    3,    4,   73,   21,   34,    8,   11,   23,   35,   36,
   74,   46,   75,   76,   77,   78,   79,   80,   81,   82,
   83,   84,   94,   86,   96,   88,  190,   89,  201,  208,
  209,  146,  204,  107,  108,
};
final static short yysindex[] = {                      -227,
 -244,    0, -227,    0, -224,    0, -235,  -67,    0,    0,
 -106,    0,    0,    0,    0,    0, -223,  -46,    0,    0,
   15,  -87,    0,    0,  -85,    0,   23,  -29,   33,  -46,
    0,  -46,    0,  -73,   38,   36,   55,    0,  -22,  -46,
  -22,    0,    0,    0,    0,    5,   62,    0,    0,   71,
   72,    0,   73,  127,    0,  354,   75,   77,   80,   81,
    0,   84,   85,   87,  127,  127,  127,   74,    0,  127,
  127,  127,    0,    0,    0,   70,    0,    0,    0,   82,
   83,   86,   88,   91,   43,  901,    0, -138,    0,  127,
  127,  127,  127,    0,  901,    0,  106,   57,  127,  127,
  118,  123,  127,  127,  127,  474, -267,    0,  -37,  -37,
 -115,  500,  901,  901,  901,    0,    0,    0,    0,    0,
    0,  127,  127,  127,  127,  127,  127,  127,  127,  127,
  127,  127,  127,  127,  127,    0,  127,  129,  526,  537,
  111,  559,  130,  104,  901,   44,   45,    0,    0,  587,
  611,  730,   42,  127,    0,  132,    0,  901,  940,  933,
   89,   89,  -32,  -32,   25,   25,  -37,  -37,  -37,   89,
   89,  790,  127,   51,   42,  127,   42,    0,  817,  127,
    0,    0, -102,    0,    0,    0,    0,  127,    0,  147,
  145,    0,    0,  843,  -82,    0,  901,  151,    0,    0,
 -204,  127,   42,    0,    0,  135,  137,   78,    0,  163,
    0,  127,  127,    0,   42,  869,  880,    0,    0,    0,
};
final static short yyrindex[] = {                         0,
    0,    0,  205,    0,   94,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,  148,    0,    0,  165,
    0,  165,    0,    0,    0,  168,    0,    0,    0,    0,
    0,    0,    0,    0,    0,  -58,    0,    0,    0,    0,
    0,    0,    0,  -42,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,  -63,  -63,  -63,  -63,    0,  -63,
  -63,  -63,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,  912,    0,    6,    0,    0,  -63,
  -63,  -58,  -63,    0,  160,    0,    0,    0,  -63,  -63,
    0,    0,  -63,  -63,  -63,    0,    0,    0,  393,  402,
    0,    0,  284,  317,  494,    0,    0,    0,    0,    0,
    0,  -63,  -63,  -63,  -63,  -63,  -63,  -63,  -63,  -63,
  -63,  -63,  -63,  -63,  -63,    0,  -63,  140,    0,    0,
    0,    0,    0,  -63,   50,    0,    0,    0,    0,    0,
    0,    0,  -58,  -63,    0,    0,    0,  -20,   64,   40,
  357,  860,  117, 1009,  963,  989,  429,  438,  465,  999,
 1001,    0,  -25,    0,  -58,  -63,  -58,    0,    0,  -63,
    0,    0,    0,    0,    0,    0,    0,  -63,    0,    0,
  179,    0,    0,    0,  -33,    0,   59,    0,    0,    0,
    0,  -12,  -58,    0,    0,    0,    0,    0,    0,    0,
    0,  -63,  -63,    0,  -58,    0,    0,    0,    0,    0,
};
final static short yygindex[] = {                         0,
    0,  218,  211,    4,   14,    0,    0,    0,  217,    0,
  -17,    0, -120,  -84,    0,    0,    0,    0,    0,    0,
    0,    0,  484, 1231,  663,    0,    0,   49,    0,    0,
    0,  -80,    0,    0,   97,
};
final static int YYTABLESIZE=1444;
static short yytable[];
static { yytable();}
static void yytable(){
yytable = new short[]{                         95,
   41,   95,   95,   28,  133,   28,   95,  141,  136,  131,
  129,   95,  130,  136,  132,   87,   97,   28,   19,  147,
   39,   43,  154,   45,   22,   95,  155,  135,   41,  134,
   95,   25,  186,   33,    1,   33,    5,   67,   39,   72,
   71,    7,   48,   44,   68,    9,   40,   48,   48,   66,
   48,   48,   48,  137,  193,   10,  195,   24,  137,  206,
   48,  133,   30,   31,   40,   48,  131,   48,   70,   98,
  136,  132,   32,   26,   67,   61,   72,   71,   39,   40,
   62,   68,  211,   62,  181,  182,   66,  180,  180,   95,
   89,   95,  191,   89,  218,   41,   48,   62,   62,   88,
   42,   90,   88,  122,   61,   70,   67,   61,   72,   71,
   91,   92,   93,   68,   99,  137,  100,  210,   66,  101,
  102,   61,   61,  103,  104,  133,  105,   42,  116,   69,
  131,  129,   62,  130,  136,  132,   67,   70,   72,   71,
  117,  118,  138,   68,  119,  143,  120,  144,   66,  121,
   12,   13,   14,   15,   16,   17,   61,   55,  148,   67,
   55,   72,   71,  149,   42,  156,   68,   70,  173,  176,
  178,   66,  188,  192,   55,   55,   44,   18,  198,  137,
   44,   44,   44,   44,   44,   44,   44,  200,  180,  203,
   70,  205,  212,   27,  213,   29,   31,   44,   44,   44,
   44,   44,  214,  215,    1,   20,    5,   38,   19,   55,
   12,   13,   14,   15,   16,   17,   15,   43,   96,   86,
    6,   20,   43,   95,   95,   95,   95,   95,   95,   95,
   44,   95,   44,   95,   95,   95,   95,   95,   43,   95,
   95,   95,   95,   95,   95,   95,   95,   95,   37,  207,
  187,   95,    0,  125,  126,   43,   95,   95,   95,   95,
   95,   12,   13,   14,   15,   16,   17,   47,   43,   48,
    0,   49,   50,   51,   52,   53,    0,   54,   55,   56,
   57,   58,   59,   60,   61,    0,    0,   48,   48,   62,
    0,   48,   48,   48,   48,   63,   64,   65,   12,   13,
   14,   15,   16,   17,   47,    0,   48,    0,   49,   50,
   51,   52,   53,    0,   54,   55,   56,   57,   58,   59,
   60,   61,   62,    0,   66,    0,   62,   66,    0,    0,
    0,    0,   63,   64,   65,  111,   47,    0,   48,    0,
   49,   66,   66,   52,    0,   61,   61,    0,   56,    0,
    0,   59,   60,   61,    0,    0,    0,   67,   62,    0,
   67,    0,    0,    0,   63,   64,   47,    0,   48,    0,
   49,    0,    0,   52,   67,   67,   66,    0,   56,    0,
    0,   59,   60,   61,    0,    0,    0,    0,   62,   47,
    0,   48,    0,   49,   63,   64,   52,   59,   55,   55,
   59,   56,    0,    0,   59,   60,   61,    0,    0,   67,
    0,   62,    0,    0,   59,   59,    0,   63,   64,    0,
    0,   44,   44,    0,    0,   44,   44,   44,   44,   64,
    0,    0,    0,   64,   64,   64,   64,   64,   65,   64,
    0,    0,   65,   65,   65,   65,   65,    0,   65,   59,
   64,   64,   64,    0,   64,    0,    0,    0,    0,   65,
   65,   65,    0,   65,    0,   52,    0,    0,    0,   52,
   52,   52,   52,   52,   53,   52,    0,    0,   53,   53,
   53,   53,   53,    0,   53,   64,   52,   52,   52,    0,
   52,    0,    0,    0,   65,   53,   53,   53,    0,   53,
    0,   54,    0,    0,    0,   54,   54,   54,   54,   54,
  133,   54,    0,    0,    0,  131,  129,    0,  130,  136,
  132,   52,   54,   54,   54,    0,   54,    0,    0,   85,
   53,  153,    0,  135,   68,  134,  133,   68,    0,    0,
  157,  131,  129,    0,  130,  136,  132,    0,    0,    0,
    0,   68,   68,    0,    0,    0,    0,   54,    0,  135,
    0,  134,  133,    0,  137,    0,  174,  131,  129,    0,
  130,  136,  132,  133,    0,   85,    0,  175,  131,  129,
    0,  130,  136,  132,    0,  135,   68,  134,    0,    0,
  137,    0,    0,    0,    0,  133,  135,    0,  134,  177,
  131,  129,    0,  130,  136,  132,    0,    0,    0,    0,
   12,   13,   14,   15,   16,   17,  137,    0,  135,    0,
  134,    0,    0,  133,    0,    0,    0,  137,  131,  129,
  183,  130,  136,  132,   97,    0,   85,    0,   59,   59,
    0,    0,    0,    0,   59,   59,  135,  133,  134,  137,
    0,  184,  131,  129,    0,  130,  136,  132,   85,    0,
   85,    0,    0,    0,    0,    0,    0,    0,    0,    0,
  135,    0,  134,    0,   64,   64,    0,  137,   64,   64,
   64,   64,    0,   65,   65,   85,   85,   65,   65,   65,
   65,    0,    0,    0,    0,    0,    0,    0,   85,    0,
    0,  137,    0,    0,    0,    0,    0,    0,   87,    0,
   52,   52,    0,    0,   52,   52,   52,   52,    0,   53,
   53,    0,    0,   53,   53,   53,   53,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,   54,   54,    0,    0,
   54,   54,   54,   54,   87,  123,  124,    0,    0,  125,
  126,  127,  128,    0,    0,    0,  133,    0,    0,    0,
  185,  131,  129,    0,  130,  136,  132,    0,    0,    0,
    0,  123,  124,    0,    0,  125,  126,  127,  128,  135,
    0,  134,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,  123,  124,    0,
    0,  125,  126,  127,  128,   87,    0,    0,  123,  124,
  137,    0,  125,  126,  127,  128,  133,    0,    0,    0,
    0,  131,  129,    0,  130,  136,  132,   87,    0,   87,
  123,  124,    0,    0,  125,  126,  127,  128,    0,  135,
    0,  134,    0,  133,    0,    0,    0,    0,  131,  129,
    0,  130,  136,  132,   87,   87,    0,    0,  123,  124,
    0,    0,  125,  126,  127,  128,  135,   87,  134,  133,
  137,    0,  189,    0,  131,  129,    0,  130,  136,  132,
    0,    0,  123,  124,    0,    0,  125,  126,  127,  128,
   60,  202,  135,   60,  134,  133,    0,  137,    0,  196,
  131,  129,    0,  130,  136,  132,  133,   60,   60,    0,
    0,  131,  129,    0,  130,  136,  132,  219,  135,    0,
  134,    0,    0,  137,    0,    0,    0,  133,  220,  135,
    0,  134,  131,  129,    0,  130,  136,  132,   47,    0,
    0,    0,   60,   47,   47,    0,   47,   47,   47,  137,
  135,    0,  134,    0,    0,    0,    0,    0,    0,  133,
  137,   47,    0,   47,  131,  129,  133,  130,  136,  132,
    0,  131,  129,    0,  130,  136,  132,    0,    0,    0,
    0,  137,  135,    0,  134,    0,    0,    0,    0,  135,
    0,  134,   47,   50,    0,   50,   50,   50,    0,    0,
    0,  123,  124,    0,    0,  125,  126,  127,  128,    0,
   50,   50,   50,  137,   50,    0,    0,    0,    0,   51,
  137,   51,   51,   51,    0,    0,    0,    0,    0,   58,
    0,   57,   58,    0,   57,    0,   51,   51,   51,   56,
   51,    0,   56,    0,    0,   50,   58,   58,   57,   57,
    0,    0,    0,    0,    0,    0,   56,   56,    0,    0,
    0,  123,  124,    0,    0,  125,  126,  127,  128,    0,
    0,   51,    0,    0,    0,    0,    0,    0,    0,    0,
    0,   58,    0,   57,    0,    0,    0,    0,  123,  124,
    0,   56,  125,  126,  127,  128,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,  123,  124,    0,    0,  125,  126,
  127,  128,    0,    0,    0,    0,    0,    0,    0,    0,
    0,   60,   60,    0,    0,    0,    0,   60,   60,    0,
  123,  124,    0,    0,  125,  126,  127,  128,    0,    0,
    0,  123,  124,    0,    0,  125,  126,  127,  128,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,  123,  124,    0,    0,  125,  126,  127,  128,
    0,    0,    0,   47,   47,    0,    0,   47,   47,   47,
   47,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,  123,    0,    0,    0,  125,  126,
  127,  128,    0,    0,    0,  125,  126,  127,  128,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,   50,   50,    0,    0,   50,   50,
   50,   50,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
   51,   51,    0,    0,   51,   51,   51,   51,    0,    0,
   58,   58,   57,   57,   95,    0,   58,   58,   57,   57,
   56,   56,    0,    0,    0,  106,  109,  110,  112,    0,
  113,  114,  115,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
  139,  140,    0,  142,    0,    0,    0,    0,    0,  145,
  145,    0,    0,  150,  151,  152,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,  158,  159,  160,  161,  162,  163,  164,  165,
  166,  167,  168,  169,  170,  171,    0,  172,    0,    0,
    0,    0,    0,    0,  179,    0,    0,    0,    0,    0,
    0,    0,    0,    0,  106,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,  145,    0,    0,  194,    0,    0,    0,
  197,    0,    0,    0,    0,    0,    0,    0,  199,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,  216,  217,
};
}
static short yycheck[];
static { yycheck(); }
static void yycheck() {
yycheck = new short[] {                         33,
   59,   35,   36,   91,   37,   91,   40,   92,   46,   42,
   43,   45,   45,   46,   47,   41,   59,   91,  125,  100,
   41,   39,  290,   41,   11,   59,  294,   60,   41,   62,
   64,   18,  153,   30,  262,   32,  281,   33,   59,   35,
   36,  266,   37,   40,   40,  281,   41,   42,   43,   45,
   45,   46,   47,   91,  175,  123,  177,  281,   91,  264,
  265,   37,   40,   93,   59,   60,   42,   62,   64,   56,
   46,   47,   40,   59,   33,  280,   35,   36,   41,   44,
   41,   40,  203,   44,   41,   41,   45,   44,   44,  123,
   41,  125,  173,   44,  215,   41,   91,   58,   59,   41,
  123,   40,   44,   61,   41,   64,   33,   44,   35,   36,
   40,   40,   40,   40,   40,   91,   40,  202,   45,   40,
   40,   58,   59,   40,   40,   37,   40,  123,   59,  125,
   42,   43,   93,   45,   46,   47,   33,   64,   35,   36,
   59,   59,  281,   40,   59,   40,   59,   91,   45,   59,
  257,  258,  259,  260,  261,  262,   93,   41,   41,   33,
   44,   35,   36,   41,  123,  281,   40,   64,   40,   59,
   41,   45,   41,  123,   58,   59,   37,  284,  281,   91,
   41,   42,   43,   44,   45,   46,   47,   41,   44,  272,
   64,   41,   58,  281,   58,  281,   93,   58,   59,   60,
   61,   62,  125,   41,    0,   41,   59,  281,   41,   93,
  257,  258,  259,  260,  261,  262,  123,  281,   59,   41,
    3,   11,  281,  257,  258,  259,  260,  261,  262,  263,
   91,  265,   93,  267,  268,  269,  270,  271,  281,  273,
  274,  275,  276,  277,  278,  279,  280,  281,   32,  201,
  154,  285,   -1,  286,  287,  281,  290,  291,  292,  293,
  294,  257,  258,  259,  260,  261,  262,  263,  281,  265,
   -1,  267,  268,  269,  270,  271,   -1,  273,  274,  275,
  276,  277,  278,  279,  280,   -1,   -1,  282,  283,  285,
   -1,  286,  287,  288,  289,  291,  292,  293,  257,  258,
  259,  260,  261,  262,  263,   -1,  265,   -1,  267,  268,
  269,  270,  271,   -1,  273,  274,  275,  276,  277,  278,
  279,  280,  283,   -1,   41,   -1,  285,   44,   -1,   -1,
   -1,   -1,  291,  292,  293,  262,  263,   -1,  265,   -1,
  267,   58,   59,  270,   -1,  282,  283,   -1,  275,   -1,
   -1,  278,  279,  280,   -1,   -1,   -1,   41,  285,   -1,
   44,   -1,   -1,   -1,  291,  292,  263,   -1,  265,   -1,
  267,   -1,   -1,  270,   58,   59,   93,   -1,  275,   -1,
   -1,  278,  279,  280,   -1,   -1,   -1,   -1,  285,  263,
   -1,  265,   -1,  267,  291,  292,  270,   41,  282,  283,
   44,  275,   -1,   -1,  278,  279,  280,   -1,   -1,   93,
   -1,  285,   -1,   -1,   58,   59,   -1,  291,  292,   -1,
   -1,  282,  283,   -1,   -1,  286,  287,  288,  289,   37,
   -1,   -1,   -1,   41,   42,   43,   44,   45,   37,   47,
   -1,   -1,   41,   42,   43,   44,   45,   -1,   47,   93,
   58,   59,   60,   -1,   62,   -1,   -1,   -1,   -1,   58,
   59,   60,   -1,   62,   -1,   37,   -1,   -1,   -1,   41,
   42,   43,   44,   45,   37,   47,   -1,   -1,   41,   42,
   43,   44,   45,   -1,   47,   93,   58,   59,   60,   -1,
   62,   -1,   -1,   -1,   93,   58,   59,   60,   -1,   62,
   -1,   37,   -1,   -1,   -1,   41,   42,   43,   44,   45,
   37,   47,   -1,   -1,   -1,   42,   43,   -1,   45,   46,
   47,   93,   58,   59,   60,   -1,   62,   -1,   -1,   46,
   93,   58,   -1,   60,   41,   62,   37,   44,   -1,   -1,
   41,   42,   43,   -1,   45,   46,   47,   -1,   -1,   -1,
   -1,   58,   59,   -1,   -1,   -1,   -1,   93,   -1,   60,
   -1,   62,   37,   -1,   91,   -1,   41,   42,   43,   -1,
   45,   46,   47,   37,   -1,   92,   -1,   41,   42,   43,
   -1,   45,   46,   47,   -1,   60,   93,   62,   -1,   -1,
   91,   -1,   -1,   -1,   -1,   37,   60,   -1,   62,   41,
   42,   43,   -1,   45,   46,   47,   -1,   -1,   -1,   -1,
  257,  258,  259,  260,  261,  262,   91,   -1,   60,   -1,
   62,   -1,   -1,   37,   -1,   -1,   -1,   91,   42,   43,
   44,   45,   46,   47,  281,   -1,  153,   -1,  282,  283,
   -1,   -1,   -1,   -1,  288,  289,   60,   37,   62,   91,
   -1,   41,   42,   43,   -1,   45,   46,   47,  175,   -1,
  177,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   60,   -1,   62,   -1,  282,  283,   -1,   91,  286,  287,
  288,  289,   -1,  282,  283,  202,  203,  286,  287,  288,
  289,   -1,   -1,   -1,   -1,   -1,   -1,   -1,  215,   -1,
   -1,   91,   -1,   -1,   -1,   -1,   -1,   -1,   46,   -1,
  282,  283,   -1,   -1,  286,  287,  288,  289,   -1,  282,
  283,   -1,   -1,  286,  287,  288,  289,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,  282,  283,   -1,   -1,
  286,  287,  288,  289,   92,  282,  283,   -1,   -1,  286,
  287,  288,  289,   -1,   -1,   -1,   37,   -1,   -1,   -1,
   41,   42,   43,   -1,   45,   46,   47,   -1,   -1,   -1,
   -1,  282,  283,   -1,   -1,  286,  287,  288,  289,   60,
   -1,   62,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,  282,  283,   -1,
   -1,  286,  287,  288,  289,  153,   -1,   -1,  282,  283,
   91,   -1,  286,  287,  288,  289,   37,   -1,   -1,   -1,
   -1,   42,   43,   -1,   45,   46,   47,  175,   -1,  177,
  282,  283,   -1,   -1,  286,  287,  288,  289,   -1,   60,
   -1,   62,   -1,   37,   -1,   -1,   -1,   -1,   42,   43,
   -1,   45,   46,   47,  202,  203,   -1,   -1,  282,  283,
   -1,   -1,  286,  287,  288,  289,   60,  215,   62,   37,
   91,   -1,   93,   -1,   42,   43,   -1,   45,   46,   47,
   -1,   -1,  282,  283,   -1,   -1,  286,  287,  288,  289,
   41,   59,   60,   44,   62,   37,   -1,   91,   -1,   93,
   42,   43,   -1,   45,   46,   47,   37,   58,   59,   -1,
   -1,   42,   43,   -1,   45,   46,   47,   59,   60,   -1,
   62,   -1,   -1,   91,   -1,   -1,   -1,   37,   59,   60,
   -1,   62,   42,   43,   -1,   45,   46,   47,   37,   -1,
   -1,   -1,   93,   42,   43,   -1,   45,   46,   47,   91,
   60,   -1,   62,   -1,   -1,   -1,   -1,   -1,   -1,   37,
   91,   60,   -1,   62,   42,   43,   37,   45,   46,   47,
   -1,   42,   43,   -1,   45,   46,   47,   -1,   -1,   -1,
   -1,   91,   60,   -1,   62,   -1,   -1,   -1,   -1,   60,
   -1,   62,   91,   41,   -1,   43,   44,   45,   -1,   -1,
   -1,  282,  283,   -1,   -1,  286,  287,  288,  289,   -1,
   58,   59,   60,   91,   62,   -1,   -1,   -1,   -1,   41,
   91,   43,   44,   45,   -1,   -1,   -1,   -1,   -1,   41,
   -1,   41,   44,   -1,   44,   -1,   58,   59,   60,   41,
   62,   -1,   44,   -1,   -1,   93,   58,   59,   58,   59,
   -1,   -1,   -1,   -1,   -1,   -1,   58,   59,   -1,   -1,
   -1,  282,  283,   -1,   -1,  286,  287,  288,  289,   -1,
   -1,   93,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   93,   -1,   93,   -1,   -1,   -1,   -1,  282,  283,
   -1,   93,  286,  287,  288,  289,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,  282,  283,   -1,   -1,  286,  287,
  288,  289,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,  282,  283,   -1,   -1,   -1,   -1,  288,  289,   -1,
  282,  283,   -1,   -1,  286,  287,  288,  289,   -1,   -1,
   -1,  282,  283,   -1,   -1,  286,  287,  288,  289,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,  282,  283,   -1,   -1,  286,  287,  288,  289,
   -1,   -1,   -1,  282,  283,   -1,   -1,  286,  287,  288,
  289,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,  282,   -1,   -1,   -1,  286,  287,
  288,  289,   -1,   -1,   -1,  286,  287,  288,  289,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,  282,  283,   -1,   -1,  286,  287,
  288,  289,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
  282,  283,   -1,   -1,  286,  287,  288,  289,   -1,   -1,
  282,  283,  282,  283,   54,   -1,  288,  289,  288,  289,
  282,  283,   -1,   -1,   -1,   65,   66,   67,   68,   -1,
   70,   71,   72,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   90,   91,   -1,   93,   -1,   -1,   -1,   -1,   -1,   99,
  100,   -1,   -1,  103,  104,  105,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,  122,  123,  124,  125,  126,  127,  128,  129,
  130,  131,  132,  133,  134,  135,   -1,  137,   -1,   -1,
   -1,   -1,   -1,   -1,  144,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,  154,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,  173,   -1,   -1,  176,   -1,   -1,   -1,
  180,   -1,   -1,   -1,   -1,   -1,   -1,   -1,  188,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,  212,  213,
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
"COMPLEX","CLASS","CASE","DEFAULT","NULL","EXTENDS","THIS","WHILE","FOR",
"SUPER","IF","ELSE","RETURN","BREAK","NEW","PRINT","PRINTCOMP","READ_INTEGER",
"READ_LINE","LITERAL","IDENTIFIER","AND","OR","STATIC","INSTANCEOF",
"LESS_EQUAL","GREATER_EQUAL","EQUAL","NOT_EQUAL","SPLIT","DCOPY","SCOPY","DO",
"OD","UMINUS","EMPTY",
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
"Stmt : PrintCompStmt ';'",
"Stmt : BreakStmt ';'",
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
"Expr : '!' Expr",
"Expr : '@' Expr",
"Expr : '$' Expr",
"Expr : '#' Expr",
"Expr : READ_INTEGER '(' ')'",
"Expr : READ_LINE '(' ')'",
"Expr : THIS",
"Expr : SUPER",
"Expr : DCOPY '(' Expr ')'",
"Expr : SCOPY '(' Expr ')'",
"Expr : NEW IDENTIFIER '(' ')'",
"Expr : NEW Type '[' Expr ']'",
"Expr : INSTANCEOF '(' Expr ',' IDENTIFIER ')'",
"Expr : '(' CLASS IDENTIFIER ')' Expr",
"Expr : CASE '(' Expr ')' '{' CasePairs DefCasePair '}'",
"CasePairs : CasePairs CasePair",
"CasePairs :",
"CasePair : Constant ':' Expr ';'",
"DefCasePair : DEFAULT ':' Expr ';'",
"Constant : LITERAL",
"Constant : NULL",
"Actuals : ExprList",
"Actuals :",
"ExprList : ExprList ',' Expr",
"ExprList : Expr",
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
"DoStmt : DO Branches OD",
"Branches : Branches SPLIT CondStmt",
"Branches : CondStmt",
"CondStmt : Expr ':' Stmt",
};

//#line 504 "Parser.y"
    
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
//#line 714 "Parser.java"
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
//#line 55 "Parser.y"
{
						tree = new Tree.TopLevel(val_peek(0).clist, val_peek(0).loc);
					}
break;
case 2:
//#line 61 "Parser.y"
{
						yyval.clist.add(val_peek(0).cdef);
					}
break;
case 3:
//#line 65 "Parser.y"
{
                		yyval.clist = new ArrayList<Tree.ClassDef>();
                		yyval.clist.add(val_peek(0).cdef);
                	}
break;
case 5:
//#line 75 "Parser.y"
{
						yyval.vdef = new Tree.VarDef(val_peek(0).ident, val_peek(1).type, val_peek(0).loc);
					}
break;
case 6:
//#line 81 "Parser.y"
{
						yyval.type = new Tree.TypeIdent(Tree.INT, val_peek(0).loc);
					}
break;
case 7:
//#line 85 "Parser.y"
{
                		yyval.type = new Tree.TypeIdent(Tree.VOID, val_peek(0).loc);
                	}
break;
case 8:
//#line 89 "Parser.y"
{
                		yyval.type = new Tree.TypeIdent(Tree.BOOL, val_peek(0).loc);
                	}
break;
case 9:
//#line 93 "Parser.y"
{
                        yyval.type = new Tree.TypeIdent(Tree.COMPLEX, val_peek(0).loc);
                    }
break;
case 10:
//#line 97 "Parser.y"
{
                		yyval.type = new Tree.TypeIdent(Tree.STRING, val_peek(0).loc);
                	}
break;
case 11:
//#line 101 "Parser.y"
{
                		yyval.type = new Tree.TypeClass(val_peek(0).ident, val_peek(1).loc);
                	}
break;
case 12:
//#line 105 "Parser.y"
{
                		yyval.type = new Tree.TypeArray(val_peek(2).type, val_peek(2).loc);
                	}
break;
case 13:
//#line 111 "Parser.y"
{
						yyval.cdef = new Tree.ClassDef(val_peek(4).ident, val_peek(3).ident, val_peek(1).flist, val_peek(5).loc);
					}
break;
case 14:
//#line 117 "Parser.y"
{
						yyval.ident = val_peek(0).ident;
					}
break;
case 15:
//#line 121 "Parser.y"
{
                		yyval = new SemValue();
                	}
break;
case 16:
//#line 127 "Parser.y"
{
						yyval.flist.add(val_peek(0).vdef);
					}
break;
case 17:
//#line 131 "Parser.y"
{
						yyval.flist.add(val_peek(0).fdef);
					}
break;
case 18:
//#line 135 "Parser.y"
{
                		yyval = new SemValue();
                		yyval.flist = new ArrayList<Tree>();
                	}
break;
case 20:
//#line 143 "Parser.y"
{
                		yyval = new SemValue();
                		yyval.vlist = new ArrayList<Tree.VarDef>(); 
                	}
break;
case 21:
//#line 150 "Parser.y"
{
						yyval.vlist.add(val_peek(0).vdef);
					}
break;
case 22:
//#line 154 "Parser.y"
{
                		yyval.vlist = new ArrayList<Tree.VarDef>();
						yyval.vlist.add(val_peek(0).vdef);
                	}
break;
case 23:
//#line 161 "Parser.y"
{
						yyval.fdef = new MethodDef(true, val_peek(4).ident, val_peek(5).type, val_peek(2).vlist, (Block) val_peek(0).stmt, val_peek(4).loc);
					}
break;
case 24:
//#line 165 "Parser.y"
{
						yyval.fdef = new MethodDef(false, val_peek(4).ident, val_peek(5).type, val_peek(2).vlist, (Block) val_peek(0).stmt, val_peek(4).loc);
					}
break;
case 25:
//#line 171 "Parser.y"
{
						yyval.stmt = new Block(val_peek(1).slist, val_peek(2).loc);
					}
break;
case 26:
//#line 177 "Parser.y"
{
						yyval.slist.add(val_peek(0).stmt);
					}
break;
case 27:
//#line 181 "Parser.y"
{
                		yyval = new SemValue();
                		yyval.slist = new ArrayList<Tree>();
                	}
break;
case 28:
//#line 188 "Parser.y"
{
						yyval.stmt = val_peek(0).vdef;
					}
break;
case 29:
//#line 193 "Parser.y"
{
                		if (yyval.stmt == null) {
                			yyval.stmt = new Tree.Skip(val_peek(0).loc);
                		}
                	}
break;
case 39:
//#line 210 "Parser.y"
{
						yyval.stmt = new Tree.Assign(val_peek(2).lvalue, val_peek(0).expr, val_peek(1).loc);
					}
break;
case 40:
//#line 214 "Parser.y"
{
                		yyval.stmt = new Tree.Exec(val_peek(0).expr, val_peek(0).loc);
                	}
break;
case 41:
//#line 218 "Parser.y"
{
                		yyval = new SemValue();
                	}
break;
case 43:
//#line 225 "Parser.y"
{
                		yyval = new SemValue();
                	}
break;
case 44:
//#line 231 "Parser.y"
{
						yyval.lvalue = new Tree.Ident(val_peek(1).expr, val_peek(0).ident, val_peek(0).loc);
						if (val_peek(1).loc == null) {
							yyval.loc = val_peek(0).loc;
						}
					}
break;
case 45:
//#line 238 "Parser.y"
{
                		yyval.lvalue = new Tree.Indexed(val_peek(3).expr, val_peek(1).expr, val_peek(3).loc);
                	}
break;
case 46:
//#line 244 "Parser.y"
{
						yyval.expr = new Tree.CallExpr(val_peek(4).expr, val_peek(3).ident, val_peek(1).elist, val_peek(3).loc);
						if (val_peek(4).loc == null) {
							yyval.loc = val_peek(3).loc;
						}
					}
break;
case 47:
//#line 253 "Parser.y"
{
						yyval.expr = val_peek(0).lvalue;
					}
break;
case 50:
//#line 259 "Parser.y"
{
                		yyval.expr = new Tree.Binary(Tree.PLUS, val_peek(2).expr, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 51:
//#line 263 "Parser.y"
{
                		yyval.expr = new Tree.Binary(Tree.MINUS, val_peek(2).expr, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 52:
//#line 267 "Parser.y"
{
                		yyval.expr = new Tree.Binary(Tree.MUL, val_peek(2).expr, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 53:
//#line 271 "Parser.y"
{
                		yyval.expr = new Tree.Binary(Tree.DIV, val_peek(2).expr, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 54:
//#line 275 "Parser.y"
{
                		yyval.expr = new Tree.Binary(Tree.MOD, val_peek(2).expr, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 55:
//#line 279 "Parser.y"
{
                		yyval.expr = new Tree.Binary(Tree.EQ, val_peek(2).expr, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 56:
//#line 283 "Parser.y"
{
                		yyval.expr = new Tree.Binary(Tree.NE, val_peek(2).expr, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 57:
//#line 287 "Parser.y"
{
                		yyval.expr = new Tree.Binary(Tree.LT, val_peek(2).expr, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 58:
//#line 291 "Parser.y"
{
                		yyval.expr = new Tree.Binary(Tree.GT, val_peek(2).expr, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 59:
//#line 295 "Parser.y"
{
                		yyval.expr = new Tree.Binary(Tree.LE, val_peek(2).expr, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 60:
//#line 299 "Parser.y"
{
                		yyval.expr = new Tree.Binary(Tree.GE, val_peek(2).expr, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 61:
//#line 303 "Parser.y"
{
                		yyval.expr = new Tree.Binary(Tree.AND, val_peek(2).expr, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 62:
//#line 307 "Parser.y"
{
                		yyval.expr = new Tree.Binary(Tree.OR, val_peek(2).expr, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 63:
//#line 311 "Parser.y"
{
                		yyval = val_peek(1);
                	}
break;
case 64:
//#line 315 "Parser.y"
{
                		yyval.expr = new Tree.Unary(Tree.NEG, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 65:
//#line 319 "Parser.y"
{
                		yyval.expr = new Tree.Unary(Tree.NOT, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 66:
//#line 323 "Parser.y"
{
                        yyval.expr = new Tree.Unary(Tree.RE, val_peek(0).expr, val_peek(1).loc);
                    }
break;
case 67:
//#line 327 "Parser.y"
{
                        yyval.expr = new Tree.Unary(Tree.IM, val_peek(0).expr, val_peek(1).loc);
                    }
break;
case 68:
//#line 331 "Parser.y"
{
                        yyval.expr = new Tree.Unary(Tree.COMPCAST, val_peek(0).expr, val_peek(1).loc);
                    }
break;
case 69:
//#line 335 "Parser.y"
{
                		yyval.expr = new Tree.ReadIntExpr(val_peek(2).loc);
                	}
break;
case 70:
//#line 339 "Parser.y"
{
                		yyval.expr = new Tree.ReadLineExpr(val_peek(2).loc);
                	}
break;
case 71:
//#line 343 "Parser.y"
{
                		yyval.expr = new Tree.ThisExpr(val_peek(0).loc);
                	}
break;
case 72:
//#line 347 "Parser.y"
{
                        yyval.expr = new Tree.SuperExpr(val_peek(0).loc);
                    }
break;
case 73:
//#line 351 "Parser.y"
{
                        yyval.expr = new Tree.DCopyExpr(val_peek(1).expr, val_peek(3).loc);
                    }
break;
case 74:
//#line 355 "Parser.y"
{
                        yyval.expr = new Tree.SCopyExpr(val_peek(1).expr, val_peek(3).loc);
                    }
break;
case 75:
//#line 359 "Parser.y"
{
                		yyval.expr = new Tree.NewClass(val_peek(2).ident, val_peek(3).loc);
                	}
break;
case 76:
//#line 363 "Parser.y"
{
                		yyval.expr = new Tree.NewArray(val_peek(3).type, val_peek(1).expr, val_peek(4).loc);
                	}
break;
case 77:
//#line 367 "Parser.y"
{
                		yyval.expr = new Tree.TypeTest(val_peek(3).expr, val_peek(1).ident, val_peek(5).loc);
                	}
break;
case 78:
//#line 371 "Parser.y"
{
                		yyval.expr = new Tree.TypeCast(val_peek(2).ident, val_peek(0).expr, val_peek(0).loc);
                	}
break;
case 79:
//#line 375 "Parser.y"
{
                        yyval.expr = new Tree.CaseExpr(val_peek(5).expr, val_peek(2).pairlist, val_peek(1).defpair, val_peek(7).loc);
                    }
break;
case 80:
//#line 381 "Parser.y"
{
                        yyval.pairlist.add(val_peek(0).pair);
                    }
break;
case 81:
//#line 385 "Parser.y"
{
                        yyval.pairlist = new ArrayList<Tree.CasePair>();
                    }
break;
case 82:
//#line 390 "Parser.y"
{
                        yyval.pair = new Tree.CasePair(val_peek(3).expr, val_peek(1).expr, val_peek(3).loc);
                    }
break;
case 83:
//#line 395 "Parser.y"
{
                        yyval.defpair = new Tree.DefCasePair(val_peek(1).expr, val_peek(3).loc);
                    }
break;
case 84:
//#line 401 "Parser.y"
{
						yyval.expr = new Tree.Literal(val_peek(0).typeTag, val_peek(0).literal, val_peek(0).loc);
					}
break;
case 85:
//#line 405 "Parser.y"
{
						yyval.expr = new Null(val_peek(0).loc);
					}
break;
case 87:
//#line 412 "Parser.y"
{
                		yyval = new SemValue();
                		yyval.elist = new ArrayList<Tree.Expr>();
                	}
break;
case 88:
//#line 419 "Parser.y"
{
						yyval.elist.add(val_peek(0).expr);
					}
break;
case 89:
//#line 423 "Parser.y"
{
                		yyval.elist = new ArrayList<Tree.Expr>();
						yyval.elist.add(val_peek(0).expr);
                	}
break;
case 90:
//#line 430 "Parser.y"
{
						yyval.stmt = new Tree.WhileLoop(val_peek(2).expr, val_peek(0).stmt, val_peek(4).loc);
					}
break;
case 91:
//#line 436 "Parser.y"
{
						yyval.stmt = new Tree.ForLoop(val_peek(6).stmt, val_peek(4).expr, val_peek(2).stmt, val_peek(0).stmt, val_peek(8).loc);
					}
break;
case 92:
//#line 442 "Parser.y"
{
						yyval.stmt = new Tree.Break(val_peek(0).loc);
					}
break;
case 93:
//#line 448 "Parser.y"
{
						yyval.stmt = new Tree.If(val_peek(3).expr, val_peek(1).stmt, val_peek(0).stmt, val_peek(5).loc);
					}
break;
case 94:
//#line 454 "Parser.y"
{
						yyval.stmt = val_peek(0).stmt;
					}
break;
case 95:
//#line 458 "Parser.y"
{
						yyval = new SemValue();
					}
break;
case 96:
//#line 464 "Parser.y"
{
						yyval.stmt = new Tree.Return(val_peek(0).expr, val_peek(1).loc);
					}
break;
case 97:
//#line 468 "Parser.y"
{
                		yyval.stmt = new Tree.Return(null, val_peek(0).loc);
                	}
break;
case 98:
//#line 474 "Parser.y"
{
						yyval.stmt = new Print(val_peek(1).elist, val_peek(3).loc);
					}
break;
case 99:
//#line 479 "Parser.y"
{
                        yyval.stmt = new PrintComp(val_peek(1).elist, val_peek(3).loc);
                    }
break;
case 100:
//#line 484 "Parser.y"
{
                        yyval.stmt = new Tree.Do(val_peek(1).branches, val_peek(2).loc);
                    }
break;
case 101:
//#line 489 "Parser.y"
{
                        yyval.branches.add((Tree.Cond)val_peek(0).stmt);
                    }
break;
case 102:
//#line 493 "Parser.y"
{
                        yyval.branches = new ArrayList<Tree.Cond>();
                        yyval.branches.add((Tree.Cond)val_peek(0).stmt);
                    }
break;
case 103:
//#line 499 "Parser.y"
{
                        yyval.stmt = new Tree.Cond(val_peek(2).expr, val_peek(0).stmt, val_peek(2).loc);
                    }
break;
//#line 1404 "Parser.java"
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
