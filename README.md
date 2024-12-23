# christmas-coding-challenge-2024
This project was developed within the framework of the Christmas Coding Challenge 2024, organized by Women Coding Community.

# 📅 Challenge Goals
-Solve one LeetCode problem daily in Pyhton.

-Focus on a variety of topics such as arrays, strings, dynamic programming, graphs, and more.

-Document each solution with explanations and, if relevant, alternative approaches or optimizations.

# DAY 1
Longest Substring Without Repeating Characters

This repository contains a Python solution to find the length of the longest substring without repeating characters in a given string.

📚 Algorithm Overview
Technique: Sliding Window

Time Complexity: O(n), where n is the length of the string

Space Complexity: O(k), where k is the size of the character set (e.g., English letters, digits, symbols, etc.)


# DAY 2
Nth Highest Salary

This repository contains a Python solution to find Nth Highest Salary.

Given an Employee table with id and salary, write a function nth_highest_salary to return the nth highest salary. If there are fewer distinct salaries than n, the function should return None.

# DAY 3
Rank Scores

This repository contains a Python solution to find Rank Scores.

The ranking should be calculated according to the following rules:

-The scores should be ranked from the highest to the lowest.

-If there is a tie between two scores, both should have the same ranking.

-After a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no holes between ranks.

Return the result table ordered by score in descending order.

# DAY 4

Delete Duplicate Emails

Remove duplicate email entries from a DataFrame. Retain only the row with the smallest id for each unique email. Modify the DataFrame in place.

Method

Sort the DataFrame by the id column to ensure the smallest id appears first.

Use drop_duplicates on the email column, keeping only the first occurrence.

