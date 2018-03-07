VTABLE(_Main) {
    <empty>
    Main
}

VTABLE(_animal) {
    <empty>
    animal
    _animal.setage;
    _animal.getage;
}

VTABLE(_people) {
    <empty>
    people
    _people.setaniage;
    _people.getage;
    _people.setage;
}

FUNCTION(_Main_New) {
memo ''
_Main_New:
    _T7 = 4
    parm _T7
    _T8 =  call _Alloc
    _T9 = VTBL <_Main>
    *(_T8 + 0) = _T9
    return _T8
}

FUNCTION(_animal_New) {
memo ''
_animal_New:
    _T10 = 8
    parm _T10
    _T11 =  call _Alloc
    _T12 = 0
    *(_T11 + 4) = _T12
    _T13 = VTBL <_animal>
    *(_T11 + 0) = _T13
    return _T11
}

FUNCTION(_people_New) {
memo ''
_people_New:
    _T14 = 20
    parm _T14
    _T15 =  call _Alloc
    _T16 = 0
    *(_T15 + 4) = _T16
    *(_T15 + 8) = _T16
    *(_T15 + 12) = _T16
    *(_T15 + 16) = _T16
    _T17 = VTBL <_people>
    *(_T15 + 0) = _T17
    return _T15
}

FUNCTION(main) {
memo ''
main:
    _T21 =  call _people_New
    _T19 = _T21
    parm _T19
    _T22 = *(_T19 + 0)
    _T23 = *(_T19 + 0)
    _T24 = *(_T23 + 16)
    call _T24
    *(_T19 + 0) = _T22
    _T25 =  call _people_New
    _T26 = 20
    _T27 = *(_T19 + 4)
    *(_T25 + 4) = _T27
    _T28 = *(_T19 + 8)
    *(_T25 + 8) = _T28
    _T29 = *(_T19 + 12)
    *(_T25 + 12) = _T29
    _T30 = *(_T19 + 16)
    *(_T25 + 16) = _T30
    _T20 = _T25
    _T31 = 99
    parm _T20
    parm _T31
    _T32 = *(_T20 + 0)
    _T33 = *(_T20 + 0)
    _T34 = *(_T33 + 8)
    call _T34
    *(_T20 + 0) = _T32
    _T35 = "a: \n"
    parm _T35
    call _PrintString
    parm _T19
    _T36 = *(_T19 + 0)
    _T37 = *(_T19 + 0)
    _T38 = *(_T37 + 12)
    call _T38
    *(_T19 + 0) = _T36
    _T39 = "b: \n"
    parm _T39
    call _PrintString
    parm _T20
    _T40 = *(_T20 + 0)
    _T41 = *(_T20 + 0)
    _T42 = *(_T41 + 12)
    call _T42
    *(_T20 + 0) = _T40
}

FUNCTION(_animal.setage) {
memo '_T0:4 _T1:8'
_animal.setage:
    _T43 = *(_T0 + 4)
    *(_T0 + 4) = _T1
}

FUNCTION(_animal.getage) {
memo '_T2:4'
_animal.getage:
    _T44 = *(_T2 + 4)
    parm _T44
    call _PrintInt
    _T45 = "\n"
    parm _T45
    call _PrintString
}

FUNCTION(_people.setaniage) {
memo '_T3:4 _T4:8'
_people.setaniage:
    _T46 = *(_T3 + 12)
    parm _T46
    parm _T4
    _T47 = *(_T46 + 0)
    _T48 = *(_T46 + 0)
    _T49 = *(_T48 + 8)
    call _T49
    *(_T46 + 0) = _T47
}

FUNCTION(_people.getage) {
memo '_T5:4'
_people.getage:
    _T50 = *(_T5 + 4)
    parm _T50
    call _PrintInt
    _T51 = "\n"
    parm _T51
    call _PrintString
    _T52 = *(_T5 + 8)
    _T53 = *(_T52 + 0)
    parm _T53
    call _PrintInt
    _T54 = "+"
    parm _T54
    call _PrintString
    _T55 = *(_T52 + 4)
    parm _T55
    call _PrintInt
    _T56 = "j"
    parm _T56
    call _PrintString
    _T57 = "\n"
    parm _T57
    call _PrintString
    _T58 = *(_T5 + 12)
    parm _T58
    _T59 = *(_T58 + 0)
    _T60 = *(_T58 + 0)
    _T61 = *(_T60 + 12)
    call _T61
    *(_T58 + 0) = _T59
    _T62 = *(_T5 + 16)
    parm _T62
    call _PrintString
    _T63 = "\n"
    parm _T63
    call _PrintString
}

FUNCTION(_people.setage) {
memo '_T6:4'
_people.setage:
    _T64 = *(_T6 + 12)
    _T65 =  call _animal_New
    *(_T6 + 12) = _T65
    _T66 = 100
    parm _T6
    parm _T66
    _T67 = *(_T6 + 0)
    _T68 = *(_T6 + 0)
    _T69 = *(_T68 + 8)
    call _T69
    *(_T6 + 0) = _T67
    _T70 = *(_T6 + 4)
    _T71 = 10
    *(_T6 + 4) = _T71
    _T72 = *(_T6 + 16)
    _T73 = "11"
    *(_T6 + 16) = _T73
    _T74 = *(_T6 + 8)
    _T75 = 89
    _T76 = 8
    parm _T76
    _T77 =  call _Alloc
    _T78 = 8
    _T79 = 0
    *(_T77 + 0) = _T79
    *(_T77 + 4) = _T78
    _T80 = 8
    parm _T80
    _T81 =  call _Alloc
    _T82 = 0
    *(_T81 + 0) = _T75
    *(_T81 + 4) = _T82
    _T83 = 8
    parm _T83
    _T84 =  call _Alloc
    _T85 = *(_T81 + 0)
    _T86 = *(_T77 + 0)
    _T87 = (_T85 + _T86)
    _T88 = *(_T81 + 4)
    _T89 = *(_T77 + 4)
    _T90 = (_T88 + _T89)
    *(_T84 + 0) = _T87
    *(_T84 + 4) = _T90
    *(_T6 + 8) = _T84
}

