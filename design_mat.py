{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "d6375c2f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "9\n",
      "------------.|.------------\n",
      "---------.|..|..|.---------\n",
      "------.|..|..|..|..|.------\n",
      "---.|..|..|..|..|..|..|.---\n"
     ]
    }
   ],
   "source": [
    "import math\n",
    "N= int(input()) \n",
    "M=N*3\n",
    "\n",
    "for i in range(0,math.floor(N/2)): \n",
    "    s='.|.'*i\n",
    "    print (s.rjust(math.floor((M-2)/2),'-')+'.|.'+('.|.'*i).ljust(math.floor((M-2)/2),'-'))\n",
    "# print ('WELCOME'.center(M,'-'))\n",
    "# for i in reversed(range(0,math.floor(N/2))): \n",
    "#     s='.|.'*i\n",
    "#     print (s.rjust(math.floor((M-2)/2),'-')+'.|.'+('.|.'*i).ljust(math.floor((M-2)/2),'-'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0ed03c4e",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(math.floor(0.6))\n",
    "print(math.floor(1.4))\n",
    "print(math.floor(5.3))\n",
    "print(math.floor(-5.3))\n",
    "print(math.floor(22.6))\n",
    "print(math.floor(10.0))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "3ef11b7b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3.3333333333333335\n",
      "3\n",
      "1\n",
      "3\n",
      "3.3333333333333335\n"
     ]
    }
   ],
   "source": [
    "print(10/3)\n",
    "print(10//3)\n",
    "print(10%3)\n",
    "print(math.floor(10/3))\n",
    "print(10/3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a1e5bce2",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
