VTABLE(_A) {
    <empty>
    A
    _A.setA;
    _A.print;
    _A.fun;
}

VTABLE(_B) {
    _A
    B
    _A.setA;
    _B.print;
    _B.fun;
    _B.setB;
}

VTABLE(_C) {
    _A
    C
    _A.setA;
    _C.print;
    _C.fun;
    _C.setC;
}

VTABLE(_D) {
    _B
    D
    _A.setA;
    _D.print;
    _D.fun;
    _B.setB;
    _D.setD;
}

VTABLE(_E) {
    _C
    E
    _A.setA;
    _E.print;
    _E.fun;
    _C.setC;
    _E.setE;
}

VTABLE(_F) {
    _E
    F
    _A.setA;
    _F.print;
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
    _T34 = 12
    parm _T34
    _T35 =  call _Alloc
    _T36 = 0
    *(_T35 + 4) = _T36
    *(_T35 + 8) = _T36
    _T37 = VTBL <_A>
    *(_T35 + 0) = _T37
    return _T35
}

FUNCTION(_B_New) {
memo ''
_B_New:
    _T38 = 20
    parm _T38
    _T39 =  call _Alloc
    _T40 = 0
    *(_T39 + 4) = _T40
    *(_T39 + 8) = _T40
    *(_T39 + 12) = _T40
    *(_T39 + 16) = _T40
    _T41 = VTBL <_B>
    *(_T39 + 0) = _T41
    return _T39
}

FUNCTION(_C_New) {
memo ''
_C_New:
    _T42 = 20
    parm _T42
    _T43 =  call _Alloc
    _T44 = 0
    *(_T43 + 4) = _T44
    *(_T43 + 8) = _T44
    *(_T43 + 12) = _T44
    *(_T43 + 16) = _T44
    _T45 = VTBL <_C>
    *(_T43 + 0) = _T45
    return _T43
}

FUNCTION(_D_New) {
memo ''
_D_New:
    _T46 = 28
    parm _T46
    _T47 =  call _Alloc
    _T48 = 0
    _T49 = 4
    _T50 = (_T47 + _T46)
_L34:
    _T51 = (_T50 - _T49)
    _T50 = _T51
    _T52 = (_T46 - _T49)
    _T46 = _T52
    if (_T46 == 0) branch _L35
    *(_T50 + 0) = _T48
    branch _L34
_L35:
    _T53 = VTBL <_D>
    *(_T50 + 0) = _T53
    return _T50
}

FUNCTION(_E_New) {
memo ''
_E_New:
    _T54 = 28
    parm _T54
    _T55 =  call _Alloc
    _T56 = 0
    _T57 = 4
    _T58 = (_T55 + _T54)
_L37:
    _T59 = (_T58 - _T57)
    _T58 = _T59
    _T60 = (_T54 - _T57)
    _T54 = _T60
    if (_T54 == 0) branch _L38
    *(_T58 + 0) = _T56
    branch _L37
_L38:
    _T61 = VTBL <_E>
    *(_T58 + 0) = _T61
    return _T58
}

FUNCTION(_F_New) {
memo ''
_F_New:
    _T62 = 36
    parm _T62
    _T63 =  call _Alloc
    _T64 = 0
    _T65 = 4
    _T66 = (_T63 + _T62)
_L40:
    _T67 = (_T66 - _T65)
    _T66 = _T67
    _T68 = (_T62 - _T65)
    _T62 = _T68
    if (_T62 == 0) branch _L41
    *(_T66 + 0) = _T64
    branch _L40
_L41:
    _T69 = VTBL <_F>
    *(_T66 + 0) = _T69
    return _T66
}

FUNCTION(_G_New) {
memo ''
_G_New:
    _T70 = 24
    parm _T70
    _T71 =  call _Alloc
    _T72 = 0
    _T73 = 4
    _T74 = (_T71 + _T70)
_L43:
    _T75 = (_T74 - _T73)
    _T74 = _T75
    _T76 = (_T70 - _T73)
    _T70 = _T76
    if (_T70 == 0) branch _L44
    *(_T74 + 0) = _T72
    branch _L43
_L44:
    _T77 = VTBL <_G>
    *(_T74 + 0) = _T77
    return _T74
}

FUNCTION(_Main_New) {
memo ''
_Main_New:
    _T78 = 4
    parm _T78
    _T79 =  call _Alloc
    _T80 = VTBL <_Main>
    *(_T79 + 0) = _T80
    return _T79
}

FUNCTION(_A.setA) {
memo '_T0:4 _T1:8 _T2:12'
_A.setA:
    _T81 = *(_T0 + 4)
    *(_T0 + 4) = _T1
    _T82 = *(_T0 + 8)
    *(_T0 + 8) = _T2
}

FUNCTION(_A.print) {
memo '_T3:4'
_A.print:
    _T83 = " a="
    parm _T83
    call _PrintString
    _T84 = *(_T3 + 4)
    parm _T84
    call _PrintInt
    _T85 = " a1="
    parm _T85
    call _PrintString
    _T86 = *(_T3 + 8)
    parm _T86
    call _PrintInt
    _T87 = " "
    parm _T87
    call _PrintString
}

FUNCTION(_A.fun) {
memo '_T4:4'
_A.fun:
    _T88 = "A"
    parm _T88
    call _PrintString
    parm _T4
    _T89 = *(_T4 + 0)
    _T90 = *(_T4 + 0)
    _T91 = *(_T90 + 12)
    call _T91
    *(_T4 + 0) = _T89
    _T92 = "\n"
    parm _T92
    call _PrintString
}

FUNCTION(_B.setB) {
memo '_T5:4 _T6:8 _T7:12'
_B.setB:
    _T93 = *(_T5 + 12)
    *(_T5 + 12) = _T6
    _T94 = *(_T5 + 16)
    *(_T5 + 16) = _T7
}

FUNCTION(_B.print) {
memo '_T8:4'
_B.print:
    _T95 = " b="
    parm _T95
    call _PrintString
    _T96 = *(_T8 + 12)
    parm _T96
    call _PrintInt
    _T97 = " b1="
    parm _T97
    call _PrintString
    _T98 = *(_T8 + 16)
    parm _T98
    call _PrintInt
    _T99 = " "
    parm _T99
    call _PrintString
}

FUNCTION(_B.fun) {
memo '_T9:4'
_B.fun:
    _T100 = "B"
    parm _T100
    call _PrintString
    parm _T9
    _T101 = *(_T9 + 0)
    _T102 = *(_T9 + 0)
    _T103 = *(_T102 + 0)
    *(_T9 + 0) = _T103
    _T104 = *(_T9 + 0)
    _T105 = *(_T104 + 12)
    call _T105
    *(_T9 + 0) = _T101
    parm _T9
    _T106 = *(_T9 + 0)
    _T107 = *(_T9 + 0)
    _T108 = *(_T107 + 12)
    call _T108
    *(_T9 + 0) = _T106
    _T109 = "\n"
    parm _T109
    call _PrintString
}

FUNCTION(_C.setC) {
memo '_T10:4 _T11:8 _T12:12'
_C.setC:
    _T110 = *(_T10 + 12)
    *(_T10 + 12) = _T11
    _T111 = *(_T10 + 16)
    *(_T10 + 16) = _T12
}

FUNCTION(_C.print) {
memo '_T13:4'
_C.print:
    _T112 = " c="
    parm _T112
    call _PrintString
    _T113 = *(_T13 + 12)
    parm _T113
    call _PrintInt
    _T114 = " c1="
    parm _T114
    call _PrintString
    _T115 = *(_T13 + 16)
    parm _T115
    call _PrintInt
    _T116 = " "
    parm _T116
    call _PrintString
}

FUNCTION(_C.fun) {
memo '_T14:4'
_C.fun:
    _T117 = "C"
    parm _T117
    call _PrintString
    parm _T14
    _T118 = *(_T14 + 0)
    _T119 = *(_T14 + 0)
    _T120 = *(_T119 + 0)
    *(_T14 + 0) = _T120
    _T121 = *(_T14 + 0)
    _T122 = *(_T121 + 12)
    call _T122
    *(_T14 + 0) = _T118
    parm _T14
    _T123 = *(_T14 + 0)
    _T124 = *(_T14 + 0)
    _T125 = *(_T124 + 12)
    call _T125
    *(_T14 + 0) = _T123
    _T126 = "\n"
    parm _T126
    call _PrintString
}

FUNCTION(_D.setD) {
memo '_T15:4 _T16:8 _T17:12'
_D.setD:
    _T127 = *(_T15 + 20)
    *(_T15 + 20) = _T16
    _T128 = *(_T15 + 24)
    *(_T15 + 24) = _T17
}

FUNCTION(_D.print) {
memo '_T18:4'
_D.print:
    _T129 = " d="
    parm _T129
    call _PrintString
    _T130 = *(_T18 + 20)
    parm _T130
    call _PrintInt
    _T131 = " d1="
    parm _T131
    call _PrintString
    _T132 = *(_T18 + 24)
    parm _T132
    call _PrintInt
    _T133 = " "
    parm _T133
    call _PrintString
}

FUNCTION(_D.fun) {
memo '_T19:4'
_D.fun:
    _T134 = "D"
    parm _T134
    call _PrintString
    parm _T19
    _T135 = *(_T19 + 0)
    _T136 = *(_T19 + 0)
    _T137 = *(_T136 + 0)
    *(_T19 + 0) = _T137
    _T138 = *(_T19 + 0)
    _T139 = *(_T138 + 12)
    call _T139
    *(_T19 + 0) = _T135
    parm _T19
    _T140 = *(_T19 + 0)
    _T141 = *(_T19 + 0)
    _T142 = *(_T141 + 12)
    call _T142
    *(_T19 + 0) = _T140
    _T143 = "\n"
    parm _T143
    call _PrintString
}

FUNCTION(_E.setE) {
memo '_T20:4 _T21:8 _T22:12'
_E.setE:
    _T144 = *(_T20 + 20)
    *(_T20 + 20) = _T21
    _T145 = *(_T20 + 24)
    *(_T20 + 24) = _T22
}

FUNCTION(_E.print) {
memo '_T23:4'
_E.print:
    _T146 = " e="
    parm _T146
    call _PrintString
    _T147 = *(_T23 + 20)
    parm _T147
    call _PrintInt
    _T148 = " e1="
    parm _T148
    call _PrintString
    _T149 = *(_T23 + 24)
    parm _T149
    call _PrintInt
    _T150 = " "
    parm _T150
    call _PrintString
}

FUNCTION(_E.fun) {
memo '_T24:4'
_E.fun:
    _T151 = "E"
    parm _T151
    call _PrintString
    parm _T24
    _T152 = *(_T24 + 0)
    _T153 = *(_T24 + 0)
    _T154 = *(_T153 + 0)
    *(_T24 + 0) = _T154
    _T155 = *(_T24 + 0)
    _T156 = *(_T155 + 12)
    call _T156
    *(_T24 + 0) = _T152
    parm _T24
    _T157 = *(_T24 + 0)
    _T158 = *(_T24 + 0)
    _T159 = *(_T158 + 12)
    call _T159
    *(_T24 + 0) = _T157
    _T160 = "\n"
    parm _T160
    call _PrintString
}

FUNCTION(_F.setF) {
memo '_T25:4 _T26:8 _T27:12'
_F.setF:
    _T161 = *(_T25 + 28)
    *(_T25 + 28) = _T26
    _T162 = *(_T25 + 32)
    *(_T25 + 32) = _T27
}

FUNCTION(_F.print) {
memo '_T28:4'
_F.print:
    _T163 = " f="
    parm _T163
    call _PrintString
    _T164 = *(_T28 + 28)
    parm _T164
    call _PrintInt
    _T165 = " f1="
    parm _T165
    call _PrintString
    _T166 = *(_T28 + 32)
    parm _T166
    call _PrintInt
    _T167 = " "
    parm _T167
    call _PrintString
}

FUNCTION(_F.fun) {
memo '_T29:4'
_F.fun:
    _T168 = "F"
    parm _T168
    call _PrintString
    parm _T29
    _T169 = *(_T29 + 0)
    _T170 = *(_T29 + 0)
    _T171 = *(_T170 + 0)
    *(_T29 + 0) = _T171
    _T172 = *(_T29 + 0)
    _T173 = *(_T172 + 12)
    call _T173
    *(_T29 + 0) = _T169
    parm _T29
    _T174 = *(_T29 + 0)
    _T175 = *(_T29 + 0)
    _T176 = *(_T175 + 12)
    call _T176
    *(_T29 + 0) = _T174
    _T177 = "\n"
    parm _T177
    call _PrintString
}

FUNCTION(_G.setG) {
memo '_T30:4 _T31:8'
_G.setG:
    _T178 = *(_T30 + 20)
    *(_T30 + 20) = _T31
}

FUNCTION(_G.print) {
memo '_T32:4'
_G.print:
    _T179 = " g="
    parm _T179
    call _PrintString
    _T180 = *(_T32 + 20)
    parm _T180
    call _PrintInt
}

FUNCTION(_G.fun) {
memo '_T33:4'
_G.fun:
    _T181 = "G"
    parm _T181
    call _PrintString
    parm _T33
    _T182 = *(_T33 + 0)
    _T183 = *(_T33 + 0)
    _T184 = *(_T183 + 0)
    *(_T33 + 0) = _T184
    _T185 = *(_T33 + 0)
    _T186 = *(_T185 + 12)
    call _T186
    *(_T33 + 0) = _T182
    _T187 = "\n"
    parm _T187
    call _PrintString
}

FUNCTION(main) {
memo ''
main:
    _T195 =  call _A_New
    _T188 = _T195
    _T196 =  call _B_New
    _T189 = _T196
    _T197 =  call _C_New
    _T190 = _T197
    _T198 =  call _D_New
    _T191 = _T198
    _T199 =  call _E_New
    _T192 = _T199
    _T200 =  call _F_New
    _T193 = _T200
    _T201 =  call _G_New
    _T194 = _T201
    _T202 = 10
    _T203 = 11
    parm _T188
    parm _T202
    parm _T203
    _T204 = *(_T188 + 0)
    _T205 = *(_T188 + 0)
    _T206 = *(_T205 + 8)
    call _T206
    *(_T188 + 0) = _T204
    _T207 = 20
    _T208 = 21
    parm _T189
    parm _T207
    parm _T208
    _T209 = *(_T189 + 0)
    _T210 = *(_T189 + 0)
    _T211 = *(_T210 + 0)
    *(_T189 + 0) = _T211
    _T212 = *(_T189 + 0)
    _T213 = *(_T212 + 8)
    call _T213
    *(_T189 + 0) = _T209
    _T214 = 22
    _T215 = 23
    parm _T189
    parm _T214
    parm _T215
    _T216 = *(_T189 + 0)
    _T217 = *(_T189 + 0)
    _T218 = *(_T217 + 20)
    call _T218
    *(_T189 + 0) = _T216
    _T219 = 30
    _T220 = 31
    parm _T190
    parm _T219
    parm _T220
    _T221 = *(_T190 + 0)
    _T222 = *(_T190 + 0)
    _T223 = *(_T222 + 0)
    *(_T190 + 0) = _T223
    _T224 = *(_T190 + 0)
    _T225 = *(_T224 + 8)
    call _T225
    *(_T190 + 0) = _T221
    _T226 = 32
    _T227 = 33
    parm _T190
    parm _T226
    parm _T227
    _T228 = *(_T190 + 0)
    _T229 = *(_T190 + 0)
    _T230 = *(_T229 + 20)
    call _T230
    *(_T190 + 0) = _T228
    _T231 = 40
    _T232 = 41
    parm _T191
    parm _T231
    parm _T232
    _T233 = *(_T191 + 0)
    _T234 = *(_T191 + 0)
    _T235 = *(_T234 + 0)
    *(_T191 + 0) = _T235
    _T236 = *(_T191 + 0)
    _T237 = *(_T236 + 0)
    *(_T191 + 0) = _T237
    _T238 = *(_T191 + 0)
    _T239 = *(_T238 + 8)
    call _T239
    *(_T191 + 0) = _T233
    _T240 = 42
    _T241 = 43
    parm _T191
    parm _T240
    parm _T241
    _T242 = *(_T191 + 0)
    _T243 = *(_T191 + 0)
    _T244 = *(_T243 + 0)
    *(_T191 + 0) = _T244
    _T245 = *(_T191 + 0)
    _T246 = *(_T245 + 20)
    call _T246
    *(_T191 + 0) = _T242
    _T247 = 44
    _T248 = 45
    parm _T191
    parm _T247
    parm _T248
    _T249 = *(_T191 + 0)
    _T250 = *(_T191 + 0)
    _T251 = *(_T250 + 24)
    call _T251
    *(_T191 + 0) = _T249
    _T252 = 50
    _T253 = 51
    parm _T192
    parm _T252
    parm _T253
    _T254 = *(_T192 + 0)
    _T255 = *(_T192 + 0)
    _T256 = *(_T255 + 0)
    *(_T192 + 0) = _T256
    _T257 = *(_T192 + 0)
    _T258 = *(_T257 + 0)
    *(_T192 + 0) = _T258
    _T259 = *(_T192 + 0)
    _T260 = *(_T259 + 8)
    call _T260
    *(_T192 + 0) = _T254
    _T261 = 52
    _T262 = 53
    parm _T192
    parm _T261
    parm _T262
    _T263 = *(_T192 + 0)
    _T264 = *(_T192 + 0)
    _T265 = *(_T264 + 0)
    *(_T192 + 0) = _T265
    _T266 = *(_T192 + 0)
    _T267 = *(_T266 + 20)
    call _T267
    *(_T192 + 0) = _T263
    _T268 = 54
    _T269 = 55
    parm _T192
    parm _T268
    parm _T269
    _T270 = *(_T192 + 0)
    _T271 = *(_T192 + 0)
    _T272 = *(_T271 + 24)
    call _T272
    *(_T192 + 0) = _T270
    _T273 = 60
    _T274 = 61
    parm _T193
    parm _T273
    parm _T274
    _T275 = *(_T193 + 0)
    _T276 = *(_T193 + 0)
    _T277 = *(_T276 + 0)
    *(_T193 + 0) = _T277
    _T278 = *(_T193 + 0)
    _T279 = *(_T278 + 0)
    *(_T193 + 0) = _T279
    _T280 = *(_T193 + 0)
    _T281 = *(_T280 + 0)
    *(_T193 + 0) = _T281
    _T282 = *(_T193 + 0)
    _T283 = *(_T282 + 8)
    call _T283
    *(_T193 + 0) = _T275
    _T284 = 62
    _T285 = 63
    parm _T193
    parm _T284
    parm _T285
    _T286 = *(_T193 + 0)
    _T287 = *(_T193 + 0)
    _T288 = *(_T287 + 0)
    *(_T193 + 0) = _T288
    _T289 = *(_T193 + 0)
    _T290 = *(_T289 + 0)
    *(_T193 + 0) = _T290
    _T291 = *(_T193 + 0)
    _T292 = *(_T291 + 20)
    call _T292
    *(_T193 + 0) = _T286
    _T293 = 64
    _T294 = 65
    parm _T193
    parm _T293
    parm _T294
    _T295 = *(_T193 + 0)
    _T296 = *(_T193 + 0)
    _T297 = *(_T296 + 0)
    *(_T193 + 0) = _T297
    _T298 = *(_T193 + 0)
    _T299 = *(_T298 + 24)
    call _T299
    *(_T193 + 0) = _T295
    _T300 = 66
    _T301 = 67
    parm _T193
    parm _T300
    parm _T301
    _T302 = *(_T193 + 0)
    _T303 = *(_T193 + 0)
    _T304 = *(_T303 + 28)
    call _T304
    *(_T193 + 0) = _T302
    _T305 = 70
    _T306 = 71
    parm _T194
    parm _T305
    parm _T306
    _T307 = *(_T194 + 0)
    _T308 = *(_T194 + 0)
    _T309 = *(_T308 + 0)
    *(_T194 + 0) = _T309
    _T310 = *(_T194 + 0)
    _T311 = *(_T310 + 0)
    *(_T194 + 0) = _T311
    _T312 = *(_T194 + 0)
    _T313 = *(_T312 + 8)
    call _T313
    *(_T194 + 0) = _T307
    _T314 = 72
    _T315 = 73
    parm _T194
    parm _T314
    parm _T315
    _T316 = *(_T194 + 0)
    _T317 = *(_T194 + 0)
    _T318 = *(_T317 + 0)
    *(_T194 + 0) = _T318
    _T319 = *(_T194 + 0)
    _T320 = *(_T319 + 20)
    call _T320
    *(_T194 + 0) = _T316
    _T321 = 74
    parm _T194
    parm _T321
    _T322 = *(_T194 + 0)
    _T323 = *(_T194 + 0)
    _T324 = *(_T323 + 24)
    call _T324
    *(_T194 + 0) = _T322
    parm _T188
    _T325 = *(_T188 + 0)
    _T326 = *(_T188 + 0)
    _T327 = *(_T326 + 16)
    call _T327
    *(_T188 + 0) = _T325
    parm _T189
    _T328 = *(_T189 + 0)
    _T329 = *(_T189 + 0)
    _T330 = *(_T329 + 16)
    call _T330
    *(_T189 + 0) = _T328
    parm _T190
    _T331 = *(_T190 + 0)
    _T332 = *(_T190 + 0)
    _T333 = *(_T332 + 16)
    call _T333
    *(_T190 + 0) = _T331
    parm _T191
    _T334 = *(_T191 + 0)
    _T335 = *(_T191 + 0)
    _T336 = *(_T335 + 16)
    call _T336
    *(_T191 + 0) = _T334
    parm _T192
    _T337 = *(_T192 + 0)
    _T338 = *(_T192 + 0)
    _T339 = *(_T338 + 16)
    call _T339
    *(_T192 + 0) = _T337
    parm _T193
    _T340 = *(_T193 + 0)
    _T341 = *(_T193 + 0)
    _T342 = *(_T341 + 16)
    call _T342
    *(_T193 + 0) = _T340
    parm _T194
    _T343 = *(_T194 + 0)
    _T344 = *(_T194 + 0)
    _T345 = *(_T344 + 16)
    call _T345
    *(_T194 + 0) = _T343
}

