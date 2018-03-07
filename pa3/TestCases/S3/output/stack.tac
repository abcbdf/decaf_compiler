VTABLE(_Stack) {
    <empty>
    Stack
    _Stack.Init;
    _Stack.Push;
    _Stack.Pop;
    _Stack.NumElems;
}

VTABLE(_Main) {
    <empty>
    Main
}

FUNCTION(_Stack_New) {
memo ''
_Stack_New:
    _T5 = 12
    parm _T5
    _T6 =  call _Alloc
    _T7 = 0
    *(_T6 + 4) = _T7
    *(_T6 + 8) = _T7
    _T8 = VTBL <_Stack>
    *(_T6 + 0) = _T8
    return _T6
}

FUNCTION(_Main_New) {
memo ''
_Main_New:
    _T9 = 4
    parm _T9
    _T10 =  call _Alloc
    _T11 = VTBL <_Main>
    *(_T10 + 0) = _T11
    return _T10
}

FUNCTION(_Stack.Init) {
memo '_T0:4'
_Stack.Init:
    _T12 = *(_T0 + 8)
    _T13 = 100
    _T14 = 0
    _T15 = (_T13 < _T14)
    if (_T15 == 0) branch _L16
    _T16 = "Decaf runtime error: Cannot create negative-sized array\n"
    parm _T16
    call _PrintString
    call _Halt
_L16:
    _T17 = 4
    _T18 = (_T17 * _T13)
    _T19 = (_T17 + _T18)
    parm _T19
    _T20 =  call _Alloc
    *(_T20 + 0) = _T13
    _T21 = 0
    _T20 = (_T20 + _T19)
_L17:
    _T19 = (_T19 - _T17)
    if (_T19 == 0) branch _L18
    _T20 = (_T20 - _T17)
    *(_T20 + 0) = _T21
    branch _L17
_L18:
    *(_T0 + 8) = _T20
    _T22 = *(_T0 + 4)
    _T23 = 0
    *(_T0 + 4) = _T23
    _T24 = 3
    parm _T0
    parm _T24
    _T25 = *(_T0 + 0)
    _T26 = *(_T0 + 0)
    _T27 = *(_T26 + 12)
    call _T27
    *(_T0 + 0) = _T25
}

FUNCTION(_Stack.Push) {
memo '_T1:4 _T2:8'
_Stack.Push:
    _T28 = *(_T1 + 8)
    _T29 = *(_T1 + 4)
    _T30 = *(_T28 - 4)
    _T31 = (_T29 < _T30)
    if (_T31 == 0) branch _L19
    _T32 = 0
    _T33 = (_T29 < _T32)
    if (_T33 == 0) branch _L20
_L19:
    _T34 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T34
    call _PrintString
    call _Halt
_L20:
    _T35 = 4
    _T36 = (_T29 * _T35)
    _T37 = (_T28 + _T36)
    _T38 = *(_T37 + 0)
    _T39 = 4
    _T40 = (_T29 * _T39)
    _T41 = (_T28 + _T40)
    *(_T41 + 0) = _T2
    _T42 = *(_T1 + 4)
    _T43 = *(_T1 + 4)
    _T44 = 1
    _T45 = (_T43 + _T44)
    *(_T1 + 4) = _T45
}

FUNCTION(_Stack.Pop) {
memo '_T3:4'
_Stack.Pop:
    _T47 = *(_T3 + 8)
    _T48 = *(_T3 + 4)
    _T49 = 1
    _T50 = (_T48 - _T49)
    _T51 = *(_T47 - 4)
    _T52 = (_T50 < _T51)
    if (_T52 == 0) branch _L21
    _T53 = 0
    _T54 = (_T50 < _T53)
    if (_T54 == 0) branch _L22
_L21:
    _T55 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T55
    call _PrintString
    call _Halt
_L22:
    _T56 = 4
    _T57 = (_T50 * _T56)
    _T58 = (_T47 + _T57)
    _T59 = *(_T58 + 0)
    _T46 = _T59
    _T60 = *(_T3 + 4)
    _T61 = *(_T3 + 4)
    _T62 = 1
    _T63 = (_T61 - _T62)
    *(_T3 + 4) = _T63
    return _T46
}

FUNCTION(_Stack.NumElems) {
memo '_T4:4'
_Stack.NumElems:
    _T64 = *(_T4 + 4)
    return _T64
}

FUNCTION(_Stack.main) {
memo ''
_Stack.main:
    _T66 =  call _Stack_New
    _T65 = _T66
    parm _T65
    _T67 = *(_T65 + 0)
    _T68 = *(_T65 + 0)
    _T69 = *(_T68 + 8)
    call _T69
    *(_T65 + 0) = _T67
    _T70 = 3
    parm _T65
    parm _T70
    _T71 = *(_T65 + 0)
    _T72 = *(_T65 + 0)
    _T73 = *(_T72 + 12)
    call _T73
    *(_T65 + 0) = _T71
    _T74 = 7
    parm _T65
    parm _T74
    _T75 = *(_T65 + 0)
    _T76 = *(_T65 + 0)
    _T77 = *(_T76 + 12)
    call _T77
    *(_T65 + 0) = _T75
    _T78 = 4
    parm _T65
    parm _T78
    _T79 = *(_T65 + 0)
    _T80 = *(_T65 + 0)
    _T81 = *(_T80 + 12)
    call _T81
    *(_T65 + 0) = _T79
    parm _T65
    _T82 = *(_T65 + 0)
    _T83 = *(_T65 + 0)
    _T84 = *(_T83 + 20)
    _T85 =  call _T84
    *(_T65 + 0) = _T82
    parm _T85
    call _PrintInt
    _T86 = " "
    parm _T86
    call _PrintString
    parm _T65
    _T87 = *(_T65 + 0)
    _T88 = *(_T65 + 0)
    _T89 = *(_T88 + 16)
    _T90 =  call _T89
    *(_T65 + 0) = _T87
    parm _T90
    call _PrintInt
    _T91 = " "
    parm _T91
    call _PrintString
    parm _T65
    _T92 = *(_T65 + 0)
    _T93 = *(_T65 + 0)
    _T94 = *(_T93 + 16)
    _T95 =  call _T94
    *(_T65 + 0) = _T92
    parm _T95
    call _PrintInt
    _T96 = " "
    parm _T96
    call _PrintString
    parm _T65
    _T97 = *(_T65 + 0)
    _T98 = *(_T65 + 0)
    _T99 = *(_T98 + 16)
    _T100 =  call _T99
    *(_T65 + 0) = _T97
    parm _T100
    call _PrintInt
    _T101 = " "
    parm _T101
    call _PrintString
    parm _T65
    _T102 = *(_T65 + 0)
    _T103 = *(_T65 + 0)
    _T104 = *(_T103 + 20)
    _T105 =  call _T104
    *(_T65 + 0) = _T102
    parm _T105
    call _PrintInt
}

FUNCTION(main) {
memo ''
main:
    call _Stack.main
}

