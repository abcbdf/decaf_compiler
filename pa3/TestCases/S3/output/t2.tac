VTABLE(_Main) {
    <empty>
    Main
}

FUNCTION(_Main_New) {
memo ''
_Main_New:
    _T0 = 4
    parm _T0
    _T1 =  call _Alloc
    _T2 = VTBL <_Main>
    *(_T1 + 0) = _T2
    return _T1
}

FUNCTION(main) {
memo ''
main:
    _T7 = 1
    _T5 = _T7
    _T8 = "wow!"
    _T4 = _T8
    _T9 = 3
    _T3 = _T9
    _T10 = 1
    _T11 = 8
    parm _T11
    _T12 =  call _Alloc
    _T13 = 3
    _T14 = 0
    *(_T12 + 0) = _T14
    *(_T12 + 4) = _T13
    _T15 = 8
    parm _T15
    _T16 =  call _Alloc
    _T17 = 0
    *(_T16 + 0) = _T10
    *(_T16 + 4) = _T17
    _T18 = 8
    parm _T18
    _T19 =  call _Alloc
    _T20 = *(_T16 + 0)
    _T21 = *(_T12 + 0)
    _T22 = (_T20 + _T21)
    _T23 = *(_T16 + 4)
    _T24 = *(_T12 + 4)
    _T25 = (_T23 + _T24)
    *(_T19 + 0) = _T22
    *(_T19 + 4) = _T25
    _T6 = _T19
    if (_T5 == 0) branch _L10
    _T26 = 5
    _T27 = (_T3 * _T26)
    _T3 = _T27
_L10:
    parm _T5
    call _PrintBool
    _T28 = " "
    parm _T28
    call _PrintString
    parm _T3
    call _PrintInt
}

