# Generated from MusicNotation.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MusicNotationParser import MusicNotationParser
else:
    from MusicNotationParser import MusicNotationParser

# This class defines a complete listener for a parse tree produced by MusicNotationParser.
class MusicNotationListener(ParseTreeListener):

    # Enter a parse tree produced by MusicNotationParser#music.
    def enterMusic(self, ctx:MusicNotationParser.MusicContext):
        pass

    # Exit a parse tree produced by MusicNotationParser#music.
    def exitMusic(self, ctx:MusicNotationParser.MusicContext):
        pass


    # Enter a parse tree produced by MusicNotationParser#part.
    def enterPart(self, ctx:MusicNotationParser.PartContext):
        pass

    # Exit a parse tree produced by MusicNotationParser#part.
    def exitPart(self, ctx:MusicNotationParser.PartContext):
        pass


    # Enter a parse tree produced by MusicNotationParser#key.
    def enterKey(self, ctx:MusicNotationParser.KeyContext):
        pass

    # Exit a parse tree produced by MusicNotationParser#key.
    def exitKey(self, ctx:MusicNotationParser.KeyContext):
        pass


    # Enter a parse tree produced by MusicNotationParser#tempo.
    def enterTempo(self, ctx:MusicNotationParser.TempoContext):
        pass

    # Exit a parse tree produced by MusicNotationParser#tempo.
    def exitTempo(self, ctx:MusicNotationParser.TempoContext):
        pass


    # Enter a parse tree produced by MusicNotationParser#measure.
    def enterMeasure(self, ctx:MusicNotationParser.MeasureContext):
        pass

    # Exit a parse tree produced by MusicNotationParser#measure.
    def exitMeasure(self, ctx:MusicNotationParser.MeasureContext):
        pass


    # Enter a parse tree produced by MusicNotationParser#noteSequence.
    def enterNoteSequence(self, ctx:MusicNotationParser.NoteSequenceContext):
        pass

    # Exit a parse tree produced by MusicNotationParser#noteSequence.
    def exitNoteSequence(self, ctx:MusicNotationParser.NoteSequenceContext):
        pass


    # Enter a parse tree produced by MusicNotationParser#musicalElement.
    def enterMusicalElement(self, ctx:MusicNotationParser.MusicalElementContext):
        pass

    # Exit a parse tree produced by MusicNotationParser#musicalElement.
    def exitMusicalElement(self, ctx:MusicNotationParser.MusicalElementContext):
        pass


    # Enter a parse tree produced by MusicNotationParser#note_or_chord.
    def enterNote_or_chord(self, ctx:MusicNotationParser.Note_or_chordContext):
        pass

    # Exit a parse tree produced by MusicNotationParser#note_or_chord.
    def exitNote_or_chord(self, ctx:MusicNotationParser.Note_or_chordContext):
        pass


    # Enter a parse tree produced by MusicNotationParser#rest.
    def enterRest(self, ctx:MusicNotationParser.RestContext):
        pass

    # Exit a parse tree produced by MusicNotationParser#rest.
    def exitRest(self, ctx:MusicNotationParser.RestContext):
        pass


    # Enter a parse tree produced by MusicNotationParser#articulation.
    def enterArticulation(self, ctx:MusicNotationParser.ArticulationContext):
        pass

    # Exit a parse tree produced by MusicNotationParser#articulation.
    def exitArticulation(self, ctx:MusicNotationParser.ArticulationContext):
        pass


    # Enter a parse tree produced by MusicNotationParser#expression.
    def enterExpression(self, ctx:MusicNotationParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MusicNotationParser#expression.
    def exitExpression(self, ctx:MusicNotationParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MusicNotationParser#dynamic.
    def enterDynamic(self, ctx:MusicNotationParser.DynamicContext):
        pass

    # Exit a parse tree produced by MusicNotationParser#dynamic.
    def exitDynamic(self, ctx:MusicNotationParser.DynamicContext):
        pass



del MusicNotationParser