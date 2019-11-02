

def making_dict(keys, values):
    dictionary = {}
    lst = []
    j = 1
    for i in range(len(keys)):
        # print("keys :"+str(keys[i])+" string : "+str(values[i]))
        dictionary[keys[i]] = values[i] 
    return dictionary


def making_unique_list(lst):
    temp = []
    j = 1
    for i in lst:
        if i in temp:
            num = i + (i / j) + j  
            j += 1
            lst.append(num)
        else:
            temp.append(i)
    return temp


def generate_pattern(string):
    DNA = "ACGT"
    lst = []
    for i in range(len(string)):
        s = list(string)
        temp = s
        temp[i] = DNA[0]
        temp = "".join(temp)

        lst.append(temp)
        temp = s
        temp[i] = DNA[1]
        temp = "".join(temp)
        lst.append(temp)
        temp = s
        temp[i] = DNA[2]
        temp = "".join(temp)
        lst.append(temp)
        temp = s
        temp[i] = DNA[3]
        temp = "".join(temp)
        lst.append(temp)
    return lst
    # print(lst)
    


def count_number_of_matching_character(str1, str2):  
    c, j = 0, 0 
    for i in str1:     
        if str2.find(i)>= 0 and j == str1.find(i):  
            c += 1
        j += 1
    return c; 




def making_all_pattern_lst(all_patterns, pattern_lst):
    for i in pattern_lst:

        # print("add"+str(i))
        # if i in all_patterns:
        #     print(i)
        #     # pattern_lst.remove(i)
        # else:
        #     print(i)
        all_patterns.append(i)
        
    lst = [all_patterns,pattern_lst]
    # print(lst)
    return lst



def count_patterns(patterns, lst):
    final_lst = []
    for i in patterns:
        count = 0 
        for j in lst:
            if i == j:
                count += 1
        final_lst.append(count)
    print(final_lst)
    print(patterns)






def main_code():
    with open('file.txt') as fp:
        test_cases = int(fp.readline())
        # print(int(test_cases))
        for i in range(test_cases):

            #taking data from file and make list and variables
            input_data = fp.readline().split("\n")
            data_in_lst = input_data[0].split(" ") 
            total_number_string_t = int(data_in_lst[0])
            data_in_lst.remove(data_in_lst[0])
            length_of_pattern_k = int(data_in_lst[0])
            data_in_lst.remove(data_in_lst[0])

            #finding unique letters in every list the list with minimum unique is the string to start matching
            unique_letter_in_each_string = []
            for i in data_in_lst:
                unique_letter_in_each_string.append(len(list(set(i))))
            unique_letter_in_each_string = making_unique_list(unique_letter_in_each_string)

            #making dictionary with unique letters as keys and DNA strings as values
            data_in_dict = making_dict(unique_letter_in_each_string, data_in_lst)
            # print(data_in_dict)
            unique_letter_in_each_string.sort()

            #selecting starting DNA string
            pattern_starting_index = 0
            index_of_starter_DNA = unique_letter_in_each_string[0]
            unique_letter_in_each_string.remove(unique_letter_in_each_string[0])
            starter_DNA = data_in_dict[index_of_starter_DNA]
            # print(unique_letter_in_each_string)
            
            final_patterns = []
            all_patterns = []
            for j in range(len(starter_DNA)-length_of_pattern_k+1):
                pattern = starter_DNA[j: j+length_of_pattern_k]
                # print(pattern)
                
                pattern_lst = generate_pattern(pattern)
                lsts = making_all_pattern_lst(all_patterns, pattern_lst)
                all_patterns = lsts[0]
                pattern_lst = lsts[1]
                
                for l in unique_letter_in_each_string:
                    string = data_in_dict[l]
            
                    for k in range(len(string)-length_of_pattern_k+1):
                        internal_pattern = string[k: k+length_of_pattern_k]
                        for m in pattern_lst:
                            # print(m)
                            number_of_match = count_number_of_matching_character(m, internal_pattern)
                            # print(number_of_match)
                            if(length_of_pattern_k == number_of_match ):
                                final_patterns.append(m)
                            if(length_of_pattern_k-1 == number_of_match):
                                final_patterns.append(m)
            print(final_patterns)
            print(all_patterns)
            
            count_patterns(all_patterns, final_patterns)
            


main_code()

# generate_pattern("GG")




