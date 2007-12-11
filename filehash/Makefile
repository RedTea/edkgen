# Project: ed2k
# Makefile created by kernel1983

CPP  = g++
CC   = gcc
OBJ  = main.o md4.o ed2k.o
LINKOBJ  = main.o md4.o ed2k.o
#LIBS =  -L"C:/Dev-Cpp/lib"  
LIBS =
#INCS =  -I"C:/Dev-Cpp/include" 
INCS =
#CXXINCS =  -I"C:/Dev-Cpp/lib/gcc/mingw32/3.4.2/include"  -I"C:/Dev-Cpp/include/c++/3.4.2/backward"  -I"C:/Dev-Cpp/include/c++/3.4.2/mingw32"  -I"C:/Dev-Cpp/include/c++/3.4.2"  -I"C:/Dev-Cpp/include" 
CXXINCS = 
BIN = ed2k
CXXFLAGS = $(CXXINCS)  
CFLAGS = $(INCS)  
RM = rm -f


$(BIN): $(OBJ)
	$(CC) $(LINKOBJ) -O2 -o "$(BIN)" $(LIBS)

main.o: main.c
	$(CC) -O2 -c main.c -o main.o $(CXXFLAGS)

ed2k.o: ed2k.c
	$(CC) -O2 -c ed2k.c -o ed2k.o $(CXXFLAGS)

md4.o: md4.c
	$(CC) -O2 -c md4.c -o md4.o $(CXXFLAGS)


clean:
	${RM} $(OBJ) $(BIN)


test:
	$(CC) -c test.c -o test.o $(CXXFLAGS)
	$(CC) test.o md4.o -o test

clean_test:
	$(RM) test.o test

