grammar MusicNotation;

// Non-terminal rules
music           : part+ ;
part            : title? author? year? key tempo time_signature measure+ ;
title           : 'TITLE=' STRING;
author          : 'AUTHOR=' STRING;
year            : 'YEAR=' YEAR;
key             : KEY ;
tempo           : TEMPO ;
time_signature  : TS;
measure         : time_signature? PIPE noteSequence PIPE ;
noteSequence    : musicalElement+ ;
musicalElement  : note_or_chord | rest | expression ;
note_or_chord   : (NOTE (SHARP? | FLAT?) OCTAVE)+ DURATION articulation? ;
rest            : REST DURATION ;
articulation    : STACCATO ;
expression      : dynamic;
dynamic         : CRESCENDO noteSequence+ DIMINUENDO | DIMINUENDO noteSequence+ CRESCENDO ;

// Terminal rules
NOTE            : [a-gA-G] ;
OCTAVE          : [0-8] ;
DURATION        : [whqest] ;
REST            : 'R' ;
SHARP           : '#' ;
FLAT            : 'b' ;
PIPE            : '|' ;
NUMBER          : [0-9]+ ;
STRING          : [a-zA-Z]+ ;
YEAR            : NUMBER;
TEMPO           : NUMBER 'bpm' ;
KEY             : 'KEY=' [A-G] ('#' | 'b')? 'm'? ;
TS              : NUMBER'/'NUMBER;
STACCATO        : '.' ;
CRESCENDO       : '<' ;
DIMINUENDO      : '>' ;
WS              : [ \t\r\n]+ -> skip ;
