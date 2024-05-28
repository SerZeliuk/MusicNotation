# Generated from MusicNotation.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,14,102,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,4,0,26,8,0,11,
        0,12,0,27,1,1,3,1,31,8,1,1,1,3,1,34,8,1,1,1,4,1,37,8,1,11,1,12,1,
        38,1,2,1,2,1,3,1,3,1,4,1,4,1,4,1,4,1,5,4,5,50,8,5,11,5,12,5,51,1,
        6,1,6,1,6,3,6,57,8,6,1,7,1,7,3,7,61,8,7,1,7,3,7,64,8,7,3,7,66,8,
        7,1,7,4,7,69,8,7,11,7,12,7,70,1,7,1,7,3,7,75,8,7,1,8,1,8,1,8,1,9,
        1,9,1,10,1,10,1,11,1,11,4,11,86,8,11,11,11,12,11,87,1,11,1,11,1,
        11,1,11,4,11,94,8,11,11,11,12,11,95,1,11,1,11,3,11,100,8,11,1,11,
        0,0,12,0,2,4,6,8,10,12,14,16,18,20,22,0,0,104,0,25,1,0,0,0,2,30,
        1,0,0,0,4,40,1,0,0,0,6,42,1,0,0,0,8,44,1,0,0,0,10,49,1,0,0,0,12,
        56,1,0,0,0,14,68,1,0,0,0,16,76,1,0,0,0,18,79,1,0,0,0,20,81,1,0,0,
        0,22,99,1,0,0,0,24,26,3,2,1,0,25,24,1,0,0,0,26,27,1,0,0,0,27,25,
        1,0,0,0,27,28,1,0,0,0,28,1,1,0,0,0,29,31,3,4,2,0,30,29,1,0,0,0,30,
        31,1,0,0,0,31,33,1,0,0,0,32,34,3,6,3,0,33,32,1,0,0,0,33,34,1,0,0,
        0,34,36,1,0,0,0,35,37,3,8,4,0,36,35,1,0,0,0,37,38,1,0,0,0,38,36,
        1,0,0,0,38,39,1,0,0,0,39,3,1,0,0,0,40,41,5,10,0,0,41,5,1,0,0,0,42,
        43,5,9,0,0,43,7,1,0,0,0,44,45,5,7,0,0,45,46,3,10,5,0,46,47,5,7,0,
        0,47,9,1,0,0,0,48,50,3,12,6,0,49,48,1,0,0,0,50,51,1,0,0,0,51,49,
        1,0,0,0,51,52,1,0,0,0,52,11,1,0,0,0,53,57,3,14,7,0,54,57,3,16,8,
        0,55,57,3,20,10,0,56,53,1,0,0,0,56,54,1,0,0,0,56,55,1,0,0,0,57,13,
        1,0,0,0,58,65,5,1,0,0,59,61,5,5,0,0,60,59,1,0,0,0,60,61,1,0,0,0,
        61,66,1,0,0,0,62,64,5,6,0,0,63,62,1,0,0,0,63,64,1,0,0,0,64,66,1,
        0,0,0,65,60,1,0,0,0,65,63,1,0,0,0,66,67,1,0,0,0,67,69,5,2,0,0,68,
        58,1,0,0,0,69,70,1,0,0,0,70,68,1,0,0,0,70,71,1,0,0,0,71,72,1,0,0,
        0,72,74,5,3,0,0,73,75,3,18,9,0,74,73,1,0,0,0,74,75,1,0,0,0,75,15,
        1,0,0,0,76,77,5,4,0,0,77,78,5,3,0,0,78,17,1,0,0,0,79,80,5,11,0,0,
        80,19,1,0,0,0,81,82,3,22,11,0,82,21,1,0,0,0,83,85,5,12,0,0,84,86,
        3,10,5,0,85,84,1,0,0,0,86,87,1,0,0,0,87,85,1,0,0,0,87,88,1,0,0,0,
        88,89,1,0,0,0,89,90,5,12,0,0,90,100,1,0,0,0,91,93,5,13,0,0,92,94,
        3,10,5,0,93,92,1,0,0,0,94,95,1,0,0,0,95,93,1,0,0,0,95,96,1,0,0,0,
        96,97,1,0,0,0,97,98,5,13,0,0,98,100,1,0,0,0,99,83,1,0,0,0,99,91,
        1,0,0,0,100,23,1,0,0,0,14,27,30,33,38,51,56,60,63,65,70,74,87,95,
        99
    ]

class MusicNotationParser ( Parser ):

    grammarFileName = "MusicNotation.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'R'", "'#'", "'b'", "'|'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'.'", "'<'", "'>'" ]

    symbolicNames = [ "<INVALID>", "NOTE", "OCTAVE", "DURATION", "REST", 
                      "SHARP", "FLAT", "PIPE", "NUMBER", "TEMPO", "KEY", 
                      "STACCATO", "CRESCENDO", "DIMINUENDO", "WS" ]

    RULE_music = 0
    RULE_part = 1
    RULE_key = 2
    RULE_tempo = 3
    RULE_measure = 4
    RULE_noteSequence = 5
    RULE_musicalElement = 6
    RULE_note_or_chord = 7
    RULE_rest = 8
    RULE_articulation = 9
    RULE_expression = 10
    RULE_dynamic = 11

    ruleNames =  [ "music", "part", "key", "tempo", "measure", "noteSequence", 
                   "musicalElement", "note_or_chord", "rest", "articulation", 
                   "expression", "dynamic" ]

    EOF = Token.EOF
    NOTE=1
    OCTAVE=2
    DURATION=3
    REST=4
    SHARP=5
    FLAT=6
    PIPE=7
    NUMBER=8
    TEMPO=9
    KEY=10
    STACCATO=11
    CRESCENDO=12
    DIMINUENDO=13
    WS=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class MusicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def part(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MusicNotationParser.PartContext)
            else:
                return self.getTypedRuleContext(MusicNotationParser.PartContext,i)


        def getRuleIndex(self):
            return MusicNotationParser.RULE_music

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMusic" ):
                listener.enterMusic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMusic" ):
                listener.exitMusic(self)




    def music(self):

        localctx = MusicNotationParser.MusicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_music)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 24
                self.part()
                self.state = 27 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1664) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def key(self):
            return self.getTypedRuleContext(MusicNotationParser.KeyContext,0)


        def tempo(self):
            return self.getTypedRuleContext(MusicNotationParser.TempoContext,0)


        def measure(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MusicNotationParser.MeasureContext)
            else:
                return self.getTypedRuleContext(MusicNotationParser.MeasureContext,i)


        def getRuleIndex(self):
            return MusicNotationParser.RULE_part

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPart" ):
                listener.enterPart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPart" ):
                listener.exitPart(self)




    def part(self):

        localctx = MusicNotationParser.PartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 29
                self.key()


            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 32
                self.tempo()


            self.state = 36 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 35
                    self.measure()

                else:
                    raise NoViableAltException(self)
                self.state = 38 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEY(self):
            return self.getToken(MusicNotationParser.KEY, 0)

        def getRuleIndex(self):
            return MusicNotationParser.RULE_key

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKey" ):
                listener.enterKey(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKey" ):
                listener.exitKey(self)




    def key(self):

        localctx = MusicNotationParser.KeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_key)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(MusicNotationParser.KEY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TempoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEMPO(self):
            return self.getToken(MusicNotationParser.TEMPO, 0)

        def getRuleIndex(self):
            return MusicNotationParser.RULE_tempo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTempo" ):
                listener.enterTempo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTempo" ):
                listener.exitTempo(self)




    def tempo(self):

        localctx = MusicNotationParser.TempoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_tempo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(MusicNotationParser.TEMPO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MeasureContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PIPE(self, i:int=None):
            if i is None:
                return self.getTokens(MusicNotationParser.PIPE)
            else:
                return self.getToken(MusicNotationParser.PIPE, i)

        def noteSequence(self):
            return self.getTypedRuleContext(MusicNotationParser.NoteSequenceContext,0)


        def getRuleIndex(self):
            return MusicNotationParser.RULE_measure

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMeasure" ):
                listener.enterMeasure(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMeasure" ):
                listener.exitMeasure(self)




    def measure(self):

        localctx = MusicNotationParser.MeasureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_measure)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(MusicNotationParser.PIPE)
            self.state = 45
            self.noteSequence()
            self.state = 46
            self.match(MusicNotationParser.PIPE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NoteSequenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def musicalElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MusicNotationParser.MusicalElementContext)
            else:
                return self.getTypedRuleContext(MusicNotationParser.MusicalElementContext,i)


        def getRuleIndex(self):
            return MusicNotationParser.RULE_noteSequence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNoteSequence" ):
                listener.enterNoteSequence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNoteSequence" ):
                listener.exitNoteSequence(self)




    def noteSequence(self):

        localctx = MusicNotationParser.NoteSequenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_noteSequence)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 48
                    self.musicalElement()

                else:
                    raise NoViableAltException(self)
                self.state = 51 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MusicalElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def note_or_chord(self):
            return self.getTypedRuleContext(MusicNotationParser.Note_or_chordContext,0)


        def rest(self):
            return self.getTypedRuleContext(MusicNotationParser.RestContext,0)


        def expression(self):
            return self.getTypedRuleContext(MusicNotationParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MusicNotationParser.RULE_musicalElement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMusicalElement" ):
                listener.enterMusicalElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMusicalElement" ):
                listener.exitMusicalElement(self)




    def musicalElement(self):

        localctx = MusicNotationParser.MusicalElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_musicalElement)
        try:
            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.note_or_chord()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.rest()
                pass
            elif token in [12, 13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 55
                self.expression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Note_or_chordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DURATION(self):
            return self.getToken(MusicNotationParser.DURATION, 0)

        def NOTE(self, i:int=None):
            if i is None:
                return self.getTokens(MusicNotationParser.NOTE)
            else:
                return self.getToken(MusicNotationParser.NOTE, i)

        def OCTAVE(self, i:int=None):
            if i is None:
                return self.getTokens(MusicNotationParser.OCTAVE)
            else:
                return self.getToken(MusicNotationParser.OCTAVE, i)

        def articulation(self):
            return self.getTypedRuleContext(MusicNotationParser.ArticulationContext,0)


        def SHARP(self, i:int=None):
            if i is None:
                return self.getTokens(MusicNotationParser.SHARP)
            else:
                return self.getToken(MusicNotationParser.SHARP, i)

        def FLAT(self, i:int=None):
            if i is None:
                return self.getTokens(MusicNotationParser.FLAT)
            else:
                return self.getToken(MusicNotationParser.FLAT, i)

        def getRuleIndex(self):
            return MusicNotationParser.RULE_note_or_chord

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNote_or_chord" ):
                listener.enterNote_or_chord(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNote_or_chord" ):
                listener.exitNote_or_chord(self)




    def note_or_chord(self):

        localctx = MusicNotationParser.Note_or_chordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_note_or_chord)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 58
                self.match(MusicNotationParser.NOTE)
                self.state = 65
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                if la_ == 1:
                    self.state = 60
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==5:
                        self.state = 59
                        self.match(MusicNotationParser.SHARP)


                    pass

                elif la_ == 2:
                    self.state = 63
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==6:
                        self.state = 62
                        self.match(MusicNotationParser.FLAT)


                    pass


                self.state = 67
                self.match(MusicNotationParser.OCTAVE)
                self.state = 70 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

            self.state = 72
            self.match(MusicNotationParser.DURATION)
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 73
                self.articulation()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RestContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REST(self):
            return self.getToken(MusicNotationParser.REST, 0)

        def DURATION(self):
            return self.getToken(MusicNotationParser.DURATION, 0)

        def getRuleIndex(self):
            return MusicNotationParser.RULE_rest

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRest" ):
                listener.enterRest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRest" ):
                listener.exitRest(self)




    def rest(self):

        localctx = MusicNotationParser.RestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_rest)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(MusicNotationParser.REST)
            self.state = 77
            self.match(MusicNotationParser.DURATION)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArticulationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STACCATO(self):
            return self.getToken(MusicNotationParser.STACCATO, 0)

        def getRuleIndex(self):
            return MusicNotationParser.RULE_articulation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArticulation" ):
                listener.enterArticulation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArticulation" ):
                listener.exitArticulation(self)




    def articulation(self):

        localctx = MusicNotationParser.ArticulationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_articulation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(MusicNotationParser.STACCATO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dynamic(self):
            return self.getTypedRuleContext(MusicNotationParser.DynamicContext,0)


        def getRuleIndex(self):
            return MusicNotationParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = MusicNotationParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.dynamic()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DynamicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CRESCENDO(self, i:int=None):
            if i is None:
                return self.getTokens(MusicNotationParser.CRESCENDO)
            else:
                return self.getToken(MusicNotationParser.CRESCENDO, i)

        def noteSequence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MusicNotationParser.NoteSequenceContext)
            else:
                return self.getTypedRuleContext(MusicNotationParser.NoteSequenceContext,i)


        def DIMINUENDO(self, i:int=None):
            if i is None:
                return self.getTokens(MusicNotationParser.DIMINUENDO)
            else:
                return self.getToken(MusicNotationParser.DIMINUENDO, i)

        def getRuleIndex(self):
            return MusicNotationParser.RULE_dynamic

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDynamic" ):
                listener.enterDynamic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDynamic" ):
                listener.exitDynamic(self)




    def dynamic(self):

        localctx = MusicNotationParser.DynamicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_dynamic)
        try:
            self.state = 99
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 83
                self.match(MusicNotationParser.CRESCENDO)
                self.state = 85 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 84
                        self.noteSequence()

                    else:
                        raise NoViableAltException(self)
                    self.state = 87 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

                self.state = 89
                self.match(MusicNotationParser.CRESCENDO)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 91
                self.match(MusicNotationParser.DIMINUENDO)
                self.state = 93 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 92
                        self.noteSequence()

                    else:
                        raise NoViableAltException(self)
                    self.state = 95 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

                self.state = 97
                self.match(MusicNotationParser.DIMINUENDO)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





