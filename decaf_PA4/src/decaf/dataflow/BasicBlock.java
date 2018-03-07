package decaf.dataflow;

import java.io.PrintWriter;
import java.util.*;

import decaf.machdesc.Asm;
import decaf.machdesc.Register;
import decaf.tac.Label;
import decaf.tac.Tac;
import decaf.tac.Temp;

public class BasicBlock {
    public int bbNum;

    public enum EndKind {
        BY_BRANCH, BY_BEQZ, BY_BNEZ, BY_RETURN
    }

    public EndKind endKind;

    public int endId; // last TAC's id for this basic block

    public int inDegree;

    public Tac tacList;

    public Label label;

    public Temp var;

    public Register varReg;

    public int[] next;

    public boolean cancelled;

    public boolean mark;

    public Set<Temp> def;
    
    public Set<Temp> hasDefined;

    public Set<Temp> liveUse;

    public Set<Temp> liveIn;

    public Set<Temp> liveOut;
    
    public Set<Pair> liveUsePair;
    
    public Set<Pair> liveInPair;
    
    public Set<Pair> liveOutPair;

    public Set<Temp> saves;

    private List<Asm> asms;

    /**
     * DUChain.
     *
     * 琛ㄤ腑鐨勬瘡涓�椤� `Pair(p, A) -> ds` 琛ㄧず 鍙橀噺 `A` 鍦ㄥ畾鍊肩偣 `p` 鐨� DU 閾句负 `ds`.
     * 杩欓噷 `p` 鍜� `ds` 涓殑姣忎竴椤瑰潎鎸囩殑瀹氬�肩偣鎴栧紩鐢ㄧ偣瀵瑰簲鐨勯偅涓�鏉� TAC 鐨� `id`.
     */
    private Map<Pair, Set<Integer>> DUChain;

    public BasicBlock() {
        def = new TreeSet<Temp>(Temp.ID_COMPARATOR);
        hasDefined = new TreeSet<Temp>(Temp.ID_COMPARATOR);
        liveUse = new TreeSet<Temp>(Temp.ID_COMPARATOR);
        liveIn = new TreeSet<Temp>(Temp.ID_COMPARATOR);
        liveOut = new TreeSet<Temp>(Temp.ID_COMPARATOR);
        liveUsePair = new TreeSet<Pair>(Pair.COMPARATOR);
        liveInPair = new TreeSet<Pair>(Pair.COMPARATOR);
        liveOutPair = new TreeSet<Pair>(Pair.COMPARATOR);
        next = new int[2];
        asms = new ArrayList<Asm>();

        DUChain = new TreeMap<Pair, Set<Integer>>(Pair.COMPARATOR);
    }

    public void allocateTacIds() {
        for (Tac tac = tacList; tac != null; tac = tac.next) {
            tac.id = IDAllocator.apply();
        }
        endId = IDAllocator.apply();
    }

    public void computeDefAndLiveUse() {
        for (Tac tac = tacList; tac != null; tac = tac.next) {
            switch (tac.opc) {
                case ADD:
                case SUB:
                case MUL:
                case DIV:
                case MOD:
                case LAND:
                case LOR:
                case GTR:
                case GEQ:
                case EQU:
                case NEQ:
                case LEQ:
                case LES:
                /* use op1 and op2, def op0 */
                	//System.out.println(tac.opc);
                    if (tac.op1.lastVisitedBB != bbNum) {
                        liveUse.add(tac.op1);                       
                        tac.op1.lastVisitedBB = bbNum;
                    }
                    if (!hasDefined.contains(tac.op1))
                    {
                    	liveUsePair.add(new Pair(tac.id, tac.op1));
                    }
                    
                    if (tac.op2.lastVisitedBB != bbNum) {
                        liveUse.add(tac.op2);                        
                        tac.op2.lastVisitedBB = bbNum;
                    }
                    if (!hasDefined.contains(tac.op2))
                    {
                    	liveUsePair.add(new Pair(tac.id, tac.op2));
                    }
                    if (tac.op0.lastVisitedBB != bbNum) {
                        def.add(tac.op0);
                        tac.op0.lastVisitedBB = bbNum;
                    }
                    hasDefined.add(tac.op0);
                    break;
                case NEG:
                case LNOT:
                case ASSIGN:
                case INDIRECT_CALL:
                case LOAD:
				/* use op1, def op0 */
                    if (tac.op1.lastVisitedBB != bbNum) {
                        liveUse.add(tac.op1);                        
                        tac.op1.lastVisitedBB = bbNum;
                    }
                    if (!hasDefined.contains(tac.op1))
                    {
                    	liveUsePair.add(new Pair(tac.id, tac.op1));
                    }
                    if (tac.op0 != null && tac.op0.lastVisitedBB != bbNum) {  // in INDIRECT_CALL with return type VOID,
                        // tac.op0 is null
                        def.add(tac.op0);
                        tac.op0.lastVisitedBB = bbNum;
                    }
                    if (tac.op0 != null)
                    {
                    	hasDefined.add(tac.op0);
                    }
                    
                    break;
                case LOAD_VTBL:
                case DIRECT_CALL:
                case RETURN:
                case LOAD_STR_CONST:
                case LOAD_IMM4:
				/* def op0 */
                    if (tac.op0 != null && tac.op0.lastVisitedBB != bbNum) {  // in DIRECT_CALL with return type VOID,
                        // tac.op0 is null
                        def.add(tac.op0);
                        tac.op0.lastVisitedBB = bbNum;
                    }
                    if (tac.op0 != null)
                    {
                    	hasDefined.add(tac.op0);
                    }
                    
                    break;
                case STORE:
				/* use op0 and op1*/
                    if (tac.op0.lastVisitedBB != bbNum) {
                        liveUse.add(tac.op0);                        
                        tac.op0.lastVisitedBB = bbNum;
                    }
                    if (!hasDefined.contains(tac.op0))
                    {
                    	liveUsePair.add(new Pair(tac.id, tac.op0));
                    }
                    if (tac.op1.lastVisitedBB != bbNum) {
                        liveUse.add(tac.op1);                        
                        tac.op1.lastVisitedBB = bbNum;
                    }
                    if (!hasDefined.contains(tac.op1))
                    {
                    	liveUsePair.add(new Pair(tac.id, tac.op1));
                    }
                    break;
                case PARM:
				/* use op0 */
                    if (tac.op0.lastVisitedBB != bbNum) {
                        liveUse.add(tac.op0);
                        tac.op0.lastVisitedBB = bbNum;
                    }
                    if (!hasDefined.contains(tac.op0))
                    {
                    	liveUsePair.add(new Pair(tac.id, tac.op0));
                    }
                    break;
                default:
				/* BRANCH MEMO MARK PARM*/
                    break;
            }
        }
        if (var != null && var.lastVisitedBB != bbNum) {
            liveUse.add(var);
            var.lastVisitedBB = bbNum;
        }
        if (var != null && !hasDefined.contains(var))
        {
        	liveUsePair.add(new Pair(endId, var));
        }
        //System.out.println(liveUsePair);
        //System.out.println(hasDefined);
        liveIn.addAll(liveUse);
        liveInPair.addAll(liveUsePair);
    }

    public void analyzeLiveness() {
        if (tacList == null)
            return;
        Tac tac = tacList;
        for (; tac.next != null; tac = tac.next) ;

        tac.liveOut = new HashSet<Temp>(liveOut);
        tac.liveOutPair = new HashSet<Pair>(liveOutPair);
        if (var != null)
            tac.liveOut.add(var);
        	tac.liveOutPair.add(new Pair(endId, var));
        for (; tac != tacList; tac = tac.prev) {
        	Pair pair = new Pair(tac.id, tac.op0);
        	Set<Integer> set = new TreeSet<Integer>();
            tac.prev.liveOut = new HashSet<Temp>(tac.liveOut);
            tac.prev.liveOutPair = new HashSet<Pair>(tac.liveOutPair);
            final Temp op = tac.op0;
            //Set<Pair> removeSet = new TreeSet<Pair>(Pair.COMPARATOR);
            switch (tac.opc) {
                case ADD:
                case SUB:
                case MUL:
                case DIV:
                case MOD:
                case LAND:
                case LOR:
                case GTR:
                case GEQ:
                case EQU:
                case NEQ:
                case LEQ:
                case LES:
				/* use op1 and op2, def op0 */
                	if(tac.op0 != null)
                	{
                        tac.prev.liveOut.remove(tac.op0);
                        tac.prev.liveOutPair.removeIf(x -> x.tmp == op);
                        for(Iterator<Pair> iterator = tac.liveOutPair.iterator(); iterator.hasNext();)
                        {
                        	Pair temp_pair = iterator.next();
                        	if(temp_pair.tmp == op)
                        	{
                        		set.add(temp_pair.pos);
                        	}                    	
                        }
                        DUChain.put(pair, set);
                	}

//                    for(Iterator<Pair> iterator = tac.prev.liveOutPair.iterator(); iterator.hasNext();)
//                    {
//                    	Pair temp_pair = iterator.next();
//                    	if(temp_pair.tmp == op)
//                    	{
//                    		removeSet.add(temp_pair);
//                    	}
//                    }
//                    tac.prev.liveOutPair.removeAll(removeSet);
                    tac.prev.liveOut.add(tac.op1);
                    tac.prev.liveOutPair.add(new Pair(tac.id, tac.op1));
                    tac.prev.liveOut.add(tac.op2);
                    tac.prev.liveOutPair.add(new Pair(tac.id, tac.op2));
                    break;
                case NEG:
                case LNOT:
                case ASSIGN:
                case INDIRECT_CALL:
                case LOAD:
				/* use op1, def op0 */
                	if(tac.op0 != null)
                	{
                        tac.prev.liveOut.remove(tac.op0);
                        tac.prev.liveOutPair.removeIf(x -> x.tmp == op);
                        for(Iterator<Pair> iterator = tac.liveOutPair.iterator(); iterator.hasNext();)
                        {
                        	Pair temp_pair = iterator.next();
                        	if(temp_pair.tmp == op)
                        	{
                        		set.add(temp_pair.pos);
                        	}                    	
                        }
                        DUChain.put(pair, set);
                	}
//                    for(Iterator<Pair> iterator = tac.prev.liveOutPair.iterator(); iterator.hasNext();)
//                    {
//                    	Pair temp_pair = iterator.next();
//                    	//System.out.println(temp_pair);
//                    	if(temp_pair.tmp == op)
//                    	{
//                    		removeSet.add(temp_pair);
//                    	}
//                    }
//                    tac.prev.liveOutPair.removeAll(removeSet);
                    tac.prev.liveOut.add(tac.op1);
                    tac.prev.liveOutPair.add(new Pair(tac.id, tac.op1));
                    break;
                case LOAD_VTBL:
                case DIRECT_CALL:
                case RETURN:
                case LOAD_STR_CONST:
                case LOAD_IMM4:
				/* def op0 */
                	if(tac.op0 != null)
                	{
                        tac.prev.liveOut.remove(tac.op0);
                        tac.prev.liveOutPair.removeIf(x -> x.tmp == op);
                        for(Iterator<Pair> iterator = tac.liveOutPair.iterator(); iterator.hasNext();)
                        {
                        	Pair temp_pair = iterator.next();
                        	if(temp_pair.tmp == op)
                        	{
                        		set.add(temp_pair.pos);
                        	}                    	
                        }
                        DUChain.put(pair, set);
                	}
//                    for(Iterator<Pair> iterator = tac.prev.liveOutPair.iterator(); iterator.hasNext();)
//                    {
//                    	Pair temp_pair = iterator.next();
//                    	
//                    	if(temp_pair.tmp == op)
//                    	{
//                    		removeSet.add(temp_pair);
//                    	}
//                    }
//                    tac.prev.liveOutPair.removeAll(removeSet);
                    break;
                case STORE:
				/* use op0 and op1*/
                    tac.prev.liveOut.add(tac.op0);
                    tac.prev.liveOutPair.add(new Pair(tac.id, tac.op0));
                    tac.prev.liveOut.add(tac.op1);
                    tac.prev.liveOutPair.add(new Pair(tac.id, tac.op1));
                    break;
                case BEQZ:
                case BNEZ:
                case PARM:
				/* use op0 */
                    tac.prev.liveOut.add(tac.op0);
                    tac.prev.liveOutPair.add(new Pair(tac.id, tac.op0));
                    //System.out.println(new Pair(tac.id, tac.op0));
                    break;
                default:
				/* BRANCH MEMO MARK PARM*/
                    break;
            }
        }
        tac = tacList;
    	Pair pair = new Pair(tac.id, tac.op0);
    	Set<Integer> set = new TreeSet<Integer>();
        final Temp op = tac.op0;
    	if(tac.op0 == null)
    	{
    		return;
    	}
    	switch (tac.opc) {
	        case ADD:
	        case SUB:
	        case MUL:
	        case DIV:
	        case MOD:
	        case LAND:
	        case LOR:
	        case GTR:
	        case GEQ:
	        case EQU:
	        case NEQ:
	        case LEQ:
	        case LES:
			/* use op1 and op2, def op0 */
	            for(Iterator<Pair> iterator = tac.liveOutPair.iterator(); iterator.hasNext();)
	            {
	            	Pair temp_pair = iterator.next();
	            	if(temp_pair.tmp == op)
	            	{
	            		set.add(temp_pair.pos);
	            	}                    	
	            }
	            DUChain.put(pair, set);
	            break;
	        case NEG:
	        case LNOT:
	        case ASSIGN:
	        case INDIRECT_CALL:
	        case LOAD:
			/* use op1, def op0 */
	            for(Iterator<Pair> iterator = tac.liveOutPair.iterator(); iterator.hasNext();)
	            {
	            	Pair temp_pair = iterator.next();
	            	if(temp_pair.tmp == op)
	            	{
	            		set.add(temp_pair.pos);
	            	}                    	
	            }
	            DUChain.put(pair, set);
	            break;
	        case LOAD_VTBL:
	        case DIRECT_CALL:
	        case RETURN:
	        case LOAD_STR_CONST:
	        case LOAD_IMM4:
			/* def op0 */
	            for(Iterator<Pair> iterator = tac.liveOutPair.iterator(); iterator.hasNext();)
	            {
	            	Pair temp_pair = iterator.next();
	            	if(temp_pair.tmp == op)
	            	{
	            		set.add(temp_pair.pos);
	            	}                    	
	            }
	            DUChain.put(pair, set);
	            break;
	        case STORE:
			/* use op0 and op1*/
	            break;
	        case BEQZ:
	        case BNEZ:
	        case PARM:
			/* use op0 */
	            //System.out.println(new Pair(tac.id, tac.op0));
	            break;
	        default:
			/* BRANCH MEMO MARK PARM*/
	            break;
	    }

    	
    }

    public void printTo(PrintWriter pw) {
        pw.println("BASIC BLOCK " + bbNum + " : ");
        for (Tac t = tacList; t != null; t = t.next) {
            pw.println("    " + t);
        }
        switch (endKind) {
            case BY_BRANCH:
                pw.println("END BY BRANCH, goto " + next[0]);
                break;
            case BY_BEQZ:
                pw.println("END BY BEQZ, if " + var.name + " = ");
                pw.println("    0 : goto " + next[0] + "; 1 : goto " + next[1]);
                break;
            case BY_BNEZ:
                pw.println("END BY BGTZ, if " + var.name + " = ");
                pw.println("    1 : goto " + next[0] + "; 0 : goto " + next[1]);
                break;
            case BY_RETURN:
                if (var != null) {
                    pw.println("END BY RETURN, result = " + var.name);
                } else {
                    pw.println("END BY RETURN, void result");
                }
                break;
        }
    }

    public void printLivenessTo(PrintWriter pw) {
        pw.println("BASIC BLOCK " + bbNum + " : ");
        pw.println("  Def     = " + toString(def));
        pw.println("  liveUse = " + toString(liveUse));
        pw.println("  liveIn  = " + toString(liveIn));
        pw.println("  liveOut = " + toString(liveOut));

        for (Tac t = tacList; t != null; t = t.next) {
            pw.println("    " + t + " " + toString(t.liveOut));
        }

        switch (endKind) {
            case BY_BRANCH:
                pw.println("END BY BRANCH, goto " + next[0]);
                break;
            case BY_BEQZ:
                pw.println("END BY BEQZ, if " + var.name + " = ");
                pw.println("    0 : goto " + next[0] + "; 1 : goto " + next[1]);
                break;
            case BY_BNEZ:
                pw.println("END BY BGTZ, if " + var.name + " = ");
                pw.println("    1 : goto " + next[0] + "; 0 : goto " + next[1]);
                break;
            case BY_RETURN:
                if (var != null) {
                    pw.println("END BY RETURN, result = " + var.name);
                } else {
                    pw.println("END BY RETURN, void result");
                }
                break;
        }
    }

    public void printDUChainTo(PrintWriter pw) {
        pw.println("BASIC BLOCK " + bbNum + " : ");

        for (Tac t = tacList; t != null; t = t.next) {
            pw.print(t.id + "\t" + t);

            Pair pair = null;
            switch (t.opc) {
                case ADD:
                case SUB:
                case MUL:
                case DIV:
                case MOD:
                case LAND:
                case LOR:
                case GTR:
                case GEQ:
                case EQU:
                case NEQ:
                case LEQ:
                case LES:
                case NEG:
                case LNOT:
                case ASSIGN:
                case INDIRECT_CALL:
                case LOAD:
                case LOAD_VTBL:
                case DIRECT_CALL:
                case RETURN:
                case LOAD_STR_CONST:
                case LOAD_IMM4:
                    if (t.op0 != null) {
                        pair = new Pair(t.id, t.op0);
                    }
                    break;
                case STORE:
                case BEQZ:
                case BNEZ:
                case PARM:
                    break;
                default:
				/* BRANCH MEMO MARK PARM */
                    break;
            }

            if (pair == null) {
                pw.println();
            } else {
                pw.print(" [ ");
                if (pair != null) {
                    Set<Integer> locations = DUChain.get(pair);
                    if (locations != null) {
                        for (Integer loc : locations) {
                            pw.print(loc + " ");
                        }
                    }
                }
                pw.println("]");
            }
        }

        pw.print(endId + "\t");
        switch (endKind) {
            case BY_BRANCH:
                pw.println("END BY BRANCH, goto " + next[0]);
                break;
            case BY_BEQZ:
                pw.println("END BY BEQZ, if " + var.name + " = ");
                pw.println("\t    0 : goto " + next[0] + "; 1 : goto " + next[1]);
                break;
            case BY_BNEZ:
                pw.println("END BY BGTZ, if " + var.name + " = ");
                pw.println("\t    1 : goto " + next[0] + "; 0 : goto " + next[1]);
                break;
            case BY_RETURN:
                if (var != null) {
                    pw.println("END BY RETURN, result = " + var.name);
                } else {
                    pw.println("END BY RETURN, void result");
                }
                break;
        }
    }

    public String toString(Set<Temp> set) {
        StringBuilder sb = new StringBuilder("[ ");
        for (Temp t : set) {
            sb.append(t.name + " ");
        }
        sb.append(']');
        return sb.toString();
    }

    public void insertBefore(Tac insert, Tac base) {
        if (base == tacList) {
            tacList = insert;
        } else {
            base.prev.next = insert;
        }
        insert.prev = base.prev;
        base.prev = insert;
        insert.next = base;
    }

    public void insertAfter(Tac insert, Tac base) {
        if (tacList == null) {
            tacList = insert;
            insert.next = null;
            return;
        }
        if (base.next != null) {
            base.next.prev = insert;
        }
        insert.prev = base;
        insert.next = base.next;
        base.next = insert;
    }

    public void appendAsm(Asm asm) {
        asms.add(asm);
    }

    public List<Asm> getAsms() {
        return asms;
    }
}
