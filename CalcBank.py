# -*- coding: utf-8 -*-
import os
import random
import logging

import math


def is_prime(num):
    for i in range(2, int(math.sqrt(num))):
        if (num % i) == 0:
            return False
        return True


def get_factor(num):
    factors = []
    for i in range(2, int(math.sqrt(num))):
        if (num % i) == 0:
            factors.append(i)
    if len(factors) == 0:
        return num
    return factors[random.randrange(0, len(factors))]


class CalcBank:
    def __init__(self, logger=None, cap=1000, c_type=('+', '-', '×', '÷'), num_of_operands=3):
        self.logger = logger
        self.c_list = []
        self.c_type = c_type
        self.cap = cap
        self.num_of_operands = num_of_operands

    def get_list(self, count, valid_guarantee=True):
        for i in range(0, count):
            if valid_guarantee:
                self.c_list.append(self.get_question_valid_guarantee(self.num_of_operands))
            else:
                self.c_list.append(self.get_question(self.num_of_operands))
        return self.c_list

    def get_question(self, num_of_operands):
        operands = []
        operations = []
        t = self.cap
        for i in range(0, num_of_operands - 1):
            t = random.randrange(t/2, t)
            operands.append(t)
            operations.append(self.c_type[random.randrange(0, len(self.c_type))])
        operands.append(random.randrange(0, t))
        return Question(operands, operations)

    def get_question_valid_guarantee(self, num_of_operands):
        operands = []
        operations = []

        operand = self.get_seed()
        operands.append(operand)

        for i in range(0, num_of_operands - 1):
            operation = self.next_operation(operations)
            operations.append(operation)
            operand = self.next_valid_operand(operand, operation)
            operands.append(operand)

        return Question(operands, operations)

    def next_valid_operand(self, pre_operand, operation):
        if pre_operand == 0:
            return self.get_seed()
        if operation == '÷':
            return get_factor(pre_operand)
        if operation == '-':
            return pre_operand / 2
        return self.get_seed()

    def next_operation(self, operations):
        not_used = list(set(self.c_type) - set(operations))
        return not_used[random.randrange(0, len(not_used))]

    def get_seed(self):
        seed = random.randrange(self.cap/2, self.cap)
        while is_prime(seed):
            seed = random.randrange(self.cap/2, self.cap)
        return seed


class Question:
    def __init__(self, operands, operations):
        self.operands = operands
        self.operations = operations


class Printer:
    def __init__(self, question_list, chars_per_line=80, blank_lines_between=5):
        self.question_list = question_list
        self.chars_per_line = chars_per_line
        self.blank_lines_between = blank_lines_between

    def print_out(self):
        line = ""
        for question in self.question_list:
            i = 0
            for i in range(0, len(question.operations)):
                line = line + str(question.operands[i]) + " "
                line = line + str(question.operations[i]) + " "
            line = line + str(question.operands[i+1])
            line = line + " =         "
            if len(line) < (self.chars_per_line / 2):
                line = line + " "
            else:
                print line
                if self.blank_lines_between > 0:
                    print "\n" * (self.blank_lines_between-1)
                line = ""


if __name__ == "__main__":
    calc_bank = CalcBank(cap=1000, num_of_operands=3)
    list = calc_bank.get_list(20, True)
    Printer(list, blank_lines_between=0).print_out()