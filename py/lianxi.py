while True:
    a = 0
    sum = int(input('请输入密码：'))
    if sum == 198764 :
        print('密码正确')
        break
    else :
        print('密码错误请从新输入，你还有{}次机会：'.format(4-a))
        a += 1
        if a == 4 :
            print('机会用完了')
            break