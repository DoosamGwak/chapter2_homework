import random

def try_again():
    yn = input('게임을 다시 하시겠습니까? (y/n): ')
    
    if yn == 'y':
        ud_game()
    elif yn =='n': 
        return
    else:
        print('잘못된 입력값입니다. 다시 입력해주세요.\n')
        try_again()

def check_ud(com, cnt):
    try:
        player = int(input('1~100의 자연수 중 하나를 입력 하세요: '))
        
    except ValueError as b:
        print('잘못된 입력값입니다. 다시 입력해주세요.\n')
        check_ud(com, cnt)

    else:
        if player < 1:
            print('1보다 작습니다. 다시 입력해주세요.\n')
            check_ud(com,cnt)

        elif player > 100:
            print('100보다 큽니다. 다시 입력해주세요.\n')
            check_ud(com,cnt)

        elif com < player:
            cnt += 1
            print('DOWN')
            check_ud(com,cnt)

        elif com > player:
            cnt += 1 
            print('UP')
            check_ud(com,cnt)

        elif com == player:
            cnt += 1
            print(f'정답입니다. {cnt}번만에 정답을 맞추셨네요. 축하합니다.')
            return
    
        return

def ud_game():
    com = random.randrange(1,101)
    cnt_try = 0
    
    check_ud(com, cnt_try)
    try_again()

    return

ud_game()