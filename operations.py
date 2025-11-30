#!/usr/bin/python3

def calculate_bonus(salary):
    return salary * 0.10


def calculate_discount(salary):
    return salary * 0.5


def get_remaining_holidays(days_absent):
    TOTAL_LEGAL_HOLIDAYS = 21
    return TOTAL_LEGAL_HOLIDAYS - days_absent
