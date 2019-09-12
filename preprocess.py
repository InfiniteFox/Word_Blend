# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 04:21:52 2019

@author: IF
"""

import time

start_word_dict = {}
end_word_dict = {}


with open("dict.txt") as file:
    for line in file:
        w = line.rstrip()
        if len(w)>1:
            start_word = w[0]
            end_word = w[-1]
            #Start
            if (start_word in start_word_dict):
                start_word_dict[start_word].append(w)
            else:
                start_word_dict[start_word] = [w]
            #End
            if (end_word in end_word_dict):
                end_word_dict[end_word].append(w)
            else:
                end_word_dict[end_word] = [w]


candidates = []
with open("candidates.txt") as file:
    for line in file:
        w = line.rstrip()
        candidates.append(w)




def get_prefix_number_dict(candidates):
    prefix_number_dict = {}
    for w in start_word_dict[candidates[0]]:
        for l in range(len(candidates)):
            number = l+1
            #print(number,candidates[-number:],w[-number:])
            if candidates[:number] != w[:number]:
                if l in prefix_number_dict:
                    prefix_number_dict[l].append(w)
                else:
                    prefix_number_dict[l] = [w]
                break  
    return prefix_number_dict

def get_suffix_number_dict(candidates):
    suffix_number_dict = {}
    for w in end_word_dict[candidates[-1]]:
        for l in range(len(candidates)):
            number = l+1
            #print(l,candidates[-number:],w[-number:])
            if candidates[-number:] != w[-number:]:
                if l in suffix_number_dict:
                    suffix_number_dict[l].append(w)
                else:
                    suffix_number_dict[l] = [w]
                break   
    return suffix_number_dict


l = get_suffix_number_dict("acortan")

def check_lastword_repeat(word):
    lastword = word[-1]
    for i in range(len(word)-1):
        number = i+2
        if lastword != word[-number]:
            return i
    return len(word)-1





def check_word_blend_1(candidate):
    prefix_number_dict = get_prefix_number_dict(candidate)
    suffix_number_dict = get_suffix_number_dict(candidate)
    #isBlend = False
    for l in range(len(candidate)):
        prefix_number = l+1
        suffix_number = len(candidate)-(l+1)
        if prefix_number in prefix_number_dict and suffix_number in suffix_number_dict:
            #Check 
            return True
    return False

def check_word_blend_2(candidate, same_words=0):
    prefix_number_dict = get_prefix_number_dict(candidate)
    suffix_number_dict = get_suffix_number_dict(candidate)
    max_prefix_number = max(prefix_number_dict.keys())
    max_suffix_number = max(suffix_number_dict.keys())
    if max_prefix_number + max_suffix_number >= len(candidate) + same_words:
        return True
    return False

def start_check(check_lastword=False, check_method=1):
    checked = 0
    checked_in_dict = 0
    blend = []
    for i in range(len(candidates)):
        if (i%200==0):
            step = i / len(candidates) * 100
            print('Finish:','%.2f' % step,'%')
        
        c = candidates[i] 
        if check_lastword:
            clr = check_lastword_repeat(c)
            if clr >= 2: #Last word repeat at least twice
                checked += 1
                nc = c[:-clr]
                if nc in start_word_dict[nc[0]]:
                    checked_in_dict += 1
                continue
        if check_method == 1:
            if check_word_blend_1(c):
                blend.append(c)
        elif check_method == 2:
            if check_word_blend_2(c):
                blend.append(c)
    return blend, checked, checked_in_dict
    # =============================================================================
    #             for prefix in prefix_number_dict[prefix_number]:
    #                 for suffix in suffix_number_dict[suffix_number]:
    #                     output.append([prefix, suffix])
    # =============================================================================


start_time = time.time()
blend, checked, checked_in_dict = start_check(True, 2)
used_time = time.time() - start_time
print('Finish in:', '%.2f' % used_time, 's')
print(f'Totoal Blend Prediction:{len(blend)}')
print(f'Totoal checked:{checked}')
print(f'Totoal checked_in_dict:{checked_in_dict}')

with open("prediction_3.txt", "w") as file:
    for b in blend:
        file.write(b)
        file.write('\n')
            
            
    