import formuls as f
import get 

def clc(r):
    res1 = 1e10
    oxi_ = 0
    e_ = 0
    for oxi in range(1, 481):      
        for e in range(1, 81):
            trash = []
            for i in range(e):
                r1 = r
                if sum(trash)+i <= e:
                    trash.append(i)
                else:
                    break
            t = len(trash)

            sh = 8
            Vbig = []
            shbig = []
            counter = 0
            while r1 > 0:
                v = f.V(e, sh, oxi, t)
                sh = f.SHnew(sh, t, oxi)
                Vbig.append(v)
                shbig.append(sh)
                counter += 1
                r1 -= v
            if res1 >= counter:
                oxi_ = oxi
                e_ = e
                res1 = counter
    return res1, oxi_, e_

def one_route(data, no):
    sum = 0
    max_oxi = 0
    for i in data[no]['points']:
        ans = clc(i['distance'])
        sum += ans[0]
        max_oxi = max(max_oxi, ans[1])
    return [i for i in range(1, sum+1)], max_oxi

#print(one_route(get.req("https://dt.miet.ru/ppo_it_final", "9e83w26h"), 0))
