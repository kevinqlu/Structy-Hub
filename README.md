# Structy-Hub

My solutions to the [Structy](https://structy.net) data structures and algorithms course, written in Python. Each accepted submission is committed automatically with [StructyHub](https://github.com/cbkinase/StructyHub), so the commit history shows how my solutions change over time.

## Why I'm doing this

I'm preparing for software engineering interviews. I finished a B.S. in Computer Science in December 2025 and want to be able to solve and explain these patterns without looking anything up. This repo is my record of that work.

## Progress

### Solutions

> This repo was started a few months into my Structy course. "Before repo" counts coding problems I solved before the repo existed, so they have no commit history here. "In repo" counts solutions committed since. I've also completed 10 multiple-choice and quiz items, which aren't tracked here.

<!-- SOLUTIONS:START -->
| Topic | In repo | Before repo | Total |
|---|---|---|---|
| BigO | 1 | 1 | 2 |
| BinaryTree | 5 | 9 | 14 |
| Hashing | 0 | 8 | 8 |
| Introduction | 1 | 4 | 5 |
| LinkedList | 3 | 8 | 11 |
| Recursion | 1 | 5 | 6 |
| **Total** | **11** | **35** | **46** |
<!-- SOLUTIONS:END -->

### Review (Anki)

<!-- ANKI:START -->
| Topic | Cards | Mature (21d+ interval) | Reviews |
|---|---|---|---|
| BigO | 4 | 3 | 38 |
| BinaryTree | 27 | 2 | 214 |
| Hashing | 17 | 9 | 233 |
| Introduction | 5 | 4 | 73 |
| LinkedList | 23 | 6 | 366 |
| Recursion | 7 | 4 | 98 |

1022 total reviews, 28 in the last 7 days. Last review: October 29, 2026.
<!-- ANKI:END -->

Solving a problem once doesn't mean I know it. The first table counts what I've solved; the second shows how much of it has stuck.

## How I study

I review with spaced repetition:

1. Each problem has an Anki card that links straight to the Structy problem.
2. I solve the problem from scratch without notes.
3. I rate the card honestly: Again, Hard, Good, or Easy. If I needed a hint, I don't rate it Good.
4. Problems I keep failing get tagged as leeches. For those, I run a weak-spot session: cold attempt, trace by hand with a real input, write one sentence on exactly where my thinking broke, then redo it cold the next day. Results are logged in [WEAK_SPOTS.md](WEAK_SPOTS.md).

Many problems have two solutions, iterative and recursive, or depth-first and breadth-first. I keep both, because the interview question is often "now do it the other way."

## Patterns I'm working on

- **Linked lists:** tracking the current node and what comes next while reversing, and remembering to attach leftover nodes when merging or zipping lists
- **Trees:** choosing between depth-first and breadth-first, and writing each one iteratively and recursively
- **Hashing:** reducing a brute-force solution to O(n) with a dictionary or set

## Notes

Problem statements and tests belong to Structy, so this repo contains only my own solutions. Go to [structy.net](https://structy.net) to see the problems.

The tables above are generated: the Solutions table by `update_readme.py`, the Anki table by `anki_progress.py`. Don't edit inside the marker comments by hand.

---
Made with [StructyHub](https://github.com/cbkinase/StructyHub)
