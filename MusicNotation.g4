grammar MusicNotation;

// Non-terminal rules
music           : part+ ;
part            : key? tempo? measure+ ;
key             : KEY ;
tempo           : TEMPO ;
measure         : PIPE noteSequence PIPE ;
noteSequence    : musicalElement+ ;
musicalElement  : note_or_chord | rest | expression ;
note_or_chord   : (NOTE (SHARP? | FLAT?) OCTAVE)+ DURATION articulation? ;
rest            : REST DURATION ;
articulation    : STACCATO ;
expression      : dynamic;
dynamic         : CRESCENDO noteSequence+ CRESCENDO | DIMINUENDO noteSequence+ DIMINUENDO ;

// Terminal rules
NOTE            : [a-gA-G] ;
OCTAVE          : [0-8] ;
DURATION        : [whqest] ;
REST            : 'R' ;
SHARP           : '#' ;
FLAT            : 'b' ;
PIPE            : '|' ;
NUMBER          : [0-9]+ ;
TEMPO           : NUMBER 'bpm' ;
KEY             : 'KEY=' [A-G] ('#' | 'b')? 'm'? ;
STACCATO        : '.' ;
CRESCENDO       : '<' ;
DIMINUENDO      : '>' ;
WS              : [ \t\r\n]+ -> skip ;
