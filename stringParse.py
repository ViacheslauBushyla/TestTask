#!/bin/python

import math
import os
import random
import re
import sys

# this my function
def parse(source, queries):
   result = []   
   for query in queries:      
      splitByAttribute = []
      splitByTag = query.split('.')
      sourceElementToSearchIndex = 0
      subQueryElement = splitByTag[0]
      # define source element and subquery
      # nested level query
      if (len(splitByTag) > 1):
         sourceElementToSearchIndex = len(splitByTag) - 1
         subQueryElement = splitByTag[sourceElementToSearchIndex]
         if ':' not in subQueryElement:
            result.append('None')
            continue
      # first level query
      else:
         splitByValue = splitByTag[0].split(':')
         for i in range(len(source)):
            if splitByValue[0] in source[i]:
               sourceElementToSearchIndex = i
               break         
      splitByAttribute = subQueryElement.split(':')
      attributeValue = splitByAttribute[-1]
      
      # parseString
      sourceElement = source[sourceElementToSearchIndex]
      if (attributeValue not in sourceElement):
         result.append('None')
         continue
      searchFromIndexStart = sourceElement.index(attributeValue) + len(attributeValue) + 1
      searchRest = sourceElement[searchFromIndexStart:]
      trimRestUntilIndex = len(searchRest)
      if (' ' in searchRest):
          trimRestUntilIndex = searchRest.index(' ')
      addToResult = searchRest[:trimRestUntilIndex]     
      result.append(addToResult)             
   
   return result



if __name__ == '__main__':
 
   source = [
      '(tag1 :value "HelloWorld" secondValue "MySecondValue"',
      '(tag2 :name "Name1"', 
      '(tag3 :parameter "MyParameter"', ')', ')',
      ]
   queries = [
      'tag1:secondValue',
      'tag1.tag2.tag3:parameter', #"Name1"
      'tag1.tag2:name', #"Name1"
      'tag1:value', #"HelloWorld"
      'tag2:name', #"Name1"
      'tag1.value', #None
      'tag2.name', #None
      'tag1:name', #None
      'tag2.value' #None
      ]

   result = parse(source, queries)
   print(result) 

