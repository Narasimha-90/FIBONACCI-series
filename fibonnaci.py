a = 0
b = 1
number = int(input("Enter the Number to Obtain Fibonacci Series"))
if number == 1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(1,number+1):
        c = a + b
        a = b
        b = c
        print(c)
{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "5d95f3fe-a592-46e2-a13c-1b807158ef97",
   "metadata": {},
   "source": [
    "PROJECT 1"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1c59e469-55d1-4ea5-92c0-69fa7d5a5afb",
   "metadata": {},
   "source": [
    "FIBONACCI GENERATOR"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "15024751-bc07-4774-a362-421fd944b7b2",
   "metadata": {},
   "outputs": [],
   "source": [
    "a = 0\n",
    "b = 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "8cbb1c4d-ee2f-4c33-b202-528241a0206d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the Number to Obtain Fibonacci Seires 15\n"
     ]
    }
   ],
   "source": [
    "number = int(input(\"Enter the Number to Obtain Fibonacci Seires\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "282e6190-f336-483e-8a1d-94d52c12babb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "1\n",
      "1\n",
      "2\n",
      "3\n",
      "5\n",
      "8\n",
      "13\n",
      "21\n",
      "34\n",
      "55\n",
      "89\n",
      "144\n",
      "233\n",
      "377\n",
      "610\n",
      "987\n"
     ]
    }
   ],
   "source": [
    "if number == 1:\n",
    "    print(a)\n",
    "else:\n",
    "    print(a)\n",
    "    print(b)\n",
    "    for i in range(1,number+1):\n",
    "        c = a + b\n",
    "        a = b\n",
    "        b = c\n",
    "        print(c)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}