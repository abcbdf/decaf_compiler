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
    _T8 = 6
    _T3 = _T8
    _T9 = 2
    _T4 = _T9
    _T10 = 3
    _T5 = _T10
    _T11 = 3
    _T12 = (_T3 * _T11)
    _T14 = 0
    _T15 = (_T4 + _T5)
    _T16 = (_T12 == _T14)
    if (_T16 == 0) branch _L11
    _T13 = _T15
    branch _L10
_L11:
    _T17 = 3
    _T18 = 3
    _T19 = (_T4 + _T18)
    _T20 = (_T12 == _T17)
    if (_T20 == 0) branch _L12
    _T13 = _T19
    branch _L10
_L12:
    _T21 = 9
    _T22 = 2
    _T23 = (_T5 * _T22)
    _T24 = 6
    _T25 = (_T23 + _T24)
    _T26 = (_T12 == _T21)
    if (_T26 == 0) branch _L13
    _T13 = _T25
    branch _L10
_L13:
    _T27 = 100
    _T13 = _T27
_L10:
    _T4 = _T13
    parm _T4
    call _PrintInt
    _T28 = "\n"
    parm _T28
    call _PrintString
    _T29 = 3
    _T6 = _T29
    _T31 = 0
    _T32 = (_T4 + _T5)
    _T33 = (_T6 == _T31)
    if (_T33 == 0) branch _L15
    _T30 = _T32
    branch _L14
_L15:
    _T34 = 3
    _T35 = 3
    _T36 = (_T4 + _T35)
    _T37 = (_T6 == _T34)
    if (_T37 == 0) branch _L16
    _T30 = _T36
    branch _L14
_L16:
    _T38 = 6
    _T39 = 2
    _T40 = (_T5 * _T39)
    _T41 = 6
    _T42 = (_T40 + _T41)
    _T43 = (_T6 == _T38)
    if (_T43 == 0) branch _L17
    _T30 = _T42
    branch _L14
_L17:
    _T44 = 100
    _T30 = _T44
_L14:
    _T4 = _T30
    parm _T4
    call _PrintInt
    _T45 = "\n"
    parm _T45
    call _PrintString
    _T47 = 0
    _T48 = (_T4 + _T5)
    _T49 = (_T3 == _T47)
    if (_T49 == 0) branch _L19
    _T46 = _T48
    branch _L18
_L19:
    _T50 = 3
    _T51 = 3
    _T52 = (_T4 + _T51)
    _T53 = (_T3 == _T50)
    if (_T53 == 0) branch _L20
    _T46 = _T52
    branch _L18
_L20:
    _T54 = 6
    _T55 = 2
    _T56 = (_T5 * _T55)
    _T57 = 6
    _T58 = (_T56 + _T57)
    _T59 = (_T3 == _T54)
    if (_T59 == 0) branch _L21
    _T46 = _T58
    branch _L18
_L21:
    _T60 = 100
    _T46 = _T60
_L18:
    _T4 = _T46
    parm _T4
    call _PrintInt
    _T61 = "\n"
    parm _T61
    call _PrintString
    _T62 = 6
    _T63 = (_T3 - _T62)
    _T65 = 0
    _T66 = (_T4 + _T5)
    _T67 = (_T63 == _T65)
    if (_T67 == 0) branch _L23
    _T64 = _T66
    branch _L22
_L23:
    _T68 = 3
    _T69 = 3
    _T70 = (_T4 + _T69)
    _T71 = (_T63 == _T68)
    if (_T71 == 0) branch _L24
    _T64 = _T70
    branch _L22
_L24:
    _T72 = 9
    _T73 = 2
    _T74 = (_T5 * _T73)
    _T75 = 6
    _T76 = (_T74 + _T75)
    _T77 = (_T63 == _T72)
    if (_T77 == 0) branch _L25
    _T64 = _T76
    branch _L22
_L25:
    _T78 = 100
    _T64 = _T78
_L22:
    _T4 = _T64
    parm _T4
    call _PrintInt
    _T79 = "\n"
    parm _T79
    call _PrintString
    _T81 = 0
    _T82 = (_T4 + _T5)
    _T83 = (_T3 == _T81)
    if (_T83 == 0) branch _L27
    _T80 = _T82
    branch _L26
_L27:
    _T84 = 3
    _T85 = 3
    _T86 = (_T4 + _T85)
    _T87 = (_T3 == _T84)
    if (_T87 == 0) branch _L28
    _T80 = _T86
    branch _L26
_L28:
    _T88 = 6
    _T89 = 2
    _T90 = (_T5 * _T89)
    _T91 = 6
    _T92 = (_T90 + _T91)
    _T93 = (_T3 == _T88)
    if (_T93 == 0) branch _L29
    _T80 = _T92
    branch _L26
_L29:
    _T94 = 100
    _T80 = _T94
_L26:
    _T95 = 8
    parm _T95
    _T96 =  call _Alloc
    _T97 = 0
    *(_T96 + 0) = _T80
    *(_T96 + 4) = _T97
    _T7 = _T96
    _T98 = *(_T7 + 0)
    parm _T98
    call _PrintInt
    _T99 = "+"
    parm _T99
    call _PrintString
    _T100 = *(_T7 + 4)
    parm _T100
    call _PrintInt
    _T101 = "j"
    parm _T101
    call _PrintString
    _T102 = "\n"
    parm _T102
    call _PrintString
    _T104 = 8
    _T105 = (_T4 + _T5)
    _T106 = (_T3 == _T104)
    if (_T106 == 0) branch _L31
    _T103 = _T105
    branch _L30
_L31:
    _T107 = 3
    _T108 = (_T4 + _T3)
    _T109 = (_T3 == _T107)
    if (_T109 == 0) branch _L32
    _T103 = _T108
    branch _L30
_L32:
    _T110 = 0
    _T111 = 8
    _T112 = (_T3 == _T110)
    if (_T112 == 0) branch _L33
    _T103 = _T111
    branch _L30
_L33:
    _T113 = 100
    _T103 = _T113
_L30:
    _T114 = 8
    parm _T114
    _T115 =  call _Alloc
    _T116 = 0
    *(_T115 + 0) = _T103
    *(_T115 + 4) = _T116
    _T7 = _T115
    _T117 = *(_T7 + 0)
    parm _T117
    call _PrintInt
    _T118 = "+"
    parm _T118
    call _PrintString
    _T119 = *(_T7 + 4)
    parm _T119
    call _PrintInt
    _T120 = "j"
    parm _T120
    call _PrintString
    _T121 = "\n"
    parm _T121
    call _PrintString
}

