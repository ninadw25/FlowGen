package main

import "fmt"

func fibonacci(n int) int {
    if n <= 1 {
        return n
    }
    return fibonacci(n-1) + fibonacci(n-2)
}

func main() {
    n := 10
    for i := 0; i < n; i++ {
        fmt.Printf("%d ", fibonacci(i))
    }
}
