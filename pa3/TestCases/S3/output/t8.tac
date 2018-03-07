VTABLE(_Animal) {
    <empty>
    Animal
    _Animal.InitAnimal;
    _Animal.GetHeight;
    _Animal.GetMom;
}

VTABLE(_Cow) {
    _Animal
    Cow
    _Animal.InitAnimal;
    _Animal.GetHeight;
    _Animal.GetMom;
    _Cow.InitCow;
    _Cow.IsSpottedCow;
}

VTABLE(_Main) {
    <empty>
    Main
}

FUNCTION(_Animal_New) {
memo ''
_Animal_New:
    _T10 = 12
    parm _T10
    _T11 =  call _Alloc
    _T12 = 0
    *(_T11 + 4) = _T12
    *(_T11 + 8) = _T12
    _T13 = VTBL <_Animal>
    *(_T11 + 0) = _T13
    return _T11
}

FUNCTION(_Cow_New) {
memo ''
_Cow_New:
    _T14 = 16
    parm _T14
    _T15 =  call _Alloc
    _T16 = 0
    *(_T15 + 4) = _T16
    *(_T15 + 8) = _T16
    *(_T15 + 12) = _T16
    _T17 = VTBL <_Cow>
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

FUNCTION(_Animal.InitAnimal) {
memo '_T0:4 _T1:8 _T2:12'
_Animal.InitAnimal:
    _T21 = *(_T0 + 4)
    *(_T0 + 4) = _T1
    _T22 = *(_T0 + 8)
    *(_T0 + 8) = _T2
}

FUNCTION(_Animal.GetHeight) {
memo '_T3:4'
_Animal.GetHeight:
    _T23 = *(_T3 + 4)
    return _T23
}

FUNCTION(_Animal.GetMom) {
memo '_T4:4'
_Animal.GetMom:
    _T24 = *(_T4 + 8)
    return _T24
}

FUNCTION(_Cow.InitCow) {
memo '_T5:4 _T6:8 _T7:12 _T8:16'
_Cow.InitCow:
    _T25 = *(_T5 + 12)
    *(_T5 + 12) = _T8
    parm _T5
    parm _T6
    parm _T7
    _T26 = *(_T5 + 0)
    _T27 = *(_T5 + 0)
    _T28 = *(_T27 + 0)
    *(_T5 + 0) = _T28
    _T29 = *(_T5 + 0)
    _T30 = *(_T29 + 8)
    call _T30
    *(_T5 + 0) = _T26
}

FUNCTION(_Cow.IsSpottedCow) {
memo '_T9:4'
_Cow.IsSpottedCow:
    _T31 = *(_T9 + 12)
    return _T31
}

FUNCTION(main) {
memo ''
main:
    _T34 =  call _Cow_New
    _T32 = _T34
    _T35 = 5
    _T36 = 0
    _T37 = 1
    parm _T32
    parm _T35
    parm _T36
    parm _T37
    _T38 = *(_T32 + 0)
    _T39 = *(_T32 + 0)
    _T40 = *(_T39 + 20)
    call _T40
    *(_T32 + 0) = _T38
    _T33 = _T32
    parm _T33
    _T41 = *(_T33 + 0)
    _T42 = *(_T33 + 0)
    _T43 = *(_T42 + 16)
    _T44 =  call _T43
    *(_T33 + 0) = _T41
    _T45 = "spots: "
    parm _T45
    call _PrintString
    parm _T32
    _T46 = *(_T32 + 0)
    _T47 = *(_T32 + 0)
    _T48 = *(_T47 + 24)
    _T49 =  call _T48
    *(_T32 + 0) = _T46
    parm _T49
    call _PrintBool
    _T50 = "    height: "
    parm _T50
    call _PrintString
    parm _T33
    _T51 = *(_T33 + 0)
    _T52 = *(_T33 + 0)
    _T53 = *(_T52 + 12)
    _T54 =  call _T53
    *(_T33 + 0) = _T51
    parm _T54
    call _PrintInt
}

