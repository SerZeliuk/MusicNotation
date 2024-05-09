lexer grammar MusicNotationLexer;

NOTE        : [a-gA-G];
OCTAVE      : [0-8];
DURATION    : 'w' | 'h' | 'q' | 'e' | 's' | 't';
REST        : 'R';
SHARP       : '#';
FLAT        : 'b';
PIPE        : '|';
NUMBER      : [0-9]+;
TEMPO       : NUMBER 'bpm';
KEY         : [A-G] ('#' | 'b')? ('m')? ;
STACCATO    : '.';
CRESCENDO   : '<';
DIMINUENDO  : '>';
WS          : [ \t\r\n]+ -> skip;
