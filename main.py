__author__ = "Jie Lin"
__date__ = "May 04, 2019"

import os
import sys
import json


def load_text(path):
    f = open(path)
    word_lines = f.readlines()
    f.close()
    return [int(num) for num in word_lines]


def load_text2(path):
    f = open(path)
    word_lines = f.readlines()
    f.close()
    return [str(num.strip()) for num in word_lines]


def normalized(score):
    if score > 1:
        score = 1
    elif score < 0:
        score = 0
    return round(score, 2)


def main_def():
    number = load_text('words/number.txt')
    bad = load_text2('words/bad.txt')
    love = load_text2('words/love.txt')
    positive = load_text2('words/positive.txt')
    negative = load_text2('words/negative.txt')
    common = load_text2('words/common.txt')
    path = "Lyrics/"
    if len(sys.argv) > 1:
        if str(sys.argv[1])[-1] == '\\':
            path = str(sys.argv[1])
        else:
            print("Path is wrong, using the default path: Lyrics/")
            path = "Lyrics/"
    files = os.listdir(path)
    ch = []
    for file in files:
        song = {}
        words_number, bad_words, love_words, common_words = 0, 0, 0, 0
        positive_words, negative_words = 0, 0
        info = file.strip(".txt").split("~")
        f = open(path+file, encoding="utf8")
        lyrics = f.readlines()
        f.close()
        for line in lyrics:
            words_list = line.strip("\n").split()
            words_number += len(words_list)
            for lst in words_list:
                if lst not in bad:
                    if bad_words < 1.0:
                        bad_words += 1
                if lst in love:
                    love_words += 1
                if lst in positive:
                    positive_words += 1
                if lst in negative:
                    negative_words += 1
                if lst not in common:
                    common_words += 1

        index, length = 0, 0
        run = 1
        while run:
            if words_number <= number[index]:
                run = 0
            else:
                index += 1
                length += 0.1

        safe_score = normalized(100 * bad_words / words_number)
        love_score = normalized(10 * love_words / words_number)
        mood_score = normalized(0.5 + (positive_words - negative_words) / words_number)
        length_score = round(length, 2)
        complexity_score = normalized(common_words/words_number)
        song["id"] = int(info[0])
        song["artist"] = info[1].replace("-", " ")
        song["title"] = info[2].replace("-", " ")
        song["kid_safe"] = safe_score
        song["love"] = love_score
        song["mood"] = mood_score
        song["length"] = length_score
        song["complexity"] = complexity_score
        ch.append(song)

    result = {"characterizations": ch}
    output = json.dumps(result)
    return output


if __name__ == '__main__':
    output = main_def()
    name = "result.txt"
    f = open(name, 'w')
    f.write(output)

