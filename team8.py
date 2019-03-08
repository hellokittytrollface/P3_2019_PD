import random
####
# Each team's file must define four tokens:
#     team_name: LM10
#     strategy_name: COPYING
#     strategy_description: starts by cooperating, then replicates opponent's moves
#     move: A function that returns 'c' or 'b'
####

team_name = 'LM10' # Only 10 chars displayed.
strategy_name = 'COPYING'
strategy_description = 'Start with cooperation and then copy opponents moves.'

    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    strategy = 'copy'
    if strategy == 'copy':
        if len(their_history) == 0:
            return 'c'
        else:
            return their_history[-1]
    if strategy == 'always betray':
        return 'b'
    if strategy == 'betray then always cooparate':
        if len(their_history) == 0:
            return 'b'
        else:
            return 'c'
    if strategy == 'cooperate until betray':
        if 'b' not in their_history:
            return 'c'
        else:
            return 'b'
    if strategy == 'random':
        if random.randint(0, 1) == 0:
            return 'c'
        else:
            return 'b'

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.

   
