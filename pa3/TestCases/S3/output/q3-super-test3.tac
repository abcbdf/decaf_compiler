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
    _E.allprint;
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
    _T41 = 12
    parm _T41
    _T42 =  call _Alloc
    _T43 = 0
    *(_T42 + 4) = _T43
    *(_T42 + 8) = _T43
    _T44 = VTBL <_A>
    *(_T42 + 0) = _T44
    return _T42
}

FUNCTION(_B_New) {
memo ''
_B_New:
    _T45 = 20
    parm _T45
    _T46 =  call _Alloc
    _T47 = 0
    *(_T46 + 4) = _T47
    *(_T46 + 8) = _T47
    *(_T46 + 12) = _T47
    *(_T46 + 16) = _T47
    _T48 = VTBL <_B>
    *(_T46 + 0) = _T48
    return _T46
}

FUNCTION(_C_New) {
memo ''
_C_New:
    _T49 = 20
    parm _T49
    _T50 =  call _Alloc
    _T51 = 0
    *(_T50 + 4) = _T51
    *(_T50 + 8) = _T51
    *(_T50 + 12) = _T51
    *(_T50 + 16) = _T51
    _T52 = VTBL <_C>
    *(_T50 + 0) = _T52
    return _T50
}

FUNCTION(_D_New) {
memo ''
_D_New:
    _T53 = 28
    parm _T53
    _T54 =  call _Alloc
    _T55 = 0
    _T56 = 4
    _T57 = (_T54 + _T53)
_L41:
    _T58 = (_T57 - _T56)
    _T57 = _T58
    _T59 = (_T53 - _T56)
    _T53 = _T59
    if (_T53 == 0) branch _L42
    *(_T57 + 0) = _T55
    branch _L41
_L42:
    _T60 = VTBL <_D>
    *(_T57 + 0) = _T60
    return _T57
}

FUNCTION(_E_New) {
memo ''
_E_New:
    _T61 = 28
    parm _T61
    _T62 =  call _Alloc
    _T63 = 0
    _T64 = 4
    _T65 = (_T62 + _T61)
_L44:
    _T66 = (_T65 - _T64)
    _T65 = _T66
    _T67 = (_T61 - _T64)
    _T61 = _T67
    if (_T61 == 0) branch _L45
    *(_T65 + 0) = _T63
    branch _L44
_L45:
    _T68 = VTBL <_E>
    *(_T65 + 0) = _T68
    return _T65
}

FUNCTION(_F_New) {
memo ''
_F_New:
    _T69 = 36
    parm _T69
    _T70 =  call _Alloc
    _T71 = 0
    _T72 = 4
    _T73 = (_T70 + _T69)
_L47:
    _T74 = (_T73 - _T72)
    _T73 = _T74
    _T75 = (_T69 - _T72)
    _T69 = _T75
    if (_T69 == 0) branch _L48
    *(_T73 + 0) = _T71
    branch _L47
_L48:
    _T76 = VTBL <_F>
    *(_T73 + 0) = _T76
    return _T73
}

FUNCTION(_G_New) {
memo ''
_G_New:
    _T77 = 24
    parm _T77
    _T78 =  call _Alloc
    _T79 = 0
    _T80 = 4
    _T81 = (_T78 + _T77)
_L50:
    _T82 = (_T81 - _T80)
    _T81 = _T82
    _T83 = (_T77 - _T80)
    _T77 = _T83
    if (_T77 == 0) branch _L51
    *(_T81 + 0) = _T79
    branch _L50
_L51:
    _T84 = VTBL <_G>
    *(_T81 + 0) = _T84
    return _T81
}

FUNCTION(_Main_New) {
memo ''
_Main_New:
    _T85 = 4
    parm _T85
    _T86 =  call _Alloc
    _T87 = VTBL <_Main>
    *(_T86 + 0) = _T87
    return _T86
}

FUNCTION(_A.setA) {
memo '_T0:4 _T1:8 _T2:12'
_A.setA:
    _T88 = *(_T0 + 4)
    *(_T0 + 4) = _T1
    _T89 = *(_T0 + 8)
    *(_T0 + 8) = _T2
}

FUNCTION(_A.print) {
memo '_T3:4'
_A.print:
    _T90 = " a="
    parm _T90
    call _PrintString
    _T91 = *(_T3 + 4)
    parm _T91
    call _PrintInt
    _T92 = " a1="
    parm _T92
    call _PrintString
    _T93 = *(_T3 + 8)
    parm _T93
    call _PrintInt
    _T94 = " "
    parm _T94
    call _PrintString
}

FUNCTION(_A.allprint) {
memo '_T4:4'
_A.allprint:
    parm _T4
    _T95 = *(_T4 + 0)
    _T96 = *(_T4 + 0)
    _T97 = *(_T96 + 12)
    call _T97
    *(_T4 + 0) = _T95
}

FUNCTION(_A.fun) {
memo '_T5:4'
_A.fun:
    _T98 = "A"
    parm _T98
    call _PrintString
    parm _T5
    _T99 = *(_T5 + 0)
    _T100 = *(_T5 + 0)
    _T101 = *(_T100 + 12)
    call _T101
    *(_T5 + 0) = _T99
    _T102 = "\n"
    parm _T102
    call _PrintString
}

FUNCTION(_B.setB) {
memo '_T6:4 _T7:8 _T8:12'
_B.setB:
    _T103 = *(_T6 + 12)
    *(_T6 + 12) = _T7
    _T104 = *(_T6 + 16)
    *(_T6 + 16) = _T8
}

FUNCTION(_B.print) {
memo '_T9:4'
_B.print:
    _T105 = " b="
    parm _T105
    call _PrintString
    _T106 = *(_T9 + 12)
    parm _T106
    call _PrintInt
    _T107 = " b1="
    parm _T107
    call _PrintString
    _T108 = *(_T9 + 16)
    parm _T108
    call _PrintInt
    _T109 = " "
    parm _T109
    call _PrintString
}

FUNCTION(_B.allprint) {
memo '_T10:4'
_B.allprint:
    parm _T10
    _T110 = *(_T10 + 0)
    _T111 = *(_T10 + 0)
    _T112 = *(_T111 + 0)
    *(_T10 + 0) = _T112
    _T113 = *(_T10 + 0)
    _T114 = *(_T113 + 16)
    call _T114
    *(_T10 + 0) = _T110
    parm _T10
    _T115 = *(_T10 + 0)
    _T116 = *(_T10 + 0)
    _T117 = *(_T116 + 12)
    call _T117
    *(_T10 + 0) = _T115
}

FUNCTION(_B.fun) {
memo '_T11:4'
_B.fun:
    _T118 = "B"
    parm _T118
    call _PrintString
    parm _T11
    _T119 = *(_T11 + 0)
    _T120 = *(_T11 + 0)
    _T121 = *(_T120 + 0)
    *(_T11 + 0) = _T121
    _T122 = *(_T11 + 0)
    _T123 = *(_T122 + 16)
    call _T123
    *(_T11 + 0) = _T119
    parm _T11
    _T124 = *(_T11 + 0)
    _T125 = *(_T11 + 0)
    _T126 = *(_T125 + 12)
    call _T126
    *(_T11 + 0) = _T124
    _T127 = "\n"
    parm _T127
    call _PrintString
}

FUNCTION(_C.setC) {
memo '_T12:4 _T13:8 _T14:12'
_C.setC:
    _T128 = *(_T12 + 12)
    *(_T12 + 12) = _T13
    _T129 = *(_T12 + 16)
    *(_T12 + 16) = _T14
}

FUNCTION(_C.print) {
memo '_T15:4'
_C.print:
    _T130 = " c="
    parm _T130
    call _PrintString
    _T131 = *(_T15 + 12)
    parm _T131
    call _PrintInt
    _T132 = " c1="
    parm _T132
    call _PrintString
    _T133 = *(_T15 + 16)
    parm _T133
    call _PrintInt
    _T134 = " "
    parm _T134
    call _PrintString
}

FUNCTION(_C.allprint) {
memo '_T16:4'
_C.allprint:
    parm _T16
    _T135 = *(_T16 + 0)
    _T136 = *(_T16 + 0)
    _T137 = *(_T136 + 0)
    *(_T16 + 0) = _T137
    _T138 = *(_T16 + 0)
    _T139 = *(_T138 + 16)
    call _T139
    *(_T16 + 0) = _T135
    parm _T16
    _T140 = *(_T16 + 0)
    _T141 = *(_T16 + 0)
    _T142 = *(_T141 + 12)
    call _T142
    *(_T16 + 0) = _T140
}

FUNCTION(_C.fun) {
memo '_T17:4'
_C.fun:
    _T143 = "C"
    parm _T143
    call _PrintString
    parm _T17
    _T144 = *(_T17 + 0)
    _T145 = *(_T17 + 0)
    _T146 = *(_T145 + 0)
    *(_T17 + 0) = _T146
    _T147 = *(_T17 + 0)
    _T148 = *(_T147 + 16)
    call _T148
    *(_T17 + 0) = _T144
    parm _T17
    _T149 = *(_T17 + 0)
    _T150 = *(_T17 + 0)
    _T151 = *(_T150 + 12)
    call _T151
    *(_T17 + 0) = _T149
    _T152 = "\n"
    parm _T152
    call _PrintString
}

FUNCTION(_D.setD) {
memo '_T18:4 _T19:8 _T20:12'
_D.setD:
    _T153 = *(_T18 + 20)
    *(_T18 + 20) = _T19
    _T154 = *(_T18 + 24)
    *(_T18 + 24) = _T20
}

FUNCTION(_D.print) {
memo '_T21:4'
_D.print:
    _T155 = " d="
    parm _T155
    call _PrintString
    _T156 = *(_T21 + 20)
    parm _T156
    call _PrintInt
    _T157 = " d1="
    parm _T157
    call _PrintString
    _T158 = *(_T21 + 24)
    parm _T158
    call _PrintInt
    _T159 = " "
    parm _T159
    call _PrintString
}

FUNCTION(_D.allprint) {
memo '_T22:4'
_D.allprint:
    parm _T22
    _T160 = *(_T22 + 0)
    _T161 = *(_T22 + 0)
    _T162 = *(_T161 + 0)
    *(_T22 + 0) = _T162
    _T163 = *(_T22 + 0)
    _T164 = *(_T163 + 16)
    call _T164
    *(_T22 + 0) = _T160
    parm _T22
    _T165 = *(_T22 + 0)
    _T166 = *(_T22 + 0)
    _T167 = *(_T166 + 12)
    call _T167
    *(_T22 + 0) = _T165
}

FUNCTION(_D.fun) {
memo '_T23:4'
_D.fun:
    _T168 = "D"
    parm _T168
    call _PrintString
    parm _T23
    _T169 = *(_T23 + 0)
    _T170 = *(_T23 + 0)
    _T171 = *(_T170 + 0)
    *(_T23 + 0) = _T171
    _T172 = *(_T23 + 0)
    _T173 = *(_T172 + 16)
    call _T173
    *(_T23 + 0) = _T169
    parm _T23
    _T174 = *(_T23 + 0)
    _T175 = *(_T23 + 0)
    _T176 = *(_T175 + 12)
    call _T176
    *(_T23 + 0) = _T174
    _T177 = "\n"
    parm _T177
    call _PrintString
}

FUNCTION(_E.setE) {
memo '_T24:4 _T25:8 _T26:12'
_E.setE:
    _T178 = *(_T24 + 20)
    *(_T24 + 20) = _T25
    _T179 = *(_T24 + 24)
    *(_T24 + 24) = _T26
}

FUNCTION(_E.print) {
memo '_T27:4'
_E.print:
    _T180 = " e="
    parm _T180
    call _PrintString
    _T181 = *(_T27 + 20)
    parm _T181
    call _PrintInt
    _T182 = " e1="
    parm _T182
    call _PrintString
    _T183 = *(_T27 + 24)
    parm _T183
    call _PrintInt
    _T184 = " "
    parm _T184
    call _PrintString
}

FUNCTION(_E.allprint) {
memo '_T28:4'
_E.allprint:
    parm _T28
    _T185 = *(_T28 + 0)
    _T186 = *(_T28 + 0)
    _T187 = *(_T186 + 0)
    *(_T28 + 0) = _T187
    _T188 = *(_T28 + 0)
    _T189 = *(_T188 + 16)
    call _T189
    *(_T28 + 0) = _T185
    parm _T28
    _T190 = *(_T28 + 0)
    _T191 = *(_T28 + 0)
    _T192 = *(_T191 + 12)
    call _T192
    *(_T28 + 0) = _T190
}

FUNCTION(_E.fun) {
memo '_T29:4'
_E.fun:
    _T193 = "E"
    parm _T193
    call _PrintString
    parm _T29
    _T194 = *(_T29 + 0)
    _T195 = *(_T29 + 0)
    _T196 = *(_T195 + 0)
    *(_T29 + 0) = _T196
    _T197 = *(_T29 + 0)
    _T198 = *(_T197 + 16)
    call _T198
    *(_T29 + 0) = _T194
    parm _T29
    _T199 = *(_T29 + 0)
    _T200 = *(_T29 + 0)
    _T201 = *(_T200 + 12)
    call _T201
    *(_T29 + 0) = _T199
    _T202 = "\n"
    parm _T202
    call _PrintString
}

FUNCTION(_F.setF) {
memo '_T30:4 _T31:8 _T32:12'
_F.setF:
    _T203 = *(_T30 + 28)
    *(_T30 + 28) = _T31
    _T204 = *(_T30 + 32)
    *(_T30 + 32) = _T32
}

FUNCTION(_F.print) {
memo '_T33:4'
_F.print:
    _T205 = " f="
    parm _T205
    call _PrintString
    _T206 = *(_T33 + 28)
    parm _T206
    call _PrintInt
    _T207 = " f1="
    parm _T207
    call _PrintString
    _T208 = *(_T33 + 32)
    parm _T208
    call _PrintInt
    _T209 = " "
    parm _T209
    call _PrintString
}

FUNCTION(_F.allprint) {
memo '_T34:4'
_F.allprint:
    parm _T34
    _T210 = *(_T34 + 0)
    _T211 = *(_T34 + 0)
    _T212 = *(_T211 + 0)
    *(_T34 + 0) = _T212
    _T213 = *(_T34 + 0)
    _T214 = *(_T213 + 16)
    call _T214
    *(_T34 + 0) = _T210
    parm _T34
    _T215 = *(_T34 + 0)
    _T216 = *(_T34 + 0)
    _T217 = *(_T216 + 12)
    call _T217
    *(_T34 + 0) = _T215
}

FUNCTION(_F.fun) {
memo '_T35:4'
_F.fun:
    _T218 = "F"
    parm _T218
    call _PrintString
    parm _T35
    _T219 = *(_T35 + 0)
    _T220 = *(_T35 + 0)
    _T221 = *(_T220 + 0)
    *(_T35 + 0) = _T221
    _T222 = *(_T35 + 0)
    _T223 = *(_T222 + 16)
    call _T223
    *(_T35 + 0) = _T219
    parm _T35
    _T224 = *(_T35 + 0)
    _T225 = *(_T35 + 0)
    _T226 = *(_T225 + 12)
    call _T226
    *(_T35 + 0) = _T224
    _T227 = "\n"
    parm _T227
    call _PrintString
}

FUNCTION(_G.setG) {
memo '_T36:4 _T37:8'
_G.setG:
    _T228 = *(_T36 + 20)
    *(_T36 + 20) = _T37
}

FUNCTION(_G.print) {
memo '_T38:4'
_G.print:
    _T229 = " g="
    parm _T229
    call _PrintString
    _T230 = *(_T38 + 20)
    parm _T230
    call _PrintInt
}

FUNCTION(_G.allprint) {
memo '_T39:4'
_G.allprint:
    parm _T39
    _T231 = *(_T39 + 0)
    _T232 = *(_T39 + 0)
    _T233 = *(_T232 + 0)
    *(_T39 + 0) = _T233
    _T234 = *(_T39 + 0)
    _T235 = *(_T234 + 16)
    call _T235
    *(_T39 + 0) = _T231
    parm _T39
    _T236 = *(_T39 + 0)
    _T237 = *(_T39 + 0)
    _T238 = *(_T237 + 12)
    call _T238
    *(_T39 + 0) = _T236
}

FUNCTION(_G.fun) {
memo '_T40:4'
_G.fun:
    _T239 = "G"
    parm _T239
    call _PrintString
    parm _T40
    _T240 = *(_T40 + 0)
    _T241 = *(_T40 + 0)
    _T242 = *(_T241 + 0)
    *(_T40 + 0) = _T242
    _T243 = *(_T40 + 0)
    _T244 = *(_T243 + 16)
    call _T244
    *(_T40 + 0) = _T240
    parm _T40
    _T245 = *(_T40 + 0)
    _T246 = *(_T40 + 0)
    _T247 = *(_T246 + 12)
    call _T247
    *(_T40 + 0) = _T245
    _T248 = "\n"
    parm _T248
    call _PrintString
}

FUNCTION(main) {
memo ''
main:
    _T256 =  call _A_New
    _T249 = _T256
    _T257 =  call _B_New
    _T250 = _T257
    _T258 =  call _C_New
    _T251 = _T258
    _T259 =  call _D_New
    _T252 = _T259
    _T260 =  call _E_New
    _T253 = _T260
    _T261 =  call _F_New
    _T254 = _T261
    _T262 =  call _G_New
    _T255 = _T262
    _T263 = 10
    _T264 = 11
    parm _T249
    parm _T263
    parm _T264
    _T265 = *(_T249 + 0)
    _T266 = *(_T249 + 0)
    _T267 = *(_T266 + 8)
    call _T267
    *(_T249 + 0) = _T265
    _T268 = 20
    _T269 = 21
    parm _T250
    parm _T268
    parm _T269
    _T270 = *(_T250 + 0)
    _T271 = *(_T250 + 0)
    _T272 = *(_T271 + 0)
    *(_T250 + 0) = _T272
    _T273 = *(_T250 + 0)
    _T274 = *(_T273 + 8)
    call _T274
    *(_T250 + 0) = _T270
    _T275 = 22
    _T276 = 23
    parm _T250
    parm _T275
    parm _T276
    _T277 = *(_T250 + 0)
    _T278 = *(_T250 + 0)
    _T279 = *(_T278 + 24)
    call _T279
    *(_T250 + 0) = _T277
    _T280 = 30
    _T281 = 31
    parm _T251
    parm _T280
    parm _T281
    _T282 = *(_T251 + 0)
    _T283 = *(_T251 + 0)
    _T284 = *(_T283 + 0)
    *(_T251 + 0) = _T284
    _T285 = *(_T251 + 0)
    _T286 = *(_T285 + 8)
    call _T286
    *(_T251 + 0) = _T282
    _T287 = 32
    _T288 = 33
    parm _T251
    parm _T287
    parm _T288
    _T289 = *(_T251 + 0)
    _T290 = *(_T251 + 0)
    _T291 = *(_T290 + 24)
    call _T291
    *(_T251 + 0) = _T289
    _T292 = 40
    _T293 = 41
    parm _T252
    parm _T292
    parm _T293
    _T294 = *(_T252 + 0)
    _T295 = *(_T252 + 0)
    _T296 = *(_T295 + 0)
    *(_T252 + 0) = _T296
    _T297 = *(_T252 + 0)
    _T298 = *(_T297 + 0)
    *(_T252 + 0) = _T298
    _T299 = *(_T252 + 0)
    _T300 = *(_T299 + 8)
    call _T300
    *(_T252 + 0) = _T294
    _T301 = 42
    _T302 = 43
    parm _T252
    parm _T301
    parm _T302
    _T303 = *(_T252 + 0)
    _T304 = *(_T252 + 0)
    _T305 = *(_T304 + 0)
    *(_T252 + 0) = _T305
    _T306 = *(_T252 + 0)
    _T307 = *(_T306 + 24)
    call _T307
    *(_T252 + 0) = _T303
    _T308 = 44
    _T309 = 45
    parm _T252
    parm _T308
    parm _T309
    _T310 = *(_T252 + 0)
    _T311 = *(_T252 + 0)
    _T312 = *(_T311 + 28)
    call _T312
    *(_T252 + 0) = _T310
    _T313 = 50
    _T314 = 51
    parm _T253
    parm _T313
    parm _T314
    _T315 = *(_T253 + 0)
    _T316 = *(_T253 + 0)
    _T317 = *(_T316 + 0)
    *(_T253 + 0) = _T317
    _T318 = *(_T253 + 0)
    _T319 = *(_T318 + 0)
    *(_T253 + 0) = _T319
    _T320 = *(_T253 + 0)
    _T321 = *(_T320 + 8)
    call _T321
    *(_T253 + 0) = _T315
    _T322 = 52
    _T323 = 53
    parm _T253
    parm _T322
    parm _T323
    _T324 = *(_T253 + 0)
    _T325 = *(_T253 + 0)
    _T326 = *(_T325 + 0)
    *(_T253 + 0) = _T326
    _T327 = *(_T253 + 0)
    _T328 = *(_T327 + 24)
    call _T328
    *(_T253 + 0) = _T324
    _T329 = 54
    _T330 = 55
    parm _T253
    parm _T329
    parm _T330
    _T331 = *(_T253 + 0)
    _T332 = *(_T253 + 0)
    _T333 = *(_T332 + 28)
    call _T333
    *(_T253 + 0) = _T331
    _T334 = 60
    _T335 = 61
    parm _T254
    parm _T334
    parm _T335
    _T336 = *(_T254 + 0)
    _T337 = *(_T254 + 0)
    _T338 = *(_T337 + 0)
    *(_T254 + 0) = _T338
    _T339 = *(_T254 + 0)
    _T340 = *(_T339 + 0)
    *(_T254 + 0) = _T340
    _T341 = *(_T254 + 0)
    _T342 = *(_T341 + 0)
    *(_T254 + 0) = _T342
    _T343 = *(_T254 + 0)
    _T344 = *(_T343 + 8)
    call _T344
    *(_T254 + 0) = _T336
    _T345 = 62
    _T346 = 63
    parm _T254
    parm _T345
    parm _T346
    _T347 = *(_T254 + 0)
    _T348 = *(_T254 + 0)
    _T349 = *(_T348 + 0)
    *(_T254 + 0) = _T349
    _T350 = *(_T254 + 0)
    _T351 = *(_T350 + 0)
    *(_T254 + 0) = _T351
    _T352 = *(_T254 + 0)
    _T353 = *(_T352 + 24)
    call _T353
    *(_T254 + 0) = _T347
    _T354 = 64
    _T355 = 65
    parm _T254
    parm _T354
    parm _T355
    _T356 = *(_T254 + 0)
    _T357 = *(_T254 + 0)
    _T358 = *(_T357 + 0)
    *(_T254 + 0) = _T358
    _T359 = *(_T254 + 0)
    _T360 = *(_T359 + 28)
    call _T360
    *(_T254 + 0) = _T356
    _T361 = 66
    _T362 = 67
    parm _T254
    parm _T361
    parm _T362
    _T363 = *(_T254 + 0)
    _T364 = *(_T254 + 0)
    _T365 = *(_T364 + 32)
    call _T365
    *(_T254 + 0) = _T363
    _T366 = 70
    _T367 = 71
    parm _T255
    parm _T366
    parm _T367
    _T368 = *(_T255 + 0)
    _T369 = *(_T255 + 0)
    _T370 = *(_T369 + 0)
    *(_T255 + 0) = _T370
    _T371 = *(_T255 + 0)
    _T372 = *(_T371 + 0)
    *(_T255 + 0) = _T372
    _T373 = *(_T255 + 0)
    _T374 = *(_T373 + 8)
    call _T374
    *(_T255 + 0) = _T368
    _T375 = 72
    _T376 = 73
    parm _T255
    parm _T375
    parm _T376
    _T377 = *(_T255 + 0)
    _T378 = *(_T255 + 0)
    _T379 = *(_T378 + 0)
    *(_T255 + 0) = _T379
    _T380 = *(_T255 + 0)
    _T381 = *(_T380 + 24)
    call _T381
    *(_T255 + 0) = _T377
    _T382 = 74
    parm _T255
    parm _T382
    _T383 = *(_T255 + 0)
    _T384 = *(_T255 + 0)
    _T385 = *(_T384 + 28)
    call _T385
    *(_T255 + 0) = _T383
    parm _T249
    _T386 = *(_T249 + 0)
    _T387 = *(_T249 + 0)
    _T388 = *(_T387 + 20)
    call _T388
    *(_T249 + 0) = _T386
    parm _T250
    _T389 = *(_T250 + 0)
    _T390 = *(_T250 + 0)
    _T391 = *(_T390 + 20)
    call _T391
    *(_T250 + 0) = _T389
    parm _T251
    _T392 = *(_T251 + 0)
    _T393 = *(_T251 + 0)
    _T394 = *(_T393 + 20)
    call _T394
    *(_T251 + 0) = _T392
    parm _T252
    _T395 = *(_T252 + 0)
    _T396 = *(_T252 + 0)
    _T397 = *(_T396 + 20)
    call _T397
    *(_T252 + 0) = _T395
    parm _T253
    _T398 = *(_T253 + 0)
    _T399 = *(_T253 + 0)
    _T400 = *(_T399 + 20)
    call _T400
    *(_T253 + 0) = _T398
    parm _T254
    _T401 = *(_T254 + 0)
    _T402 = *(_T254 + 0)
    _T403 = *(_T402 + 20)
    call _T403
    *(_T254 + 0) = _T401
    parm _T255
    _T404 = *(_T255 + 0)
    _T405 = *(_T255 + 0)
    _T406 = *(_T405 + 20)
    call _T406
    *(_T255 + 0) = _T404
}

