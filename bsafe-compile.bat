@echo off

nasm -f win32 bsafe.asm -o bsafe.o
ld -m i386pe bsafe.o -o bsafe.exe
del bsafe.o
echo done...


