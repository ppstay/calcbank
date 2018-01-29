# -*- coding: utf-8 -*-
import os
import random
import logging


class CalcBank:
    def __init__(self, logger = None):
        self.logger = logger
        self.c_list = []
        self.c_type = ['+', '-', '×'] #, '÷']
        self.cap = 1000

    def get_list(self, count):
        for i in range(0, count):
            self.c_list.append(self.get_question(3))
        return self.c_list

    def get_question(self, num_of_numbers):
        operands = []
        operations = []
        t = self.cap
        for i in range(0, num_of_numbers - 1):
            t = random.randrange(t/2, t)
            operands.append(t)
            operations.append(self.c_type[random.randrange(0,len(self.c_type))])
        operands.append(random.randrange(0,t))
        return Question(operands, operations)


class Question:
    def __init__(self, operands, operations):
        self.operands = operands
        self.operations = operations


class Printer:
    def __init__(self, question_list, char_per_line):
        self.question_list = question_list
        self.char_per_line = char_per_line
        self.lines_between = 0

    def print_out(self):
        line = ""
        for question in self.question_list:
            i = 0
            for i in range(0, len(question.operations)):
                line = line + str(question.operands[i]) + " "
                line = line + str(question.operations[i]) + " "
            line = line + str(question.operands[i+1])
            line = line + " =         "
            if len(line) < (self.char_per_line / 2):
                line = line + " "
            else:
                print line
                #print "\n" * (self.lines_between-1)
                line = ""


if __name__ == "__main__":
    calc_bank = CalcBank()
    list = calc_bank.get_list(10)
    Printer(list, 80).print_out()