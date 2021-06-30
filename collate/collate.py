#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import re

@click.command()
def collate():
    # 1つめの入力
    click.echo("[First] Please input lines for compare")
    read_flg = True
    in_texts_1 = []
    while (read_flg):
        in_text = input()
        if in_text == '':
            read_flg = False
        else:
            in_texts_1.append(in_text)
    is_match_texts_1 =  [False for _ in in_texts_1]
    # 2つめの入力
    click.echo("[Second] Please input lines for compare")
    read_flg = True
    in_texts_2 = []
    while (read_flg):
        in_text = input()
        if in_text == '':
            read_flg = False
        else:
            in_texts_2.append(in_text)
    is_match_texts_2 =  [False for _ in in_texts_2]
    # 比較
    result_lines = []
    for indx1, in_text1 in enumerate(in_texts_1):
        for indx2, in_text2 in enumerate(in_texts_2):
            
            if in_text1  ==  in_text2:
                if is_match_texts_1[indx1]:
                    # New
                    result_lines.append({
                        'left_index': indx1,
                        'left_value': in_text1,
                        'right_indx': indx2,
                        'right_value': in_text2,
                        'result': 'Same'})
                else:
                    # duplicated
                    result_lines.append({
                        'left_index': '',
                        'left_value': '',
                        'right_indx': indx2,
                        'right_value': in_text2,
                        'result': 'SameDuplicated(left:{}'.format(indx1)})

                is_match_texts_1[indx1] = True
                is_match_texts_2[indx2] = True
        
        if not(is_match_texts_1[indx1]):
            # Not Found
            result_lines.append({
                'left_index': indx1,
                'left_value': in_text1,
                'right_indx': '',
                'right_value': '',
                'result': 'Left Only'})
    
    for indx2, in_text2 in enumerate(in_texts_2):
        if is_match_texts_2(indx2):
            continue
        result_lines.append({
            'left_index': '',
            'left_value': '',
            'right_indx': indx2,
            'right_value': in_text2,
            'result': 'Right Only'})
    
    for result_line in result_lines:
        print(result_line)



if __name__ == '__main__':
    collate()
