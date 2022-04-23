import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S States Game')
image = '/Users/thanosraptis/Developer/Python/100DaysOfCode/united_states_game/blank_states_img.gif'
screen.addshape(image)
screen.setup(width=800,height=600)
turtle.shape(image)

def get_mouse_click_coor(x,y):
    print(x,y)

turtle.onscreenclick(get_mouse_click_coor)

jimmy = turtle.Turtle(visible=False)


game_is_on = True 





data = pandas.read_csv('united_states_game/50_states.csv')
states = data['state'].to_list()

guessed_states = []
unguessed_states = []

while len(guessed_states) < 50 :
    answer_state = screen.textinput(title=f'Guessed states:{len(guessed_states)}/50', prompt='Guess another state\'s name?').title()
    if answer_state == 'Exit':
        for state in states:
            if state not in guessed_states:
                unguessed_states.append(state)
        new_data = pandas.DataFrame(unguessed_states)
        new_data.to_csv('states_to_learn.csv')
        break
    for state in states:
        if answer_state == state :
            print('ok')
            guessed_states.append(state)
            state_x = int(data.loc[data['state'] == answer_state, 'x'])
            state_y = int(data.loc[data['state'] == answer_state, 'y'])
            jimmy.penup()
            jimmy.goto(state_x, state_y)
            jimmy.write(answer_state,False,'Center',('Courier', 14, 'normal'))
            
            
    




