import pandas as pd


def get_tuple(f,max = 10):#获得(user,time,id)的元组
    n = 1
    while n<= max:
        line = f.readline().split('\t')
        user = line[0]
        venue = line[1]
        # 1 = line[2]
        time = line[3]
        photo_id = line[4].split('\n')[0]
        TUPLE = (user,time,photo_id)
        yield TUPLE
        n += 1
        #print(TUPLE)

def divide_time(start,end,num=10):#均分时间段
    list = []
    gap = (end - start)/num
    for i in range(num+1):
        list.append(start+i*gap)
    return list

def find_time_index(time,list):#在均分的时间点list里找到时间的位置
    for i in range(len(list)):
        if i == len(list)-1 and time == list[i]:
            return len(list)-1
            break
        if list[i]<=time<list[i+1]:
            return i+1
            break
        else:
            pass

if __name__ == '__main__':
    #这边改成train.tsv的path
    path = r'F:\PycharmProjects\NeuralCF_tensorflow\NeuralCF_tensorflow\Data\Venue\train.tsv'
    #这边改成想读多少行数据
    line_num = 1000

    photo_dict = {}
    user_dict = {}
    time_dict = {}

    f = open(path, 'r')


    flag= 0
    for i in get_tuple(f,line_num):
        flag+=1
        print(flag)
        if user_dict.__contains__(i[0]):
            temp = user_dict[i[0]]
            #print(temp,i)
            temp.append([i[2], int(i[1])])
            user_dict[i[0]]=temp
            #print(user_dict)

        else:
            user_dict[i[0]]=[]
            #print(user_dict)
            #print(i)
            temp = user_dict[i[0]]
            #print(temp,i)
            temp.append([i[2], int(i[1])])
            user_dict[i[0]]=temp
            #print(user_dict)
#以上是为了获得{user:[[photoid,time],...],...}的字典，以便下面使用

    for user in user_dict:
        time_set = []
        for photo in user_dict[user]:
            time_set.append(photo[1])#photo[1] 为时间,[0] 为id
        #print(time_set)
        start_time = min(time_set)
        end_time = max(time_set)
        div_10 = divide_time(start_time,end_time,10)
        #print(div_10)
#对每个用户的时长十等分,得到的是list:div_10


        for index, host_photo in enumerate(user_dict[user]):
            host_photo_id = host_photo[0]
            host_photo_time = host_photo[1]
            photo_dict[(user, host_photo_time, host_photo_id)] =\
                {10:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}

            time_dict[(user, host_photo_time, host_photo_id)] =\
                [0,0,0,0,0,0,0,0,0,0]

            for guest_photo in user_dict[user]:
                guest_photo_id = guest_photo[0]
                guest_photo_time = guest_photo[1]
                if guest_photo_time < host_photo_time:
                    time_index = find_time_index(guest_photo_time,div_10)
                    photo_dict[(user,host_photo_time,host_photo_id)][time_index]\
                        .append((user,guest_photo_time,guest_photo_id))
                    time_dict[(user,host_photo_time,host_photo_id)][time_index-1] = 1
#得到两个字典

    #print(photo_dict)
    #print(time_dict)

    with open('dict1.txt','w') as f1:
        f1.write(str(photo_dict))

    with open('dict2.txt','w') as f1:
        f1.write(str(time_dict))








