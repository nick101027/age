# else if 另外如果
drive = input('請問你有沒有開過車？')
if drive != '有' and drive != '沒有':
    print('只能輸入有 或 沒有')
    raise SystemExit
    
age = input('請問你的年齡？')
age = int(age)
if drive == '有':
    if age >= 18:
        print('你通過測驗了')
    else:
        print('奇怪 你怎麼會開過車')
elif drive == '沒有':
    if age >= 18:
        print('你可以考駕照了阿，怎麼還不去考')
    else:
        print('很好，再過幾年就可以考囉！')