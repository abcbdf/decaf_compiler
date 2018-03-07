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
    _T11 = 1
    _T6 = _T11
    parm _T6
    call _PrintInt
    _T12 = "\n"
    parm _T12
    call _PrintString
    _T13 = 3
    _T14 = 8
    parm _T14
    _T15 =  call _Alloc
    _T16 = 12
    _T17 = 0
    *(_T15 + 0) = _T17
    *(_T15 + 4) = _T16
    _T18 = 8
    parm _T18
    _T19 =  call _Alloc
    _T20 = 0
    *(_T19 + 0) = _T13
    *(_T19 + 4) = _T20
    _T21 = 8
    parm _T21
    _T22 =  call _Alloc
    _T23 = *(_T19 + 0)
    _T24 = *(_T15 + 0)
    _T25 = (_T23 + _T24)
    _T26 = *(_T19 + 4)
    _T27 = *(_T15 + 4)
    _T28 = (_T26 + _T27)
    *(_T22 + 0) = _T25
    *(_T22 + 4) = _T28
    _T3 = _T22
    _T29 = *(_T3 + 0)
    parm _T29
    call _PrintInt
    _T30 = "+"
    parm _T30
    call _PrintString
    _T31 = *(_T3 + 4)
    parm _T31
    call _PrintInt
    _T32 = "j"
    parm _T32
    call _PrintString
    _T33 = "\n"
    parm _T33
    call _PrintString
    _T34 = 3
    _T35 = 8
    parm _T35
    _T36 =  call _Alloc
    _T37 = 45
    _T38 = 0
    *(_T36 + 0) = _T38
    *(_T36 + 4) = _T37
    _T39 = 8
    parm _T39
    _T40 =  call _Alloc
    _T41 = 0
    *(_T40 + 0) = _T34
    *(_T40 + 4) = _T41
    _T42 = 8
    parm _T42
    _T43 =  call _Alloc
    _T44 = *(_T40 + 0)
    _T45 = *(_T36 + 0)
    _T46 = (_T44 + _T45)
    _T47 = *(_T40 + 4)
    _T48 = *(_T36 + 4)
    _T49 = (_T47 + _T48)
    *(_T43 + 0) = _T46
    *(_T43 + 4) = _T49
    _T5 = _T43
    _T50 = *(_T3 + 0)
    _T7 = _T50
    _T51 = *(_T3 + 4)
    _T8 = _T51
    parm _T7
    call _PrintInt
    parm _T8
    call _PrintInt
    _T52 = "\n"
    parm _T52
    call _PrintString
    _T53 = (_T7 + _T8)
    _T54 = 8
    parm _T54
    _T55 =  call _Alloc
    _T56 = 0
    *(_T55 + 0) = _T53
    *(_T55 + 4) = _T56
    _T4 = _T55
    _T57 = *(_T4 + 0)
    parm _T57
    call _PrintInt
    _T58 = "+"
    parm _T58
    call _PrintString
    _T59 = *(_T4 + 4)
    parm _T59
    call _PrintInt
    _T60 = "j"
    parm _T60
    call _PrintString
    _T61 = "\n"
    parm _T61
    call _PrintString
    _T62 = 8
    parm _T62
    _T63 =  call _Alloc
    _T64 = *(_T3 + 0)
    _T65 = *(_T4 + 0)
    _T66 = (_T64 + _T65)
    _T67 = *(_T3 + 4)
    _T68 = *(_T4 + 4)
    _T69 = (_T67 + _T68)
    *(_T63 + 0) = _T66
    *(_T63 + 4) = _T69
    _T70 = *(_T63 + 0)
    parm _T70
    call _PrintInt
    _T71 = "+"
    parm _T71
    call _PrintString
    _T72 = *(_T63 + 4)
    parm _T72
    call _PrintInt
    _T73 = "j"
    parm _T73
    call _PrintString
    _T74 = "\n"
    parm _T74
    call _PrintString
    _T75 = 8
    parm _T75
    _T76 =  call _Alloc
    _T77 = *(_T3 + 0)
    _T78 = *(_T4 + 0)
    _T79 = (_T77 + _T78)
    _T80 = *(_T3 + 4)
    _T81 = *(_T4 + 4)
    _T82 = (_T80 + _T81)
    *(_T76 + 0) = _T79
    *(_T76 + 4) = _T82
    _T83 = *(_T76 + 0)
    parm _T83
    call _PrintInt
    _T84 = "+"
    parm _T84
    call _PrintString
    _T85 = *(_T76 + 4)
    parm _T85
    call _PrintInt
    _T86 = "j"
    parm _T86
    call _PrintString
    _T87 = *(_T5 + 0)
    parm _T87
    call _PrintInt
    _T88 = "+"
    parm _T88
    call _PrintString
    _T89 = *(_T5 + 4)
    parm _T89
    call _PrintInt
    _T90 = "j"
    parm _T90
    call _PrintString
    _T91 = "\n"
    parm _T91
    call _PrintString
    _T92 = 8
    parm _T92
    _T93 =  call _Alloc
    _T94 = *(_T3 + 0)
    _T95 = *(_T4 + 0)
    _T96 = (_T94 + _T95)
    _T97 = *(_T3 + 4)
    _T98 = *(_T4 + 4)
    _T99 = (_T97 + _T98)
    *(_T93 + 0) = _T96
    *(_T93 + 4) = _T99
    _T5 = _T93
    _T100 = 8
    parm _T100
    _T101 =  call _Alloc
    _T102 = 0
    *(_T101 + 0) = _T7
    *(_T101 + 4) = _T102
    _T103 = 8
    parm _T103
    _T104 =  call _Alloc
    _T105 = *(_T3 + 0)
    _T106 = *(_T101 + 0)
    _T107 = (_T105 + _T106)
    _T108 = *(_T3 + 4)
    _T109 = *(_T101 + 4)
    _T110 = (_T108 + _T109)
    *(_T104 + 0) = _T107
    *(_T104 + 4) = _T110
    _T5 = _T104
    _T111 = 8
    parm _T111
    _T112 =  call _Alloc
    _T113 = 0
    _T114 = 0
    *(_T112 + 0) = _T114
    *(_T112 + 4) = _T113
    _T115 = 8
    parm _T115
    _T116 =  call _Alloc
    _T117 = *(_T3 + 0)
    _T118 = *(_T112 + 0)
    _T119 = (_T117 + _T118)
    _T120 = *(_T3 + 4)
    _T121 = *(_T112 + 4)
    _T122 = (_T120 + _T121)
    *(_T116 + 0) = _T119
    *(_T116 + 4) = _T122
    _T5 = _T116
    _T123 = 8
    parm _T123
    _T124 =  call _Alloc
    _T125 = 0
    _T126 = 0
    *(_T124 + 0) = _T126
    *(_T124 + 4) = _T125
    _T127 = 8
    parm _T127
    _T128 =  call _Alloc
    _T129 = 0
    *(_T128 + 0) = _T7
    *(_T128 + 4) = _T129
    _T130 = 8
    parm _T130
    _T131 =  call _Alloc
    _T132 = *(_T124 + 0)
    _T133 = *(_T128 + 0)
    _T134 = (_T132 + _T133)
    _T135 = *(_T124 + 4)
    _T136 = *(_T128 + 4)
    _T137 = (_T135 + _T136)
    *(_T131 + 0) = _T134
    *(_T131 + 4) = _T137
    _T5 = _T131
    _T138 = 4
    _T139 = (_T138 + _T7)
    _T10 = _T139
    parm _T10
    call _PrintInt
    _T140 = "\n"
    parm _T140
    call _PrintString
    _T141 = *(_T5 + 0)
    parm _T141
    call _PrintInt
    _T142 = "+"
    parm _T142
    call _PrintString
    _T143 = *(_T5 + 4)
    parm _T143
    call _PrintInt
    _T144 = "j"
    parm _T144
    call _PrintString
    _T145 = "\n"
    parm _T145
    call _PrintString
    _T146 = 8
    parm _T146
    _T147 =  call _Alloc
    _T148 = *(_T3 + 0)
    _T149 = *(_T4 + 0)
    _T150 = (_T148 * _T149)
    _T151 = *(_T3 + 4)
    _T152 = *(_T4 + 4)
    _T153 = (_T151 * _T152)
    _T154 = (_T150 - _T153)
    _T155 = *(_T3 + 0)
    _T156 = *(_T4 + 4)
    _T157 = (_T155 * _T156)
    _T158 = *(_T3 + 4)
    _T159 = *(_T4 + 0)
    _T160 = (_T158 * _T159)
    _T161 = (_T157 + _T160)
    *(_T147 + 0) = _T154
    *(_T147 + 4) = _T161
    _T5 = _T147
    _T162 = 8
    parm _T162
    _T163 =  call _Alloc
    _T164 = 0
    *(_T163 + 0) = _T7
    *(_T163 + 4) = _T164
    _T165 = 8
    parm _T165
    _T166 =  call _Alloc
    _T167 = *(_T3 + 0)
    _T168 = *(_T163 + 0)
    _T169 = (_T167 * _T168)
    _T170 = *(_T3 + 4)
    _T171 = *(_T163 + 4)
    _T172 = (_T170 * _T171)
    _T173 = (_T169 - _T172)
    _T174 = *(_T3 + 0)
    _T175 = *(_T163 + 4)
    _T176 = (_T174 * _T175)
    _T177 = *(_T3 + 4)
    _T178 = *(_T163 + 0)
    _T179 = (_T177 * _T178)
    _T180 = (_T176 + _T179)
    *(_T166 + 0) = _T173
    *(_T166 + 4) = _T180
    _T5 = _T166
    _T181 = 8
    parm _T181
    _T182 =  call _Alloc
    _T183 = 0
    _T184 = 0
    *(_T182 + 0) = _T184
    *(_T182 + 4) = _T183
    _T185 = 8
    parm _T185
    _T186 =  call _Alloc
    _T187 = *(_T3 + 0)
    _T188 = *(_T182 + 0)
    _T189 = (_T187 * _T188)
    _T190 = *(_T3 + 4)
    _T191 = *(_T182 + 4)
    _T192 = (_T190 * _T191)
    _T193 = (_T189 - _T192)
    _T194 = *(_T3 + 0)
    _T195 = *(_T182 + 4)
    _T196 = (_T194 * _T195)
    _T197 = *(_T3 + 4)
    _T198 = *(_T182 + 0)
    _T199 = (_T197 * _T198)
    _T200 = (_T196 + _T199)
    *(_T186 + 0) = _T193
    *(_T186 + 4) = _T200
    _T5 = _T186
    _T201 = 8
    parm _T201
    _T202 =  call _Alloc
    _T203 = 0
    _T204 = 0
    *(_T202 + 0) = _T204
    *(_T202 + 4) = _T203
    _T205 = 8
    parm _T205
    _T206 =  call _Alloc
    _T207 = 0
    *(_T206 + 0) = _T7
    *(_T206 + 4) = _T207
    _T208 = 8
    parm _T208
    _T209 =  call _Alloc
    _T210 = *(_T202 + 0)
    _T211 = *(_T206 + 0)
    _T212 = (_T210 * _T211)
    _T213 = *(_T202 + 4)
    _T214 = *(_T206 + 4)
    _T215 = (_T213 * _T214)
    _T216 = (_T212 - _T215)
    _T217 = *(_T202 + 0)
    _T218 = *(_T206 + 4)
    _T219 = (_T217 * _T218)
    _T220 = *(_T202 + 4)
    _T221 = *(_T206 + 0)
    _T222 = (_T220 * _T221)
    _T223 = (_T219 + _T222)
    *(_T209 + 0) = _T216
    *(_T209 + 4) = _T223
    _T5 = _T209
    _T224 = 4
    _T225 = (_T224 * _T7)
    _T10 = _T225
    parm _T10
    call _PrintInt
    _T226 = "\n"
    parm _T226
    call _PrintString
    _T227 = *(_T5 + 0)
    parm _T227
    call _PrintInt
    _T228 = "+"
    parm _T228
    call _PrintString
    _T229 = *(_T5 + 4)
    parm _T229
    call _PrintInt
    _T230 = "j"
    parm _T230
    call _PrintString
    _T231 = "\n"
    parm _T231
    call _PrintString
}

