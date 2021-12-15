#!/bin/python3
#Credit to malapi.io

import re
import string

file_name = input("Name of file containing APIs called by your sample: ")

print("#########################")
print('\n')
#Converting file_name content into an array for comparisson
f = open(file_name, 'r')
apis = f.read().splitlines()
f.close()

#converting APIS from malapi.io for comparisson
f = open("enum_malapi.txt", 'r')
enummalapi = f.read().splitlines()
f.close()

f = open("injetion_malapi.txt", 'r')
injectionmalapi = f.read().splitlines()
f.close()

f = open("evade_malapi.txt", 'r')
evademalapi = f.read().splitlines()
f.close()

f = open("spy_malapi.txt", 'r')
spyapi = f.read().splitlines()
f.close

f = open("inet_malapi.txt", 'r')
inetmalapi = f.read().splitlines()
f.close()

f = open("debug_malapi.txt", 'r')
debugmalapi = f.read().splitlines()
f.close()

f = open("ransom_malapi.txt", 'r')
ransommalapi = f.read().splitlines()
f.close()

f = open("helper_malapi.txt", 'r')
helpermalapi = f.read().splitlines()
f.close()

##################################################################################

debugmatches = []
inetmatches = []
spymatches = []
enummatches = []
injmatches = []
evadematches = []
ransommatches = []
helpermatches = []


#Finding matching enumeration API
for i in apis:
    for j in enummalapi:
        if i == j:
            enummatches.append(i)

#Finding matching injection API
for i in apis:
    for j in injectionmalapi:
        if i == j:
            injmatches.append(i)

#Finding matching evasion API
for i in apis:
    for j in evademalapi:
        if i == j:
            evadematches.append(i)

#Finding matching spy API
for i in apis:
    for j in spyapi:
        if i == j:
            spymatches.append(i)

#Finding matching internet conn API
for i in apis:
    for j in inetmalapi:
        if i == j:
            inetmatches.append(i)

#Finding anti-debugging API
for i in apis:
    for j in debugmalapi:
        if i == j:
            debugmatches.append(i)

#Finding APIs commonly used in ransomware
for i in apis:
    for j in ransommalapi:
        if i == j:
            ransommatches.append(i)
            
#Finding APIs commonly used to help malware
for i in apis:
    for j in helpermalapi:
        if i == j:
            helpermatches.append(i)
            
##################################################################################

if len(enummatches) > 0:
    print("Enumeration APIs used by the sample include: ", enummatches, '\n')
else:
    print("No enumeration APIs found", '\n')

if len(injmatches) > 0:
    print("Injection APIs used by the sample include: ", injmatches, '\n')
else:
    print("No injection APIs found", '\n')

if len(evadematches) > 0:
    print("Evasion APIs used by the sample include: ", evadematches, '\n')
else:
    print("Evasion APIs used by the sample include: No evasion APIs found", '\n')

if len(spymatches) > 0:
    print("Spying (keylogger, etc.) APIs used by the sample include: ", spymatches, '\n')
else:
    print("Spy APIs used by the sample include: No Spying APIs found", '\n')
    
if len(inetmatches) > 0:
    print("Internet APIs used by the sample include: ", inetmatches, '\n')
else:
    print("Internet APIs used by the sample include: No Internet APIs found", '\n')

if len(debugmatches) > 0:
    print("Anti-debugging APIs used by the sample include: ", debugmatches, '\n')
else:
    print("Anti-debugging APIs used by the sample include: No Anti-debugging APIs found", '\n')

if len(ransommatches) > 0:
    print("APIs commonly found in Ransomware: ", ransommatches, '\n')
else:
    print("Ransomware-related APIs: No Ransomware-related APIs found", '\n')
    
if len(helpermatches) > 0:
    print("APIs commonly used to help malware: ", helpermatches, '\n')
else:
    print("Helper APIs: No malware-helper APIs found", '\n')
