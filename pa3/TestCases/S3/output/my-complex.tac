VTABLE(_Computer) {
    <empty>
    Computer
    _Computer.Crash;
}

VTABLE(_Mac) {
    _Computer
    Mac
    _Computer.Crash;
    _Mac.add;
}

VTABLE(_MM) {
    _Mac
    MM
    _MM.Crash;
    _Mac.add;
}

VTABLE(_Main) {
    <empty>
    Main
}

FUNCTION(_Computer_New) {
memo ''
_Computer_New:
    _T6 = 8
    parm _T6
    _T7 =  call _Alloc
    _T8 = 0
    *(_T7 + 4) = _T8
    _T9 = VTBL <_Computer>
    *(_T7 + 0) = _T9
    return _T7
}

FUNCTION(_Mac_New) {
memo ''
_Mac_New:
    _T10 = 12
    parm _T10
    _T11 =  call _Alloc
    _T12 = 0
    *(_T11 + 4) = _T12
    *(_T11 + 8) = _T12
    _T13 = VTBL <_Mac>
    *(_T11 + 0) = _T13
    return _T11
}

FUNCTION(_MM_New) {
memo ''
_MM_New:
    _T14 = 12
    parm _T14
    _T15 =  call _Alloc
    _T16 = 0
    *(_T15 + 4) = _T16
    *(_T15 + 8) = _T16
    _T17 = VTBL <_MM>
    *(_T15 + 0) = _T17
    return _T15
}

FUNCTION(_Main_New) {
memo ''
_Main_New:
    _T18 = 4
    parm _T18
    _T19 =  call _Alloc
    _T20 = VTBL <_Main>
    *(_T19 + 0) = _T20
    return _T19
}

FUNCTION(_Computer.Crash) {
memo '_T0:4 _T1:8'
_Computer.Crash:
    _T22 = 0
    _T21 = _T22
    branch _L16
_L17:
    _T23 = 1
    _T24 = (_T21 + _T23)
    _T21 = _T24
_L16:
    _T25 = (_T21 < _T1)
    if (_T25 == 0) branch _L18
    _T26 = "sad\n"
    parm _T26
    call _PrintString
    branch _L17
_L18:
}

FUNCTION(_Mac.add) {
memo '_T2:4 _T3:8'
_Mac.add:
    parm _T2
    parm _T3
    _T27 = *(_T2 + 0)
    _T28 = *(_T2 + 0)
    _T29 = *(_T28 + 0)
    *(_T2 + 0) = _T29
    _T30 = *(_T2 + 0)
    _T31 = *(_T30 + 8)
    call _T31
    *(_T2 + 0) = _T27
    _T32 = "ack!"
    parm _T32
    call _PrintString
}

FUNCTION(_MM.Crash) {
memo '_T4:4 _T5:8'
_MM.Crash:
    _T33 = "yes\n"
    parm _T33
    call _PrintString
    _T34 = 1
    _T35 = (_T5 - _T34)
    parm _T4
    parm _T35
    _T36 = *(_T4 + 0)
    _T37 = *(_T4 + 0)
    _T38 = *(_T37 + 0)
    *(_T4 + 0) = _T38
    _T39 = *(_T4 + 0)
    _T40 = *(_T39 + 0)
    *(_T4 + 0) = _T40
    _T41 = *(_T4 + 0)
    _T42 = *(_T41 + 8)
    call _T42
    *(_T4 + 0) = _T36
}

FUNCTION(main) {
memo ''
main:
    _T44 =  call _MM_New
    _T43 = _T44
    _T45 = 2
    parm _T43
    parm _T45
    _T46 = *(_T43 + 0)
    _T47 = *(_T43 + 0)
    _T48 = *(_T47 + 8)
    call _T48
    *(_T43 + 0) = _T46
}

