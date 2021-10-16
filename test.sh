#!/bin/bash

echo $'\n10000 Elements Sorted\n' >> out.txt
python3 main.py s 10000 s >> out.txt
python3 main.py i 10000 s >> out.txt
python3 main.py q 10000 s >> out.txt
echo $'\n10000 Elements Ordered\n' >> out.txt
python3 main.py s 10000 c >> out.txt
python3 main.py i 10000 c >> out.txt
python3 main.py q 10000 c >> out.txt
echo $'\n10000 Elements Random\n' >> out.txt
python3 main.py s 10000 r >> out.txt
python3 main.py i 10000 r >> out.txt
python3 main.py q 10000 r >> out.txt

echo $'\n\n\n' >> out.txt

echo $'\n100000 Elements Sorted\n' >> out.txt
python3 main.py s 100000 s >> out.txt
python3 main.py i 100000 s >> out.txt
python3 main.py q 100000 s >> out.txt
echo $'\n100000 Elements Ordered\n' >> out.txt
python3 main.py s 100000 c >> out.txt
python3 main.py i 100000 c >> out.txt
python3 main.py q 100000 c >> out.txt
echo $'\n100000 Elements Random\n' >> out.txt
python3 main.py s 100000 r >> out.txt
python3 main.py i 100000 r >> out.txt
python3 main.py q 100000 r >> out.txt

echo $'\n\n\n' >> out.txt
