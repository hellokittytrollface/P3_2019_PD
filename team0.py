####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####
team_name = 'Ice Tray' # Only 10 chars displayed.

'''strategy_name = 'Betray'
strategy_description = 'Always Betray'

def move(my_history, their_history, my_score, their_score):
    return b'''

strategy_name = 'Copycat'
strategy_description = 'Copy openent moves'

def move(my_history, their_history, my_score, their_score):
    if len(their_history)>=1:
        if their_history[-1] == 'c':
            return 'c'
        if their_history[-1] == 'b':
            return 'b'
    else:
        return 'b'

        
'''strategy_name = 'Diversion'
strategy_description = 'Collude, then always betray'     
        
def move(my_history, their_history, my_score, their_score):
    if 'c' in their_history:
        return 'b'
    else:
        return 'c'
        '''

