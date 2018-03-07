VTABLE(_Mac) {
    <empty>
    Mac
    _Mac.Crash;
}

VTABLE(_Main) {
    <empty>
    Main
}

FUNCTION(_Mac_New) {
memo ''
_Mac_New:
    _T4 = 12
    parm _T4
    _T5 =  call _Alloc
    _T6 = 0
    *(_T5 + 4) = _T6
    *(_T5 + 8) = _T6
    _T7 = VTBL <_Mac>
    *(_T5 + 0) = _T7
    return _T5
}

FUNCTION(_Main_New) {
memo ''
_Main_New:
    _T8 = 4
    parm _T8
    _T9 =  call _Alloc
    _T10 = VTBL <_Main>
    *(_T9 + 0) = _T10
    return _T9
}

FUNCTION(_Mac.Crash) {
memo '_T0:4 _T1:8 _T2:12 _T3:16'
_Mac.Crash:
    _T11 = *(_T0 + 8)
    *(_T0 + 8) = _T1
    _T12 = *(_T0 + 4)
    *(_T0 + 4) = _T2
    _T13 = *(_T0 + 8)
    parm _T13
    call _PrintInt
    _T14 = "\n"
    parm _T14
    call _PrintString
    parm _T3
    call _PrintInt
    _T15 = "\n"
    parm _T15
    call _PrintString
    _T16 = *(_T0 + 4)
    _T17 = *(_T16 + 0)
    parm _T17
    call _PrintInt
    _T18 = "+"
    parm _T18
    call _PrintString
    _T19 = *(_T16 + 4)
    parm _T19
    call _PrintInt
    _T20 = "j"
    parm _T20
    call _PrintString
}

FUNCTION(main) {
memo ''
main:
    _T22 =  call _Mac_New
    _T21 = _T22
    _T23 = 2
    _T24 = 3
    _T25 = 8
    parm _T25
    _T26 =  call _Alloc
    _T27 = 4
    _T28 = 0
    *(_T26 + 0) = _T28
    *(_T26 + 4) = _T27
    _T29 = 8
    parm _T29
    _T30 =  call _Alloc
    _T31 = 0
    *(_T30 + 0) = _T24
    *(_T30 + 4) = _T31
    _T32 = 8
    parm _T32
    _T33 =  call _Alloc
    _T34 = *(_T30 + 0)
    _T35 = *(_T26 + 0)
    _T36 = (_T34 + _T35)
    _T37 = *(_T30 + 4)
    _T38 = *(_T26 + 4)
    _T39 = (_T37 + _T38)
    *(_T33 + 0) = _T36
    *(_T33 + 4) = _T39
    _T40 = 5
    parm _T21
    parm _T23
    parm _T33
    parm _T40
    _T41 = *(_T21 + 0)
    _T42 = *(_T21 + 0)
    _T43 = *(_T42 + 8)
    call _T43
    *(_T21 + 0) = _T41
}

