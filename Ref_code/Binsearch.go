package main

import (
    "fmt"
)

func BinarySearch(arr []int, target int) int {
    low := 0
    high := len(arr) - 1

    for low <= high {
        mid := low + (high-low)/2

        if arr[mid] == target {
            return mid
        }

        if arr[mid] < target {
            low = mid + 1
        } else {
            high = mid - 1
        }
    }

    return -1
}

func main() {
    arr := []int{1, 2, 3, 4, 10, 20, 30, 40, 50}
    target := 10
    result := BinarySearch(arr, target)

    if result != -1 {
        fmt.Printf("Element found at index %d\n", result)
    } else {
        fmt.Println("Element not found in the array")
    }
}
