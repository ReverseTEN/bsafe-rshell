@echo off

nasm -f win32 bc.asm -o bc.o
ld -m i386pe bc.o -o bc.exe
echo done..