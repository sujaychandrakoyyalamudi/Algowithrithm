'''
## 1. Example Question (Two Sum)
**Problem statement**
> You are given an array of integers and a target value.
> Determine whether there exist **two different numbers** in the array whose **sum equals the target**.
> You may assume each input has **at most one valid pair**.
**Example**
* Array: `[2, 7, 11, 15]`
* Target: `9`
---
## 2. Visual Explanation (Step-by-Step)
### Step 1: Think in terms of **pairing**
You are not looking for one number —
you are looking for **two numbers that complement each other**.
```
Target = 9
```
---

### Step 2: Scan the array mentally
```
Index:   0   1   2    3
Array:  [2,  7, 11, 15]
```
---
### Step 3: Complement thinking (key insight)
Ask this question repeatedly:
> “If I pick this number, what number do I still need to reach the target?”
#### Visual table
| Current number | Needed to reach 9 |
| -------------- | ----------------- |
| 2              | 7                 |
| 7              | 2                 |
| 11             | -2 (invalid)      |
| 15             | -6 (invalid)      |
---
### Step 4: Match appears
* You see **2**
* You later see **7**
* Together:
```
2 + 7 = 9 ✔
```
🎯 **Valid pair found**
---
## 3. Mental Picture (Very Important)
Think of this like **fitting puzzle pieces**:
```
[2] needs [7]
[7] fits [2]
```
You are constantly asking:
> “Have I already seen the piece that completes me?”
---
## 4. How to Recognize the Two Sum Pattern in a Question
This is the **most important section**.
### ✅ Strong signals it is a Two Sum problem
Look for phrases like:
* “find two numbers such that…”
* “pair of elements whose sum equals…”
* “check if any two values add up to…”
* “return indices of two elements…”
* “exactly one solution exists”
---
### 🧠 Hidden pattern clue
If the question can be rephrased as:
> “For each number, I need to know whether its complement exists”
Then it is **Two Sum**.
---
## 5. Core Thought Process (Interview Gold)
Whenever you see a Two Sum-style question, your brain should immediately do this:
```
Given a target T
For any number X
I need (T - X)
```
This mental equation is the **pattern**.
---
## 6. Real-Life Analogy
### Wallet analogy
* You want to pay **$9**
* You pull out a **$2 bill**
* You immediately think:
  > “I need $7 more”
If you later find a **$7 bill**, you’re done.
---
## 7. Variations That Are Still Two Sum (Disguised)
Even if the problem changes wording, the pattern stays:
| Variation         | Still Two Sum? | Why                     |
| ----------------- | -------------- | ----------------------- |
| “Return indices”  | ✅              | Still pairing           |
| “Check if exists” | ✅              | Same logic              |
| “Count pairs”     | ✅              | Multiple Two Sum checks |
| “Closest sum”     | ⚠️             | Modified version        |
| “Sorted array”    | ✅              | Two-pointer version     |
---
## 8. One-Line Pattern Summary (Memorize This)
> **If the problem asks for two elements that satisfy a condition together, and one element defines what the other must be — it is a Two Sum pattern.**
'''


'''
###################test cases########################
## 1) Minimum length input

**Case:** Not enough elements to form a pair.

* Array: `[5]`
* Target: `5`
  **Result:** No pair possible (needs two distinct elements).

---

## 2) Exactly two elements

### 2a) They do match

* Array: `[2, 7]`
* Target: `9`
  **Result:** Pair exists.

### 2b) They do not match

* Array=[2, 7]
* Target: `10`
  **Result:** No pair.

---

## 3) Pair uses the first and last elements

* Array: `[8, 1, 4, 6]`
* Target: `14` (8 + 6)
  **Result:** Pair exists, far apart.

---

## 4) Negative numbers involved

### 4a) Negative + positive

* Array: `[-3, 4, 9, 1]`
* Target: `1` (-3 + 4)
  **Result:** Pair exists.

### 4b) Two negatives

* Array: `[-10, -2, -3, 7]`
* Target: `-5` (-2 + -3)
  **Result:** Pair exists.

---

## 5) Target is zero

### 5a) Opposite signs

* Array: `[-5, 2, 5, 10]`
* Target: `0` (-5 + 5)
  **Result:** Pair exists.

### 5b) Zeros present

* Array: `[0, 4, 3, 0]`
* Target: `0` (0 + 0)
  **Result:** Pair exists **only if there are at least two zeros**.

---

## 6) Duplicate values matter

### 6a) Same value can be used twice only if it appears twice

* Array: `[3, 3]`
* Target: `6` (3 + 3)
  **Result:** Pair exists because there are two 3s.

### 6b) Only one occurrence is not enough

* Array: `[3, 1, 2]`
* Target: `6` (needs 3 + 3)
  **Result:** No pair (only one 3).

---

## 7) Multiple valid pairs exist (ambiguity)

(Some problem statements say “exactly one solution,” others don’t.)

* Array: `[1, 2, 3, 4, 5]`
* Target: `6`
  Possible pairs: (1,5) and (2,4)
  **Result:** Multiple pairs exist. In interviews, clarify whether you should return *any* pair or all pairs.

---

## 8) Repeated numbers with different indices (index correctness)

* Array: `[1, 5, 5, 2]`
* Target: `10` (5 + 5)
  **Result:** Pair exists, but it must use the **two different 5s** (distinct indices).

---

## 9) Pair appears late (must not “lock in” early incorrectly)

* Array: `[1, 9, 2, 8]`
* Target: `10` (2 + 8)
  **Result:** Pair exists, but not involving early elements.

---

## 10) Very large / very small integers (overflow mindset)

(Language-dependent; in Python it’s not an issue, but interviewers may still test awareness.)

* Array: `[2_000_000_000, 147_483_647, -147_483_647]`
* Target: `2_000_000_000` (147_483_647 + 1_852_516_353 would be needed, but not present; also -147_483_647 + 2_147_483_647 would be needed, etc.)
  **Result:** Typically no pair here; the real edge case is **avoid overflow** in fixed-width integer languages.

---

## 11) Target cannot be reached

* Array: `[1, 2, 5, 10]`
* Target: `9`
  **Result:** No pair.

---

## 12) Already sorted vs unsorted (pattern-switch edge case)

### 12a) Sorted input

* Array: `[1, 2, 4, 7, 11]`
* Target: `9` (2 + 7)
  **Result:** Pair exists; in interviews, note a **two-pointer** approach becomes natural.

### 12b) Unsorted input

* Array: `[7, 1, 11, 2, 4]`
* Target: `9` (7 + 2)
  **Result:** Pair exists; complement-tracking is natural.

---

## 13) “Do not reuse the same element” trap

* Array: `[4, 2, 9]`
* Target: `8`
  A careless approach might think “4 + 4” works.
  **Result:** No pair unless there are **two 4s**.

---

## 14) Empty array

* Array: `[]`
* Target: `0`
  **Result:** No pair.

---

### What interviewers really want from edge cases

'''

Array =[3,3]
Target=6
#   **Result:** Pair exists **only if there are at least two zeros**.


def two_sum(arr,t):
    pair={}
    if len(arr)<2:
        return None,None
    for pos,i in enumerate(arr):
        x=t-i
        if x in pair:
            return pair[x],pos
        else:
            pair[i]=pos

    return None,None

    
        
   
x,y=two_sum(Array,Target)
print(f"{x} {y}")



# Testing
inputs=[[2,7,11,15],[1,2,3],[3,3],[-3,4,7],[0,4,0],[5]]
targets=[9,10,6,1,0,5]
results=[(0,1),(None,None),(0,1),(0,1),(0,2),(None,None)]


def test_two_sum(inputs,targets,results):
    for pos,val in enumerate(inputs):
        x,y=two_sum(inputs[pos],targets[pos])
        assert results[pos] == (x,y)
    

test_two_sum(inputs,targets,results)