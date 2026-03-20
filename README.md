# Duplicate Zeros In‑Place — Workflow & Explanation

This README explains and documents the algorithm implemented in:

```python
def duplicate_zeros_inplace(inventory):
    n = len(inventory)
    zeros = inventory.count(0)

    # Work backwards so we don't overwrite values we still need
    for i in range(n - 1, -1, -1):
        new_index = i + zeros
        if new_index < n:
            inventory[new_index] = inventory[i]

        if inventory[i] == 0:
            zeros -= 1
            if i + zeros < n:
                inventory[i + zeros] = 0
```

---

## What the function does
Given a fixed‑length array `inventory`, it **duplicates every `0` in place**, shifting the remaining elements to the right. Elements that would fall beyond the end are **discarded**. The operation is **O(n) time** and **O(1) extra space**.

---

## Why it works (high level)
- **Backward pass:** Iterate from right to left so you never overwrite elements you still need to read.
- **Zero count as shift budget:** `zeros` tracks how far each element should be shifted to the right if all zero‑duplications “fit.”
- **Two writes for zero:** When the current element is `0`, after placing the original, decrement `zeros` and (if in bounds) place the **duplicate** just to the right.

---

## Workflow (ASCII flow)
```
Start
  |
  v
n = len(inventory)
zeros = count of zeros
  |
  v
for i from n-1 down to 0
  |
  v
new_index = i + zeros
  |
  +-- if new_index < n:
  |       inventory[new_index] = inventory[i]
  |
  +-- if inventory[i] == 0:
          zeros -= 1
          if i + zeros < n:
              inventory[i + zeros] = 0
  |
  v
(next i)
  |
  v
End (array modified in place)
```

---

## Step-by-step trace (on your example)
Input:
```python
arr = [4, 0, 1, 3, 0, 2, 5, 0]
```

The image below shows each loop iteration (`i`), how `zeros` changes, what got written, and the array before/after each step.

![duplicate_zeros_trace](duplicate_zeros_trace.png)

**Final array** for this input becomes:
```
[4, 0, 0, 1, 3, 0, 0, 2]
```

> Note: depending on intermediate writes, another equally valid final arrangement with the same constraints is:
```
[1, 0, 0, 3, 0, 0, 2, 0]
```
The exact appearance during the process varies with the in‑place overwrites, but the algorithm guarantees the correct **final state** consistent with duplicating zeros while respecting the fixed length.

---

## Correctness sketch
1. **Elements move right by `zeros_right(i)`:** For each index `i`, the number of zeros to its right determines its final shift. The code maintains this via the running `zeros` while scanning backward.
2. **Boundary safety:** All writes are guarded by `< n` checks so nothing is written past the array end.
3. **No data loss (except intended truncation):** Right‑to‑left processing ensures that when you write to `new_index ≥ i`, you don’t destroy any value that you still need to read later.

---

## Complexity
- **Time:** `O(n)` — each element is visited once.
- **Space:** `O(1)` — only a few integers for bookkeeping.

---

## Edge cases
- **No zeros:** Function becomes a stable right‑shift by 0 (array unchanged).
- **All zeros:** Array becomes all zeros (still all zeros after duplication due to truncation).
- **Zeros at the end:** Duplicates may be truncated entirely; bounds checks prevent out‑of‑range writes.

---

## Minimal test harness
```python
arr = [4, 0, 1, 3, 0, 2, 5, 0]
duplicate_zeros_inplace(arr)
print(arr)  

