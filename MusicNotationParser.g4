lexer MusicNotation;
import MusicNotationLexer;

music       : part+ ;
part        : key tempo? (measure)+ ;
key         : KEY ;   
tempo       : TEMPO ;
measure     : PIPE noteSequence PIPE ;
noteSequence: musicalElement+ ;
musicalElement: note | rest | expression ;
note_or_chord : (NOTE(SHARP? | FLAT?))+  OCTAVE DURATION articulation?;
rest        : REST DURATION;
articulation: STACCATO;
expression  : dynamicChange ;
dynamic     : CRESCENDO noteSequence+ CRESCENDO | DIMINUENDO noteSequence+ DIMINUENDO;
