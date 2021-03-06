VTABLE(_rndModule) {
    <empty>
    rndModule
    _rndModule.Init;
    _rndModule.Random;
    _rndModule.RndInt;
}

VTABLE(_Deck) {
    <empty>
    Deck
    _Deck.Init;
    _Deck.Shuffle;
    _Deck.GetCard;
}

VTABLE(_BJDeck) {
    <empty>
    BJDeck
    _BJDeck.Init;
    _BJDeck.DealCard;
    _BJDeck.Shuffle;
    _BJDeck.NumCardsRemaining;
}

VTABLE(_Player) {
    <empty>
    Player
    _Player.Init;
    _Player.Hit;
    _Player.DoubleDown;
    _Player.TakeTurn;
    _Player.HasMoney;
    _Player.PrintMoney;
    _Player.PlaceBet;
    _Player.GetTotal;
    _Player.Resolve;
    _Player.GetYesOrNo;
}

VTABLE(_Dealer) {
    _Player
    Dealer
    _Dealer.Init;
    _Player.Hit;
    _Player.DoubleDown;
    _Dealer.TakeTurn;
    _Player.HasMoney;
    _Player.PrintMoney;
    _Player.PlaceBet;
    _Player.GetTotal;
    _Player.Resolve;
    _Player.GetYesOrNo;
}

VTABLE(_House) {
    <empty>
    House
    _House.SetupGame;
    _House.SetupPlayers;
    _House.TakeAllBets;
    _House.TakeAllTurns;
    _House.ResolveAllPlayers;
    _House.PrintAllMoney;
    _House.PlayOneGame;
}

VTABLE(_Main) {
    <empty>
    Main
}

FUNCTION(_rndModule_New) {
memo ''
_rndModule_New:
    _T42 = 8
    parm _T42
    _T43 =  call _Alloc
    _T44 = 0
    *(_T43 + 4) = _T44
    _T45 = VTBL <_rndModule>
    *(_T43 + 0) = _T45
    return _T43
}

FUNCTION(_Deck_New) {
memo ''
_Deck_New:
    _T46 = 16
    parm _T46
    _T47 =  call _Alloc
    _T48 = 0
    *(_T47 + 4) = _T48
    *(_T47 + 8) = _T48
    *(_T47 + 12) = _T48
    _T49 = VTBL <_Deck>
    *(_T47 + 0) = _T49
    return _T47
}

FUNCTION(_BJDeck_New) {
memo ''
_BJDeck_New:
    _T50 = 16
    parm _T50
    _T51 =  call _Alloc
    _T52 = 0
    *(_T51 + 4) = _T52
    *(_T51 + 8) = _T52
    *(_T51 + 12) = _T52
    _T53 = VTBL <_BJDeck>
    *(_T51 + 0) = _T53
    return _T51
}

FUNCTION(_Player_New) {
memo ''
_Player_New:
    _T54 = 28
    parm _T54
    _T55 =  call _Alloc
    _T56 = 0
    _T57 = 4
    _T58 = (_T55 + _T54)
_L43:
    _T59 = (_T58 - _T57)
    _T58 = _T59
    _T60 = (_T54 - _T57)
    _T54 = _T60
    if (_T54 == 0) branch _L44
    *(_T58 + 0) = _T56
    branch _L43
_L44:
    _T61 = VTBL <_Player>
    *(_T58 + 0) = _T61
    return _T58
}

FUNCTION(_Dealer_New) {
memo ''
_Dealer_New:
    _T62 = 28
    parm _T62
    _T63 =  call _Alloc
    _T64 = 0
    _T65 = 4
    _T66 = (_T63 + _T62)
_L46:
    _T67 = (_T66 - _T65)
    _T66 = _T67
    _T68 = (_T62 - _T65)
    _T62 = _T68
    if (_T62 == 0) branch _L47
    *(_T66 + 0) = _T64
    branch _L46
_L47:
    _T69 = VTBL <_Dealer>
    *(_T66 + 0) = _T69
    return _T66
}

FUNCTION(_House_New) {
memo ''
_House_New:
    _T70 = 16
    parm _T70
    _T71 =  call _Alloc
    _T72 = 0
    *(_T71 + 4) = _T72
    *(_T71 + 8) = _T72
    *(_T71 + 12) = _T72
    _T73 = VTBL <_House>
    *(_T71 + 0) = _T73
    return _T71
}

FUNCTION(_Main_New) {
memo ''
_Main_New:
    _T74 = 4
    parm _T74
    _T75 =  call _Alloc
    _T76 = VTBL <_Main>
    *(_T75 + 0) = _T76
    return _T75
}

FUNCTION(_rndModule.Init) {
memo '_T0:4 _T1:8'
_rndModule.Init:
    _T77 = *(_T0 + 4)
    *(_T0 + 4) = _T1
}

FUNCTION(_rndModule.Random) {
memo '_T2:4'
_rndModule.Random:
    _T78 = *(_T2 + 4)
    _T79 = 15625
    _T80 = *(_T2 + 4)
    _T81 = 10000
    _T82 = 0
    _T83 = (_T81 == _T82)
    if (_T83 == 0) branch _L50
    _T84 = "Decaf runtime error: Division by zero error.\n"
    parm _T84
    call _PrintString
    call _Halt
_L50:
    _T85 = (_T80 % _T81)
    _T86 = (_T79 * _T85)
    _T87 = 22221
    _T88 = (_T86 + _T87)
    _T89 = 65536
    _T90 = 0
    _T91 = (_T89 == _T90)
    if (_T91 == 0) branch _L51
    _T92 = "Decaf runtime error: Division by zero error.\n"
    parm _T92
    call _PrintString
    call _Halt
_L51:
    _T93 = (_T88 % _T89)
    *(_T2 + 4) = _T93
    _T94 = *(_T2 + 4)
    return _T94
}

FUNCTION(_rndModule.RndInt) {
memo '_T3:4 _T4:8'
_rndModule.RndInt:
    parm _T3
    _T95 = *(_T3 + 0)
    _T96 = *(_T3 + 0)
    _T97 = *(_T96 + 12)
    _T98 =  call _T97
    *(_T3 + 0) = _T95
    _T99 = 0
    _T100 = (_T4 == _T99)
    if (_T100 == 0) branch _L52
    _T101 = "Decaf runtime error: Division by zero error.\n"
    parm _T101
    call _PrintString
    call _Halt
_L52:
    _T102 = (_T98 % _T4)
    return _T102
}

FUNCTION(_Deck.Init) {
memo '_T5:4 _T6:8'
_Deck.Init:
    _T103 = *(_T5 + 8)
    _T104 = 52
    _T105 = 0
    _T106 = (_T104 < _T105)
    if (_T106 == 0) branch _L53
    _T107 = "Decaf runtime error: Cannot create negative-sized array\n"
    parm _T107
    call _PrintString
    call _Halt
_L53:
    _T108 = 4
    _T109 = (_T108 * _T104)
    _T110 = (_T108 + _T109)
    parm _T110
    _T111 =  call _Alloc
    *(_T111 + 0) = _T104
    _T112 = 0
    _T111 = (_T111 + _T110)
_L54:
    _T110 = (_T110 - _T108)
    if (_T110 == 0) branch _L55
    _T111 = (_T111 - _T108)
    *(_T111 + 0) = _T112
    branch _L54
_L55:
    *(_T5 + 8) = _T111
    _T113 = *(_T5 + 12)
    *(_T5 + 12) = _T6
}

FUNCTION(_Deck.Shuffle) {
memo '_T7:4'
_Deck.Shuffle:
    _T114 = *(_T7 + 4)
    _T115 = 1
    *(_T7 + 4) = _T115
    branch _L56
_L57:
    _T116 = *(_T7 + 4)
    _T117 = *(_T7 + 4)
    _T118 = 1
    _T119 = (_T117 + _T118)
    *(_T7 + 4) = _T119
_L56:
    _T120 = *(_T7 + 4)
    _T121 = 52
    _T122 = (_T120 <= _T121)
    if (_T122 == 0) branch _L58
    _T123 = *(_T7 + 8)
    _T124 = *(_T7 + 4)
    _T125 = 1
    _T126 = (_T124 - _T125)
    _T127 = *(_T123 - 4)
    _T128 = (_T126 < _T127)
    if (_T128 == 0) branch _L59
    _T129 = 0
    _T130 = (_T126 < _T129)
    if (_T130 == 0) branch _L60
_L59:
    _T131 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T131
    call _PrintString
    call _Halt
_L60:
    _T132 = 4
    _T133 = (_T126 * _T132)
    _T134 = (_T123 + _T133)
    _T135 = *(_T134 + 0)
    _T136 = *(_T7 + 4)
    _T137 = 13
    _T138 = 0
    _T139 = (_T137 == _T138)
    if (_T139 == 0) branch _L61
    _T140 = "Decaf runtime error: Division by zero error.\n"
    parm _T140
    call _PrintString
    call _Halt
_L61:
    _T141 = (_T136 % _T137)
    _T142 = 4
    _T143 = (_T126 * _T142)
    _T144 = (_T123 + _T143)
    *(_T144 + 0) = _T141
    branch _L57
_L58:
    _T145 = *(_T7 + 4)
    _T146 = *(_T7 + 4)
    _T147 = 1
    _T148 = (_T146 - _T147)
    *(_T7 + 4) = _T148
_L62:
    _T149 = *(_T7 + 4)
    _T150 = 0
    _T151 = (_T149 > _T150)
    if (_T151 == 0) branch _L63
    _T154 = *(_T7 + 12)
    _T155 = *(_T7 + 4)
    parm _T154
    parm _T155
    _T156 = *(_T154 + 0)
    _T157 = *(_T154 + 0)
    _T158 = *(_T157 + 16)
    _T159 =  call _T158
    *(_T154 + 0) = _T156
    _T152 = _T159
    _T160 = *(_T7 + 4)
    _T161 = *(_T7 + 4)
    _T162 = 1
    _T163 = (_T161 - _T162)
    *(_T7 + 4) = _T163
    _T164 = *(_T7 + 8)
    _T165 = *(_T7 + 4)
    _T166 = *(_T164 - 4)
    _T167 = (_T165 < _T166)
    if (_T167 == 0) branch _L64
    _T168 = 0
    _T169 = (_T165 < _T168)
    if (_T169 == 0) branch _L65
_L64:
    _T170 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T170
    call _PrintString
    call _Halt
_L65:
    _T171 = 4
    _T172 = (_T165 * _T171)
    _T173 = (_T164 + _T172)
    _T174 = *(_T173 + 0)
    _T153 = _T174
    _T175 = *(_T7 + 8)
    _T176 = *(_T7 + 4)
    _T177 = *(_T175 - 4)
    _T178 = (_T176 < _T177)
    if (_T178 == 0) branch _L66
    _T179 = 0
    _T180 = (_T176 < _T179)
    if (_T180 == 0) branch _L67
_L66:
    _T181 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T181
    call _PrintString
    call _Halt
_L67:
    _T182 = 4
    _T183 = (_T176 * _T182)
    _T184 = (_T175 + _T183)
    _T185 = *(_T184 + 0)
    _T186 = *(_T7 + 8)
    _T187 = *(_T186 - 4)
    _T188 = (_T152 < _T187)
    if (_T188 == 0) branch _L68
    _T189 = 0
    _T190 = (_T152 < _T189)
    if (_T190 == 0) branch _L69
_L68:
    _T191 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T191
    call _PrintString
    call _Halt
_L69:
    _T192 = 4
    _T193 = (_T152 * _T192)
    _T194 = (_T186 + _T193)
    _T195 = *(_T194 + 0)
    _T196 = 4
    _T197 = (_T176 * _T196)
    _T198 = (_T175 + _T197)
    *(_T198 + 0) = _T195
    _T199 = *(_T7 + 8)
    _T200 = *(_T199 - 4)
    _T201 = (_T152 < _T200)
    if (_T201 == 0) branch _L70
    _T202 = 0
    _T203 = (_T152 < _T202)
    if (_T203 == 0) branch _L71
_L70:
    _T204 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T204
    call _PrintString
    call _Halt
_L71:
    _T205 = 4
    _T206 = (_T152 * _T205)
    _T207 = (_T199 + _T206)
    _T208 = *(_T207 + 0)
    _T209 = 4
    _T210 = (_T152 * _T209)
    _T211 = (_T199 + _T210)
    *(_T211 + 0) = _T153
    branch _L62
_L63:
}

FUNCTION(_Deck.GetCard) {
memo '_T8:4'
_Deck.GetCard:
    _T213 = *(_T8 + 4)
    _T214 = 52
    _T215 = (_T213 >= _T214)
    if (_T215 == 0) branch _L72
    _T216 = 0
    return _T216
_L72:
    _T217 = *(_T8 + 8)
    _T218 = *(_T8 + 4)
    _T219 = *(_T217 - 4)
    _T220 = (_T218 < _T219)
    if (_T220 == 0) branch _L73
    _T221 = 0
    _T222 = (_T218 < _T221)
    if (_T222 == 0) branch _L74
_L73:
    _T223 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T223
    call _PrintString
    call _Halt
_L74:
    _T224 = 4
    _T225 = (_T218 * _T224)
    _T226 = (_T217 + _T225)
    _T227 = *(_T226 + 0)
    _T212 = _T227
    _T228 = *(_T8 + 4)
    _T229 = *(_T8 + 4)
    _T230 = 1
    _T231 = (_T229 + _T230)
    *(_T8 + 4) = _T231
    return _T212
}

FUNCTION(_BJDeck.Init) {
memo '_T9:4 _T10:8'
_BJDeck.Init:
    _T233 = *(_T9 + 4)
    _T234 = 8
    _T235 = 0
    _T236 = (_T234 < _T235)
    if (_T236 == 0) branch _L75
    _T237 = "Decaf runtime error: Cannot create negative-sized array\n"
    parm _T237
    call _PrintString
    call _Halt
_L75:
    _T238 = 4
    _T239 = (_T238 * _T234)
    _T240 = (_T238 + _T239)
    parm _T240
    _T241 =  call _Alloc
    *(_T241 + 0) = _T234
    _T242 = 0
    _T241 = (_T241 + _T240)
_L76:
    _T240 = (_T240 - _T238)
    if (_T240 == 0) branch _L77
    _T241 = (_T241 - _T238)
    *(_T241 + 0) = _T242
    branch _L76
_L77:
    *(_T9 + 4) = _T241
    _T243 = 0
    _T232 = _T243
    branch _L78
_L79:
    _T244 = 1
    _T245 = (_T232 + _T244)
    _T232 = _T245
_L78:
    _T246 = 8
    _T247 = (_T232 < _T246)
    if (_T247 == 0) branch _L80
    _T248 = *(_T9 + 4)
    _T249 = *(_T248 - 4)
    _T250 = (_T232 < _T249)
    if (_T250 == 0) branch _L81
    _T251 = 0
    _T252 = (_T232 < _T251)
    if (_T252 == 0) branch _L82
_L81:
    _T253 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T253
    call _PrintString
    call _Halt
_L82:
    _T254 = 4
    _T255 = (_T232 * _T254)
    _T256 = (_T248 + _T255)
    _T257 = *(_T256 + 0)
    _T258 =  call _Deck_New
    _T259 = 4
    _T260 = (_T232 * _T259)
    _T261 = (_T248 + _T260)
    *(_T261 + 0) = _T258
    _T262 = *(_T9 + 4)
    _T263 = *(_T262 - 4)
    _T264 = (_T232 < _T263)
    if (_T264 == 0) branch _L83
    _T265 = 0
    _T266 = (_T232 < _T265)
    if (_T266 == 0) branch _L84
_L83:
    _T267 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T267
    call _PrintString
    call _Halt
_L84:
    _T268 = 4
    _T269 = (_T232 * _T268)
    _T270 = (_T262 + _T269)
    _T271 = *(_T270 + 0)
    parm _T271
    parm _T10
    _T272 = *(_T271 + 0)
    _T273 = *(_T271 + 0)
    _T274 = *(_T273 + 8)
    call _T274
    *(_T271 + 0) = _T272
    branch _L79
_L80:
    _T275 = *(_T9 + 12)
    *(_T9 + 12) = _T10
}

FUNCTION(_BJDeck.DealCard) {
memo '_T11:4'
_BJDeck.DealCard:
    _T277 = 0
    _T276 = _T277
    _T278 = *(_T11 + 8)
    _T279 = 8
    _T280 = 52
    _T281 = (_T279 * _T280)
    _T282 = (_T278 >= _T281)
    if (_T282 == 0) branch _L85
    _T283 = 11
    return _T283
_L85:
_L86:
    _T284 = 0
    _T285 = (_T276 == _T284)
    if (_T285 == 0) branch _L87
    _T287 = *(_T11 + 12)
    _T288 = 8
    parm _T287
    parm _T288
    _T289 = *(_T287 + 0)
    _T290 = *(_T287 + 0)
    _T291 = *(_T290 + 16)
    _T292 =  call _T291
    *(_T287 + 0) = _T289
    _T286 = _T292
    _T293 = *(_T11 + 4)
    _T294 = *(_T293 - 4)
    _T295 = (_T286 < _T294)
    if (_T295 == 0) branch _L88
    _T296 = 0
    _T297 = (_T286 < _T296)
    if (_T297 == 0) branch _L89
_L88:
    _T298 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T298
    call _PrintString
    call _Halt
_L89:
    _T299 = 4
    _T300 = (_T286 * _T299)
    _T301 = (_T293 + _T300)
    _T302 = *(_T301 + 0)
    parm _T302
    _T303 = *(_T302 + 0)
    _T304 = *(_T302 + 0)
    _T305 = *(_T304 + 16)
    _T306 =  call _T305
    *(_T302 + 0) = _T303
    _T276 = _T306
    branch _L86
_L87:
    _T307 = 10
    _T308 = (_T276 > _T307)
    if (_T308 == 0) branch _L90
    _T309 = 10
    _T276 = _T309
    branch _L91
_L90:
    _T310 = 1
    _T311 = (_T276 == _T310)
    if (_T311 == 0) branch _L92
    _T312 = 11
    _T276 = _T312
_L92:
_L91:
    _T313 = *(_T11 + 8)
    _T314 = *(_T11 + 8)
    _T315 = 1
    _T316 = (_T314 + _T315)
    *(_T11 + 8) = _T316
    return _T276
}

FUNCTION(_BJDeck.Shuffle) {
memo '_T12:4'
_BJDeck.Shuffle:
    _T318 = "Shuffling..."
    parm _T318
    call _PrintString
    _T319 = 0
    _T317 = _T319
    branch _L93
_L94:
    _T320 = 1
    _T321 = (_T317 + _T320)
    _T317 = _T321
_L93:
    _T322 = 8
    _T323 = (_T317 < _T322)
    if (_T323 == 0) branch _L95
    _T324 = *(_T12 + 4)
    _T325 = *(_T324 - 4)
    _T326 = (_T317 < _T325)
    if (_T326 == 0) branch _L96
    _T327 = 0
    _T328 = (_T317 < _T327)
    if (_T328 == 0) branch _L97
_L96:
    _T329 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T329
    call _PrintString
    call _Halt
_L97:
    _T330 = 4
    _T331 = (_T317 * _T330)
    _T332 = (_T324 + _T331)
    _T333 = *(_T332 + 0)
    parm _T333
    _T334 = *(_T333 + 0)
    _T335 = *(_T333 + 0)
    _T336 = *(_T335 + 12)
    call _T336
    *(_T333 + 0) = _T334
    branch _L94
_L95:
    _T337 = *(_T12 + 8)
    _T338 = 0
    *(_T12 + 8) = _T338
    _T339 = "done.\n"
    parm _T339
    call _PrintString
}

FUNCTION(_BJDeck.NumCardsRemaining) {
memo '_T13:4'
_BJDeck.NumCardsRemaining:
    _T340 = 8
    _T341 = 52
    _T342 = (_T340 * _T341)
    _T343 = *(_T13 + 8)
    _T344 = (_T342 - _T343)
    return _T344
}

FUNCTION(_Player.Init) {
memo '_T14:4 _T15:8'
_Player.Init:
    _T345 = *(_T14 + 20)
    _T346 = 1000
    *(_T14 + 20) = _T346
    _T347 = "What is the name of player #"
    parm _T347
    call _PrintString
    parm _T15
    call _PrintInt
    _T348 = "? "
    parm _T348
    call _PrintString
    _T349 = *(_T14 + 24)
    _T350 =  call _ReadLine
    *(_T14 + 24) = _T350
}

FUNCTION(_Player.Hit) {
memo '_T16:4 _T17:8'
_Player.Hit:
    parm _T17
    _T352 = *(_T17 + 0)
    _T353 = *(_T17 + 0)
    _T354 = *(_T353 + 12)
    _T355 =  call _T354
    *(_T17 + 0) = _T352
    _T351 = _T355
    _T356 = *(_T16 + 24)
    parm _T356
    call _PrintString
    _T357 = " was dealt a "
    parm _T357
    call _PrintString
    parm _T351
    call _PrintInt
    _T358 = ".\n"
    parm _T358
    call _PrintString
    _T359 = *(_T16 + 4)
    _T360 = *(_T16 + 4)
    _T361 = (_T360 + _T351)
    *(_T16 + 4) = _T361
    _T362 = *(_T16 + 12)
    _T363 = *(_T16 + 12)
    _T364 = 1
    _T365 = (_T363 + _T364)
    *(_T16 + 12) = _T365
    _T366 = 11
    _T367 = (_T351 == _T366)
    if (_T367 == 0) branch _L98
    _T368 = *(_T16 + 8)
    _T369 = *(_T16 + 8)
    _T370 = 1
    _T371 = (_T369 + _T370)
    *(_T16 + 8) = _T371
_L98:
_L99:
    _T372 = *(_T16 + 4)
    _T373 = 21
    _T374 = (_T372 > _T373)
    _T375 = *(_T16 + 8)
    _T376 = 0
    _T377 = (_T375 > _T376)
    _T378 = (_T374 && _T377)
    if (_T378 == 0) branch _L100
    _T379 = *(_T16 + 4)
    _T380 = *(_T16 + 4)
    _T381 = 10
    _T382 = (_T380 - _T381)
    *(_T16 + 4) = _T382
    _T383 = *(_T16 + 8)
    _T384 = *(_T16 + 8)
    _T385 = 1
    _T386 = (_T384 - _T385)
    *(_T16 + 8) = _T386
    branch _L99
_L100:
}

FUNCTION(_Player.DoubleDown) {
memo '_T18:4 _T19:8'
_Player.DoubleDown:
    _T388 = *(_T18 + 4)
    _T389 = 10
    _T390 = (_T388 != _T389)
    _T391 = *(_T18 + 4)
    _T392 = 11
    _T393 = (_T391 != _T392)
    _T394 = (_T390 && _T393)
    if (_T394 == 0) branch _L101
    _T395 = 0
    return _T395
_L101:
    _T396 = "Would you like to double down?"
    parm _T18
    parm _T396
    _T397 = *(_T18 + 0)
    _T398 = *(_T18 + 0)
    _T399 = *(_T398 + 44)
    _T400 =  call _T399
    *(_T18 + 0) = _T397
    if (_T400 == 0) branch _L102
    _T401 = *(_T18 + 16)
    _T402 = *(_T18 + 16)
    _T403 = 2
    _T404 = (_T402 * _T403)
    *(_T18 + 16) = _T404
    parm _T18
    parm _T19
    _T405 = *(_T18 + 0)
    _T406 = *(_T18 + 0)
    _T407 = *(_T406 + 12)
    call _T407
    *(_T18 + 0) = _T405
    _T408 = *(_T18 + 24)
    parm _T408
    call _PrintString
    _T409 = ", your total is "
    parm _T409
    call _PrintString
    _T410 = *(_T18 + 4)
    parm _T410
    call _PrintInt
    _T411 = ".\n"
    parm _T411
    call _PrintString
    _T412 = 1
    return _T412
    branch _L103
_L102:
    _T413 = 0
    return _T413
_L103:
}

FUNCTION(_Player.TakeTurn) {
memo '_T20:4 _T21:8'
_Player.TakeTurn:
    _T415 = "\n"
    parm _T415
    call _PrintString
    _T416 = *(_T20 + 24)
    parm _T416
    call _PrintString
    _T417 = "'s turn.\n"
    parm _T417
    call _PrintString
    _T418 = *(_T20 + 4)
    _T419 = 0
    *(_T20 + 4) = _T419
    _T420 = *(_T20 + 8)
    _T421 = 0
    *(_T20 + 8) = _T421
    _T422 = *(_T20 + 12)
    _T423 = 0
    *(_T20 + 12) = _T423
    parm _T20
    parm _T21
    _T424 = *(_T20 + 0)
    _T425 = *(_T20 + 0)
    _T426 = *(_T425 + 12)
    call _T426
    *(_T20 + 0) = _T424
    parm _T20
    parm _T21
    _T427 = *(_T20 + 0)
    _T428 = *(_T20 + 0)
    _T429 = *(_T428 + 12)
    call _T429
    *(_T20 + 0) = _T427
    parm _T20
    parm _T21
    _T430 = *(_T20 + 0)
    _T431 = *(_T20 + 0)
    _T432 = *(_T431 + 16)
    _T433 =  call _T432
    *(_T20 + 0) = _T430
    _T434 = ! _T433
    if (_T434 == 0) branch _L104
    _T435 = 1
    _T414 = _T435
_L105:
    _T436 = *(_T20 + 4)
    _T437 = 21
    _T438 = (_T436 <= _T437)
    _T439 = (_T438 && _T414)
    if (_T439 == 0) branch _L106
    _T440 = *(_T20 + 24)
    parm _T440
    call _PrintString
    _T441 = ", your total is "
    parm _T441
    call _PrintString
    _T442 = *(_T20 + 4)
    parm _T442
    call _PrintInt
    _T443 = ".\n"
    parm _T443
    call _PrintString
    _T444 = "Would you like a hit?"
    parm _T20
    parm _T444
    _T445 = *(_T20 + 0)
    _T446 = *(_T20 + 0)
    _T447 = *(_T446 + 44)
    _T448 =  call _T447
    *(_T20 + 0) = _T445
    _T414 = _T448
    if (_T414 == 0) branch _L107
    parm _T20
    parm _T21
    _T449 = *(_T20 + 0)
    _T450 = *(_T20 + 0)
    _T451 = *(_T450 + 12)
    call _T451
    *(_T20 + 0) = _T449
_L107:
    branch _L105
_L106:
_L104:
    _T452 = *(_T20 + 4)
    _T453 = 21
    _T454 = (_T452 > _T453)
    if (_T454 == 0) branch _L108
    _T455 = *(_T20 + 24)
    parm _T455
    call _PrintString
    _T456 = " busts with the big "
    parm _T456
    call _PrintString
    _T457 = *(_T20 + 4)
    parm _T457
    call _PrintInt
    _T458 = "!\n"
    parm _T458
    call _PrintString
    branch _L109
_L108:
    _T459 = *(_T20 + 24)
    parm _T459
    call _PrintString
    _T460 = " stays at "
    parm _T460
    call _PrintString
    _T461 = *(_T20 + 4)
    parm _T461
    call _PrintInt
    _T462 = ".\n"
    parm _T462
    call _PrintString
_L109:
}

FUNCTION(_Player.HasMoney) {
memo '_T22:4'
_Player.HasMoney:
    _T463 = *(_T22 + 20)
    _T464 = 0
    _T465 = (_T463 > _T464)
    return _T465
}

FUNCTION(_Player.PrintMoney) {
memo '_T23:4'
_Player.PrintMoney:
    _T466 = *(_T23 + 24)
    parm _T466
    call _PrintString
    _T467 = ", you have $"
    parm _T467
    call _PrintString
    _T468 = *(_T23 + 20)
    parm _T468
    call _PrintInt
    _T469 = ".\n"
    parm _T469
    call _PrintString
}

FUNCTION(_Player.PlaceBet) {
memo '_T24:4'
_Player.PlaceBet:
    _T470 = *(_T24 + 16)
    _T471 = 0
    *(_T24 + 16) = _T471
    parm _T24
    _T472 = *(_T24 + 0)
    _T473 = *(_T24 + 0)
    _T474 = *(_T473 + 28)
    call _T474
    *(_T24 + 0) = _T472
_L110:
    _T475 = *(_T24 + 16)
    _T476 = 0
    _T477 = (_T475 <= _T476)
    _T478 = *(_T24 + 16)
    _T479 = *(_T24 + 20)
    _T480 = (_T478 > _T479)
    _T481 = (_T477 || _T480)
    if (_T481 == 0) branch _L111
    _T482 = "How much would you like to bet? "
    parm _T482
    call _PrintString
    _T483 = *(_T24 + 16)
    _T484 =  call _ReadInteger
    *(_T24 + 16) = _T484
    branch _L110
_L111:
}

FUNCTION(_Player.GetTotal) {
memo '_T25:4'
_Player.GetTotal:
    _T485 = *(_T25 + 4)
    return _T485
}

FUNCTION(_Player.Resolve) {
memo '_T26:4 _T27:8'
_Player.Resolve:
    _T488 = 0
    _T486 = _T488
    _T489 = 0
    _T487 = _T489
    _T490 = *(_T26 + 4)
    _T491 = 21
    _T492 = (_T490 == _T491)
    _T493 = *(_T26 + 12)
    _T494 = 2
    _T495 = (_T493 == _T494)
    _T496 = (_T492 && _T495)
    if (_T496 == 0) branch _L112
    _T497 = 2
    _T486 = _T497
    branch _L113
_L112:
    _T498 = *(_T26 + 4)
    _T499 = 21
    _T500 = (_T498 > _T499)
    if (_T500 == 0) branch _L114
    _T501 = 1
    _T487 = _T501
    branch _L115
_L114:
    _T502 = 21
    _T503 = (_T27 > _T502)
    if (_T503 == 0) branch _L116
    _T504 = 1
    _T486 = _T504
    branch _L117
_L116:
    _T505 = *(_T26 + 4)
    _T506 = (_T505 > _T27)
    if (_T506 == 0) branch _L118
    _T507 = 1
    _T486 = _T507
    branch _L119
_L118:
    _T508 = *(_T26 + 4)
    _T509 = (_T27 > _T508)
    if (_T509 == 0) branch _L120
    _T510 = 1
    _T487 = _T510
_L120:
_L119:
_L117:
_L115:
_L113:
    _T511 = 1
    _T512 = (_T486 >= _T511)
    if (_T512 == 0) branch _L121
    _T513 = *(_T26 + 24)
    parm _T513
    call _PrintString
    _T514 = ", you won $"
    parm _T514
    call _PrintString
    _T515 = *(_T26 + 16)
    parm _T515
    call _PrintInt
    _T516 = ".\n"
    parm _T516
    call _PrintString
    branch _L122
_L121:
    _T517 = 1
    _T518 = (_T487 >= _T517)
    if (_T518 == 0) branch _L123
    _T519 = *(_T26 + 24)
    parm _T519
    call _PrintString
    _T520 = ", you lost $"
    parm _T520
    call _PrintString
    _T521 = *(_T26 + 16)
    parm _T521
    call _PrintInt
    _T522 = ".\n"
    parm _T522
    call _PrintString
    branch _L124
_L123:
    _T523 = *(_T26 + 24)
    parm _T523
    call _PrintString
    _T524 = ", you push!\n"
    parm _T524
    call _PrintString
_L124:
_L122:
    _T525 = *(_T26 + 16)
    _T526 = (_T486 * _T525)
    _T486 = _T526
    _T527 = *(_T26 + 16)
    _T528 = (_T487 * _T527)
    _T487 = _T528
    _T529 = *(_T26 + 20)
    _T530 = *(_T26 + 20)
    _T531 = (_T530 + _T486)
    _T532 = (_T531 - _T487)
    *(_T26 + 20) = _T532
}

FUNCTION(_Player.GetYesOrNo) {
memo '_T28:4 _T29:8'
_Player.GetYesOrNo:
    parm _T29
    call _PrintString
    _T533 = " (0=No/1=Yes) "
    parm _T533
    call _PrintString
    _T534 =  call _ReadInteger
    _T535 = 0
    _T536 = (_T534 != _T535)
    return _T536
}

FUNCTION(_Dealer.Init) {
memo '_T30:4 _T31:8'
_Dealer.Init:
    _T538 = *(_T30 + 4)
    _T539 = 0
    *(_T30 + 4) = _T539
    _T540 = *(_T30 + 8)
    _T541 = 0
    *(_T30 + 8) = _T541
    _T542 = *(_T30 + 12)
    _T543 = 0
    *(_T30 + 12) = _T543
    _T544 = "Dealer"
    _T537 = _T544
    _T545 = *(_T30 + 24)
    *(_T30 + 24) = _T537
}

FUNCTION(_Dealer.TakeTurn) {
memo '_T32:4 _T33:8'
_Dealer.TakeTurn:
    _T546 = "\n"
    parm _T546
    call _PrintString
    _T547 = *(_T32 + 24)
    parm _T547
    call _PrintString
    _T548 = "'s turn.\n"
    parm _T548
    call _PrintString
_L125:
    _T549 = *(_T32 + 4)
    _T550 = 16
    _T551 = (_T549 <= _T550)
    if (_T551 == 0) branch _L126
    parm _T32
    parm _T33
    _T552 = *(_T32 + 0)
    _T553 = *(_T32 + 0)
    _T554 = *(_T553 + 0)
    *(_T32 + 0) = _T554
    _T555 = *(_T32 + 0)
    _T556 = *(_T555 + 12)
    call _T556
    *(_T32 + 0) = _T552
    branch _L125
_L126:
    _T557 = *(_T32 + 4)
    _T558 = 21
    _T559 = (_T557 > _T558)
    if (_T559 == 0) branch _L127
    _T560 = *(_T32 + 24)
    parm _T560
    call _PrintString
    _T561 = " busts with the big "
    parm _T561
    call _PrintString
    _T562 = *(_T32 + 4)
    parm _T562
    call _PrintInt
    _T563 = "!\n"
    parm _T563
    call _PrintString
    branch _L128
_L127:
    _T564 = *(_T32 + 24)
    parm _T564
    call _PrintString
    _T565 = " stays at "
    parm _T565
    call _PrintString
    _T566 = *(_T32 + 4)
    parm _T566
    call _PrintInt
    _T567 = ".\n"
    parm _T567
    call _PrintString
_L128:
}

FUNCTION(_House.SetupGame) {
memo '_T34:4'
_House.SetupGame:
    _T568 = "\nWelcome to CS143 BlackJack!\n"
    parm _T568
    call _PrintString
    _T569 = "---------------------------\n"
    parm _T569
    call _PrintString
    _T571 =  call _rndModule_New
    _T570 = _T571
    _T572 = "Please enter a random number seed: "
    parm _T572
    call _PrintString
    _T573 =  call _ReadInteger
    parm _T570
    parm _T573
    _T574 = *(_T570 + 0)
    _T575 = *(_T570 + 0)
    _T576 = *(_T575 + 8)
    call _T576
    *(_T570 + 0) = _T574
    _T577 = *(_T34 + 12)
    _T578 =  call _BJDeck_New
    *(_T34 + 12) = _T578
    _T579 = *(_T34 + 8)
    _T580 =  call _Dealer_New
    *(_T34 + 8) = _T580
    _T581 = *(_T34 + 12)
    parm _T581
    parm _T570
    _T582 = *(_T581 + 0)
    _T583 = *(_T581 + 0)
    _T584 = *(_T583 + 8)
    call _T584
    *(_T581 + 0) = _T582
    _T585 = *(_T34 + 12)
    parm _T585
    _T586 = *(_T585 + 0)
    _T587 = *(_T585 + 0)
    _T588 = *(_T587 + 16)
    call _T588
    *(_T585 + 0) = _T586
}

FUNCTION(_House.SetupPlayers) {
memo '_T35:4'
_House.SetupPlayers:
    _T591 = "How many players do we have today? "
    parm _T591
    call _PrintString
    _T592 =  call _ReadInteger
    _T590 = _T592
    _T593 = *(_T35 + 4)
    _T594 = 0
    _T595 = (_T590 < _T594)
    if (_T595 == 0) branch _L129
    _T596 = "Decaf runtime error: Cannot create negative-sized array\n"
    parm _T596
    call _PrintString
    call _Halt
_L129:
    _T597 = 4
    _T598 = (_T597 * _T590)
    _T599 = (_T597 + _T598)
    parm _T599
    _T600 =  call _Alloc
    *(_T600 + 0) = _T590
    _T601 = 0
    _T600 = (_T600 + _T599)
_L130:
    _T599 = (_T599 - _T597)
    if (_T599 == 0) branch _L131
    _T600 = (_T600 - _T597)
    *(_T600 + 0) = _T601
    branch _L130
_L131:
    *(_T35 + 4) = _T600
    _T602 = 0
    _T589 = _T602
    branch _L132
_L133:
    _T603 = 1
    _T604 = (_T589 + _T603)
    _T589 = _T604
_L132:
    _T605 = *(_T35 + 4)
    _T606 = *(_T605 - 4)
    _T607 = (_T589 < _T606)
    if (_T607 == 0) branch _L134
    _T608 = *(_T35 + 4)
    _T609 = *(_T608 - 4)
    _T610 = (_T589 < _T609)
    if (_T610 == 0) branch _L135
    _T611 = 0
    _T612 = (_T589 < _T611)
    if (_T612 == 0) branch _L136
_L135:
    _T613 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T613
    call _PrintString
    call _Halt
_L136:
    _T614 = 4
    _T615 = (_T589 * _T614)
    _T616 = (_T608 + _T615)
    _T617 = *(_T616 + 0)
    _T618 =  call _Player_New
    _T619 = 4
    _T620 = (_T589 * _T619)
    _T621 = (_T608 + _T620)
    *(_T621 + 0) = _T618
    _T622 = *(_T35 + 4)
    _T623 = *(_T622 - 4)
    _T624 = (_T589 < _T623)
    if (_T624 == 0) branch _L137
    _T625 = 0
    _T626 = (_T589 < _T625)
    if (_T626 == 0) branch _L138
_L137:
    _T627 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T627
    call _PrintString
    call _Halt
_L138:
    _T628 = 4
    _T629 = (_T589 * _T628)
    _T630 = (_T622 + _T629)
    _T631 = *(_T630 + 0)
    _T632 = 1
    _T633 = (_T589 + _T632)
    parm _T631
    parm _T633
    _T634 = *(_T631 + 0)
    _T635 = *(_T631 + 0)
    _T636 = *(_T635 + 8)
    call _T636
    *(_T631 + 0) = _T634
    branch _L133
_L134:
}

FUNCTION(_House.TakeAllBets) {
memo '_T36:4'
_House.TakeAllBets:
    _T638 = "\nFirst, let's take bets.\n"
    parm _T638
    call _PrintString
    _T639 = 0
    _T637 = _T639
    branch _L139
_L140:
    _T640 = 1
    _T641 = (_T637 + _T640)
    _T637 = _T641
_L139:
    _T642 = *(_T36 + 4)
    _T643 = *(_T642 - 4)
    _T644 = (_T637 < _T643)
    if (_T644 == 0) branch _L141
    _T645 = *(_T36 + 4)
    _T646 = *(_T645 - 4)
    _T647 = (_T637 < _T646)
    if (_T647 == 0) branch _L142
    _T648 = 0
    _T649 = (_T637 < _T648)
    if (_T649 == 0) branch _L143
_L142:
    _T650 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T650
    call _PrintString
    call _Halt
_L143:
    _T651 = 4
    _T652 = (_T637 * _T651)
    _T653 = (_T645 + _T652)
    _T654 = *(_T653 + 0)
    parm _T654
    _T655 = *(_T654 + 0)
    _T656 = *(_T654 + 0)
    _T657 = *(_T656 + 24)
    _T658 =  call _T657
    *(_T654 + 0) = _T655
    if (_T658 == 0) branch _L144
    _T659 = *(_T36 + 4)
    _T660 = *(_T659 - 4)
    _T661 = (_T637 < _T660)
    if (_T661 == 0) branch _L145
    _T662 = 0
    _T663 = (_T637 < _T662)
    if (_T663 == 0) branch _L146
_L145:
    _T664 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T664
    call _PrintString
    call _Halt
_L146:
    _T665 = 4
    _T666 = (_T637 * _T665)
    _T667 = (_T659 + _T666)
    _T668 = *(_T667 + 0)
    parm _T668
    _T669 = *(_T668 + 0)
    _T670 = *(_T668 + 0)
    _T671 = *(_T670 + 32)
    call _T671
    *(_T668 + 0) = _T669
_L144:
    branch _L140
_L141:
}

FUNCTION(_House.TakeAllTurns) {
memo '_T37:4'
_House.TakeAllTurns:
    _T673 = 0
    _T672 = _T673
    branch _L147
_L148:
    _T674 = 1
    _T675 = (_T672 + _T674)
    _T672 = _T675
_L147:
    _T676 = *(_T37 + 4)
    _T677 = *(_T676 - 4)
    _T678 = (_T672 < _T677)
    if (_T678 == 0) branch _L149
    _T679 = *(_T37 + 4)
    _T680 = *(_T679 - 4)
    _T681 = (_T672 < _T680)
    if (_T681 == 0) branch _L150
    _T682 = 0
    _T683 = (_T672 < _T682)
    if (_T683 == 0) branch _L151
_L150:
    _T684 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T684
    call _PrintString
    call _Halt
_L151:
    _T685 = 4
    _T686 = (_T672 * _T685)
    _T687 = (_T679 + _T686)
    _T688 = *(_T687 + 0)
    parm _T688
    _T689 = *(_T688 + 0)
    _T690 = *(_T688 + 0)
    _T691 = *(_T690 + 24)
    _T692 =  call _T691
    *(_T688 + 0) = _T689
    if (_T692 == 0) branch _L152
    _T693 = *(_T37 + 4)
    _T694 = *(_T693 - 4)
    _T695 = (_T672 < _T694)
    if (_T695 == 0) branch _L153
    _T696 = 0
    _T697 = (_T672 < _T696)
    if (_T697 == 0) branch _L154
_L153:
    _T698 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T698
    call _PrintString
    call _Halt
_L154:
    _T699 = 4
    _T700 = (_T672 * _T699)
    _T701 = (_T693 + _T700)
    _T702 = *(_T701 + 0)
    _T703 = *(_T37 + 12)
    parm _T702
    parm _T703
    _T704 = *(_T702 + 0)
    _T705 = *(_T702 + 0)
    _T706 = *(_T705 + 20)
    call _T706
    *(_T702 + 0) = _T704
_L152:
    branch _L148
_L149:
}

FUNCTION(_House.ResolveAllPlayers) {
memo '_T38:4'
_House.ResolveAllPlayers:
    _T708 = "\nTime to resolve bets.\n"
    parm _T708
    call _PrintString
    _T709 = 0
    _T707 = _T709
    branch _L155
_L156:
    _T710 = 1
    _T711 = (_T707 + _T710)
    _T707 = _T711
_L155:
    _T712 = *(_T38 + 4)
    _T713 = *(_T712 - 4)
    _T714 = (_T707 < _T713)
    if (_T714 == 0) branch _L157
    _T715 = *(_T38 + 4)
    _T716 = *(_T715 - 4)
    _T717 = (_T707 < _T716)
    if (_T717 == 0) branch _L158
    _T718 = 0
    _T719 = (_T707 < _T718)
    if (_T719 == 0) branch _L159
_L158:
    _T720 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T720
    call _PrintString
    call _Halt
_L159:
    _T721 = 4
    _T722 = (_T707 * _T721)
    _T723 = (_T715 + _T722)
    _T724 = *(_T723 + 0)
    parm _T724
    _T725 = *(_T724 + 0)
    _T726 = *(_T724 + 0)
    _T727 = *(_T726 + 24)
    _T728 =  call _T727
    *(_T724 + 0) = _T725
    if (_T728 == 0) branch _L160
    _T729 = *(_T38 + 4)
    _T730 = *(_T729 - 4)
    _T731 = (_T707 < _T730)
    if (_T731 == 0) branch _L161
    _T732 = 0
    _T733 = (_T707 < _T732)
    if (_T733 == 0) branch _L162
_L161:
    _T734 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T734
    call _PrintString
    call _Halt
_L162:
    _T735 = 4
    _T736 = (_T707 * _T735)
    _T737 = (_T729 + _T736)
    _T738 = *(_T737 + 0)
    _T739 = *(_T38 + 8)
    parm _T739
    _T740 = *(_T739 + 0)
    _T741 = *(_T739 + 0)
    _T742 = *(_T741 + 0)
    *(_T739 + 0) = _T742
    _T743 = *(_T739 + 0)
    _T744 = *(_T743 + 36)
    _T745 =  call _T744
    *(_T739 + 0) = _T740
    parm _T738
    parm _T745
    _T746 = *(_T738 + 0)
    _T747 = *(_T738 + 0)
    _T748 = *(_T747 + 40)
    call _T748
    *(_T738 + 0) = _T746
_L160:
    branch _L156
_L157:
}

FUNCTION(_House.PrintAllMoney) {
memo '_T39:4'
_House.PrintAllMoney:
    _T750 = 0
    _T749 = _T750
    branch _L163
_L164:
    _T751 = 1
    _T752 = (_T749 + _T751)
    _T749 = _T752
_L163:
    _T753 = *(_T39 + 4)
    _T754 = *(_T753 - 4)
    _T755 = (_T749 < _T754)
    if (_T755 == 0) branch _L165
    _T756 = *(_T39 + 4)
    _T757 = *(_T756 - 4)
    _T758 = (_T749 < _T757)
    if (_T758 == 0) branch _L166
    _T759 = 0
    _T760 = (_T749 < _T759)
    if (_T760 == 0) branch _L167
_L166:
    _T761 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T761
    call _PrintString
    call _Halt
_L167:
    _T762 = 4
    _T763 = (_T749 * _T762)
    _T764 = (_T756 + _T763)
    _T765 = *(_T764 + 0)
    parm _T765
    _T766 = *(_T765 + 0)
    _T767 = *(_T765 + 0)
    _T768 = *(_T767 + 28)
    call _T768
    *(_T765 + 0) = _T766
    branch _L164
_L165:
}

FUNCTION(_House.PlayOneGame) {
memo '_T40:4'
_House.PlayOneGame:
    _T769 = *(_T40 + 12)
    parm _T769
    _T770 = *(_T769 + 0)
    _T771 = *(_T769 + 0)
    _T772 = *(_T771 + 20)
    _T773 =  call _T772
    *(_T769 + 0) = _T770
    _T774 = 26
    _T775 = (_T773 < _T774)
    if (_T775 == 0) branch _L168
    _T776 = *(_T40 + 12)
    parm _T776
    _T777 = *(_T776 + 0)
    _T778 = *(_T776 + 0)
    _T779 = *(_T778 + 16)
    call _T779
    *(_T776 + 0) = _T777
_L168:
    parm _T40
    _T780 = *(_T40 + 0)
    _T781 = *(_T40 + 0)
    _T782 = *(_T781 + 16)
    call _T782
    *(_T40 + 0) = _T780
    _T783 = "\nDealer starts. "
    parm _T783
    call _PrintString
    _T784 = *(_T40 + 8)
    _T785 = 0
    parm _T784
    parm _T785
    _T786 = *(_T784 + 0)
    _T787 = *(_T784 + 0)
    _T788 = *(_T787 + 8)
    call _T788
    *(_T784 + 0) = _T786
    _T789 = *(_T40 + 8)
    _T790 = *(_T40 + 12)
    parm _T789
    parm _T790
    _T791 = *(_T789 + 0)
    _T792 = *(_T789 + 0)
    _T793 = *(_T792 + 0)
    *(_T789 + 0) = _T793
    _T794 = *(_T789 + 0)
    _T795 = *(_T794 + 12)
    call _T795
    *(_T789 + 0) = _T791
    parm _T40
    _T796 = *(_T40 + 0)
    _T797 = *(_T40 + 0)
    _T798 = *(_T797 + 20)
    call _T798
    *(_T40 + 0) = _T796
    _T799 = *(_T40 + 8)
    _T800 = *(_T40 + 12)
    parm _T799
    parm _T800
    _T801 = *(_T799 + 0)
    _T802 = *(_T799 + 0)
    _T803 = *(_T802 + 20)
    call _T803
    *(_T799 + 0) = _T801
    parm _T40
    _T804 = *(_T40 + 0)
    _T805 = *(_T40 + 0)
    _T806 = *(_T805 + 24)
    call _T806
    *(_T40 + 0) = _T804
}

FUNCTION(main) {
memo ''
main:
    _T808 = 1
    _T807 = _T808
    _T810 =  call _House_New
    _T809 = _T810
    parm _T809
    _T811 = *(_T809 + 0)
    _T812 = *(_T809 + 0)
    _T813 = *(_T812 + 8)
    call _T813
    *(_T809 + 0) = _T811
    parm _T809
    _T814 = *(_T809 + 0)
    _T815 = *(_T809 + 0)
    _T816 = *(_T815 + 12)
    call _T816
    *(_T809 + 0) = _T814
_L169:
    if (_T807 == 0) branch _L170
    parm _T809
    _T817 = *(_T809 + 0)
    _T818 = *(_T809 + 0)
    _T819 = *(_T818 + 32)
    call _T819
    *(_T809 + 0) = _T817
    _T820 = "\nDo you want to play another hand?"
    parm _T820
    _T821 =  call _Main.GetYesOrNo
    _T807 = _T821
    branch _L169
_L170:
    parm _T809
    _T822 = *(_T809 + 0)
    _T823 = *(_T809 + 0)
    _T824 = *(_T823 + 28)
    call _T824
    *(_T809 + 0) = _T822
    _T825 = "Thank you for playing...come again soon.\n"
    parm _T825
    call _PrintString
    _T826 = "\nCS143 BlackJack Copyright (c) 1999 by Peter Mork.\n"
    parm _T826
    call _PrintString
    _T827 = "(2001 mods by jdz)\n"
    parm _T827
    call _PrintString
}

FUNCTION(_Main.GetYesOrNo) {
memo '_T41:4'
_Main.GetYesOrNo:
    parm _T41
    call _PrintString
    _T828 = " (0=No/1=Yes) "
    parm _T828
    call _PrintString
    _T829 =  call _ReadInteger
    _T830 = 0
    _T831 = (_T829 != _T830)
    return _T831
}

