import collections

class number_swaps:
    def find_indexes(self, num=0):
        # if(num==0):
        #     return {"0": [1]}
        num_str = str(num)
        length = len(num_str)
        dict = {}
        for i in range(0,length):
            digit = num_str[i]
            # print(digit)
            # print(dict.get(digit))
            if i==0:
                dict[digit] = [i]
                continue
            if not dict.get(digit):
                dict[digit] = [i]
            else:
                val = dict.get(digit)
                val.append(i)
                dict[digit] = val
        od = collections.OrderedDict(sorted(dict.items()))
        # print(dict)
        # print(type(dict))
        # print(od)
        # print(type(od))
        # print(od.get(digit))
        return od

    def find_max(self, num=0, k_swaps=0):
        num_str = str(num)
        length = len(num_str)
        if k_swaps==0:
            print("Swap input is 0. No swap allowed")
            return
        if num==0:
            print("Number input is 0. Maximum Number is 0")
            return
        ind_dic = self.find_indexes(num)
        l_keys = list(ind_dic.keys())
        print(l_keys)
        print(type(l_keys))
        digits = len(l_keys)
        max_dig = l_keys[digits-1]
        max_num = num_str
        num_swaps = 0
        for i in range(0,length):
            digit = num_str[i]
            if digit==str(max_dig):
                continue
            for j in range(0,digits):
                indexes = ind_dic.get(l_keys[j])
                indexes_copy = indexes.copy()
                l = len(indexes)

                for k in range(0,l):
                    if indexes_copy[k]>i:
                        indexes.remove(indexes_copy[k])
                    elif(num_swaps+indexes[k]-i-1)<=k_swaps:
                        max_num[indexes[k]]=digit
                        max_num[i] = j
                        num_swaps = num_swaps + indexes[k] - i + 1
                        val = ind_dic.get(digit)
                        val.remove(j)
                        val.append(indexes[k])
                        val.sort()
                        ind_dic[digit] = val
                        indexes.remove(indexes_copy[k])
                        ind_dic[j] = indexes
                    else:
                        break
            return max_num

ns = number_swaps()


print(ns.find_max(9825462363467666912689362389632896438968961238963896238969, 2))
