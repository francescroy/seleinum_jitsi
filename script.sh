
#!/bin/bash
for i in $(seq 1 $1)
do
   python3 prova_headless.py &
done

