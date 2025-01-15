# puzzle_tools

Puzzle Tools is a collection of Python-based analysis tools for puzzle hunts, crosswords, riddles, etc.

Here is some of the functionality.

## Frequency Analysis

Uses frequency analysis of quadgrams (four-letter groups) to compute a likelihood that a given string is english rather than gibberish.

This can be used to loop over large numbers of possibilities and examine only the most promising.

It is broadly robust against erroneous letters and missing letters.

