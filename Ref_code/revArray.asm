section .data
    array dd 1, 2, 3, 4, 5      ; Define an array of integers
    n equ 5                     ; Number of elements in the array

section .text
    global _start

_start:
    ; Initialize pointers
    mov esi, array              ; esi points to the start of the array
    mov edi, array + (n - 1) * 4; edi points to the end of the array

reverse_loop:
    ; Compare pointers
    cmp esi, edi                ; Stop if pointers cross or meet
    jge reverse_done

    ; Swap the elements
    mov eax, [esi]              ; Load the value from start pointer
    mov ebx, [edi]              ; Load the value from end pointer
    mov [esi], ebx              ; Store the end value at the start
    mov [edi], eax              ; Store the start value at the end

    ; Move pointers
    add esi, 4                  ; Move start pointer forward (size of int)
    sub edi, 4                  ; Move end pointer backward (size of int)

    jmp reverse_loop            ; Repeat the loop

reverse_done:
    ; Exit program
    mov eax, 60                 ; syscall: exit
    xor edi, edi                ; status: 0
    syscall
