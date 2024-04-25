music : measure+ ;
measure : pipe noteSequence pipe ;
noteSequence : noteOrRest+ ;
noteOrRest : chord | note | rest ;
note : pitch duration ;
pitch : step octave ;
chord : pitch pitch+ duration ;