#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Project Title: Bubble-Sort (https://github.com/KafetzisThomas/Bubble-Sort)
# Author / Project Owner: KafetzisThomas - (https://github.com/KafetzisThomas)

def bubble_sort(list):
  """Print a sorted list"""
  for i in range(len(list)):
    for j in range(i+1, len(list)):
      if list[i] > list[j]:  # Otherwise, use '<' to print a reversed list
        temp = list[i]
        list[i] = list[j]
        list[j] = temp

  return list

list = [19, 13, 6, 2, 18, 8]
print(bubble_sort(list))
