VTABLE(_A) {
    <empty>
    A
    _A.setA;
    _A.print;
    _A.allprint;
    _A.fun;
}

VTABLE(_B) {
    _A
    B
    _A.setA;
    _B.print;
    _B.allprint;
    _B.fun;
    _B.setB;
}

VTABLE(_C) {
    _A
    C
    _A.setA;
    _C.print;
    _C.allprint;
    _C.fun;
    _C.setC;
}

VTABLE(_D) {
    _B
    D
    _A.setA;
    _D.print;
    _D.allprint;
    _D.fun;
    _B.setB;
    _D.setD;
}

VTABLE(_E) {
    _C
    E
    _A.setA;
    _E.print;
    _C.allprint;
    _E.fun;
    _C.setC;
    _E.setE;
}

VTABLE(_F) {
    _E
    F
    _A.setA;
    _F.print;
    _F.allprint;
    _F.fun;
    _C.setC;
    _E.setE;
    _F.setF;
}

VTABLE(_G) {
    _C
    G
    _A.setA;
    _G.print;
    _G.allprint;
    _G.fun;
    _C.setC;
    _G.setG;
}

VTABLE(_Main) {
    <empty>
    Main
}

FUNCTION(_A_New) {
memo ''
_A_New:
    _T40 = 12
    parm _T40
    _T41 =  call _Alloc
    _T42 = 0
    *(_T41 + 4) = _T42
    *(_T41 + 8) = _T42
    _T43 = VTBL <_A>
    *(_T41 + 0) = _T43
    return _T41
}

FUNCTION(_B_New) {
memo ''
_B_New:
    _T44 = 20
    parm _T44
    _T45 =  call _Alloc
    _T46 = 0
    *(_T45 + 4) = _T46
    *(_T45 + 8) = _T46
    *(_T45 + 12) = _T46
    *(_T45 + 16) = _T46
    _T47 = VTBL <_B>
    *(_T45 + 0) = _T47
    return _T45
}

FUNCTION(_C_New) {
memo ''
_C_New:
    _T48 = 20
    parm _T48
    _T49 =  call _Alloc
    _T50 = 0
    *(_T49 + 4) = _T50
    *(_T49 + 8) = _T50
    *(_T49 + 12) = _T50
    *(_T49 + 16) = _T50
    _T51 = VTBL <_C>
    *(_T49 + 0) = _T51
    return _T49
}

FUNCTION(_D_New) {
memo ''
_D_New:
    _T52 = 28
    parm _T52
    _T53 =  call _Alloc
    _T54 = 0
    _T55 = 4
    _T56 = (_T53 + _T52)
_L40:
    _T57 = (_T56 - _T55)
    _T56 = _T57
    _T58 = (_T52 - _T55)
    _T52 = _T58
    if (_T52 == 0) branch _L41
    *(_T56 + 0) = _T54
    branch _L40
_L41:
    _T59 = VTBL <_D>
    *(_T56 + 0) = _T59
    return _T56
}

FUNCTION(_E_New) {
memo ''
_E_New:
    _T60 = 28
    parm _T60
    _T61 =  call _Alloc
    _T62 = 0
    _T63 = 4
    _T64 = (_T61 + _T60)
_L43:
    _T65 = (_T64 - _T63)
    _T64 = _T65
    _T66 = (_T60 - _T63)
    _T60 = _T66
    if (_T60 == 0) branch _L44
    *(_T64 + 0) = _T62
    branch _L43
_L44:
    _T67 = VTBL <_E>
    *(_T64 + 0) = _T67
    return _T64
}

FUNCTION(_F_New) {
memo ''
_F_New:
    _T68 = 36
    parm _T68
    _T69 =  call _Alloc
    _T70 = 0
    _T71 = 4
    _T72 = (_T69 + _T68)
_L46:
    _T73 = (_T72 - _T71)
    _T72 = _T73
    _T74 = (_T68 - _T71)
    _T68 = _T74
    if (_T68 == 0) branch _L47
    *(_T72 + 0) = _T70
    branch _L46
_L47:
    _T75 = VTBL <_F>
    *(_T72 + 0) = _T75
    return _T72
}

FUNCTION(_G_New) {
memo ''
_G_New:
    _T76 = 24
    parm _T76
    _T77 =  call _Alloc
    _T78 = 0
    _T79 = 4
    _T80 = (_T77 + _T76)
_L49:
    _T81 = (_T80 - _T79)
    _T80 = _T81
    _T82 = (_T76 - _T79)
    _T76 = _T82
    if (_T76 == 0) branch _L50
    *(_T80 + 0) = _T78
    branch _L49
_L50:
    _T83 = VTBL <_G>
    *(_T80 + 0) = _T83
    return _T80
}

FUNCTION(_Main_New) {
memo ''
_Main_New:
    _T84 = 4
    parm _T84
    _T85 =  call _Alloc
    _T86 = VTBL <_Main>
    *(_T85 + 0) = _T86
    return _T85
}

FUNCTION(_A.setA) {
memo '_T0:4 _T1:8 _T2:12'
_A.setA:
    _T87 = *(_T0 + 4)
    *(_T0 + 4) = _T1
    _T88 = *(_T0 + 8)
    *(_T0 + 8) = _T2
}

FUNCTION(_A.print) {
memo '_T3:4'
_A.print:
    _T89 = " a="
    parm _T89
    call _PrintString
    _T90 = *(_T3 + 4)
    parm _T90
    call _PrintInt
    _T91 = " a1="
    parm _T91
    call _PrintString
    _T92 = *(_T3 + 8)
    parm _T92
    call _PrintInt
    _T93 = " "
    parm _T93
    call _PrintString
}

FUNCTION(_A.allprint) {
memo '_T4:4'
_A.allprint:
    parm _T4
    _T94 = *(_T4 + 0)
    _T95 = *(_T4 + 0)
    _T96 = *(_T95 + 12)
    call _T96
    *(_T4 + 0) = _T94
}

FUNCTION(_A.fun) {
memo '_T5:4'
_A.fun:
    _T97 = "A"
    parm _T97
    call _PrintString
    parm _T5
    _T98 = *(_T5 + 0)
    _T99 = *(_T5 + 0)
    _T100 = *(_T99 + 12)
    call _T100
    *(_T5 + 0) = _T98
    _T101 = "\n"
    parm _T101
    call _PrintString
}

FUNCTION(_B.setB) {
memo '_T6:4 _T7:8 _T8:12'
_B.setB:
    _T102 = *(_T6 + 12)
    *(_T6 + 12) = _T7
    _T103 = *(_T6 + 16)
    *(_T6 + 16) = _T8
}

FUNCTION(_B.print) {
memo '_T9:4'
_B.print:
    _T104 = " b="
    parm _T104
    call _PrintString
    _T105 = *(_T9 + 12)
    parm _T105
    call _PrintInt
    _T106 = " b1="
    parm _T106
    call _PrintString
    _T107 = *(_T9 + 16)
    parm _T107
    call _PrintInt
    _T108 = " "
    parm _T108
    call _PrintString
}

FUNCTION(_B.allprint) {
memo '_T10:4'
_B.allprint:
    parm _T10
    _T109 = *(_T10 + 0)
    _T110 = *(_T10 + 0)
    _T111 = *(_T110 + 0)
    *(_T10 + 0) = _T111
    _T112 = *(_T10 + 0)
    _T113 = *(_T112 + 16)
    call _T113
    *(_T10 + 0) = _T109
    parm _T10
    _T114 = *(_T10 + 0)
    _T115 = *(_T10 + 0)
    _T116 = *(_T115 + 12)
    call _T116
    *(_T10 + 0) = _T114
}

FUNCTION(_B.fun) {
memo '_T11:4'
_B.fun:
    _T117 = "B"
    parm _T117
    call _PrintString
    parm _T11
    _T118 = *(_T11 + 0)
    _T119 = *(_T11 + 0)
    _T120 = *(_T119 + 0)
    *(_T11 + 0) = _T120
    _T121 = *(_T11 + 0)
    _T122 = *(_T121 + 16)
    call _T122
    *(_T11 + 0) = _T118
    parm _T11
    _T123 = *(_T11 + 0)
    _T124 = *(_T11 + 0)
    _T125 = *(_T124 + 12)
    call _T125
    *(_T11 + 0) = _T123
    _T126 = "\n"
    parm _T126
    call _PrintString
}

FUNCTION(_C.setC) {
memo '_T12:4 _T13:8 _T14:12'
_C.setC:
    _T127 = *(_T12 + 12)
    *(_T12 + 12) = _T13
    _T128 = *(_T12 + 16)
    *(_T12 + 16) = _T14
}

FUNCTION(_C.print) {
memo '_T15:4'
_C.print:
    _T129 = " c="
    parm _T129
    call _PrintString
    _T130 = *(_T15 + 12)
    parm _T130
    call _PrintInt
    _T131 = " c1="
    parm _T131
    call _PrintString
    _T132 = *(_T15 + 16)
    parm _T132
    call _PrintInt
    _T133 = " "
    parm _T133
    call _PrintString
}

FUNCTION(_C.allprint) {
memo '_T16:4'
_C.allprint:
    parm _T16
    _T134 = *(_T16 + 0)
    _T135 = *(_T16 + 0)
    _T136 = *(_T135 + 12)
    call _T136
    *(_T16 + 0) = _T134
}

FUNCTION(_C.fun) {
memo '_T17:4'
_C.fun:
    _T137 = "C"
    parm _T137
    call _PrintString
    parm _T17
    _T138 = *(_T17 + 0)
    _T139 = *(_T17 + 0)
    _T140 = *(_T139 + 0)
    *(_T17 + 0) = _T140
    _T141 = *(_T17 + 0)
    _T142 = *(_T141 + 16)
    call _T142
    *(_T17 + 0) = _T138
    parm _T17
    _T143 = *(_T17 + 0)
    _T144 = *(_T17 + 0)
    _T145 = *(_T144 + 12)
    call _T145
    *(_T17 + 0) = _T143
    _T146 = "\n"
    parm _T146
    call _PrintString
}

FUNCTION(_D.setD) {
memo '_T18:4 _T19:8 _T20:12'
_D.setD:
    _T147 = *(_T18 + 20)
    *(_T18 + 20) = _T19
    _T148 = *(_T18 + 24)
    *(_T18 + 24) = _T20
}

FUNCTION(_D.print) {
memo '_T21:4'
_D.print:
    _T149 = " d="
    parm _T149
    call _PrintString
    _T150 = *(_T21 + 20)
    parm _T150
    call _PrintInt
    _T151 = " d1="
    parm _T151
    call _PrintString
    _T152 = *(_T21 + 24)
    parm _T152
    call _PrintInt
    _T153 = " "
    parm _T153
    call _PrintString
}

FUNCTION(_D.allprint) {
memo '_T22:4'
_D.allprint:
    parm _T22
    _T154 = *(_T22 + 0)
    _T155 = *(_T22 + 0)
    _T156 = *(_T155 + 0)
    *(_T22 + 0) = _T156
    _T157 = *(_T22 + 0)
    _T158 = *(_T157 + 16)
    call _T158
    *(_T22 + 0) = _T154
    parm _T22
    _T159 = *(_T22 + 0)
    _T160 = *(_T22 + 0)
    _T161 = *(_T160 + 12)
    call _T161
    *(_T22 + 0) = _T159
}

FUNCTION(_D.fun) {
memo '_T23:4'
_D.fun:
    _T162 = "D"
    parm _T162
    call _PrintString
    parm _T23
    _T163 = *(_T23 + 0)
    _T164 = *(_T23 + 0)
    _T165 = *(_T164 + 0)
    *(_T23 + 0) = _T165
    _T166 = *(_T23 + 0)
    _T167 = *(_T166 + 16)
    call _T167
    *(_T23 + 0) = _T163
    parm _T23
    _T168 = *(_T23 + 0)
    _T169 = *(_T23 + 0)
    _T170 = *(_T169 + 12)
    call _T170
    *(_T23 + 0) = _T168
    _T171 = "\n"
    parm _T171
    call _PrintString
}

FUNCTION(_E.setE) {
memo '_T24:4 _T25:8 _T26:12'
_E.setE:
    _T172 = *(_T24 + 20)
    *(_T24 + 20) = _T25
    _T173 = *(_T24 + 24)
    *(_T24 + 24) = _T26
}

FUNCTION(_E.print) {
memo '_T27:4'
_E.print:
    _T174 = " e="
    parm _T174
    call _PrintString
    _T175 = *(_T27 + 20)
    parm _T175
    call _PrintInt
    _T176 = " e1="
    parm _T176
    call _PrintString
    _T177 = *(_T27 + 24)
    parm _T177
    call _PrintInt
    _T178 = " "
    parm _T178
    call _PrintString
}

FUNCTION(_E.fun) {
memo '_T28:4'
_E.fun:
    _T179 = "E"
    parm _T179
    call _PrintString
    parm _T28
    _T180 = *(_T28 + 0)
    _T181 = *(_T28 + 0)
    _T182 = *(_T181 + 0)
    *(_T28 + 0) = _T182
    _T183 = *(_T28 + 0)
    _T184 = *(_T183 + 16)
    call _T184
    *(_T28 + 0) = _T180
    parm _T28
    _T185 = *(_T28 + 0)
    _T186 = *(_T28 + 0)
    _T187 = *(_T186 + 12)
    call _T187
    *(_T28 + 0) = _T185
    _T188 = "\n"
    parm _T188
    call _PrintString
}

FUNCTION(_F.setF) {
memo '_T29:4 _T30:8 _T31:12'
_F.setF:
    _T189 = *(_T29 + 28)
    *(_T29 + 28) = _T30
    _T190 = *(_T29 + 32)
    *(_T29 + 32) = _T31
}

FUNCTION(_F.print) {
memo '_T32:4'
_F.print:
    _T191 = " f="
    parm _T191
    call _PrintString
    _T192 = *(_T32 + 28)
    parm _T192
    call _PrintInt
    _T193 = " f1="
    parm _T193
    call _PrintString
    _T194 = *(_T32 + 32)
    parm _T194
    call _PrintInt
    _T195 = " "
    parm _T195
    call _PrintString
}

FUNCTION(_F.allprint) {
memo '_T33:4'
_F.allprint:
    parm _T33
    _T196 = *(_T33 + 0)
    _T197 = *(_T33 + 0)
    _T198 = *(_T197 + 0)
    *(_T33 + 0) = _T198
    _T199 = *(_T33 + 0)
    _T200 = *(_T199 + 0)
    *(_T33 + 0) = _T200
    _T201 = *(_T33 + 0)
    _T202 = *(_T201 + 16)
    call _T202
    *(_T33 + 0) = _T196
    parm _T33
    _T203 = *(_T33 + 0)
    _T204 = *(_T33 + 0)
    _T205 = *(_T204 + 12)
    call _T205
    *(_T33 + 0) = _T203
}

FUNCTION(_F.fun) {
memo '_T34:4'
_F.fun:
    _T206 = "F"
    parm _T206
    call _PrintString
    parm _T34
    _T207 = *(_T34 + 0)
    _T208 = *(_T34 + 0)
    _T209 = *(_T208 + 0)
    *(_T34 + 0) = _T209
    _T210 = *(_T34 + 0)
    _T211 = *(_T210 + 0)
    *(_T34 + 0) = _T211
    _T212 = *(_T34 + 0)
    _T213 = *(_T212 + 16)
    call _T213
    *(_T34 + 0) = _T207
    parm _T34
    _T214 = *(_T34 + 0)
    _T215 = *(_T34 + 0)
    _T216 = *(_T215 + 12)
    call _T216
    *(_T34 + 0) = _T214
    _T217 = "\n"
    parm _T217
    call _PrintString
}

FUNCTION(_G.setG) {
memo '_T35:4 _T36:8'
_G.setG:
    _T218 = *(_T35 + 20)
    *(_T35 + 20) = _T36
}

FUNCTION(_G.print) {
memo '_T37:4'
_G.print:
    _T219 = " g="
    parm _T219
    call _PrintString
    _T220 = *(_T37 + 20)
    parm _T220
    call _PrintInt
}

FUNCTION(_G.allprint) {
memo '_T38:4'
_G.allprint:
    parm _T38
    _T221 = *(_T38 + 0)
    _T222 = *(_T38 + 0)
    _T223 = *(_T222 + 0)
    *(_T38 + 0) = _T223
    _T224 = *(_T38 + 0)
    _T225 = *(_T224 + 16)
    call _T225
    *(_T38 + 0) = _T221
    parm _T38
    _T226 = *(_T38 + 0)
    _T227 = *(_T38 + 0)
    _T228 = *(_T227 + 12)
    call _T228
    *(_T38 + 0) = _T226
}

FUNCTION(_G.fun) {
memo '_T39:4'
_G.fun:
    _T229 = "G"
    parm _T229
    call _PrintString
    parm _T39
    _T230 = *(_T39 + 0)
    _T231 = *(_T39 + 0)
    _T232 = *(_T231 + 0)
    *(_T39 + 0) = _T232
    _T233 = *(_T39 + 0)
    _T234 = *(_T233 + 16)
    call _T234
    *(_T39 + 0) = _T230
    parm _T39
    _T235 = *(_T39 + 0)
    _T236 = *(_T39 + 0)
    _T237 = *(_T236 + 12)
    call _T237
    *(_T39 + 0) = _T235
    _T238 = "\n"
    parm _T238
    call _PrintString
}

FUNCTION(main) {
memo ''
main:
    _T246 =  call _A_New
    _T239 = _T246
    _T247 =  call _B_New
    _T240 = _T247
    _T248 =  call _C_New
    _T241 = _T248
    _T249 =  call _D_New
    _T242 = _T249
    _T250 =  call _E_New
    _T243 = _T250
    _T251 =  call _F_New
    _T244 = _T251
    _T252 =  call _G_New
    _T245 = _T252
    _T253 = 10
    _T254 = 11
    parm _T239
    parm _T253
    parm _T254
    _T255 = *(_T239 + 0)
    _T256 = *(_T239 + 0)
    _T257 = *(_T256 + 8)
    call _T257
    *(_T239 + 0) = _T255
    _T258 = 20
    _T259 = 21
    parm _T240
    parm _T258
    parm _T259
    _T260 = *(_T240 + 0)
    _T261 = *(_T240 + 0)
    _T262 = *(_T261 + 0)
    *(_T240 + 0) = _T262
    _T263 = *(_T240 + 0)
    _T264 = *(_T263 + 8)
    call _T264
    *(_T240 + 0) = _T260
    _T265 = 22
    _T266 = 23
    parm _T240
    parm _T265
    parm _T266
    _T267 = *(_T240 + 0)
    _T268 = *(_T240 + 0)
    _T269 = *(_T268 + 24)
    call _T269
    *(_T240 + 0) = _T267
    _T270 = 30
    _T271 = 31
    parm _T241
    parm _T270
    parm _T271
    _T272 = *(_T241 + 0)
    _T273 = *(_T241 + 0)
    _T274 = *(_T273 + 0)
    *(_T241 + 0) = _T274
    _T275 = *(_T241 + 0)
    _T276 = *(_T275 + 8)
    call _T276
    *(_T241 + 0) = _T272
    _T277 = 32
    _T278 = 33
    parm _T241
    parm _T277
    parm _T278
    _T279 = *(_T241 + 0)
    _T280 = *(_T241 + 0)
    _T281 = *(_T280 + 24)
    call _T281
    *(_T241 + 0) = _T279
    _T282 = 40
    _T283 = 41
    parm _T242
    parm _T282
    parm _T283
    _T284 = *(_T242 + 0)
    _T285 = *(_T242 + 0)
    _T286 = *(_T285 + 0)
    *(_T242 + 0) = _T286
    _T287 = *(_T242 + 0)
    _T288 = *(_T287 + 0)
    *(_T242 + 0) = _T288
    _T289 = *(_T242 + 0)
    _T290 = *(_T289 + 8)
    call _T290
    *(_T242 + 0) = _T284
    _T291 = 42
    _T292 = 43
    parm _T242
    parm _T291
    parm _T292
    _T293 = *(_T242 + 0)
    _T294 = *(_T242 + 0)
    _T295 = *(_T294 + 0)
    *(_T242 + 0) = _T295
    _T296 = *(_T242 + 0)
    _T297 = *(_T296 + 24)
    call _T297
    *(_T242 + 0) = _T293
    _T298 = 44
    _T299 = 45
    parm _T242
    parm _T298
    parm _T299
    _T300 = *(_T242 + 0)
    _T301 = *(_T242 + 0)
    _T302 = *(_T301 + 28)
    call _T302
    *(_T242 + 0) = _T300
    _T303 = 50
    _T304 = 51
    parm _T243
    parm _T303
    parm _T304
    _T305 = *(_T243 + 0)
    _T306 = *(_T243 + 0)
    _T307 = *(_T306 + 0)
    *(_T243 + 0) = _T307
    _T308 = *(_T243 + 0)
    _T309 = *(_T308 + 0)
    *(_T243 + 0) = _T309
    _T310 = *(_T243 + 0)
    _T311 = *(_T310 + 8)
    call _T311
    *(_T243 + 0) = _T305
    _T312 = 52
    _T313 = 53
    parm _T243
    parm _T312
    parm _T313
    _T314 = *(_T243 + 0)
    _T315 = *(_T243 + 0)
    _T316 = *(_T315 + 0)
    *(_T243 + 0) = _T316
    _T317 = *(_T243 + 0)
    _T318 = *(_T317 + 24)
    call _T318
    *(_T243 + 0) = _T314
    _T319 = 54
    _T320 = 55
    parm _T243
    parm _T319
    parm _T320
    _T321 = *(_T243 + 0)
    _T322 = *(_T243 + 0)
    _T323 = *(_T322 + 28)
    call _T323
    *(_T243 + 0) = _T321
    _T324 = 60
    _T325 = 61
    parm _T244
    parm _T324
    parm _T325
    _T326 = *(_T244 + 0)
    _T327 = *(_T244 + 0)
    _T328 = *(_T327 + 0)
    *(_T244 + 0) = _T328
    _T329 = *(_T244 + 0)
    _T330 = *(_T329 + 0)
    *(_T244 + 0) = _T330
    _T331 = *(_T244 + 0)
    _T332 = *(_T331 + 0)
    *(_T244 + 0) = _T332
    _T333 = *(_T244 + 0)
    _T334 = *(_T333 + 8)
    call _T334
    *(_T244 + 0) = _T326
    _T335 = 62
    _T336 = 63
    parm _T244
    parm _T335
    parm _T336
    _T337 = *(_T244 + 0)
    _T338 = *(_T244 + 0)
    _T339 = *(_T338 + 0)
    *(_T244 + 0) = _T339
    _T340 = *(_T244 + 0)
    _T341 = *(_T340 + 0)
    *(_T244 + 0) = _T341
    _T342 = *(_T244 + 0)
    _T343 = *(_T342 + 24)
    call _T343
    *(_T244 + 0) = _T337
    _T344 = 64
    _T345 = 65
    parm _T244
    parm _T344
    parm _T345
    _T346 = *(_T244 + 0)
    _T347 = *(_T244 + 0)
    _T348 = *(_T347 + 0)
    *(_T244 + 0) = _T348
    _T349 = *(_T244 + 0)
    _T350 = *(_T349 + 28)
    call _T350
    *(_T244 + 0) = _T346
    _T351 = 66
    _T352 = 67
    parm _T244
    parm _T351
    parm _T352
    _T353 = *(_T244 + 0)
    _T354 = *(_T244 + 0)
    _T355 = *(_T354 + 32)
    call _T355
    *(_T244 + 0) = _T353
    _T356 = 70
    _T357 = 71
    parm _T245
    parm _T356
    parm _T357
    _T358 = *(_T245 + 0)
    _T359 = *(_T245 + 0)
    _T360 = *(_T359 + 0)
    *(_T245 + 0) = _T360
    _T361 = *(_T245 + 0)
    _T362 = *(_T361 + 0)
    *(_T245 + 0) = _T362
    _T363 = *(_T245 + 0)
    _T364 = *(_T363 + 8)
    call _T364
    *(_T245 + 0) = _T358
    _T365 = 72
    _T366 = 73
    parm _T245
    parm _T365
    parm _T366
    _T367 = *(_T245 + 0)
    _T368 = *(_T245 + 0)
    _T369 = *(_T368 + 0)
    *(_T245 + 0) = _T369
    _T370 = *(_T245 + 0)
    _T371 = *(_T370 + 24)
    call _T371
    *(_T245 + 0) = _T367
    _T372 = 74
    parm _T245
    parm _T372
    _T373 = *(_T245 + 0)
    _T374 = *(_T245 + 0)
    _T375 = *(_T374 + 28)
    call _T375
    *(_T245 + 0) = _T373
    parm _T239
    _T376 = *(_T239 + 0)
    _T377 = *(_T239 + 0)
    _T378 = *(_T377 + 20)
    call _T378
    *(_T239 + 0) = _T376
    parm _T240
    _T379 = *(_T240 + 0)
    _T380 = *(_T240 + 0)
    _T381 = *(_T380 + 20)
    call _T381
    *(_T240 + 0) = _T379
    parm _T241
    _T382 = *(_T241 + 0)
    _T383 = *(_T241 + 0)
    _T384 = *(_T383 + 20)
    call _T384
    *(_T241 + 0) = _T382
    parm _T242
    _T385 = *(_T242 + 0)
    _T386 = *(_T242 + 0)
    _T387 = *(_T386 + 20)
    call _T387
    *(_T242 + 0) = _T385
    parm _T243
    _T388 = *(_T243 + 0)
    _T389 = *(_T243 + 0)
    _T390 = *(_T389 + 20)
    call _T390
    *(_T243 + 0) = _T388
    parm _T244
    _T391 = *(_T244 + 0)
    _T392 = *(_T244 + 0)
    _T393 = *(_T392 + 20)
    call _T393
    *(_T244 + 0) = _T391
    parm _T245
    _T394 = *(_T245 + 0)
    _T395 = *(_T245 + 0)
    _T396 = *(_T395 + 20)
    call _T396
    *(_T245 + 0) = _T394
}

