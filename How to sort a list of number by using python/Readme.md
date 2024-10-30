# Effective Way of Sorting by Using Python

**Sorting is a technique by using this we can sort a list of numbers in a particular order, for example, ascending and descending order. In this article, we will talk about multiple ways to sort a list of numbers or integers by using Python.**



**Method 1: We can use the `sorted()` function.**

It's a built-in function that allows us to sort a list of numbers easily. This method is effective for sorting numerical data in a particular order, like ascending or descending. For descending order, we need to use the `reverse` parameter.
![Alt text](https://github.com/Sadhin404/professional-Certificate-In-Python-For-Machine-Learning-and-Data-Science-/blob/bafafb7f2da479a3200fbc54e1b0af07bc7c578b/How%20to%20sort%20a%20list%20of%20number%20by%20using%20python/Screenshot_2024-10-30-19-40-48-740_com.android.chrome.png)


**Method 2: We can use the `sort()` function**

which is the best method for effective sorting. It's similar to the `sorted()` function. We can also use the `reverse` parameter for descending order. The `sort()` function is much easier and straightforward for effective sorting.
**Example**
numbers = [5, 2, 9, 1]
numbers.sort()



**Method 3: In this method, we will use the slicing technique**

which is `[::-1]`. This returns the result in descending order. Rather than using the reverse method, which we already explored from `sort()` and `sorted()` methods, this method is easier and effective for sorting a list of numbers in descending order.
**Example**
numbers = [5, 2, 9, 1]
sorted_numbers = numbers[::-1]


**Method 4: We can use a lambda function with the `sorted()` function for more complex sorting criteria.** 

In this method, we divide each number by 5, and the list of numbers will be sorted based on their remainders. We can also customize our lambda function based on specific sorting criteria.
**Example**
numbers = [5, 2, 9, 1]
sorted_by_remainder = sorted(numbers, key=lambda x: x % 5)


**Method 5: We can use the `heapq` module for sorting large lists of numbers.**

When we deal with ultra-large lists, we need to use the `heapq` module. It's a heap-based algorithm that is more memory efficient. So, where memory is our main concern, we use the `heapq` module for effective sorting.
