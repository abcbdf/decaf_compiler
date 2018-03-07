VTABLE(_QueueItem) {
    <empty>
    QueueItem
    _QueueItem.Init;
    _QueueItem.GetData;
    _QueueItem.GetNext;
    _QueueItem.GetPrev;
    _QueueItem.SetNext;
    _QueueItem.SetPrev;
}

VTABLE(_Queue) {
    <empty>
    Queue
    _Queue.Init;
    _Queue.EnQueue;
    _Queue.DeQueue;
}

VTABLE(_Main) {
    <empty>
    Main
}

FUNCTION(_QueueItem_New) {
memo ''
_QueueItem_New:
    _T15 = 16
    parm _T15
    _T16 =  call _Alloc
    _T17 = 0
    *(_T16 + 4) = _T17
    *(_T16 + 8) = _T17
    *(_T16 + 12) = _T17
    _T18 = VTBL <_QueueItem>
    *(_T16 + 0) = _T18
    return _T16
}

FUNCTION(_Queue_New) {
memo ''
_Queue_New:
    _T19 = 12
    parm _T19
    _T20 =  call _Alloc
    _T21 = 0
    *(_T20 + 4) = _T21
    *(_T20 + 8) = _T21
    _T22 = VTBL <_Queue>
    *(_T20 + 0) = _T22
    return _T20
}

FUNCTION(_Main_New) {
memo ''
_Main_New:
    _T23 = 4
    parm _T23
    _T24 =  call _Alloc
    _T25 = VTBL <_Main>
    *(_T24 + 0) = _T25
    return _T24
}

FUNCTION(_QueueItem.Init) {
memo '_T0:4 _T1:8 _T2:12 _T3:16'
_QueueItem.Init:
    _T26 = *(_T0 + 4)
    *(_T0 + 4) = _T1
    _T27 = *(_T0 + 8)
    *(_T0 + 8) = _T2
    _T28 = *(_T2 + 12)
    *(_T2 + 12) = _T0
    _T29 = *(_T0 + 12)
    *(_T0 + 12) = _T3
    _T30 = *(_T3 + 8)
    *(_T3 + 8) = _T0
}

FUNCTION(_QueueItem.GetData) {
memo '_T4:4'
_QueueItem.GetData:
    _T31 = *(_T4 + 4)
    return _T31
}

FUNCTION(_QueueItem.GetNext) {
memo '_T5:4'
_QueueItem.GetNext:
    _T32 = *(_T5 + 8)
    return _T32
}

FUNCTION(_QueueItem.GetPrev) {
memo '_T6:4'
_QueueItem.GetPrev:
    _T33 = *(_T6 + 12)
    return _T33
}

FUNCTION(_QueueItem.SetNext) {
memo '_T7:4 _T8:8'
_QueueItem.SetNext:
    _T34 = *(_T7 + 8)
    *(_T7 + 8) = _T8
}

FUNCTION(_QueueItem.SetPrev) {
memo '_T9:4 _T10:8'
_QueueItem.SetPrev:
    _T35 = *(_T9 + 12)
    *(_T9 + 12) = _T10
}

FUNCTION(_Queue.Init) {
memo '_T11:4'
_Queue.Init:
    _T36 = *(_T11 + 8)
    _T37 =  call _QueueItem_New
    *(_T11 + 8) = _T37
    _T38 = *(_T11 + 8)
    _T39 = 0
    _T40 = *(_T11 + 8)
    _T41 = *(_T11 + 8)
    parm _T38
    parm _T39
    parm _T40
    parm _T41
    _T42 = *(_T38 + 0)
    _T43 = *(_T38 + 0)
    _T44 = *(_T43 + 8)
    call _T44
    *(_T38 + 0) = _T42
}

FUNCTION(_Queue.EnQueue) {
memo '_T12:4 _T13:8'
_Queue.EnQueue:
    _T46 =  call _QueueItem_New
    _T45 = _T46
    _T47 = *(_T12 + 8)
    parm _T47
    _T48 = *(_T47 + 0)
    _T49 = *(_T47 + 0)
    _T50 = *(_T49 + 16)
    _T51 =  call _T50
    *(_T47 + 0) = _T48
    _T52 = *(_T12 + 8)
    parm _T45
    parm _T13
    parm _T51
    parm _T52
    _T53 = *(_T45 + 0)
    _T54 = *(_T45 + 0)
    _T55 = *(_T54 + 8)
    call _T55
    *(_T45 + 0) = _T53
}

FUNCTION(_Queue.DeQueue) {
memo '_T14:4'
_Queue.DeQueue:
    _T57 = *(_T14 + 8)
    parm _T57
    _T58 = *(_T57 + 0)
    _T59 = *(_T57 + 0)
    _T60 = *(_T59 + 20)
    _T61 =  call _T60
    *(_T57 + 0) = _T58
    _T62 = *(_T14 + 8)
    _T63 = (_T61 == _T62)
    if (_T63 == 0) branch _L21
    _T64 = "Queue Is Empty"
    parm _T64
    call _PrintString
    _T65 = 0
    return _T65
    branch _L22
_L21:
    _T67 = *(_T14 + 8)
    parm _T67
    _T68 = *(_T67 + 0)
    _T69 = *(_T67 + 0)
    _T70 = *(_T69 + 20)
    _T71 =  call _T70
    *(_T67 + 0) = _T68
    _T66 = _T71
    parm _T66
    _T72 = *(_T66 + 0)
    _T73 = *(_T66 + 0)
    _T74 = *(_T73 + 12)
    _T75 =  call _T74
    *(_T66 + 0) = _T72
    _T56 = _T75
    parm _T66
    _T76 = *(_T66 + 0)
    _T77 = *(_T66 + 0)
    _T78 = *(_T77 + 20)
    _T79 =  call _T78
    *(_T66 + 0) = _T76
    parm _T66
    _T80 = *(_T66 + 0)
    _T81 = *(_T66 + 0)
    _T82 = *(_T81 + 16)
    _T83 =  call _T82
    *(_T66 + 0) = _T80
    parm _T79
    parm _T83
    _T84 = *(_T79 + 0)
    _T85 = *(_T79 + 0)
    _T86 = *(_T85 + 24)
    call _T86
    *(_T79 + 0) = _T84
    parm _T66
    _T87 = *(_T66 + 0)
    _T88 = *(_T66 + 0)
    _T89 = *(_T88 + 16)
    _T90 =  call _T89
    *(_T66 + 0) = _T87
    parm _T66
    _T91 = *(_T66 + 0)
    _T92 = *(_T66 + 0)
    _T93 = *(_T92 + 20)
    _T94 =  call _T93
    *(_T66 + 0) = _T91
    parm _T90
    parm _T94
    _T95 = *(_T90 + 0)
    _T96 = *(_T90 + 0)
    _T97 = *(_T96 + 28)
    call _T97
    *(_T90 + 0) = _T95
_L22:
    return _T56
}

FUNCTION(main) {
memo ''
main:
    _T100 =  call _Queue_New
    _T98 = _T100
    parm _T98
    _T101 = *(_T98 + 0)
    _T102 = *(_T98 + 0)
    _T103 = *(_T102 + 8)
    call _T103
    *(_T98 + 0) = _T101
    _T104 = 0
    _T99 = _T104
    branch _L23
_L24:
    _T105 = 1
    _T106 = (_T99 + _T105)
    _T99 = _T106
_L23:
    _T107 = 10
    _T108 = (_T99 < _T107)
    if (_T108 == 0) branch _L25
    parm _T98
    parm _T99
    _T109 = *(_T98 + 0)
    _T110 = *(_T98 + 0)
    _T111 = *(_T110 + 12)
    call _T111
    *(_T98 + 0) = _T109
    branch _L24
_L25:
    _T112 = 0
    _T99 = _T112
    branch _L26
_L27:
    _T113 = 1
    _T114 = (_T99 + _T113)
    _T99 = _T114
_L26:
    _T115 = 4
    _T116 = (_T99 < _T115)
    if (_T116 == 0) branch _L28
    parm _T98
    _T117 = *(_T98 + 0)
    _T118 = *(_T98 + 0)
    _T119 = *(_T118 + 16)
    _T120 =  call _T119
    *(_T98 + 0) = _T117
    parm _T120
    call _PrintInt
    _T121 = " "
    parm _T121
    call _PrintString
    branch _L27
_L28:
    _T122 = "\n"
    parm _T122
    call _PrintString
    _T123 = 0
    _T99 = _T123
    branch _L29
_L30:
    _T124 = 1
    _T125 = (_T99 + _T124)
    _T99 = _T125
_L29:
    _T126 = 10
    _T127 = (_T99 < _T126)
    if (_T127 == 0) branch _L31
    parm _T98
    parm _T99
    _T128 = *(_T98 + 0)
    _T129 = *(_T98 + 0)
    _T130 = *(_T129 + 12)
    call _T130
    *(_T98 + 0) = _T128
    branch _L30
_L31:
    _T131 = 0
    _T99 = _T131
    branch _L32
_L33:
    _T132 = 1
    _T133 = (_T99 + _T132)
    _T99 = _T133
_L32:
    _T134 = 17
    _T135 = (_T99 < _T134)
    if (_T135 == 0) branch _L34
    parm _T98
    _T136 = *(_T98 + 0)
    _T137 = *(_T98 + 0)
    _T138 = *(_T137 + 16)
    _T139 =  call _T138
    *(_T98 + 0) = _T136
    parm _T139
    call _PrintInt
    _T140 = " "
    parm _T140
    call _PrintString
    branch _L33
_L34:
    _T141 = "\n"
    parm _T141
    call _PrintString
}

