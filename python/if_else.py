go_stay = input('fire or water? ').lower()
if go_stay == str('water'):
    left_right = input('left or right? ').lower()
    if left_right == str('right'):
        follow = input('follow the lights? ').lower()
        if follow == str('no'):
            up_down = input('go up or down? ').lower()
            if up_down == str('down'):
                go_on = input('explore or turn back? ').lower()
                if go_on == str('explore'):
                    idol_feather = input('idol or feather? ').lower()
                    if idol_feather == str('feather'):
                        print('you win')
                    elif idol_feather == str('idol'):
                        print('you die')
                elif go_on == str('go back'):
                    print('coward')
            elif up_down == str('up'):
                print('back to the beach')
        elif follow == str('yes'):
            print('you drowned')
    elif left_right == str('left'):
        print('eaten by a tiger')
elif go_stay == ('fire'):
    print('no rescue in sight')
else:
    print('unknown input')
                
