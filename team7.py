####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = '1337'
strategy_name = 'copycat'
strategy_description = 'if i cant beat them join them'
    
def move(my_history, their_history, my_score, their_score):
    '''
    Begin with cooperate, then copy opponent's last move.
    '''
    
    #This example player always betrays.      
    if(len(their_history) == 0):
      return 'c'
    else:
      return their_history[-1]
