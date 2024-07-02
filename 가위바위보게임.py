import random

count_wdl = [0,0,0]

def try_again():
    a = input('게임을 다시 하시겠습니까? (y/n): ')
    
    if a == 'y':
        rsp_game()
    elif a =='n': 
        return
    else:
        print('잘못된 입력값입니다. 다시 입력해주세요.\n')
        try_again()

def rsp_game():
    
    list_rsp= ['가위', '바위', '보']
    player = ''
    com = list_rsp[random.randrange(0,3)]
    
    player = check_rsp()

    print(f'컴퓨터: {com} \n플레이어: {player}\n')

    win_or_lose(com, player)

    try_again()

    return

def check_rsp():

    a = input('가위 바위 보 중 하나를 입력 하세요: \n')
    
    if a == '가위':
        a = '가위'
    elif a == '바위':
        a = '바위'
    elif  a == '보':
        a = '보'
    else:
        print('잘못된 입력값입니다. 다시 입력해주세요.\n')
        check_rsp()
    
    return a

def win_or_lose(a, b):

    TXTWIN = '이겼습니다. 축하드립니다.\n'
    TXTLOSE = '졌습니다. 다음기회에...\n'
    TXTDRAW = '비겼습니다. 한번 더 ?\n'

    if a=='바위':
        if b=='바위':
            print(TXTDRAW)
            count_wdl[1] += 1
        elif b=='가위':
            print(TXTLOSE)
            count_wdl[2] += 1
        else:
            print(TXTWIN)
            count_wdl[0] += 1
    elif a=='가위':
        if b=='바위':
            print(TXTWIN)
            count_wdl[0] += 1
        elif b=='가위':
            print(TXTDRAW)
            count_wdl[1] += 1
        else:
            print(TXTLOSE)
            count_wdl[2] += 1
    else:
        if b=='바위':
            print(TXTLOSE)
            count_wdl[2] += 1
        elif b=='가위':
            print(TXTWIN)
            count_wdl[0] += 1
        else:
            print(TXTDRAW)
            count_wdl[1] += 1
    
    print(f'현재 전적 {count_wdl[0]}승 {count_wdl[1]}무 {count_wdl[2]}패\n승률:{round((count_wdl[0]/sum(count_wdl)),4)*100}%\n')

    return

rsp_game()